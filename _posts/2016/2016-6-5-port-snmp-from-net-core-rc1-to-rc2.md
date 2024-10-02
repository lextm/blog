---
layout: post
title: "Port #SNMP from .NET Core RC1 to RC2"
description: "This post is about how I port #SNMP Library from .NET Core RC1 to RC2."
tags: SNMP .NET
permalink: /port-snmp-from-net-core-rc1-to-rc2-141207cbe4f
excerpt_separator: <!--more-->
---
You probably read my first post on how to migrate from .NET Framework to .NET Core RC1. Now it is time to update the code base to RC2. [The actual commits](https://github.com/lextudio/sharpsnmplib/commits/netcore5) were made two weeks ago. So this post will cover the necessary details.
<!--more-->

## .NET Core RC2 ABC
The tooling started with `k` and `kvm` (a reminder of JVM, as K is the adjacent letter), and then became `dnx` and `dnvm` in RC1. With more confusion, RC2 introduced the new `dotnet` command to replace them all. You are warned that this is not yet the end. The tooling is still called Preview 1, which means we should expect more changes in the next few months.

Luckily the core libraries are already quite stable, so I just need to modify the project.json file to match [the latest specifications](https://github.com/lextudio/sharpsnmplib/commit/36017c8112ab3665303fcb20b66c27b2032c9257).

The `dotnet5.4` to `netstandard1.3` change has been known for months, and finally I can make it. Several packages in RC1 have been split into smaller packages in RC2, so you noticed more package references. The previous [package search site](http://packagesearch.azurewebsites.net/) is still functional.

So make sure you use it smartly.

## Conditional Defines

As I decided to keep .NET Framework 4.5 around, [conditional compilation is required](https://github.com/lextudio/sharpsnmplib/commit/dd7bf11af1a959ffb5576e7fb432b11a8d3d60a3).

I dug further in the above commit, and learned how to use `define` under `buildOptions` in project.json to define the constants I want to use (`net451` and `netstandard13`). Then I successfully moved many more classes from full .NET Framework to .NET Core.

However, there are still missing pieces to fill which I will leave for the future.

## Conclusion

The official guide from Microsoft is a must-read,

https://docs.asp.net/en/latest/migration/rc1-to-rc2.html

Without installing RC2 properly and performing the basic steps (such as global.json), you probably will get lost easily.

From now on, please clear `k/kvm/dnx/dnvm` from your mind, and focus on `dotnet` (well, I could not tell how long can `dotnet` live).

I personally believe Microsoft would ship .NET Core 1.0 on time by the end of this month, but the tooling is still far from complete. If you are not a hard core developer with plenty of time to try (and try as hard as you can), the advice is "wait wait wait".
