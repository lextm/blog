---
layout: post
title: "Obfuscar: Slightly Upgraded and 2.0 RC 2"
description: "This post talks about Obfuscar 2.0 RC 2."
tags: .NET
permalink: /obfuscar-slightly-upgraded-and-2-0-rc-2-ba25398933e7
excerpt_separator: <!--more-->
---
Do you think that I have abandoned this project? No, no, that's not the case. In a few minutes I am going to upload a new build to Obfuscar homepage, which contains many critical bug fixes. They address many typical obfuscation scenarios and important open source libraries. So make sure you visit the download page and check out the latest.
<!--more-->

The following are the most significant changes made since RC 1,

## Initial BAML Support

WPF applications embed BAML in the executable, so that at runtime the type names stored in BAML files are verified and converted to live objects. As a result, normal obfuscation on type names cause type resolution failures as the untouched type names cannot be resolved at runtime.

A complete fix should be able to update the names in BAML files, but I was not able to spare enough time on that subject. So [a quick workaround](https://github.com/lextm/obfuscar/commit/d0b825c2b6f998421f0da80bba4e2db9d69432d3) is used that we simply ignore types who are referred in BAML. Once I have enough time, I will try to complete the BAML update algorithm.

## Heavily Nested Types

When I tried to obfuscate DockPanel Suite I found that some exceptions occurred in the final applications. By tracking down to source code I can see that the original algorithm made an assumption that in the code only one level of nesting exists for nested classes. Of course this is a wrong assumption, especially for DPS, where many internal types are in fact heavily nested.

By slightly [modifying the algorithm](https://github.com/lextm/obfuscar/commit/be1c23adaee1d5d45abc33efbc0759b9e40bdd63) we easily get DPS obfuscated correctly.

## Generic Instance Method

Another issue was found when obfuscating Microsoft Unity that some method references were not updated even though the method definition had already been modified.

After some debugging it is obvious that only generic instance methods trigger the bug, as whenever they appear they are both a declaration (instantiating the generic definition with a concrete type) and reference (referring to the original generic method definition). Knowing this, [a fix can be easily found](https://github.com/lextm/obfuscar/commit/eb176c9dd1487ca061656bbc40a3327a8c54f6b5), by treating such methods differently during method reference scan and renaming.

So now Obfuscar fully supports more .NET assemblies including ANTLR 3, #SNMP Library, SharpSnmpPro.Mib, DockPanel Suite, and Microsoft Unity.
