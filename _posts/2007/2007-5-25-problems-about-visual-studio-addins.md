---
description: This post describes some of my thoughts on Visual Studio.
excerpt_separator: <!--more-->
layout: post
permalink: /problems-about-visual-studio-addins-6ee50c6b2244
tags: visual-studio
categories: [Tools and Platforms]
title: Problems about Visual Studio Addins
---
When I designed Code Beautifier Collection I knew it was easy to install it. Just copy the assemblies to a folder and add a registry item under the BDS tree.

However, when I install a Visual Studio addin, usually devenv.exe will execute for a long time and consume a lot of memory. I have to say it is not convenient but there must be something under the hood.

I do not plan to write an addin for Visual Studio, so I will not go any deeper, but I think in this aspect, BDS has some advantage.
<!--more-->
