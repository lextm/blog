---
layout: post
title: "DockPanel Suite Tip #5: We Could Go Mono"
description: "This post is about DockPanel Suite Mono support"
tags: DockPanel-Suite Mono
permalink: /dockpanel-suite-tip-5-we-could-go-mono-63ee484f77a0
excerpt_separator: <!--more-->
---
DockPanel Suite was designed for Windows. Its original author and later contributors do not yet port it to Mono. However, so many people including me would like to have a Mono friendly DPS, then how can we achieve that?
<!--more-->

A full port to Mono requires us to get rid of all Win32 PInvoke, but unless someone who masters Windows/Linux/DPS comes I bet it is not likely that we see a full port.

I chose the easy way to sacrifice certain features. For example, if we disable end user drag and drop, all such PInvoke parts can be safely commented out. Is that all I need? Yes, my applications at this moment do not need any drag and drop, so why not use this lite version?

I now happily see the applications run fine on Mono (well, one infinite loop issue needs to be worked around though). So do you plan to use such a lite version?

The lite version of source code is available here, http://code.google.com/p/sharpsnmplib/source/browse/#hg%2FWinFormsUI. You can check out the entire WinFormsUI folder and analyze it to see what changes I've made.

![img-description](/images/dps-mono.png)
_Figure 1: DockPanel Suite on Mono._

(Updated: Now I become a maintainer of DockPanel Suite. The latest DPS can be found at https://github.com/dockpanelsuite/dockpanelsuite, which contains this patch and many other useful patches.)

(Updated again: Due to Mono WinForms limitations, DockPanel Suite on Mono is provided as it is and will not be actively maintained. Please consider native UI frameworks such as GTK# on Linux, and Xamarin.Mac on macOS.)
