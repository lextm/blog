---
layout: post
title: "CatPaw Rumors: The Solution Files"
description: "This post is about the solution files in #SNMP 5 codebase"
tags: SNMP
permalink: /catpaw-rumors-the-solution-files-3cf989f268fe
excerpt_separator: <!--more-->
---
(Updated to latest for our release 5.0 development)

We ship many solution files in #SNMP 5 codebase for different Visual Studio IDE versions (default one for VS2010, vs2008 for VS2008), and platforms (cf3 for .NET CF 3.5).
<!--more-->

From now on I make the following rules,

1. The default VS version I use is Visual Studio 2010, so the default solution file is the standard one who contains all projects.
1. Other solution files contain only the core projects (for #SNMP Library and so on).
1. The CF solution only contains one project. That's SharpSnmpLib.dll.

Why? Different Visual Studio versions have incompatibilities, especially in visual designers. That explains why new VS version always asks to upgrade project files created by an older version. To avoid mysterious issues related to such incompatibilities, only core projects (who has no visual parts) are shared among different solution files.
