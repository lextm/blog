---
categories: [Frameworks and Libraries]
description: A comprehensive analysis of MonoDevelop's licensing history - from GPL to LGPL/MIT X11 dual licensing, the impact on commercial distributions, and implications for future community-driven development efforts
excerpt_separator: <!--more-->
layout: post
tags: .net linux microsoft mono xamarin open-source
title: Summary about MonoDevelop Source Code Licensing
---
A group of passionate developers want to revive MonoDevelop, so they [discussed about the source code licensing issues here](https://github.com/dotdevelop/dotdevelop/issues/51).

I think some historical context wasn't properly captured, so I wrote a post there and hoped to help clarify the situation.

## MonoDevelop 2.2 Relicensing

> Original announcement by Miguel de Icaza on his personal blog at https://tirania.org/blog/archive/2009/Dec-15.html
>
> "MonoDevelop code is now LGPLv2 and MIT X11 licensed. We have removed all of the GPL code, allowing addins to use Apache, MS-PL code as well as allowing proprietary add-ins to be used with MonoDevelop (like RemObject's Oxygene)."

Like I commented earlier, in 2008-2009 there was enough attention around Mono and MonoDevelop due to the collaboration with Unity (called Unity3D at that time) and the promising product MonoTouch (later Xamarin.iOS). The previous GPL coverage of the MonoDevelop code base prevented external firms (like Unity3D and RemObjects) from shipping closed source extensions.

> RemObjects requested the relicensing of MonoDevelop code base, because they wanted to ship their Oxygene language as a closed source extension to MonoDevelop. This was a significant motivation for the relicensing.

MonoDevelop 2.2 relicensed all code under LGPLv2 and MIT X11 so all those licensing issues were resolved (Mono runtime was still licensed under a more restricted license then).

After this, commercial distributions of MonoDevelop started to rise,

* MonoDevelop-Unity, a game IDE by Unity
* MonoTouch, an iOS IDE by Novell
* Xamarin Studio, a mobile centric IDE by Xamarin
* Visual Studio for Mac, a macOS IDE by Microsoft

> Only VS for Mac was created only Microsoft acquired Xamarin, but the other three were created long before that.

## Contributions to MonoDevelop

In recent years, there was no CLA set up for MonoDevelop, but a different approach was used to govern the patches,

> All new code and modifications to existing code should be licensed under MIT X11. The MS-PL and Apache 2 licenses are acceptable for new libraries and new addins.
>
> Code and libraries licensed under version 2 of the LGPL license are acceptable under extraordinary circumstances.
>
> Code licensed under the GPL cannot be accepted.
>
> Although addins that do not follow these rules cannot be accepted into the MonoDevelop source repository, they can be hosted elsewhere. However, this generally means that they are much less likely to be maintained and distributed.

https://www.monodevelop.com/developers/#a-note-on-licensing

As patches were released under MIT X11 by their authors, they were suitable to be shipped with other code in MonoDevelop.

## Side Notes

If everyone accepts the fact that the relicensing in Dec 2009 is valid, then there isn't much more to discuss further here. Microsoft has no obligation to publish any of its private patches, as LGPL/X11 dual licensing allows such private patches.

I think Microsoft still holds the copyright of most MonoDevelop code base due to its acquisition of Xamarin (along with other assets like monodevelop.com domain and the GitHub repo). Any attempt to revive MonoDevelop (or create a new variant) should respect that and follow the requirements of LGPL/X11 dual licensing. The various contributors still hold copyright of the public patches, but since those patches were released under X11 in general, following the requirements won't be any different.

> Based on the [public roadmap of VS for Mac](https://docs.microsoft.com/en-us/visualstudio/productinfo/mac-roadmap), Microsoft is clearly replacing many components with new code, such as "Move the IDE to fully native macOS UI". Ultimately VS for Mac should share a lot with VS for Windows (might include the extension system), so making it a closed source product early in 2020 can be explained well.
