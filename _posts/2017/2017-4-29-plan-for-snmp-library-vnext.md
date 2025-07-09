---
layout: post
title: "Plan for #SNMP Library vNext"
description: "This post would show you the plan for #SNMP Library vNext."
tags: SNMP .NET
permalink: /plan-for-snmp-library-vnext-b6759e5b10dc
excerpt_separator: <!--more-->
---

As .NET Core 2.0 is coming, I think it is time to write about the plan for #SNMP Library vNext (the version number is uncertain yet, 9.5 or 10.0).
<!--more-->

## Minimal .NET Framework Version

Now the plan is to require .NET Framework 4.6.0 and above. If Microsoft does resolve multiple target framework support in .NET Standard Class Library project, then I might add back .NET Framework 4.5.x support.

## Minimal .NET Standard Version

The plan is to support .NET Standard 1.3 and above. Won't support other .NET Standard versions, as they are too limited. But since a workaround is used to run this library on .NET Standard 1.3, I might build a .NET Standard 2.0 assembly in NuGet package to remove this workaround.

## Extra Assemblies

We still need to have SharpSnmpLib.Full.dll, SharpSnmpLib.iOS.dll, and SharpSnmpLib.Android.dll, although now they only contain two classes each. This is a limitation of .NET Standard 1.3.

Probably when .NET Standard 2.0 comes, we can finally have a single SharpSnmpLib.NetStandard20.dll to rule all the platforms.

Stay tuned.
