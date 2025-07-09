---
layout: post
title: "TritonMate Words: 8.0 Release"
description: "This post talks about the release of #SNMP 8.0."
tags: SNMP
permalink: /tritonmate-words-8-0-release-fe233a4078c4
excerpt_separator: <!--more-->
---

While I am busy working on the closed source Compiler Pro, we do have some progress on open source side.

<!--more-->

Today I publish the release candidate of #SNMP 8.0, which contains significant new features,

- Better compliance with RFC documents (2574 and 3414).
- Official Xamarin platforms support (Mono, Xamarin.iOS, Xamarin.Android).
- Enhanced snmpd with ifTable implementation.
- Brand new BytesViewer sample.
- Project wide licensing change (from Lesser GPL to MIT/X11), except the MIB compiling portion (which is already re-licensed under BSD 3-Clause in 7.5 release).

Note that though the open source version of #SNMP MIB Compiler now contains significantly less features than the Pro edition, it still receives patches from the paid version, as the two still shares the same grammar file and a common code base.

Stay tuned.

(Updated: After releasing the RC build, no big issue is found, so today I mark it as RTW. Yes, the RC bits become final release.)

BTW, the Pro edition is now [in private beta]({% post_url 2013/2013-5-4-snmp-pro-private-beta-is-ready-and-early-access-program-starts %}).
