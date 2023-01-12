---
layout: post
title: "How to Install Custom Controls to Visual Studio, Part II"
description: "This post is about how to install custom controls to Visual Studio."
tags: .NET Visual-Studio
permalink: /how-to-install-custom-controls-to-visual-studio-part-ii-cff4b3227ed3
excerpt_separator: <!--more-->
---

> [Part I is here]({% post_url 2012/2012-8-11-how-to-install-custom-controls-to-visual-studio-part-i %})

In part I I mentioned all you need to install your custom WinForms controls to Visual Studio 2008.

I thought it would be challenging to add support for Visual Studio 2010 and 2012. However, I was fortunately wrong.

<!--more-->

If you have done the basic integration for .NET 4 AssemblyFoldersEx, then all you need is an updated Toolbox.exe that supports other Visual Studio versions, which is available in

https://github.com/lextm/ActionListWinForms

I have also updated the Inno Setup installer script to reflect the changes (only a few lines) needed.

Now you should be able to start working on your own installer. Good luck.

## Sidenote on SharpDevelop

If you are a control vendor that also wants to support SharpDevelop users, you might note that SharpDevelop does not try to locate design time support assemblies following Visual Studio's approach. Instead, [SharpDevelop reads its own bin folder](https://github.com/lextm/ActionListWinForms/issues/10).

Besides, I did not yet find a way to automate changes to SharpDevelop's tool box.

So in all, it is reasonable to write a good FAQ article specifically for SharpDevelop users to show them how to manually create the tool box items and add the design time support.
