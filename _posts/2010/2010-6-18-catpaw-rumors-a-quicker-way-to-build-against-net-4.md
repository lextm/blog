---
layout: post
title: "CatPaw Rumors: A Quick Way to Build Against .NET 4"
description: This post is about a quick way to build against .NET 4.
tags: SNMP
permalink: /catpaw-rumors-a-quick-way-to-build-against-net-4-88b7fad6d346
excerpt_separator: <!--more-->
---
Starting from 5.0 release, you can build #SNMP thing against .NET 4 simply via command line.
<!--more-->

The trick on Windows is like this,

1. Open a Visual Studio 2010 command prompt and navigate to the folder that contains `sharpsnmplib.sln`.
1. Execute

   ``` text
   msbuild sharpsnmplib.sln /p:TargetFrameworkVersion=v4.0
   ```

Then all resulting assemblies are linked against .NET 4 version of `mscorlib.dll`, and so on.

This is much easier than opening all `csproj`/`vbproj` files and modifying them. Right?

Of course, this trick applies to our upcoming 6.0 release, HoneyCell.
