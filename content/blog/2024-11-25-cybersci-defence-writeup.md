<!-- title: CyberSci, Voter Registry Defence Write-up -->
<!-- author: Andrew -->

This year's CyberSci regionals had several defence challenges which involved patching vulnerable services. Solving these challenges gave us a ton of points and helped us win for our region.
I'll be going over how I patched three vulnerabilities that were inside of the voter ballot registry.

If you want to try to solve it yourself first, here are the unmodified service files.
<a href="/misc/voter-registry.tar.gz">voter-registry.tar.gz</a>

Taking a look at the Dockerfile, it's a pretty simple service. Python is installed, a few libraries, static assets, as well as a key pair (this comes in later).

The files contained within the service are pretty simple. There's only one script found within there: `voter_registry.py` which really simplifies things for us.

We'll start with the two easy fixes and then finish with the one which involves the most code.

## 1. Disabled JWT Verification

This bug fix is very easy. For some reason the service came shipped with JWT signature verification disabled by default. If we simply change line 23 from `sig_verify = None` to `sig_verify = True`, we enable verification of JWT tokens which ensures that JWT keys haven't been forged by an attacker.

## 2. Unauthorized Access to Voter Records

Another super easy thing to check in challenges like this is that all routes have adequate authentication checks. Most of them seem fine except for the `/voter/<id>` path. It's commented as being only accessible for the admin and the voter themselves. But this check just isn't programmed.

We can add it with this single if statement:

```
    if not user.is_admin() and user.get_id() != id:
        return get_error_page("You are not authorized to access this page."), 403
```

## 3. Signature Forging

Very briefly we should look through the comments in the code as often hints are left here. On line 256 in the code responsible for authenticating user's login QR codes, we find this extremely suspicious piece of code.

```
    # This is a good enough verification for now
    if len(signature) != 64:
        return None
```

This is not good enough verification! We could easily forge a signature that matches these requirements and log in as any user.

For example if we check the `voter-list.db` file we can see that "Nieves Ugarte" is an admin, and his id is "273-85-2654" we could forge a QR code to contain the required JSON to log us in as him. We'll insert his id and then base64 encode some arbitrary 64 character string: 

```
{
    "id":  "273-85-2564",
    "sig": "YWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYQ=="
}
```

If you submit a QR code with this info to the login system it'll log you straight in as "Nieves Ugarte". How can we fix this?

Well if you look back to the code you'll find something else suspicious. Those keys that are copied into the docker container are nowhere mentioned in the code. Additionally, asymmetric key encryption libraries are imported but never used.

Gathering this info we can assume that the signatures which are embedded within the QR codes are signed with the private key in the service file.

We can replace the previous verification code with the following which uses the public key to verify the signature:

```
    try:
        key = ECC.import_key(open('public_key.pem').read())
        verifier = eddsa.new(key, 'rfc8032')
        message = payload['id'].encode('utf-8')
        verifier.verify(message, signature)
    except (ValueError, Exception) as e:
        print(f"Signature verification failed: {e}")
        return None
```

Now our previous exploit of forging a signature will no longer work.
