---
layout: post
title: Make Obfuscar A Global Tool in.NET Core
description: How to transform Obfuscar into a .NET Core Global Tool, making it easier to install, update, and use across platforms including Windows, macOS, and Linux.
tags: .net open-source obfuscar
categories: [Programming Languages]
permalink: /make-obfuscar-a-global-tool-in-net-core-1cc3ee2cfe30
excerpt_separator: <!--more-->
image:
  path: /images/night-montreal.jpg
  alt: Copyright © Lex Li. One night, Montreal.
---

In the past it is hard to distribute command line utilities for developers. For example, when I started to work on Obfuscar, there was hardly a way to release the tool to end users and provide a simple update mechanism.

The temporary solution I chose was to publish NuGet packages (which provides the update mechanism), but still users found it hard to call the command line utility from the NuGet cache folder (even with some MSBuild hack). [A sample project was published at GitHub](https://github.com/lextm/obfuscar_example), merely to show how to use the command line.
<!--more-->

Luckily [.NET Core SDK 2.1 Preview 1](https://blogs.msdn.microsoft.com/dotnet/2018/02/27/announcing-net-core-2-1-preview-1/) was released a few days ago, and it starts to support Global Tools. Finally I can make Obfuscar a good citizen on your machine,

``` batch
$ dotnet install tool -g Obfuscar.GlobalTool --version 1.0.0-beta1
```

Then it is super easy to launch Obfuscar from command prompt or bash

``` batch
$ obfuscar --help
```

Next time I publish an update, you should be able to see an update hint.

You probably also notice this build of Obfuscar runs on macOS and Linux. That's because behind the scene I modified the code base to run on .NET Core. The current limitation is that certain features (like BAML) have to be disabled/removed, as they require Windows specific features. I will try to address them in the coming builds.

Stay tuned.
