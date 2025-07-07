<!-- title: The Necessity of Ad Block -->
<!-- author: Alan Zhou -->

According to Charles “Penguinz0” White Jr., “Internet Is Unusable Without
Ad Block” on YouTube. Using an ad blocker provides essential cybersecurity
protections and enhances privacy while browsing the web. As a result,
websites load faster, function better, and appear more organized. Some
advertisements even block website buttons, making navigating websites annoying.
Ad blockers are free to use and essential when navigating the Internet safely.

![](/img/ads3.png)

Digital advertisements can serve as attack vectors that steal personal data,
defraud people, and infect devices with malware. Ad blockers remove
advertisements on websites, whether they are images, videos, or audio. This
helps eliminate malvertising, reducing the risks to your computer. Furthermore,
ad blockers also prevent advertisers from tracking your online activity and
collecting personal data, improving user privacy. Advertisers collect data
through cookies, tracking pixels, and UTM codes. It reduces the risk of
browser fingerprinting and private data leaks.

![](/img/ads2.png)

Users can use browser settings to improve the website experience and Internet
safety. For example, Google Chrome has a setting that allows users to block
intrusive advertisements.

Here are some ad blockers I recommend using:
1. AdBlock Plus
2. uBlock Origin (Open-source)
3. Brave Ad Blocker (Open-source)

Brave is available on computers and mobile devices. The Brave Browser provides
an ad blocker. Users can install uBlock Origin on computers and mobile devices
by installing the Mozilla Firefox browser and then installing the uBlock Origin
extension.

Alternatively, one can use Pi-Hole to block advertisements at the network level.
The equipment required is an Ethernet cable and a Raspberry Pi. Pi-Hole blocks
ads by acting as a DNS sinkhole.

There are some differences between Pi-Hole and browser extensions, primarily
in how they operate and their scope of ad-blocking capabilities. Both extensions
and Pi-Hole operate and block advertisements on devices differently. Pi-hole
functions as a network-wide ad blocker by filtering DNS requests for all devices
connected to your network. This means it can block ads before they are downloaded,
effectively eliminating many unwanted advertisements across various platforms.
However, Pi-Hole requires maintenance and can be challenging to set up.

In contrast, an ad-block extension blocks advertisements on the browser and device
only. The extensions intercept and filter web page content, effectively removing ads
only during browsing sessions. These extensions are easier to install and use, making
them accessible for users who may not be comfortable with more complex setups.

### Note

Some websites, such as Spotify and YouTube, prohibit ad blockers as stated in their 
terms of service. To comply with the terms of service, it is advisable to disable 
your ad blocker or Pi-Hole setup. Alternatively, you may consider purchasing a premium 
subscription, if available, to enjoy an ad-free experience.

### References

* [Block ads at home with Pi-hole - Raspberry Pi](https://www.raspberrypi.com/tutorials/running-pi-hole-on-a-raspberry-pi/)
* [Internet Is Unusable Without Ad Block](https://www.youtube.com/watch?v=Dab8sKg8Ko8)
* [Pi-hole – Network-wide Ad Blocking](https://pi-hole.net/)
* [Remove unwanted ads, pop-ups & malware - Computer - Google Chrome Help](https://support.google.com/chrome/answer/2765944?hl=en&co=GENIE.Platform%3DDesktop)
* [What is an Ad Blocker? - Bitdefender Cyberpedia](https://www.bitdefender.com/en-us/cyberpedia/what-is-an-ad-blocker)
* [What’s the best free ad blocker? | Brave](https://brave.com/learn/best-ad-blocker/#extension-based-ad-blockers-and-their-impact-on-internet-privacy)
