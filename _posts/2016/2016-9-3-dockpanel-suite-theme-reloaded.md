---
layout: post
title: "DockPanel Suite: Theme Reloaded"
description: "This post would show you how we ported VS2012 Light theme in, how the related API was refactored, and how themes became separate NuGet packages."
tags: DockPanel-Suite
permalink: /dockpanel-suite-theme-reloaded-3bb41273d127
excerpt_separator: <!--more-->
---
I blogged about DPS theming a few times, aiming to demonstrate how we ported VS2012 Light theme in, how the related API was refactored, and how themes became separate NuGet packages. But I never expected that today I can blog about two new themes and potentially more from you. So let's get started.
<!--more-->

## Visual Studio 2010

Interestingly that Microsoft gave up Windows Forms and built Visual Studio 2010 on WPF. That instantly led to a brand new theme being shipped,

![img-description](/images/vs2010-blue.png)
_Figure 1: Visual Studio 2010 Blue Theme._

This is a blue theme, which many people easily got bored with.

## Visual Studio Color Theme Manager
So [an extension](https://blogs.msdn.microsoft.com/visualstudio/2010/01/04/changing-visual-studios-color-palette/) was soon released by Microsoft for end users to design their own themes.

![img-description](/images/theme-editor.png)
_Figure 2: Visual Studio Color Theme Manager._

## Visual Studio 2012 Themes
When Microsoft initially designed Visual Studio 2012, they came across the idea to ship by default, a light theme and a dark theme.

![img-description](/images/vs2012-light.png)
_Figure 3: Visual Studio 2012 Light Theme._

![img-description](/images/vs2012-dark.jpg)
_Figure 4: Visual Studio 2012 Dark Theme._

Surprisingly, the blue theme was added back in a later update, due to community feedback. Color Theme Manager is also updated for VS2012.

## Later Visual Studio Releases
Visual Studio 2013 and 2015 do ship all three themes by default (Light, Dark, and Blue), and they also have Color Theme Manager extensions.

## DockPanel Suite's Old Themes
If you are familiar with our previous code base (2.10 for example), you know that we use `DockPanelSkin` to store the colors used in each themes. It was an old design mainly for Visual Studio 2003/2005 themes. So using it to help render Visual Studio 2012 Light and 2013 Blue themes is painful.

## New Theme Design
As Color Theme Manager exposes the internals of Visual Studio themes as color palette, it is in fact quite easy to design a few new classes in DPS to map the palette and the colors. So in 2.11 release, I finally have some time to finish it.

`DockPanelSkin` now has a `ColorPalette` property, which in turn contains further properties to map to each of the core colors of a theme. So to create a new theme like `VS2012DarkTheme`, we just need to change the colors to the values provided by Color Theme Manager. Yes, it is just that simple. And now we have a full family of VS2012 themes (Light, Dark, and Blue).

The testing of new themes also revealed a few minor bugs that we neglected in the past. For example, the last tab on tool window strip does not have a separator unless it is active. They are now fixed.

However, one price we have to pay is that VS2013 Blue theme is now broken. I will see if I can fix it before we ship 2.11 final release. But you can of course switch to VS2012 Blue theme which is more mature.

So now if you want to create a new theme, you can follow [this guide](http://docs.dockpanelsuite.com/themes/creating-new-theme.html).

## New Alpha Builds
[2.11 Alpha 4](https://www.nuget.org/packages/DockPanelSuite/2.11.0-alpha4) is now available for you to test out the new themes.

Stay tuned.
