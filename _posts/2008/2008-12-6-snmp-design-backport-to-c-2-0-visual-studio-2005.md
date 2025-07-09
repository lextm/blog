---
layout: post
title: "#SNMP Design: Backport to C# 2.0/Visual Studio 2005"
description: "This post is about the work to back port #SNMP to C# 2.0/Visual Studio 2005."
tags: SNMP .NET Visual-Studio
permalink: /snmp-design-backport-to-c-2-0-visual-studio-2005-253d6b099c55
excerpt_separator: <!--more-->
---
Steve contributed a lot by back porting the library to C# 2.0. This is out of my original plan. This port was required because Visual Studio 2005 becomes Steve's primary platform lately. It is interesting to notice that only a few classes modified. Well, luckily I stopped using a lot of C# 3.0 specific features when I realized they will probably prevent such a port in late August.

However, here comes a small problem. Now we need to keep VS2005 and VS2008 project files in sync. Before an automatic way is found, manual sync is a must. In order to reduce the sync effort, during the release cycle we will focus on VS2005 project files and sync changes to VS2008 files whenever a release is coming. From now on please always use VS2005 project files for source code in the repository. Otherwise, you may find some projects broken.

Stay tuned.
<!--more-->
