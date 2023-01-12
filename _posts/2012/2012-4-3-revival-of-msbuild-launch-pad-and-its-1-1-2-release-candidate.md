---
layout: post
title: "Revival of MSBuild Launch Pad and Its 1.1.2 Release Candidate"
description: "This post is about the revival of MSBuild Launch Pad and its 1.1.2 release candidate."
tags: .NET
permalink: /revival-of-msbuild-launch-pad-and-its-1-1-2-release-candidate-d8a915e8366a
excerpt_separator: <!--more-->
---
I haven't been updating mPad for a long time (since June 11, 2011). There was no strong drive because all major features have been implemented (though ugly, they work). I kind of forgot about it till this bug report came a few weeks ago.

Alright, finally I got all the necessary details about the crash, and started to fix it. But was that all I could do this time? Nope :) I have explored a lot.
<!--more-->

## NuGet Packages

This has been the best way to publish your .NET libraries (I published #SNMP Library to NuGet last October). But today is the first time I tried to consume packages in the NuGet way.

First, I removed nunit assembly from lib folder and UnitTests project reference list. Then within Visual Studio 11, I chosed Manage NuGet Packages… menu item from the context menu in Solution Explorer. Well, after that it is easy to search online for the latest NUnit package, and add it to UnitTests project. The magic is that NuGet automatically downloads the package to packages folder, extracts contents, and adds the correct reference for me. So of course I added moq in the same way.

To make sure that I don't need to check in NuGet packages to source control, I followed this article,

http://docs.nuget.org/docs/workflows/using-nuget-without-committing-packages

Now dependencies can be easily managed. (NuGet is Mono friendly, too).

## More Unit Testing

It was not easy to write a unit test case for MSBuild path resolution (MSBuildTask.FindMSBuildPath), but this time using moq I can fake the path validation part, and simulate the following scenarios effortlessly, so all test cases can be easily written,

* .NET 2
* .NET 3.5
* .NET 4.*
* .NET 2 + .NET 4.*
* .NET 3.5 + .NET 4.*

> .NET 4.* means either .NET 4 or .NET 4.5.

## Less Hardcoded Information

In previous builds, .NET Framework versions and MSBuild path were almost all hardcoded in C# files. If .NET 4.5 were not an in-place upgrade of .NET 4, I would have to change a lot of lines to support it.

So in the past few days, I extracted all such information into the app.config file, and wrote custom section to handle them. Now if Microsoft decide to release .NET Framework 5 and Visual Studio 12, I guess I can support them by simply updating the app.config file :)

You can receive our latest change sets to see how the above changes have been made.

Don't forget to download the latest 1.1.2 RC.

Stay tuned.
