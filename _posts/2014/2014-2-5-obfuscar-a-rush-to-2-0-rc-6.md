---
layout: post
title: "Obfuscar: A Rush to 2.0 RC 6"
description: "This post covers RC 6, which contains accumulated bug fixes and new features."
tags: .NET
permalink: /obfuscar-a-rush-to-2-0-rc-6-c4eb72357d03
excerpt_separator: <!--more-->
---

[I blogged about RC 2]({% post_url 2013/2013-8-24-obfuscar-slightly-upgraded-and-2-0-rc-2 %}) a long time ago. This post covers RC 6, which contains accumulated bug fixes and new features.

<!--more-->

## Inclusion Rules

An important thing to notice is that Obfuscar only supports exclusion rules. That's because the original design follows this principle that everything should be obfuscated, unless it is excluded by a rule. The principle is simple but the real world is complicated. Thus, sometimes it is very difficult to write exclusion rules if you just want to exclude what you want. Thus, in RC 6 inclusion rules are added, which are named as Force\*.

If you know how to use the exclusion rules, Skip\*, you should be quite familiar with the new inclusion rules.

## KeepPublicApi and HidePrivateApi

If you don't want to write any rule but to achieve simplest obfuscation (all private/internal are striped out, and all public/protected remain), now you can use two new options,

```xml
<Var name="KeepPublicApi" value="true" />
<Var name="HidePrivateApi" value="true" />
```

Isn't that simple?

To learn more about the two new options and how rules are prioritized, please check the Wiki page.

## No More Un-renaming

A breaking change was introduced in RC 6, where if a series of classes/interfaces define a method group then all methods in the group must be obfuscated together or ignored together. Your rules cannot lead them to an inconsistent state.

In the past, Obfuscar tries to un-rename methods in the group which can lead to surprises and unintended information leak.

## HideString Bug

I was not familiar with Cecil at the very beginning, so when I attempted to fix the code base a bug was introduced in HideString function, where .NET 4's mscorlib is imported to all obfuscated assemblies mistakenly. This can lead to various issues, and luckily today I learned how to avoid that.

More unit test cases are now included, and after RC 6 we should see a final release very soon.
