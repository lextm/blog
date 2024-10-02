---
layout: post
title: "Product Review: DockPanel Suite"
description: This post is a product review of DockPanel Suite.
tags: DockPanel-Suite
permalink: /product-review-dockpanel-suite-b6a6a0f24750
excerpt_separator: <!--more-->
---
Weifen Luo creates this free and open source DockPanel Suite. With it, it is possible to develop flexible user interface like Visual Studio .NET.
<!--more-->

Today I finally got a chance to test this suite and found it nearly perfect. Even though there are still tens of bugs logged on SF.net, during my evaluation, I found no critical issues that prevents me.

However, lacking of samples makes me sad. I have been trying my best and wish soon I can make full use of the suite.

In this afternoon, I found out the following tips for starters,

* Don't try to load configuration from file at startup. It will make you nervous most of the time.
* Don't try to play too many features at first. The sample inside is in fact complicated than I imagine. So try one feature at a time.
* Don't try to migrate your project using this suite too fast. I have to split the tasks into pieces and migrate step by step.

It is funny to see that tool window classes can be converted to Singletons. That pattern also enables interactions between panels easily. However, I did not try this approach yet so I am not sure if it is a good practice.

It seems that only well designed applications can enjoy this suite because panel interactions will become hell if your structure is bad.

(Updated: Now I become a maintainer of DockPanel Suite. The latest DPS can be found at https://github.com/dockpanelsuite/dockpanelsuite.)
