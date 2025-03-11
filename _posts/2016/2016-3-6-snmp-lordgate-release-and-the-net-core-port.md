---
layout: post
title: "#SNMP: LordGate Release and The .NET Core Port"
description: "This post is about the 9.0 release of #SNMP Library and the .NET Core port."
tags: SNMP .NET
permalink: /snmp-lordgate-release-and-the-net-core-port-8c655a5eaa69
excerpt_separator: <!--more-->
---
The 9.0 release (LordGate) was published on Feb 12 at NuGet.
<!--more-->

The most important change is this new package requires .NET Framework 4.5 and above. More accurately speaking, only if you are using it on .NET Framework 4.5.2, there would be technical support from LeXtudio. That's because Microsoft stops support older .NET Framework (4.0.*, 4.5, and 4.5.1) releases in Jan. The next move is to port #SNMP Library to .NET Core.

You probably don't realize that I attempted several times, but finally today I got everything in place and generated a NuGet package for public testing.

This package is generated using .NET Core 1.0 RC 1. So, there are a few known issues,

* The package ID has to be changed, as currently the Visual Studio tool chain does not allow me to specify the previous package ID anywhere. I think it would be good to switch to such a new ID, as the library API has changed a lot.
* Most of the methods related to SNMP messages are now converted to async/await friendly signatures. Sync methods are removed, as the underlying methods on Socket class are no longer available.
* UWP is now supported (but I haven't tested it out), thanks to .NET Core's Platform Standard support.
* SNMP v3 becomes broken, as MD5/DES/AES algorithms are now missing on .NET Core. They might come in a future .NET Core release, and then we can add the necessary SNMP v3 classes back.

Microsoft should be ready to ship .NET Core 1.0 RC 2 later this month for the BUILD conference. Then I should give a further update on my progress.
