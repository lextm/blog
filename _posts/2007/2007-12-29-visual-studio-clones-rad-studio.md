---
description: This post is about features Visual Studio clones from RAD Studio.
excerpt_separator: <!--more-->
layout: post
permalink: /visual-studio-clones-rad-studio-c8aba372adc3
tags: .net visual-studio
categories: [Programming Languages]
title: Visual Studio Clones RAD Studio?
---
After releasing Visual Studio 2008, MSBuild team asks its users what should be implemented in next version of Visual Studio. It is funny to see the following items are highlighted,

Make .sln files MSBuild compliant.
Make .vcproj files MSBuild compliant and remove VCBuild.
Why I find them funny? Because CodeGear RAD Studio 2007 already makes all project group files and project files MSBuild compliant. Take a look at .groupproj/.dproj/.cproj files you will see MSBuild script.

I was wondering why there was no .sln files in RAD Studio. At last I know that .groupproj files are much more convenient than .sln files.
<!--more-->