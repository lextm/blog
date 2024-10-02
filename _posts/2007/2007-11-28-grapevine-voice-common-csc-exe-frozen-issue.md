---
layout: post
title: "GrapeVine Voice: Common csc.exe Frozen Issue"
description: This post talks about that csc.exe may freeze when deserializing preferences.
tags: Code-Beautifier-Collection Delphi
permalink: /grapevine-common-csc-exe-frozen-issue-85bebd48a310
excerpt_separator: <!--more-->
---
When I started CBC in 2005, I never thought that there would be so many options I needed to provide. Therefore, it was in 2006 I began to search for preferences management system. And that's why serialization became the solution.
<!--more-->

The only problem of serialization is that deserialization process requires csc.exe to run in the background. And if the process is started by an IDE plug in, sometimes csc.exe freezes. I guess the freezing is caused by limited memory of the system but I am not sure.

Today, when I launch Visual Studio 2005 in a 300-M memory VM, I met the exact problem, too. Both GhostDoc and ReSharper have this issue. And you can imagine this issue only affects .NET written plug ins.

I do not know of any fix. The only workaround is to kill csc.exe and devenv.exe, then restart VS. Do you come across this issue? Do you have a better solution or fix?
