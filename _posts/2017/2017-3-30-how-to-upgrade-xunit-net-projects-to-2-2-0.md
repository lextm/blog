---
layout: post
title: "How to Upgrade xUnit.net Projects to 2.2.0"
description: "This post is about how to upgrade xUnit.net projects to 2.2.0."
tags: .NET Visual-Studio
permalink: /how-to-upgrade-xunit-net-projects-to-2-2-0-f8fb943b725d
excerpt_separator: <!--more-->
---

You already know Obfuscar uses xUnit.net for unit testing. It was [a .NET Framework 4.5 Class Library project](https://github.com/lextm/obfuscar/blob/2.2.2/Tests/ObfuscarTests.csproj). So now I simply upgraded its xUnit.net dependencies to latest 2.2.0 release, and wow Visual Studio 2017 refuses to show the test cases in Test Explorer.
<!--more-->

So what's up? Well, many small pieces.

* You have to upgrade the project to at least .NET Framework 4.5.2. I don't know why.
* You have to manually change one reference from xunit.execution.dotnet to xunit.execution.desktop. I don't know why the upgrade process chooses a wrong reference.

So the final project is [as below](https://github.com/lextm/obfuscar/blob/d7787fa1fe73265d3ce9400dbbe8e9148fe46924/Tests/ObfuscarTests.csproj).

Hope this can save you a few minutes when you hit the same issue.
