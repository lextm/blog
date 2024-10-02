---
layout: post
title: "DockPanel Suite patch to support lite mode on Mono"
description: "This post is about a patch to enable DockPanel Suite on Mono."
tags: DockPanel-Suite Mono
permalink: /dockpanel-suite-patch-to-support-lite-mode-on-mono-217547fc710b
excerpt_separator: <!--more-->
---

Back in 2010 [I wrote about using lite mode of DPS on Mono]({% post_url 2010/2010-5-2-dockpanel-suite-tip-5-we-can-go-mono %}).

<!--more-->

Today I announce a better lite mode implementation,

- Built on DPS 2.5 (latest revision in SVN trunk)
- Full feature on Windows/.NET (drag and drop is supported)
- Lite mode on Mono (drag and drop is not supported)

Note that you need to use Win32Helper.IsRunningOnMono() to detect Mono in your applications and disable drag and drop pro-actively.

Source code is available on GitHub,

https://github.com/lextudio/sharpsnmplib/tree/7.5/WinFormsUI

Tested in #SNMP project on both Windows 7 (.NET) and openSUSE (Mono).

Hope the maintainers of DPS can merge the changes into the official repository for everyone.

(Updated: Now I become a maintainer of DockPanel Suite. The latest DPS can be found at https://github.com/dockpanelsuite/dockpanelsuite, which contains this patch and many other useful patches.)
