---
layout: post
title: "DockPanel Suite: Too Many Themes and New Goodies"
description: "This post is about DockPanel Suite recent changes and how easy it is now to generate new themes."
tags: DockPanel-Suite
permalink: /dockpanel-suite-too-many-themes-and-new-goodies-fb4fe55d127e
excerpt_separator: <!--more-->
---
I blogged a few days ago on DockPanel Suite recent changes, but well excitingly there is much more to share this time.
<!--more-->

## New Features

Remember that I mentioned the "new theme design"? It has been greatly upgraded in the past few days, with the following features I personally never thought I could have achieved,

* All button images are generated on-the-fly based on the color palette.
* All dock indicator images are generated on-the-fly based on the color palette.
* Dock indicators are now transparent just like VS does.
Pressed images are now supported (only normal and hovered were supported).
* Color palettes now can come from .vstheme files exported by Visual Studio Color Theme Manager.

What do they mean? They mean that in just a few minutes you should be able now to create a new theme by using the greatest visual tool developed by Microsoft for Visual Studio, and then enable it in DockPanel Suite. I have updated [the new theme creation guide](http://docs.dockpanelsuite.com/themes/creating-new-theme.html) to reflect the changes and hope you like them immediately,

## New Themes and 2.11 Beta 1

The result of all such efforts is that now the following themes are shipped,

* VS2003
* VS2005
* VS2012 Blue/Dark/Light
* VS2013 Blue/Dark/Light

Totally you get 8 themes for the first time. You can now grab them [via NuGet](https://www.nuget.org/packages/DockPanelSuite/2.11.0-beta1). The upcoming Beta 2 will add VS2015 Blue/Dark/Light to the list.

## Interesting Facts
You might think that well we shipped VS2012 Light and VS2013 Blue themes already, so what's the big deal. Well, even they receive significant updates in many aspects,

1. By using the .vstheme files from Microsoft, a few incorrect colors are now fixed.
1. By using the image generation algorithms based on mask images, the final assembly size is smaller.
1. The missing borders of dock panes in VS2013 theme are added.
1. The missing borders in dock outline windows are added.
1. The auto-hide window splitter size is fixed.
1. Dock panel theme switching is more reliable.
1. Incorrect pixels in auto-hide strip are fixed.
1. Pens and brushes are cached to minimize memory footprint.
1. VS2012 Blue theme uses many VS2013 theme elements (such as splitters).
1. VS2012 themes and their corresponding VS2013 themes might use a few different colors (for instance, VS2012 Blue theme uses a yellow color, which is no longer used in VS2013 Blue).
1. VS2012 Blue theme's active document tab's blue color is different from the one specified in Color Theme Manager.

[A review on the facts](http://docs.dockpanelsuite.com/themes/review.html) can be found at the doc site.

You are welcome to create new themes and send us PR via GitHub. Happy theming!

Stay tuned.
