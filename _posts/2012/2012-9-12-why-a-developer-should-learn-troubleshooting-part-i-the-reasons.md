---
layout: post
title: "Why A Developer Should Learn Troubleshooting, Part I: The Reasons"
description: "This post is about why a developer should learn troubleshooting skills."
tags: Others
permalink: /why-a-developer-should-learn-troubleshooting-part-i-the-reasons-bfccd3cf5529
excerpt_separator: <!--more-->
---
I often appear on IIS.net forums (http://forums.iis.net) and also would like to visit StackOverflow (http://stackoverflow.com) to answer questions I am interested in. My observation seems to indicate that developers do not pay enough attention to troubleshooting. It is so easy to say the fault is caused by another piece of code or another application, or even the operating system itself (how many times you see a guy crying out and saying "I've found a Windows/.NET bug!"). But is that always the truth?
<!--more-->

As a long time developer and pre-support engineer at Microsoft, I have been trying to share tips of troubleshooting/debugging. I have my reasons not to focus on the kind of answers the questioners expect, and the very first of them is the questioners 9 out of 10 have collected too little data and known so little about the real symptoms.

A good example is [this forum thread](http://forums.iis.net/t/1191449.aspx) that I've participated.

Firstly, it has been mentioned almost everywhere that when you use HttpWebRequest, or WebBrowser control in .NET Framework to simulate a typical web browser (such as Internet Explorer), various differences occur. That's because IE hides so many technical challenges from you (proxy detection, and many others), while HttpWebRequest leaves you working with the raw data and raw connection in most aspects. Such differences usually only appear on client side, not on server side. Neither IIS nor other web servers treats IE and HttpWebRequest differently in a manner that gives significant performance impact.

So will you focus on those differences at the beginning? There is no such a list of all differences documented. And even if you have such a long list at hand, will you go through them one by one? Unless this list is available and it is short (of less than 10 items), this approach can be a dead end. (It is interesting that scientists have got great discoveries by using this approach. But we are in the engineering world, and things are different.)

Secondly, performance issues are so common, but almost all cases have their own root causes (there are way too many causes can hurt the fragile performance). Like we discussed above you are not recommended to dive into the list of possible root causes this early.

Thirdly, your application runs in a special environment (don't neglect this fact, as it matters the most), so it will be only you, or a person that at your site, or a support guy connects to your site that can effectively locate the culprit. You might read from a blog, a forum, or an article that someone hit a similar problem. However, read carefully and you might find the fix does not apply to your case.

So if you become caution after reading the previous paragraphs, you will understand why only troubleshoot/debugging can set up a bridge between the symptoms on the surface (slow in general) and the real root cause (which is always hidden in the dark) for you.

It requires extensive experience to know which tools and approaches to use when a problem occurs. So learn the tools, learn the approaches, and bit by bit you turn yourself to be a better developer.

Good luck.
