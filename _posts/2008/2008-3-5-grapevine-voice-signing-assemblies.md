---
layout: post
title: "GrapeVine Voice: Signing Assemblies"
description: This post talks about signing assemblies.
tags: Code-Beautifier-Collection Delphi
permalink: /grapevine-voice-signing-assemblies-1fdc8737cb52
excerpt_separator: <!--more-->
---
Compared to Visual Studio/SharpDevelop, Delphi for .NET lacks a few IDE elements. One of them is the signing support.

In SharpDevelop, it is so easy to sign an assembly.

If you do not have a key file already, a key file can be generated for you by clicking .

However, in Delphi for .NET, all you get is this.

So how to generate a key file yourself? When I was a newbie I did not know until I read the readme file of .NET SDK 2.0. Using sn.exe is not hard but is it intuitive?

That's why now I add an item in Project Aid of CBC.

Click this item and CBC will generate a key file for you and add it to your project. The result is like this,

At last, you can easily sign your assembly with this key file,

This feature will be available in 6.0 Update 1.

Stay tuned. I will try to enhance Delphi for .NET support in CBC as well as Delphi for Win32 support.
<!--more-->
