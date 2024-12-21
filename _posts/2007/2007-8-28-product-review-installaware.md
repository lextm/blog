---
layout: post
title: "Product Review: InstallAware"
description: "This post talks about InstallAware, a professional installer solution."
tags: Windows
permalink: /product-review-installaware-7d3088d8e806
excerpt_separator: <!--more-->
---
It is so common to distribute software as installers, that so many installation solutions are available in the market.

Even though I am just running a small open source project named Code Beautifier Collection, I have to make a good quality installer to please users.
<!--more-->

## Inno Setup

I have been using Inno Setup for a long time. Generally speaking, with help of Pascal Script support, I could do nearly everything in the installer to provide as many features as I can imagine.

However, it is not yet a perfect solution too. Its main disadvantages are,

1. Inno Setup installers are Microsoft standard compliant. You should create MSI installers in order to pass the certifications.
1. Inno Setup does not provide a powerful wizard to guide newbies. The learning curve is tough. That's why I spent so much time learning it.
1. Pascal Script authoring is really hard and sometimes error prone. Usually I wrote the script in Delphi, test it and then copy back to Inno script file.

## InstallAware Studio

When I install InstallAware I soon understand why Marco Cantu find it professional.

I think Ribbon UI is cool but I prefer a VS-like UI.

Compared to Inno Setup, IA has some main advantages,

1. IA creates standard MSI installers.
1. IA allows you to work with wizards and with script based development simultaneously.
1. MSIcode can be debugged within IA. This reminds of modern IDEs such as Delphi and C++Builder. Meanwhile, you do need to type MSIcode manually and every line is generated using a panel and wizard, so you can make fewer mistakes.

IA provides professional dialog templates, web deploy and other advanced features which I do not want to touch right now. They are cool, but maybe required only by large projects such as CodeGear Delphi and C++Builder.

In all, it is nice to have a copy of IA. It really reduces the complexity of creating a powerful installer.
