<!-- title: CyberSci, Ballot Falsification Write-up -->
<!-- author: Folah -->

This year's CyberSci competition featured several challenges. I'll
cover the first two in the web category and one from the forensics,
where the main objective was to falsify election results by submitting
modified ballot papers.

## Part 1: Uploading a Screenshot

In the first part, the website provided a sample ballot paper for
testing. I took a screenshot of the sample ballot and uploaded it, which
successfully produced the desired output.

![](/img/barcode.png)

After uploading this, it returned:

![](/img/ballottesting.png)

`FLAG: TESTING-kynjoKdvH63VZpWBXw4TZoq8`

## Part 2: Modifying the Barcode

In the second part, the task was to submit a modified version of the
barcode on the ballot.

**Initial Observations:** Analyzing the sample ballot, I realized that the
precinct code embedded in the barcode should remain unchanged. I
identified the barcode format as Code 39 after some research.

**Initial Attempts:** Using Burp Suite, I intercepted the HTTP requests and
attempted to modify the barcode data directly. However, this didn't
yield the desired results.

**Final Approach:** I decided to modify only the last digit of the barcode.
Below is a Python script I wrote to generate multiple barcode variations
and automate the scanning process.

![](/img/ballotflag.png)

flag=**07XB98CQE155**

# Forensics Challenge: Data is the new currency

In this challenge, we were given a <a href="/misc/artifact.pcap">PCAP file</a> 
that captured the communication flow between two individuals. The task 
was to determine the file sent to a customer who had just purchased access 
to the voter information service.

## Challenge Details

The hint mentioned that two types of cryptography were used: AES-CBC
and RSA. AES-CBC was likely used for encryption, while RSA handled
public and private key exchanges. From this, I inferred that the
communication was encrypted and needed to be analyzed
accordingly.

## Approach

### Analyzing the PCAP File

I wrote a Python script to parse the PCAP file and identify the
protocols in use. Based on the data flow, I determined that the most
likely communication methods were HTTP or SMTP.

### Extracting Encrypted and Non-Encrypted Data

For HTTP packets, I used Scapy to create another Python script that
extracted and printed both encrypted and plaintext payloads.

Since the SMTP packets were relatively few, I decided to manually
inspect them for any relevant information.

By combining automated analysis and manual inspection, I was able to
piece together the details and identify the file in question.

Here is the <a href="/misc/forensic.py">python script</a>.

Alternatively using wireshark by putting this display filter
`http.request.method == \"GET\" && (http.request.uri contains \"flag\"
\|\| http.request.uri contains \".\")` it returns all http GET packets
that have the word "flag" or have a file extension.

`FLAG=/62608e08adc29a8d6dbc9754e659f125/file.zip`
