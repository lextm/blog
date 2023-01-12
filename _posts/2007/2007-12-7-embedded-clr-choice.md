---
layout: post
title: "Embedded CLR Choice"
description: This post talks about the choice of embedded CLR.
tags: .NET Mono
permalink: /embedded-clr-choice-448cdc55137c
excerpt_separator: <!--more-->
---
I know a lot of Chinese companies choose Windows CE and .NET CF. It is OK, but just not that convenient, isn't it? You must compile the source code differently from the desktop .NET (even the source code should be modified somewhere which is boring).
<!--more-->

I remember that when Danny Thorpe talked about CF development, he commented that Microsoft shouldn't have ripped so many things out of CF. Guess if Microsoft provides better binary compatibility between desktop .NET and CF, this post would never be written like this.

Is there an alternative? Obviously, Mono + Linux is a better choice. Linux has been a successful embedded OS for a long time while Mono CLR is compatible to .NET desktop. Therefore, you can build and test on your laptop and download the assemblies to the embedded device. Run, and it is done.

Give Mono a try, because [someone has already succeeded](http://tirania.org/blog/archive/2007/Dec-07-2.html).
