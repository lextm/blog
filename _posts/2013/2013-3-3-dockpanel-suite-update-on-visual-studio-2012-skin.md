---
layout: post
title: "DockPanel Suite: Update on Visual Studio 2012 Skin"
description: "This post talks about the update on Visual Studio 2012 skin for DockPanel Suite."
tags: DockPanel-Suite
permalink: /dockpanel-suite-update-on-visual-studio-2012-skin-1dcb4e32fe67
excerpt_separator: <!--more-->
---
We have received patches from @han6man as he/she has attempted to create a new skin for DockPanel Suite that simulates Visual Studio 2012 Light theme. This is really a lot of work though the changes are merely a few lines of new code. So I would like to thank him/her for this great contribution to the community.
<!--more-->

However, several problems occur before we can fully make use of the patches,

* The patches were submitted using a non-standard way. @han6man posted the changes in a few issue reports, which is quite hard to integrate into the code base. If you want to contribute to an open source project, make sure that you use standard patch file, or simply a pull request (for Git).
* Meanwhile, the modifications are all applied directly to files which are shared among all skins. This breaks existing Visual Studio 2005 (and 2003) skins, which is troublesome. So I extracted the changes and tried to create new source files aside to incorporate the new skin with existing ones.
* The existing extension model of DockPanel Suite shows its age, that some changes cannot be easily integrated. Refactoring must be performed so as to support customization (in a new skin) on several elements (splitter for example).
* The current implementation of the new skin seems to be incomplete. Either @han6man shares more patches in the future, or we need someone else to continue working on this new skin.

Not sure if we can finish this work in the next few weeks. If the introduction of this new skin will lead to significant refactoring, we might have to defer it to a breaking release such as 3.0.

Anyway you are welcome to check out the patches (originally on https://github.com/dockpanelsuite/dockpanelsuite/issues/59, or under my feature branch https://github.com/dockpanelsuite/dockpanelsuite/commit/7d430b7e0188067e5826529ab2c5b7a034e38e76).

Comments are also welcome.
