---
layout: post
title: "InstallAware Runtime Authoring"
description: "This post is about how to author InstallAware runtimes."
tags: Windows
permalink: /installaware-runtime-authoring-ec8d08213f1c
excerpt_separator: <!--more-->
---
It is nice to see InstallAware 7 bundled lots of runtimes. As a result, you can easily add .NET runtimes and other into your installer. The magic is that the runtimes can be included in one executable setup.exe if you let IA generate Single File from your project.
<!--more-->

However, sometimes your applications need extra runtimes that are not listed in IA. What to do next? It is easy to write your own runtimes and share with others.

I created a runtime package for WinPcap last week and published it on IA forum. It is funny that MSIcode is easy to author (just drag and drop) but hard to master (you need to read a few examples before diving to it). I started by reading this post, and it helped me a lot.

http://www.installaware.com/forums/viewtopic.php?t=2898

http://www.installaware.com/forums/viewtopic.php?t=1096

Later I will try to write a Mono runtime package because now Mono has implemented 98% of System.Windows.Forms classes and methods maybe I could use it someday without Microsoft .NET runtime installed. Yes, it is quite possible.

http://dufoli.files.wordpress.com/2007/09/mwf-class-status.jpg

Did you create runtime packages for IA. Better share it on the forum so everyone can enjoy your work.
