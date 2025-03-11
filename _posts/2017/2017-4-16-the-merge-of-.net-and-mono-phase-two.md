---
layout: post
title: "The Merge of .NET and Mono: Phase Two"
description: "This post is about the second phase of the merge of .NET and Mono."
tags: .NET Mono
permalink: /the-merge-of-net-and-mono-phase-two-6442efc11331
excerpt_separator: <!--more-->
---

> You can find [phase one post here]({% post_url 2017/2017-4-16-the-merge-of-.net-and-mono-phase-one %}).

The relationship between Mono and Microsoft .NET teams have been closer and closer in the past few years. We can see Miguel de Icaza showed his appreciation multiple times at different circumstances (C# compiler async/await support, PCL support, and BCL documentation for example).

<!--more-->

If we roughly dissemble Mono to modules, then we can see the following,

- Mono CLR
- Mono BCL
- Mono C# Compiler
- xbuild
- Other libraries

Based on the public information from different Mono sources, we can see the following actions are being executed,

1. Mono BCL will further incorporate Microsoft source code from .NET Framework and .NET Core. One day there should be no significant difference between Mono BCL and .NET BCL.
1. Mono 4.x started to ship Roslyn compilers and MSBuild to test compatibility. In the upcoming Mono 5.x releases, those two would become the default. Mono C# compiler and xbuild would soon be obsolete.
1. .NET Core CLR is quite modular, and the possibility of integration is being investigated.
1. Many libraries start to support .NET Framework/.NET Core, and Mono.

If you run latest Visual Studio for Mac build, you should have been using Mono 5.x already. Enjoy it and report bugs, so that we can all help Mono and .NET out.
