---
layout: post
title: "Building HTML Help on Windows"
description: This post talks about how to build HTML Help on Windows.
tags: Windows
permalink: /building-html-help-on-windows-88f2168cb4b1
excerpt_separator: <!--more-->
---
Microsoft released two versions of HTML help in order to replace its popular WinHelp format. And it seems Microsoft is so confident with these two new formats that it removes WinHelp support from Windows Vista (and possibly Windows Server 2008). Therefore right now if your application needs a help file, you should use either CHM or HTML Help 2 formats.
<!--more-->

For .NET developers, compilers make documenting of assemblies (DLLs and EXEs) much easier. But how to get things done? I believe you want to know. I am now demonstrating how to set up the environment for generating CHM format help files.

1. Download the CHM compiler from here and install it.
1. Download Sandcastle from here and install it.
1. Download Sandcastle Help Builder from here and install it.

Now you have all the toolset ready. Begin to configure your project in Visual Studio.

Open your project's Properties dialogue and switch to Build tab. Then you must check the XML documentation file box.

After building the project, you can see in the output folder a new XML file which contains XML comment extracted from your source code.

At last, launch Sandcastle Help File Builder GUI. You must learn how to create a new project in it because it is rather easy and I do not want to say more.

Press the compile button when you are done. Sandcastle compiler will start to finish those dirty tasks for you. If you meet no compile errors, congratulation! Your help file is ready.

You know I always hate to mention too many details because it is rather boring for me.
