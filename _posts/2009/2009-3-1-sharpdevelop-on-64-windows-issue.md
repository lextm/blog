---
layout: post
title: "SharpDevelop on x64 Windows Issue"
description: "This post is about the issue I met when using SharpDevelop on Windows 7 x64 build 7000."
tags: Windows .NET
permalink: /sharpdevelop-on-x64-windows-issue-2e845c12cdc1
excerpt_separator: <!--more-->
---
SharpDevelop is my main IDE when developing Code Beautifier Collection, Alex and #SNMP. But now as I use Windows 7 x64 build 7000 as my workstation at home, this IDE starts to show a few issues. Luckily the one I met today was documented in this old thread.

http://community.sharpdevelop.net/forums/p/7562/21398.aspx#21398
<!--more-->

So here is the steps I took to make things work again.

1. Launch an elevated Visual Studio Command Prompt (you may use .NET Framework 2.0 SDK Command Prompt if you don't have VS installed).
1. Navigate to PartCover folder. By default it should be `C:\Program Files (x86)\SharpDevelop\3.0\Bin\Tools\PartCover`.
1. Execute `corflags partcover.exe`. Make sure that it shows 0 for 32BIT and 1 for Signed like mine.
1. Execute `corflags partcover.exe /32BIT+ /Force`.
1. Now execute `corflag partcover.exe`. If it shows 1 for 32BIT and 1 for Signed you are done.
1. Download the snk file from this link. I choose `C:\Users\lextm\Downloads\PartCover.Console.snk`.
1. Execute `sn -R PartCover.exe c:\users\lextm\downloads\partcover.console.snk`. This will resign the executable so it is strong named again.
1. Execute `corflags ..\NUnit\nunit-console.exe`. Make sure that 32BIT is 0 and Signed is 0.
1. Execute `corflags ..\NUnit\nunit-console.exe /32BIT+`.
1. Execute `corflags ..\NUnit\nunit-console.exe` again. Now you are done if 32BIT is 1.

Good luck.
