---
layout: post
title: "#SNMP Design: Backport Flaw Or Best Practice"
description: "This post is about the technical challenges back porting #SNMP to C# 2.0 and Visual Studio 2005."
tags: SNMP
permalink: /snmp-design-backport-flaw-or-best-practice-2bbe343b98f6
excerpt_separator: <!--more-->
---

When Steve [finished the backport]({% post_url 2008/2008-12-6-snmp-design-backport-to-c-2-0-visual-studio-2005 %}) and discussed with me, both of us were aware that maintaining both VS2005 and VS2008 solution and project files are hard. Therefore, I began to research on that topic.

<!--more-->

A bug report set the fire bigger, so I made big progress too yesterday. Now we no longer have to maintain duplicate project files (\*.csproj) except separate solution files for each IDE. How we achieve this? Simple.

A lot of people meet such problems before us, so there are many posts available. After analysis, I found it impossible to share solution files, but it is possible to add VS2008 project files into VS2005 solution files (with some patches). Now let's see the steps if you already have VS2008 solutions and projects at hand and want to back port to VS2005.

1. Create a solution file for VS2005. Although it is not possible to only create a solution file in VS2005 IDE, you can start by creating an empty project and make sure of its solution file.
1. Add existing VS2008 projects into this solution from VS2005.

See how easy it is! But horrible warnings may be sent by VS2005 that a project is invalid. Don't panic 'cause it is normal. In such cases, you need to manually edit the \*.csproj file in NotePad. Simply replace the import tag with this one,

and you can finish step 2 now.

Have to confess it is rather easy to sync solution files, isn't it compared to sync project files? :)
