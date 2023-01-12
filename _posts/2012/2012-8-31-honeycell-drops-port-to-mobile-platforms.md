---
layout: post
title: "HoneyCell Drops: Port to Mobile Platforms"
description: "This post is about #SNMP port to mobile platforms."
tags: SNMP
permalink: /honeycell-drops-port-to-mobile-platforms-9959f6e4b303
excerpt_separator: <!--more-->
---
I was trying to port #SNMP Library to Windows Compact Edition (CE), and we still have the .NET Compact Framework (CF) compliant assembly (sharpsnmplib.cf35.dll) in binary distribution, which is a good legacy of that attempt.
<!--more-->

However, the next port to Silverlight has been marked as a big failure. Microsoft does not design this platform as a suitable one for UDP/SNMP, so any attempt is doomed to fail.

I did not pay much attention to Windows Phone (which uses a Silverlight alike .NET Framework profile), so there was no such port.

OK, above I summarized all official ports (successful or failed) and I thought the story ended a long time ago. Luckily I am now proven to be wrong.

Early this month, this discussion thread attracted my attention, which mentioned successful port to new mobile platforms (MonoTouch and Mono for Android). Though it is based on HoneyCell code base (which is #SNMP 6.1.1), this attempt seems to be quite interesting according to the detailed approach.

If you happen to be interesting in MonoTouch and Mono for Android, now you might try out [the unofficial #SNMP port](https://github.com/moljac/MonoMobile.SharpSNMP) from GitHub.

Miljenko (mel) has started to work on a port of BigDipper (#SNMP 7.5), and let's see if this latest monster can be turned into something good on mobile platforms.

I will keep an eye on the new attempt and see when and in which way we can accept the changes in official repository.

Stay tuned.
