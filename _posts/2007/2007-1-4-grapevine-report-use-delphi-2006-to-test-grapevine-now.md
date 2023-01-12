---
layout: post
title: "GrapeVine Report: Use Delphi 2006 to test GrapeVine now"
description: "This post reports the progress of GrapeVine."
tags: Code-Beautifier-Collection Delphi
permalink: /grapevine-report-use-delphi-2006-to-test-grapevine-now-75458ab97c9f
excerpt_separator: <!--more-->
---
(CSDN Jan 04, 2007)

What is GrapeVine?

What is GrapeVine? If you do not remember, remind you that it is the next major version of Code Beautifier Collection exclusively for BDS 5. There are a few things I have to finish before its birthday.
<!--more-->

First, surely it will be compiled against .NET 2.0. It is easy to compile HardQuery against .NET 2.0. When NAnt was used to compile the assemblies, -t:net-2.0 is sufficient. It is not hard for MSBuild projects now, if you compile CBC without MSBee installed or referenced.

Second, debug and test GrapeVine in the BDS IDE. If you build CBC on .NET 2.0 and try to load it in BDS 2006, you will see an exception because BDS 2006 or in fact .NET 1.1 runtime can not understand the assembly file format.

Now CodeGear R&D is working hard on Highlander, or Delphi 2007, which will support .NET 2.0 and 3.0. It can be sure that this IDE will be running on .NET 2.0 and must be able to load GrapeVine. However, I have not applied to the test project. Why? I can easily test GrapeVine builds now using Delphi 2006 with only one line of code modified.

If you ever take a deep look into bin folder of Delphi 2006 installation, you will see a file named bds.exe.config. It is apparent that bds.exe is a Win32 executable, but why does it need a .NET configuration file? Open it in Notepad and you will see something very interesting. Yes, it defines what version of .NET runtime BDS should use.

If you change it to .NET 2.0, well, BDS 4 loads .NET 2.0 runtime and runs on it. After this modification, CBC GrapeVine which is compiled against .NET 2.0 can be loaded and tested.

## How I find this method?

Did you use C#Builder 1.0 ever? When you install .NET 2.0, you will see a strange but cute thing happening. C#Builder 1.0 will mistakenly run on .NET 2.0, and this change will prevent you from developing in it. For example, all forms you create then will be .NET 2.0 forms and cannot be compiled against .NET 1.1.

BTW, even if you change bds.exe.config you cannot easily develop .NET 2.0 projects in BDS 1–4 because they lack a lot of necessary supports.

## Another Hint

In last year I thought it was impossible for BDS 1–4 users to use GrapeVine. However, now I see some possibilities. If you are using Delphi 8/2005/2006, and focusing exclusively on Win32 platform, you can modify your bds.exe.config file as described above. After that, you can enjoy the fun GrapeVine provides. But if you are working on .NET and using C# or Delphi for .NET, you have to upgrade to BDS 2007/Highlander.
