---
layout: post
title: "Localization in .NET Framework 2.0"
description: "This article talks about localization in .NET Framework 2.0."
tags: .NET Visual-Studio
permalink: /localization-in-net-2-0-fdb682f7f996
excerpt_separator: <!--more-->
---
It is easy to localize a .NET WinForms project in Visual Studio. However, something you should be careful with. An article should be your guide when you need to do some localization. That is Walkthrough: Localizing Windows Forms inside MSDN.
<!--more-->

When you try to translate the `WinFormStrings.resx`, you will find .NET Language Localizator 2 for .NET 2 very helpful. After translating in it, you can rename the compiled `resx` to `WinFormStrings.**.resx`.

I have to confess it is still hard to localize a project even with the help of Visual Studio and .NET Language Localizator 2 for .NET 2. So, before any exercise, think twice.

And you see, that is why I hadn't localize CBC even though so many Chinese users asked me to.
