---
layout: post
title: "Hacking xbuild: Part I, Grab a Box"
description: "This post talks about how to set up a clean environment for hacking xbuild."
tags: Linux Mono
permalink: /hacking-xbuild-part-i-grab-a-box-24e70b6d2821
excerpt_separator: <!--more-->
---
Recently I decided to hack on xbuild. But soon I found it was not easy to set up a clean environment.
<!--more-->

## Windows box with Mono
It is possible to build a Windows box and then install Mono on it. But Mono's Windows installer already contains a build of xbuild. Besides, the most difficult part is that under that scenario, there is not feasible IDE to speed up hacking.

I did find a way to compile MonoDevelop source code on a Windows with .NET 4 (please avoid .NET 4.5 on the build machine), and then copy the binaries to the Windows with Mono box. However, there are various issues arising when MonoDevelop is hosted by Mono on Windows (miserable hang and crash). I guess nobody ever tries this combination seriously, so those issues are never reported or fixed.

> Anyway, if you plan to play out Mono, I recommend you use Mono on Linux/OS X instead of Windows. Note this DOES NOT include MonoDevelop/Mono for Android, as they work fine with Microsoft .NET Framework/Visual Studio ecosystem.

## openSUSE box with Mono
The previous efforts on getting NuGet running on Mono do help me out by learning how Mono is packaged on Linux distros. It was early today that I suddenly realized that openSUSE is a nice choice for my hacking environment.

So after building a clean openSUSE, I use the following commands to install the bits I need

``` bash
sudo zypper install mono-complete monodevelop git
```

and then I remove xbuild and its components by executing

``` bash
sudo rpm -e --nodeps mono-devel
```

This is why I love openSUSE's Mono packages, as mono-devel contains all xbuild related bits. However, even after removing it, MonoDevelop works fine (well, I could not enable xbuild integration inside MD then).

(Updated: it is unnecessary to remove mono-devel, so the above step is deleted.)

At last, it is time to clone mono source code from https://github.com/mono/mono and start hacking on my own fork of xbuild.
