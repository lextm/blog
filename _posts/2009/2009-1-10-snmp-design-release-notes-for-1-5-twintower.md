---
layout: post
title: "#SNMP Design: Release Notes for 1.5 (TwinTower)"
description: "This post is about the release notes of #SNMP 1.5 (TwinTower)."
tags: SNMP
permalink: /snmp-design-release-notes-for-1-5-twintower-2de00443601c
excerpt_separator: <!--more-->
---
Well, this release takes much longer than we expected even though luckily Steve joined me. But I am sure that it worth the while because finally we have more features implemented in the suite.
<!--more-->

The key changes are,

* SNMP v2c support is almost complete. So now we have GET BULK, INFORM and so on in the library.
* Manager component API is adjusted. Finally we have better overloading methods exposed.
* Experimental Agent component API is designed. Although it only provides limited functionalities, you can use it as a start point for your SNMP agent applications.
* Limited thread-safe support is added. Static methods of Manager component are now thread-safe.
* #SNMP MIB Browser is created. It offers basic features so you can load MIB documents and try to manipulate the managed objects.
* #SNMP Library now supports both Visual Studio 2005 and 2008. Experimental support for .NET Compact Framework 3.5 is also added.
* Experimental #SNMP MIB Compiler is created.
* Bug fixes and other enhancements.

I think now we are pretty close to the release date so it is time to publish this information ahead. Stay tuned.
