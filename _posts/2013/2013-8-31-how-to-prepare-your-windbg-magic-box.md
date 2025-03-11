---
layout: post
title: How to Prepare Your WinDbg Magic Box
description: "This post talks about how to prepare your toolbox around WinDbg."
tags: Visual-Studio .NET
permalink: /how-to-prepare-your-windbg-magic-box-43b5e9ad8a03
excerpt_separator: <!--more-->
---

If you are an advanced developer that often needs to debug either native or managed Windows applications, you should be quite familiar with WinDbg, a low level debugger from Microsoft. It has a sharp learning curve, but is indeed the ultimate tool for debugging.

<!--more-->
## Grab The Basic Bits
The WinDbg installers can be found in latest Windows SDK downloads/images and I suggest you find an x64 machine and install both 32 bit and 64 bit of WinDbg.

OK, then let's create a single folder such as `E:\Debuggers\` on your machine, and copy both `C:\Program Files (x86)\Windows Kits\8.0\Debuggers\x64` and `C:\Program Files (x86)\Windows Kits\8.0\Debuggers\x86` directories to it.

> Note that the directories are available on Windows 8 after installing Windows 8 SDK.

OK. In the future we will only launch WinDbg from either `x86` or `x64` folder under `Debuggers`.

## Prepare the Symbol Path
Launch WinDbg from `E:\Debuggers\x64\windbg.exe`, choose `File | Symbol File Path …` and then type
`srv*e:\Debuggers\symbols*http://msdl.microsoft.com/download/symbols`
as `Symbol path`.

Click OK.

Click `File | Exit` and click Yes when a prompt appears.

After setting this, WinDbg will store symbols downloaded from Microsoft to the symbol folder we set.

## Download Famous WinDbg Extensions
SOSEX is a famous WinDbg extension for managed debugging. So let's download the bits from `http://stevestechspot.com/SOSEXV40NowAvailable.aspx` and then put the 32 bit dll in `E:\Debuggers\x86`, and 64 bit dll in `E:\Debuggers\x64`. Bitness must match.

We can do the same for PSSCOR2 and PSSCOR4. You can add other extensions you like follow the bitness rule.

## Accumulate .NET mscordacwks.dll
The patching mechanism of .NET Framework sometimes introduces new versions of `mscordacwks.dll`. As this is a critical part of .NET debugging, such updates can lead to a common issue called "Failed to load data access DLL, 0x80004005". So whenever we try to analyze a .NET application dump file captured from another machine, we should try to get `mscordacwks.dll` and `sos.dll` from that machine (pay attention to .NET Framework version used by that application, and process bitness). If the failure occurs when we try to execute a command in SOS, please rename the received `mscordacwks.dll` to the proper name mentioned in the WinDbg error message (as that's the name expected) and then put it into either `E:\Debuggers\x64` or `E:\Debuggers\x86` to match the bitness. Then you should be able to analyze the dump.

> There is a tool called Mscordacwks Collector to help you get the files. Find it on [GitHub](https://github.com/mscordacwks/MscordacwksCollector).

> Note that under some scenarios you even need to explicitly load the `sos.dll` received. For example, debugging a .NET 4.0 dump on a .NET 4.5 installed machine is such a case.

## The End
OK, if you have followed the tips and prepare the folder, then `E:\Debuggers` becomes your magic box for debugging, as it contains almost every bits you need.

Under corporate network, you can even share this folder with others, so they can be enabled by your magic (just remember that on another machine the symbol path should be adjusted a little bit).
