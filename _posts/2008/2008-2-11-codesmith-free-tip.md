---
layout: post
title: "CodeSmith Free Tip"
description: This post talks about the free version of CodeSmith.
tags: Others
permalink: /codesmith-free-tip-a057dd4a617f
excerpt_separator: <!--more-->
---
It is said that CodeSmith is a must for .NET developers. However, even though I have been doing C# for years, I do not use it that frequently. So I prefer the free 2.6 version.

http://www.codesmithtools.com/freeware.aspx

But time goes by so quickly that you may find it fails to launch on Windows Vista. Why it complains that while Vista pre-installs .NET 2.0 and 3.0? I guess .NET beginners would find it miserable.

The answer is quite simple that its config file prevents you from using it on .NET 2.0/3.0. Therefore, here comes an easy workaround in `<app.config>`

Adding a .NET 2.0 line is enough.
<!--more-->