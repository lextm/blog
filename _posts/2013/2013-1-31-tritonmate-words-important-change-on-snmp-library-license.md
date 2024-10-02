---
layout: post
title: "TritonMate Words: Important Change on #SNMP Library License"
description: "This post talks about the license change of #SNMP Library."
tags: SNMP
permalink: /tritonmate-words-important-change-on-snmp-library-license-724c3c25e237
excerpt_separator: <!--more-->
---
For years, #SNMP Library has been covered by Lesser GPL. This was the license that I were most comfortable with in 2008. However, things have changed so rapidly that makes this license less useful, or even troublesome.
<!--more-->

I don't care much if you use #SNMP in a commercial project but never contribute back, as I have a day job, and I can afford the time and efforts on this project in my spare time (though I have to sacrifice other interesting projects). But the rise of mobile platforms, and the reborn of Mono/Xamarin along with those new emerging platforms, significantly changes how applications are developed and deployed, it is rather hard for a developer to consume an LGPL assembly and provide its user base a chance to patch that assembly when bugs are detected, as this is mobile world we are talking about.

I should have thought about such scenarios the very first time we started to support .NET Compact Framework. But luckily that's not an active platform any more. So hope the recent change of licenses is not too late :)

You should have read about our announcement on switching from LGPL to BSD 3 Clause for the MIB support assembly. Today, I am happy to announce that all contributors of #SNMP agree to re-license the source code under MIT/X11. This is heavily inspired by Mono's choice on how to license its class library. Hope you find this change useful.

Note that this change of license only covers our latest release. I am tired of tracking down old releases (even 7.5). Please start to evaluate 7.6, which contains many bugfixes and new additions.

Later I am going to publish the emails among the other contributors and me about the license change on my DropBox public folder for your reference. Let's thank them for their great efforts on making this project so successful today.
