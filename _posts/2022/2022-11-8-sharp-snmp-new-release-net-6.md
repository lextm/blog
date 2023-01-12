---
layout: post
title: "#SNMP New Release for .NET 6"
description: "A post about new release of #SNMP Library specific to .NET 6."
tags: Visual-Studio .NET SNMP
excerpt_separator: <!--more-->
---

.NET 7 is going to be released by Microsoft, but I just got sometime to finally release #SNMP Library 12.5. It has been a release driven mainly by the new features of .NET 6, so below I try to write more on what users should pay attention to.

<!--more-->

## Old .NET Framework Versions Are Dropped
Microsoft retired more legacy platforms in 2022, so this project follows the trend and only supports .NET Framework 4.6.2 and above in this release.

## Nullable Annotations
Microsoft has been working on nullable reference types for decades (even Anders Hejlsberg admitted that this should be added to C# many years earlier). But the adoption of this new language feature is rather painful, because it in general breaks too many things. But throughout the years, the syntax and tooling have been steadily improved.

In .NET 6, Microsoft is finally comfortable to [enable this feature on new projects](https://learn.microsoft.com/dotnet/csharp/nullable-references), so #SNMP Library starts to offer the same convenience. Behind the scenes, [the Nullable NuGet package](https://github.com/manuelroemer/Nullable) plays an important role as it enables nullable attributes on a variety of platforms that Microsoft left behind.

This is just the first release with nullable annotations enabled, so slight changes are expected in the future releases.

## Cancellation Token Support
Microsoft uses .NET Framework and .NET Core to explore how to better design async API in general, and many world class innovation proved the quality of the exploration. Concepts like async/await and cancellation tokens are widely adopted in other programming languages/frameworks. However, .NET itself didn't fully utilize cancellation tokens throughout the API surface, especially around socket API.

.NET 6 is the first release to add the long missing cancellation token based async API for socket related classes, so finally #SNMP Library can wrap over them to provide essential features like timeout control in async SNMP operations.

> Note that such new API can only be consumed in projects that target .NET 6 and above.

> Also note that in old projects there is really no easy fix. You have to close the socket object to stop async operations.

## Cryptography Uplift
In the early days of .NET Core, Microsoft mainly focused on popular cryptography algorithms. That's why for a period of time #SNMP Library users had to rely on [Bouncy Castle based providers](https://docs.sharpsnmp.com/tutorials/aes.html) for SNMP v3 operations. .NET 5 made fundamental changes in this field, so in 12.4 release #SNMP Library removed Bouncy Castle dependencies.

[.NET 6 closes more gaps now by introducing simplified API](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-6/#cryptography), which also boosts performance significantly. #SNMP Library has adopted all the required changes, but users might not even notice such.

## Side Notes
All other changes are minor or only useful for a tiny group of users.

12.5.1 was released due to a change that affects #SNMP Pro users, so it is not a mandatory update for other users.
