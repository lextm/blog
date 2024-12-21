---
layout: post
title: "DockPanel Suite Tip #3: Make Your Apps More Visual Studio"
description: This post talks about how to make DockPanel Suite more like Visual Studio.
tags: DockPanel-Suite
permalink: /dockpanel-suite-tip-3-make-your-apps-more-visual-studio-da921c4f92cb
excerpt_separator: <!--more-->
---
I know Visual Studio is not an adjective, but I find it much easier to understand. Default DockPanel Suite is not all that you need to clone Visual Studio. There are two elements missing, the tool strips and the middle mouse click action. Because [I talked about the tool strips here]({% post_url 2008/2008-2-18-tool-strips-vs-fluent-ribbon-ui %}), this post focuses on the latter.

You must find out that Document instances in DockPanel cannot be closed as easily as in Visual Studio. For example, in Visual Studio it is rather convenient to middle click on the document title to close it. And that's why there is no Close button beside the title like CodeGear RAD Studio 2007 (though RAD Studio IDE supports middle click too). However, DockPanel Suite does not make thing this easy.

But you can add this action yourself because the source code is open. According to this forum thread, a simple middle click action can be achieved by adding a few code. You can see both see_sharp's original code and my modification there. In fact, the fix is so simple that at first I was surprised to see it is not included in the DockPanel Suite.

https://sourceforge.net/p/dockpanelsuite/discussion/402316/thread/2a5b0493/

Even you have the correct tool strips and middle click action, there is still a few issues. The most significant one is that if you dock a few panels in one pane, then you will see active panel's tab is not highlighted correctly as the colour is slightly darker than Visual Studio's tabs.

(Updated: See tip 4 where I found a fix for the last colour issue.)

(Updated: Now I become a maintainer of DockPanel Suite. The latest DPS can be found at https://github.com/dockpanelsuite/dockpanelsuite.)
<!--more-->