---
layout: post
title: "TritonMate Words: Official Port to Mono for Android"
description: "This post is about the official #SNMP port to Mono for Android."
tags: SNMP Mono
permalink: /tritonmate-words-official-port-to-mono-for-android-6eb298f9a66
excerpt_separator: <!--more-->
---
As announced, my new laptop arrived last Monday. So this has been a fabulous week for me.

My very first task was to finish the official port to Mono for Android.
<!--more-->

And today I think I have done a lot,

1. Ported ANTLR 3.4 C# runtime to Mono for Android, https://github.com/lextudio/sharpsnmplib/blob/8.0/lib/MonoAndroid/Antlr3.Runtime.ma.dll (The source code is not yet available as I need to discuss with ANTLR maintainers to see how I can submit the patch to them.)
1. SharpSnmpLib.Mib.csproj has been ported to SharpSnmpLib.Mib.ma.csproj.
1. SharpSnmpLib.Optional.csproj is obsolete. All files are now part of SharpSnmpLib.csproj.

The experience of porting to Mono for Android is happy and painless, compared to the frustrating port to .NET CF 3.5 a few years ago,

* Mono for Android profile is almost identical to the full desktop profile, where I don't need to grad any Mono source files.
* The IDE integration works almost flawless in both Visual Studio 2010 and 2012.

I did find a bug of Mono for Android, that when I tried to change project properties sometimes the changes were lost for no reason. Anyway I can manually edit the project file as a workaround.

Sadly log4net is not yet ported to Mono for Android (this patch https://t.co/NdGuTp7K is not accepted by Apache yet), so I have to use #if everywhere to comment out log4net usage in the MIB assembly. I hope I can find a better way out later.

So the last bit of this task is to write a test utility to test out functionalities on the Android simulator. That should be fun and I am looking forward to it next weekend. It will be my first Mono for Android application!

Stay tuned.
