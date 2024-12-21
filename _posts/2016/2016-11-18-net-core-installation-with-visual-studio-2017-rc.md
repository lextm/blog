---
layout: post
title: ".NET Core Installation with Visual Studio 2017 RC"
description: "This post is about what .NET Core bits are installed with Visual Studio 2017 RC."
tags: .NET Visual-Studio
permalink: /net-core-installation-with-visual-studio-2017-rc-e4fc1b4c5905
excerpt_separator: <!--more-->
---

Microsoft announced Visual Studio 2017 RC on Microsoft Connect so I guess you already have it installed on your machine while it is hot. So what exactly does this new release ship for .NET Core developers?
<!--more-->

![img-description](/images/net-core-installed.png)
_Figure 1: .NET Core bits installed along with Visual Studio 2017._

Well, easily you can see a list of installed products on your machine from Control Panel | Programs, whose names are really confusing. Let's try to understand them in the following way.

## .NET Core 1.0.0 Family
The 1.0.0 release was published in June. So the first three items are related to it.

* The Runtime is what our apps compile against and link with.
* The SDK contains the tooling we use such as dotnet commands.
T* he Windows Server Hosting should be ASP.NET Core module for IIS.

## .NET Core 1.0.1 Family
.NET Core 1.0.1 was published in September. So the last three items are for it.

* It has no Runtime installed. (Why?)
* It has two versions of SDK, Preview 2 and 3. SDK Preview 3 enables MSBuild support to replace project.json.
* It has VS 2015 Tooling Preview 2.

## My Guess
* 1.0.1 does not have an individual runtime because it is only a patched release and many bits can reuse 1.0.0's.
* Its Preview 2 SDK is provided to match 1.0.0 release. If any project with global.json mandates this SDK version, then it can still work.
* Preview 3 is the version that MSBuild support is back.
* Once the SDK and VS Tooling reaches RTM, we won't need to be confused by their versions.

I will do more digging to see what else I can find.
