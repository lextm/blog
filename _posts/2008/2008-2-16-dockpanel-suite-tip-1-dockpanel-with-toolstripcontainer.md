---
layout: post
title: "DockPanel Suite Tip #1: DockPanel with ToolStripContainer"
description: This post talks about how to use DockPanel with ToolStripContainer.
tags: DockPanel-Suite
permalink: /dockpanel-suite-tip-1-dockpanel-with-toolstripcontainer-e783a774e90
excerpt_separator: <!--more-->
---
If you want to use both items together, please make sure that ToolStripContainer fills the Form and in turn DockPanel fills the its ContentPanel.

However, you must notice that DockPanel can only work with some of DocumentStyle then because MDI styles are impossible now.

> BTW, Even though it is possible to persist DockPanel state, I do not find a way to persist ToolStripContainer state when I place five ToolStrip items in it. So I have to fix those items.

(Updated: Now I become a maintainer of DockPanel Suite. The latest DPS can be found at https://github.com/dockpanelsuite/dockpanelsuite.)
<!--more-->