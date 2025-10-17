---
description: This post is about how to troubleshoot MonoDevelop errors on openSUSE.
excerpt_separator: <!--more-->
layout: post
permalink: /how-to-troubleshoot-monodevelop-errors-on-opensuse-93498e626335
tags: linux mono monodevelop
categories: [Operating Systems]
title: How to Troubleshoot MonoDevelop Errors on openSUSE
---
I am using openSUSE 12.1 and MonoDevelop (2.x and 3.x) displays an exception dialog at startup saying `/MonoDevelop/Core/PlatformService` experienced a problem. In fact, if you launch MonoDevelop from the Terminal (execute `monodevelop` at prompt), more information will be displayed.

So the conclusion for me is simple, that MonoDevelop failed to find `libgnomeui.*.so` on this machine, which can be easily fixed by installing this package `libgnomeui`,

``` bash
zypper install libgnomeui
```

You may hit another problem, but the message got from the Terminal should be your guide.
<!--more-->