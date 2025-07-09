---
layout: post
title: "Tool Strips vs. Fluent/Ribbon UI"
description: This post talks about the difference between tool strips and Ribbon UI.
tags: Windows
permalink: /tool-strips-vs-fluent-ribbon-ui-fac98821c7bd
excerpt_separator: <!--more-->
---
Ribbon UI is cool. If you have tried Office 2007, InstallAware 7, or NDepend, you know why it is cool. Although there are negative comments, I really find Ribbon UI a good way to organize so many commands in a rational manner (don't know why Microsoft decides to call it Fluent UI at last).
<!--more-->

It is easy to see Ribbon not always a correct option (and probably that is why Microsoft makes Ribbon UI licensing this complex, Ribbon is not a silver bullet). For example, my project at office has only about twenty menu items at all. If I move it to Ribbon, there would be a lot of empty space in the panels which is very ugly. Although I got a license for r.a.d. Ribbonbar after registering Visual Studio 2005, I would not use it until the time is right.

In my case, menu and bar style is enough. Therefore, I have been working on tool strips heavily lately.

At first I was going to implement something similar to Visual Studio 2005/2008 but I couldn't understand why Microsoft does not make it default,

``` csharp
ToolStripProfessionalRenderer renderer = new ToolStripProfessionalRenderer();
renderer.ColorTable.UseSystemColors = true;
ToolStripManager.Renderer = renderer;
```

If Mike did not publish this in a post, I might never know it.

Suddenly I came across another wonderful renderer on CodeProject and its enhancement, I soon gave up the VS style. Yes, I guess you would love the Office 2007 renderer too. Because it highlights items in such a natural and obvious way, I couldn't resist using it anywhere suitable.

http://www.codeproject.com/KB/menus/Office2007Renderer.aspx

http://www.angelonline.net/Portal/Blog/tabid/73/EntryID/13/Default.aspx

The only issue right now is that I don't know whether Microsoft claims any restriction on the Office 2007 renderer alike controls because it seems that Fluent Visual Appearance is part of the Fluent UI License. OMG, it is so hard to make my project look fabulous.

I have sent a mail to the Microsoft guys. Wish they could clarify the thing for me soon.

(Update: Phil, the creator of Krypton Toolkit kindly reminded me that only Krypton Ribbon users are affected by Microsoft Fluent UI License. So now I have started to use Krypton Toolkit instead of this renderer.)
