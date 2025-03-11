---
layout: post
title: "Migration to DockPanel"
description: This post talks about my work to migrate a project to DockPanel Suite.
tags: DockPanel-Suite
permalink: /migration-to-dockpanel-296ecd64e9ea
excerpt_separator: <!--more-->
---
I have been maintaining a Windows Forms application (Project E) for about 10 months since last April. The user interface was very complex because the original creator left so many lines of code inside event handlers.

Right now after countless rounds of refactoring, I successfully cut off most lines and move them into a low level layer. So I start to add unit tests to the low level layer in order to achieve automatic testing.
<!--more-->

However, this is not what the marketing department wants. One message from our customers is that the user interface is not friendly enough compared to other Windows applications.

In order to avoid unpredictable consequences, I won't take the risks to publish a photo here to illustrate why that UI is bad. All I could tell is that every operation is done in a modal dialogue. So you always see a dialogue popping up and away.

That was the Win 9x way. Now on Windows XP and Windows Vista, Microsoft promotes more natural UI styles hard. Two examples are Visual Studio .NET and Office 2007.

After evaluation, I have to say Ribbon UI is much cooler but harder to achieve in a few weeks because there are so many rules to follow and all stable components are commercial. On the other hand, Visual Studio .NET style has been there for years so free components such as DockPanel Suite is stable enough. And our original design is only a few steps behind this approach.

In the last post I talked about my first day with DockPanel Suite. And unbelievably that today I was able to create a more complex demo with latest Project E source code checked out from our Vault. Because my first demo is based on an old version of Project E and I have written down steps I took carefully, I gained enough experience and found a few shortcuts.

The result is very promising so I may present it to my manager after the holidays.
