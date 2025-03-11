---
layout: post
title: "DockPanel Suite: How to Write a New Theme"
description: "This post talks about how to write a new theme for DockPanel Suite."
tags: DockPanel-Suite
permalink: /dockpanel-suite-how-to-write-a-new-theme-573f46197486
excerpt_separator: <!--more-->
---
(Originally posted to CSDN on Feb 21, 2006)
<!--more-->

> [WARNING: This post is too old to be true, and you should read http://docs.dockpanelsuite.com/themes/creating-new-theme.html to get the latest guide.]

Today I finished integration of VS2012 Light theme patches into DockPanel Suite code base. All the changes are now on gh59 branch,

https://github.com/dockpanelsuite/dockpanelsuite/tree/gh59

Please note that I also made a few minor changes (such as tuning splitter size and color and introducing `ITheme` interface). So now it is time to document what is required to write a brand new theme, using the extension points left by the original developers of DPS.

## 1. DockPanel Suite Skin
It is possible to change the various colors and fonts used in DPS elements, and the quickest way to switch is to set `DockPanel.SkinStyle` property to the value you want. Sadly there was only one `VisualStudio2005` option for you to choose. By merging the new patches, I created a second option named `VisualStudio2012Light`. So if you plan to write a new theme, you might consider adding another option here, or more easily construct your own `DockPanelSkin` instance and assign to `DockPanel.Skin`.

Although the default `DockPanelSkin` instance provides you Visual Studio 2005 settings, you can easily configure Visual Studio 2012 Light settings (or any other you like) in the same way I did in `DockPanelSkinBuilder.CreateVisualStudio2012Light`. It is highly configurable.

## 2. DockPanel Suite Extender
Via DockPanel.Extender we can further customize how the elements look, because there are lots of factory instances we can override.

For example, `DockPanelExtender.DockPaneStripFactory` is used every time to construct a dock pane strip object. So by leaving it unchanged, we use the `DefaultDockPaneStripFactory` type to construct Visual Studio 2005 style pane strips. To use Visual Studio 2003 style strips, we need to set this factory to `VS2003DockPaneStripFactory` (which is defined in `DockSample` project). The same applies to Visual Studio 2012 Light, where we use `VS2012LightDockPaneStripFactory`.

The `Extender` class provides many factories for us to override,

* `DockPaneFactory`
* `DockPaneSplitterControlFactory` (* new in gh59 branch)
* `FloatWindowFactory`
* `DockWindowFactory` (* new in gh59 branch)
* `DockPaneCaptureFactory`
* `DockPaneStripFactory`
* `AutoHideStripFactory`
* `AutoHideWindowFactory` (* new in gh59 branch)

The new factories added in gh59 branch are required by Visual Studio 2012 Light theme.

## 3. Other Properties
I had to expose `Measures.SplitterSize` as Visual Studio 2012 Light theme requires a change from 4 to 6. I think in the future we might make it configurable via DockPanelSkin, instead of the current hack. I am not sure if there is any other similar edge cases in the code base.

At this moment, you might have a better understanding of DockPanel Suite customization. Before the end of this article, I'd like to also introduce the latest changes I made, the `ITheme` interface.

## `ITheme` Interface
You can see from above that to implement a new theme and apply it, there are many things you need to prepare. But if you are not a developer of new themes, and you simply want to make use of an existing theme, it might be painful to understand the above extension points and configure them one by one. [The new interface](https://github.com/dockpanelsuite/dockpanelsuite/commit/58f55b9dfc7fc9870427e4175dbd4eca3a828981) is introduced to encapsulate the pieces.

Now you just need to know what are the themes available (`VS2003Theme`, `VS2005Theme`, and `VS2012LightTheme`), create an instance of one theme, and call `Apply` method with your DPS object. Isn't that simpler?

Any feedback is welcome.