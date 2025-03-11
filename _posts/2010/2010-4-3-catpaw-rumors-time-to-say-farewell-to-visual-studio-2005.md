---
layout: post
title: "CatPaw Rumor: Time To Say Farewell to Visual Studio 2005"
description: "This post is about the fact that CatPaw will drop Visual Studio 2005 support."
tags: SNMP Visual-Studio
permalink: /catpaw-rumor-time-to-say-farewell-to-visual-studio-2005-2a0313501950
excerpt_separator: <!--more-->
---
This weekend, I started to use Visual Studio 2010 as primary IDE instead of Visual Studio 2008.
<!--more-->

This change leads to the following changes,

1. I decided to drop Visual Studio 2005 solution support. This means that I don't expect you to build from source code from within Visual Studio 2005 or with .NET 2.0 MSBuild. Visual C# 2008 Express or .NET 3.5 MSBuild is now the minimal requirement.

   *The library assemblies, (SharpSnmpLib*.dll) are still compiled against .NET 2.0, so you can continue using them if you cannot afford .NET 3.5 or .NET 4.0.

1. I started to use C# 3.0 language features extensively. The drop of Visual Studio 2005 guarantees this change. Now I can feel free to use LINQ, lambda expression, and others, which makes my life easier and happier.
1. The Agent, Browser, and Compiler started to target .NET 3.5 due to Unity 2.0 dependency.
1. All build scripts are now using .NET 4 MSBuild.

Primarily speaking, we are now .NET 4 ready, and only supports two versions of Visual Studio (2008 and 2010). Thanks for MSBuild multitargeting feature, our core assemblies can still target .NET 2.0.

Stay tuned as I will blog more about our upcoming release (5.0, CatPaw).
