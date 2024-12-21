---
layout: post
title: "#SNMP Pro: SharpSnmpPro.Mib Assembly Released"
description: "This post talks about the release of SharpSnmpPro.Mib assembly."
tags: SNMP
permalink: /snmp-pro-sharpsnmppro-mib-assembly-released-7789ae356e5a
excerpt_separator: <!--more-->
---
After a few months of baking, today I finally announce that the very first official release of SharpSnmpPro.Mib assembly is now available for purchase. The Wiki pages are going to be updated soon.
<!--more-->

The final API is similar to the obsolete open source edition, but of course has been heavily upgraded and extended. The most significant features are,

1. Metadata extraction. Now description and syntax of an object can be fully extracted.
1. Document compilation and loading is significantly faster.
1. Error reporting is more accurate. More errors (base type missing or mismatched, syntax errors) can be detected. (some error reporting are not available in trial)
1. MIB document loading and unloading. Loaded documents can be unloaded, with object tree refreshing automatically. (unloading is not available in trial)
1. Cross module type resolution. If derived types and base types are in different modules, their relationship can be correctly detected. (not available in trial)
1. Data validation based on constraints is supported. (experimental, not available in trial)
1. MIB to C# compilation. (experimental, not available in trial)

By consuming the API you can build a compiler that is similar to #SNMP MIB Compiler Pro, and it provides your application a very rich set of functionality.

This assembly and its dependencies are about 1.4-MB in size, and targets only .NET Framework 4.0 and above.

You can write to support@lextudio.com and request a trial license to play with the trial for 30 days. The full edition can be brought from this page.
