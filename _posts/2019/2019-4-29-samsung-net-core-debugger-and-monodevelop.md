---
description: Discover how Samsung's open source .NET Core debugger can be integrated with MonoDevelop to provide .NET Core debugging capabilities without Microsoft's proprietary components.
excerpt_separator: <!--more-->
image:
  alt: Copyright © Lex Li. Bell Center, Montreal.
  path: /images/bell-center.jpg
layout: post
permalink: /samsung-net-core-debugger-and-monodevelop-80a6ea4bcab3
tags: .net linux mono open-source visual-studio
categories: [Programming Languages]
title: Samsung .NET Core Debugger and MonoDevelop
---
Visual Studio for Mac has been supporting .NET Core debugging for a while, but MonoDevelop users do not get the same experience. It has been [a well known issue](https://github.com/mono/monodevelop/issues/3764), and mainly due to the fact that Microsoft does not make the core debugger redistributable for non-VS tools.
<!--more-->

Below is the diagram showing the different components involved,

![img-description](/images/components-vsdbg.png)
_Figure 1: Components for Visual Studio for Mac .NET Core debugging._

Noticeably, vsdbg is the component that only serves Visual Studio (for Windows and Mac), and Visual Studio Code. The licensing terms for vsdbg-ui is not quite clear, so we should assume it is not available for non-VS products either.

So to create the same debugging experience in MonoDevelop, Samsung's .NET Core debugger should be used, as the diagram below indicates,

![img-description](/images/components-netcoredbg.png)
_Figure 2: Components for MonoDevelop .NET Core debugging._

Now I have such a custom extension for my personal adventure, and identify several issues.

[The first one](https://github.com/Samsung/netcoredbg/issues/20) is that Samsung debugger did not yet implement "process" event. I created a pull request and hope it can be merged soon.

[The second one](https://github.com/Samsung/netcoredbg/issues/19) is a data type mismatch between Samsung debugger and Microsoft's managed implementation of the VS Code Debug Protocol. 

I hacked Samsung debugger and proved that if the data type matches then .NET Core debugging can work flawlessly. However, that hack seems to have significant side effect, so I hope Samsung guys can decide what's the best option there.

You can find the patched debugger from [my personal fork](https://github.com/lextm/netcoredbg/tree/test).

I just released all the [source code at GitHub](https://github.com/lextudio/monodevelop.netcoredbg), and you can try out the extension.

You still need to build my fork of the debugger so as to get everything ready. Once Samsung resolves the two issues and publishes their new debugger packages, this step can then be skipped.

Stay tuned.
