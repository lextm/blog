---
layout: post
title: "GrapeVine Voice: How To Debug"
description: "This post writes about how to debug GrapeVine."
tags: Code-Beautifier-Collection Delphi
permalink: /grapevine-voice-how-to-debug-8b21849e20b2
excerpt_separator: <!--more-->
---
There are a lot of debuggers I can choose from on Windows. They are,

1. .NET 2.0 SDK GUI Debugger. This debugger is part of .NET SDK. It is much similar to VS.NET debugger, but you cannot modify source files in it.
1. SharpDevelop Debugger. This debugger is still under development, so generally speaking is not powerful enough.
1. Visual C# Express Integrated Debugger. This debugger is most powerful.
<!--more-->

On Windows Vista, you should notice that if you want to debug an application that needs UAC elevation, you should elevate the debugger itself at first.

Debugging CBC is similar to debugging a library. You must set the parameters so bds.exe is launched. Ensure that the debug version of CBC is added to expert list with ExpertManager correctly (you should disable other CBC items).

You may notice log4net is used in CBC. The log file by default is in the same folder of bds.exe and named as cbc2.log. If you are on Windows Vista, you must manually edit cbc.exe.config. `.\cbc2.log` can be changed to, for example, `d:\cbc2.log`.

I will add other tips here if necessary.

Stay tuned.
