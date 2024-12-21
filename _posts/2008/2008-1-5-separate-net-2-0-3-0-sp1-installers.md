---
layout: post
title: "Separate .NET 2.0/3.0 SP1 Installers"
description: This post is about separate .NET 2.0/3.0 SP1 installers.
tags: .NET
permalink: /separate-net-2-0-3-0-sp1-installers-330e39e03ae1
excerpt_separator: <!--more-->
---
In the past few months, if you want .NET 2.0/3.0 SP1, the only installer is .NET 3.5 Framework installer. I believe that this is not feasible for everyone. And now at last Microsoft releases separate installers for them.

* .NET 2.0 SP1 (x86/x64/IA64)
* .NET 3.0 SP1

BTW, I found a Visual Studio 2005 Simplified Chinese installer issue. At first I only installed Visual C#. Then I installed .NET 3.5 which updated .NET 2.0 to SP1. Some day when I needed to install Visual C++ and J#, the installer cannot recognize .NET 2.0 SP1. Luckily it continued to install what I wanted for me without any big errors. So did Microsoft believe .NET 2.0 should never be patched after its release?
<!--more-->