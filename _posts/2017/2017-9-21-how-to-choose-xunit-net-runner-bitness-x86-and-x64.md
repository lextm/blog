---
layout: post
title: How to Choose xUnit.net Runner Bitness (x86 and x64)
description: This post is about how to choose xUnit.net runner bitness (x86 and x64) in console or Visual Studio.
tags: .NET Visual-Studio macOS xUnit
permalink: /how-to-choose-xunit-net-runner-bitness-x86-and-x64-11f1fb540478
excerpt_separator: <!--more-->
---
You clearly know that xUnit.net has many runners,

* Console runners
* Visual Studio runner
* Visual Studio for Mac/MonoDevelop runner

But if your unit test cases require certain bitness (x86 or x64), what should you do accordingly?
<!--more-->

## Console Runners
It cannot be any easier for console runners, as xUnit.net ships a console tool for x86 (xunit.console.x86.exe) and the other for x64 (xunit.console.exe).
Here I show how I use them in [Obfuscar CI script](https://github.com/obfuscar/obfuscar/blob/2.2.33/test.bat)

If you are using .NET Core, then you probably know the command `dotnet test` you should use `-a x64` or `-a x86`.

## Visual Studio Runner
You would be surprised to notice that xUnit.net configuration does not cover bitness at all from its documentation. But that's perfectly normal as Visual Studio has its builtin support, [as documented in this article](https://docs.microsoft.com/en-us/visualstudio/test/configure-unit-tests-by-using-a-dot-runsettings-file).

So by serving a `.runsettings` file, you can easily switch between x86 and x64,

``` xml
<?xml version="1.0" encoding="utf-8"?>  
<RunSettings>  
  <!-- Configurations that affect the Test Framework -->  
  <RunConfiguration>  
    <!-- [x86] | x64    
      - You can also change it from menu Test, Test Settings, Default Processor Architecture -->  
      <TargetPlatform>x64</TargetPlatform>
  </RunConfiguration>  
</RunSettings>
```

## Visual Studio for Mac/MonoDevelop Runner

> Update in 2019: The following paragraphs were written when users needed to use a third party extension to run xUnit.net test cases in VS for Mac. Today, you should follow [the following discussion instead](https://developercommunity.visualstudio.com/content/problem/357275/64-bit-unit-testing-is-not-supported.html).

As I am the current maintainer of the xUnit.net extension for these IDE products, I can confirm that before today you have no choice at all but to run the test cases in x86 only.

However, today two releases have been published (0.7.9 and 0.7.10) to fill this gap. The configuration is similar to Visual Studio, but with slight differences.
To get started, you can create a file named `xunit.runsettings` in your unit test project to hold the same settings you use in Visual Studio. However, the file name must match exactly (as Visual Studio for Mac and MonoDevelop do not allow you to select any `.runsettings` file, so I decide to use a hardcoded name).
If you decide not to use `.runsettings` file, then you can set an environment variable `MONODEVELOP_XUNIT_RUNNER_BITNESS` to `x86` or `x64`. Finally, if neither `.runsettings` nor the environment variable is detected, the default behavior is to use the x64 runner.

Hope you enjoy [the latest release](https://github.com/xunit/xamarinstudio.xunit/releases/tag/v0.7.10).
