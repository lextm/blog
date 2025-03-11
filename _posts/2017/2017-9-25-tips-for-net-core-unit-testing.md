---
layout: post
title: Tips for .NET Core Unit Testing
description: This post is about tips for .NET Core unit testing with xUnit.net.
tags: .NET Visual-Studio macOS xUnit
permalink: /tips-for-net-core-unit-testing-92a8d123a17a
excerpt_separator: <!--more-->
---
If you are managing an open source library for the community like I do, the introduction of .NET Core/.NET Standard is a bless and curse. Special care must be taken so as to make unit testing platform complete and issue free. Here I share some tips I learn from the process.
<!--more-->

## Multiple Target Frameworks

Like I did in #SNMP Library to use multiple target frameworks (`netstandard1.3` and `net452`), the associated unit testing project can be made to utilize multiple target frameworks (`netcoreapp1.0` and `net452`), so that `dotnet test` command can execute the test cases for both .NET Core 1.0 and .NET Framework 4.5.2,
``` xml
<PropertyGroup>
    <OutputType Condition="'$(TargetFramework)'!='net452'">Exe</OutputType>
    <TargetFrameworks>netcoreapp1.0;net452</TargetFrameworks>
</PropertyGroup>
```
You must make sure to use the extra `Condition` to avoid a compilation error,
``` bash
CSC : error CS5001: Program does not contain a static 'Main' method suitable for an entry point
```

## xUnit.net Versions

If you are an xUnit.net user like I am, you probably should notice the differences of 2.2.0 and 2.3.0 (in beta, 2.3.0-beta5-build3769) right now and be confused.

So its 2.2.0 is the very first major release with full .NET Core tooling integration, so that you can use `dotnet test` command to run xUnit.net based test projects. **Please verify that you are using all related NuGet packages with version number "2.2.0"**.

Its 2.3.0 is currently in beta, which introduces the new `dotnet xunit` command, which provides much more features than `dotnet test`. However, as it is still under development, **avoid using it for your projects if you can**. I personally experienced various issues when testing out this release with #SNMP Library, where it significantly increases the probability of testing failures (many test cases are socket based).

Even for 2.2.0 release, the probability of testing failures can be observable, which forces me to run unit testing and integration testing separately. This applies to #SNMP Library and might also apply to your projects.

## xUnit.net Visual Studio Runner

Just notice that if you use multiple target frameworks, then the xUnit.net VS runner (2.2.0) might not be able to detect the test cases. A workaround is to temporarily set net452 only,

``` diff
- <TargetFrameworks>netcoreapp1.0;net452</TargetFrameworks>
+ <TargetFrameworks>net452</TargetFrameworks>
```
**Remember not to check in this workaround to the source control system.**

You might refer to [#SNMP Library code base](https://github.com/lextudio/sharpsnmplib) to learn more about the setup.
