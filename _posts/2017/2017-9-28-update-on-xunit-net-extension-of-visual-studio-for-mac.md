---
layout: post
title: Update on xUnit.net Extension of Visual Studio for Mac
description: This post is about the latest progress of xUnit.net extension of Visual Studio for Mac and a tough bug.
tags: .NET Visual-Studio macOS xUnit
permalink: /update-on-xunit-net-extension-of-visual-studio-for-mac-af69457e3441
excerpt_separator: <!--more-->
---

> It is a long story, but I believe I enjoy the overall progress. So, let's get started.

A few days ago, I was notified by a user that [xUnit.net extension did not work quite well for him](https://github.com/xunit/xamarinstudio.xunit/issues/71). So he needs the extension to be able to kick off the runner as 64 bit on Mac, which I achieved and reported my research result in [a previous post]({% post_url 2017/2017-9-21-how-to-choose-xunit-net-runner-bitness-x86-and-x64 %}). However, that only addressed part of the puzzle, and made F# test cases of Miguel de Icaza's TensorFlowSharp project working. The C# test cases still [failed miserably](https://github.com/xunit/xamarinstudio.xunit/issues/72).

It took me a long while to locate the culprit, as this issue could not be reproduced under EASY_DEBUGGING mode (something specific to the extension code base). But I did find the cause, I also noticed that I could not provide the ultimate solution, as the source file `BinaryMessage.cs` was copied directly from MonoDevelop code base.

My temporarily workaround was to make a dirty hack to let things work, and in the meantime [report the issue to Xamarin Bugzilla](https://bugzilla.xamarin.com/show_bug.cgi?id=59805). Those guys responded quickly, and would deliver a better patch. So I would wait then.

No, the story did not end here, as Miguel himself still [could not run the test cases successfully](https://github.com/migueldeicaza/TensorFlowSharp/issues/143). I could not touch his machine obviously, so what could I do? So the following actions were in fact carried out by accident.

<!--more-->

Remember that I have been using Rollbar for Jexus Manager and Obfuscar? A few hours ago I finally decided to apply it to this extension, so that if users such as Miguel experience miserable exceptions, at least more information can be collected from the scene.

So on my own machine I started to do a few experiments using existing bug reports, like [this one (more than one year ago)](https://github.com/xunit/xamarinstudio.xunit/issues/38). It was an issue difficult to troubleshoot a while ago, but with Rollbar the call stack of that exception became so clear, that `BinaryMessage.cs` has another bug.

Well, my dirty hack came once again, and this time it also fixed [another old issue](https://github.com/xunit/xamarinstudio.xunit/issues/48).

One more piece of good news is that if the runner experiences some exceptions during execution, you can then see them displayed in Unit Tests panel instead of seeing nothing at all.

So, that's the story for today, and why not download the latest build and enjoy unit testing with xUnit.net on Mac?
