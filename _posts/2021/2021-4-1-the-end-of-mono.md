---
categories: [Frameworks and Libraries]
description: Analysis of Mono's declining future as Microsoft transitions to .NET 6 and beyond - understand why Mono-dependent applications face sustainability risks and the timeline of this critical platform shift
excerpt_separator: <!--more-->
layout: post
permalink: /the-end-of-mono
tags: .net linux microsoft mono xamarin open-source
title: The End of Mono Chapter at Microsoft
---
> Updated on Aug 27, 2024.

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

.NET 5/6 has cherry picked the most important asset (MonoVM/MonoCLR), so gaming/mobile platforms are now migrating to .NET 6/8,

* Visual Studio for Mac, one of the biggest Mono based applications, has [migrated to .NET 6 as well native Mac UI](https://docs.microsoft.com/visualstudio/releases/2022/mac-release-notes-preview#1700-pre5--visual-studio-2022-for-mac-version-170-preview-5-newreleasebutton). It no longer needs Mono or GTK#.
* Xamarin bits have migrated to .NET 6 as MAUI. .NET 7/8 filled up more gaps.
* Unity is [migrating to .NET CoreCLR](https://blog.unity.com/technology/unity-and-net-whats-next), and expects to finish in 2024.

The driving force to maintain the very large Mono distribution has shrunk significantly.

> Meanwhile, from [here](https://discord.com/channels/732297728826277939/732325020738519091) you can see how engineers like Jo Shields and Alexander Köplinger were trying their best to keep the Mono distribution alive and answering tough questions. I am very grateful for their efforts. But no one should bet their production applications on a small group of volunteers.

As many said, .NET 6/8 and above is going to be the right platform you migrate to. Microsoft/Unity and other companies in the ecosystem have already invested a lot there.

## 2024 and Beyond

[Xamarin has been fully deprecated by .NET MAUI on May 1, 2024](https://dotnet.microsoft.com/platform/support/policy/xamarin) and Unity will ship its new release to fully switch to .NET CoreCLR, we observe no more commits to the GitHub Mono repo(s) from Microsoft. And that concluded the long journey to unify .NET runtimes.

Therefore, it is not very surprising when [this announcement](https://github.com/mono/mono/issues/21796) was made on Aug 27, 2024,

> The Mono Project (mono/mono) (‘original mono’) has been an important part of the .NET ecosystem since it was launched in 2001. Microsoft became the steward of the Mono Project when it acquired Xamarin in 2016.
>
> The last major release of the Mono Project was in July 2019, with minor patch releases since that time. The last patch release was February 2024.
>
> We are happy to announce that the WineHQ organization will be taking over as the stewards of the Mono Project upstream at wine-mono / Mono · GitLab (winehq.org). Source code in existing mono/mono and other repos will remain available, although repos may be archived. Binaries will remain available for up to four years.
>
> Microsoft maintains a modern fork of Mono runtime in the dotnet/runtime repo and has been progressively moving workloads to that fork. That work is now complete, and we recommend that active Mono users and maintainers of Mono-based app frameworks migrate to .NET which includes work from this fork.
>
> We want to recognize that the Mono Project was the first .NET implementation on Android, iOS, Linux, and other operating systems. The Mono Project was a trailblazer for the .NET platform across many operating systems. It helped make cross-platform .NET a reality and enabled .NET in many new places and we appreciate the work of those who came before us.
>
> Thank you to all the Mono developers!

While this clearly gives hope to current Mono users, it is still up to the WineHQ organization to decide how to maintain the Mono distribution.

## Reference

* [History of .NET/Mono](https://corefx.lextudio.com/)
* [Downward trend of Mono commits, since 2020](https://github.com/mono/mono/graphs/contributors)
* [Mono Project is now under WineHQ](https://github.com/mono/mono/issues/21796)
