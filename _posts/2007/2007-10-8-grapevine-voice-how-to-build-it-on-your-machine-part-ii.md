---
layout: post
title: "GrapeVine Voice: How To Build It On Your Machine (Part II)"
description: "This post is part ii on how to build GrapeVine on your machine."
tags: Code-Beautifier-Collection Delphi
permalink: /grapevine-voice-how-to-build-it-on-your-machine-part-ii-a6f1c5577e76
excerpt_separator: <!--more-->
---
In this post I talked about how to build CBC HardQuery Release 2 Update 3 (5.3.3). However, GrapeVine (6.0) introduces many changes so it worths another post like this.
<!--more-->


* Now MSBee is no longer needed. And you should install Inno Setup Quickstart Pack instead of Inno Setup (because ISPP is now necessary).
* Another thing you should notice is that SharpDevelop 2.2 cannot open the solution any more because I am now using SharpDevelop 3.0 Alpha.
* The most important thing you may not notice is that you need to install .NET Framework 3.5 in order to make the batch file running.
* AssemblyInfo Task is also a necessary part and it must be installed into GAC.
* And if you have set up the environment right, the batch files can be used to build GrapeVine.

In next post I will talk about how to debug GrapeVine. It is very important to notice debugging on Windows Vista is rather different.

(Update: Please check out GrapeVine source code from its SVN repository according to this guide.)