---
layout: post
title: "How to Transform T4 files (.tt) without Visual Studio"
description: "This post is about how to transform T4 files (.tt) without Visual Studio."
tags: Visual-Studio Mono
permalink: /how-to-transform-t4-files-tt-without-visual-studio-d9042165a0eb
excerpt_separator: <!--more-->
---
Microsoft integrates T4 text template support inside Visual Studio. However, you usually find it troublesome to transform such files outside Visual Studio (at command prompt or in your build process). In fact, you can even transform them without installing Visual Studio, because…Mono guys have a full open source implementation of that engine :)
<!--more-->

Then how should you make use of the Mono assistance?

1. Visit MonoDevelop source repository and grab two C# projects named Mono.TextTemplating and TextTransform, https://github.com/mono/monodevelop/tree/master/main/src/addins/TextTemplating
1. Create a solution file and add these two. Compile them and now check the output of TextTransform project.

This project gives you a command line utility called TextTransform.exe. 

About how to use it, simply execute it without any parameter and read its help. If you are familiar with Mono.Options, you can even learn that from its entry function, https://github.com/mono/monodevelop/blob/master/main/src/addins/TextTemplating/TextTransform/TextTransform.cs

Good luck.

