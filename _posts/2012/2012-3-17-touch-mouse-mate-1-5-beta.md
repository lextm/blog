---
layout: post
title: "Touch Mouse Mate: 1.5 Beta"
description: "This post is about the latest news of Touch Mouse Mate."
tags: Windows
permalink: /touch-mouse-mate-1-5-beta-8dc67d90970c
excerpt_separator: <!--more-->
---
Hi guys,

I am going to take a vacation in the coming days, so decide to release 1.5 Beta right now for you to try out. It is stable enough so I set it as our default release on the project site.
<!--more-->

Compared to 1.4 release, the following changes are introduced,

* New gesture engine is implemented. A state machine is used to determine left/middle/right clicks and mouse down/up events. Therefore, it should provide more accurate response.
* Middle-click and touch-over-click now fully support drag and drop. This is a direct result of the new engine, as mouse down/up events are simulated separately.
* Touch-over-click is disabled by default, as the new engine conflicts with Microsoft's gestures. Once enabling it, Microsoft's gestures won't work properly in left/right click zones (inside the top-half surface), but they will work fine in the bottom-half. More details on the click zones will be provided later in a new blog post. I tried to avoid the conflicts by adding movement detection, but tests show that it does not work as expected.
* Installer improvements and bug fixes.

Though there is no new feature introduced in this release yet, I recommend you upgrade to it so as to enjoy the new engine.

Stay tuned.
