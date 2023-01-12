---
layout: post
title: "xUnit.NET Add-in for Xamarin Studio: Latest Update"
description: "This post is about the latest update of xUnit.NET add-in for Xamarin Studio, such as support for Xamarin Studio 6.x."
tags: .NET Mono
permalink: /xunit-net-add-in-for-xamarin-studio-latest-update-b9ef69414f54
excerpt_separator: <!--more-->
---
In last post I talked about how I made a fork to support Xamarin Studio 5.x series (as well as MonoDevelop 5.x). It was clearly a milestone, but not good enough as Xamarin Studio 6.x was at the door.
<!--more-->

So why couldn't I bring Xamarin Studio 6.x support at that time? The answer is that Xamarin has done too much to make it the best Xamarin Studio release ever, and the heavy refactoring changes how a unit testing add-in like xUnit.NET should connect. I was only able to borrow the NUnit add-in source code once again, but someone else was needed to really make xUnit.NET work.

Luckily, it is an open source project, and soon we get the new star to shed some light, and [his GitHub ID is z28wang](https://github.com/z28wang).

He cleverly remixed the NUnit add-in code with the 5.x version of xUnit.NET code, and [prepared a build](https://github.com/xunit/xamarinstudio.xunit/commit/a960fdf5a29d9eff8845cad4f2f91f6b4e973f29) that could run without significant issues.

Several minor issues could then be fixed by me without much difficulty.

Of course, he contributed [another important patch](https://github.com/xunit/xamarinstudio.xunit/commit/18738c6a6e893bacffeec5be3e865c0de35b30d2) to make `[Theory]` work for the very first time!

And that patch works for both 5.x and 6.x versions of xUnit.NET add-in. Whoa!

In the meantime, Sergey (x2bool) has been kind enough to hand over the origin repo to me (what an honor). All development works in my fork have been upstreamed since then.

Now Xamarin Studio 6.0 has finally moved from beta channel to stable channel, and hope you enjoy the xUnit.NET add-in. Hat off to z28wang, and thank him so much for helping me out.
