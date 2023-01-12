---
layout: post
title: "TritonMate Words: #SNMP and Compact Framework"
description: "This post is about #SNMP and Compact Framework."
tags: SNMP
permalink: /tritonmate-words-snmp-and-compact-framework-e2cb24d7250e
excerpt_separator: <!--more-->
---
.NET Compact Framework was a monster released by Microsoft. After so many years, we observed many of its disadvantages,

1. It is a ill-designed subset of full .NET Framework. Even many methods/classes in core class library are not available in CF and developers have to fight hard to fill the gaps.
1. It is strictly tied to Visual Studio/C#/VB.NET. The first time I heard about CF, I was using Borland's .NET product (Delphi for .NET), where CF is not supported because Microsoft does not allow/license Borland to do it.
1. Windows Compact Edition and Windows Mobile loses its popularity (do they have any?) so quickly when new platforms (iOS and Android) arise.
<!--more-->

Like the failed attempt of J2ME, personally I believe that CF will fail soon. Now Windows Phone 8 is out, and it is a good time to end CF. However, this does not mean users of CF will migrate immediately, and I just came across a Taiwan developer that would like to try out #SNMP on CF.

If you have followed this blog for a while, you know that I rarely blogged about CF

The previous releases of #SNMP only exposed a limited set of features on CF (starting from TwinTower 1.5) as I did not attempt to port all the classes. Therefore, to help out this Taiwan guy, last month I made a few new change sets that included better CF support. The important changes are,

* SharpSnmpLib.cf35.dll now contains almost all important classes in SharpSnmpLib.dll. Many classes under Messaging namespace are ported this time to CF.
* SharpSnmpLib.Engine.cf35.dll is added, which contains all classes from SharpSnmpLib.Engine.dll.

The latest change set is [here](https://github.com/lextudio/sharpsnmplib/commit/e11a757c093d8a45a0c58576b0b1b24af832d9ad).

Now it is possible to not only develop an SNMP manager application on CF, but also an SNMP agent.

The still missing piece is the MIB assembly, but since we migrated to ANTLR which is not available on CF natively, porting the MIB assembly means I need to port ANTLR runtime to CF first. That can take lots of efforts and I don't think I can afford it right now. Luckily, if you know SNMP well, the MIB assembly is optional.

In the future, I will focus more on rising platforms such as MonoTouch and Mono for Android. Thus, this post marks an end on #SNMP CF support. Period.
