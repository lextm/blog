---
layout: post
title: "DockPanel Suite: Design the Theming Experience"
description: "This post talks about the new theming experience in DockPanel Suite."
tags: DockPanel-Suite
permalink: /dockpanel-suite-design-the-theming-experience-4c55f51d65c8
excerpt_separator: <!--more-->
---
In previous change sets I attempted to add the new ITheme derived themes to DPS, so that we can easily change from one theme to another.
<!--more-->

But isn't it easier to implement the following experience?

1. Drag a DockPanel control to your main form to start using DPS.
1. Drag a few theme controls (invisible) to the same form.
1. In DockPanel control's property editor, choose a theme to apply.

I just implemented the necessary building blocks in the latest change sets, and here are a few screenshots that reflect the changes.

![img-description](/images/dps-vs.png)
_Figure 1: DockPanel Suite in VS WinForms designer._

![img-description](/images/dps-property.png)
_Figure 2: Theme property in designer._

To play out, you can check out the source code from gh59 branch,

https://github.com/dockpanelsuite/dockpanelsuite/tree/gh59

Stay tuned.