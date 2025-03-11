---
layout: post
title: The End of Mono
description: A look back on the Mono history can easily tell that it can be a risky platform to use in 2021 and beyond.
tags: Mono Microsoft Linux Xamarin .NET
categories: [History, .NET]
excerpt_separator: <!--more-->
---

If today you still run an application on Mono, I suggest you think twice whether that decision is sustainable. A look back on the Mono history can easily tell that it can be a risky platform to use in 2021 and beyond.
<!--more-->

## 2000-2003
Though limited information is publicly available, we might assume the passion to bring C# to Linux was the primary driving force.

## 2003-2008
Novell's acquisition of Ximian seemed to add enterprise needs to the driving factors, so that things like WinForms on Mono were added and improved.

## 2008-2021
The collaboration with Unity3D (later renamed to Unity) and the shift to mobile (iOS/Android) significantly move the focus towards gaming and mobile platforms. 

It is certain that the core Mono bits (CLR and BCL) have been actively maintained and improved to empower Xamarin and Unity, compared to very limited (if not none) investment on Web stack/WinForms. GTK# still received some updates, because MonoDevelop/VS for Mac relied on it.

## 2021-2024
.NET 5/6 has cherry picked the most important asset (MonoVM/MonoCLR), so gaming/mobile platforms are now migrating to .NET 6,

* Visual Studio for Mac, one of the biggest Mono based applications, has just [migrated to .NET 6 as well native Mac UI](https://docs.microsoft.com/visualstudio/releases/2022/mac-release-notes-preview#1700-pre5--visual-studio-2022-for-mac-version-170-preview-5-newreleasebutton). It no longer needs Mono or GTK#.
* Xamarin bits have almost migrated to .NET 6 as MAUI. .NET 7/8 is aiming to fills up more gaps.
* Unity is [migrating to .NET CoreCLR](https://blog.unity.com/technology/unity-and-net-whats-next), and expects to finish in 2024.

The driving force to maintain the very large Mono distribution has shrunk significantly.

> Meanwhile, you can see [here](https://discord.com/channels/732297728826277939/732325020738519091) how engineers like Jo Shields and Alexander Köplinger are trying their best to keep the Mono distribution alive and answering tough questions. I am very grateful for their efforts. But should you bet your production applications on a small group of volunteers?

As many said, .NET 6 and above is going to be the right platform you migrate to. Microsoft/Unity and other companies in the ecosystem have already invested a lot there.

## 2024 and Beyond
Once [Xamarin is fully deprecated by .NET MAUI on May 1, 2024](https://dotnet.microsoft.com/platform/support/policy/xamarin) and Unity ships its new release to fully switch to .NET CoreCLR, we should expect no more commits to the GitHub Mono repo(s) from Microsoft. And that concludes the long journey to unify .NET runtimes.

It is your freedom to stay on Mono, and have no plan to migrate to .NET Core, but then it would be your own adventure to support yourself.

## Reference

* [History of .NET/Mono](https://corefx.lextudio.com/)
* [Downward trend of Mono commits, since 2020](https://github.com/mono/mono/graphs/contributors)
