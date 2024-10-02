---
layout: post
title: "DockPanel Suite Tip #2: Conflicts with Crad Action List"
description: This post talks about how to use DockPanel with Crad Action List.
tags: DockPanel-Suite
permalink: /dockpanel-suite-tip-2-conflicts-with-crad-action-list-baf8cc207d14
excerpt_separator: <!--more-->
---
I love Crad Action List control. And in every form I create I use this control to provide menu items and tool strip items.
However, once I place an ActionList item in a DockContent, this content cannot be closed without an exception. So I know DockContent is not the same as Form.

In several Update event handlers I try to change Action's Enabled property, then items on the ToolStrip can be controlled easily. However if the content is disposed, those Update events still raise. Exceptions occur because changing Action.Enabled triggers updating those disposed controls inside the content.

But why in Form I never meet this issue? I think this might be an ActionList bug because it shouldn't work once its container is disposed. It can also be a DockPanel Suite issue because it may dispose DockContent in another way.

But all I know is that a workaround is easy. If I check whether the content is disposed in the Update event handlers, the exceptions would go. And they go now!

(Updated: Now I become a maintainer of DockPanel Suite. The latest DPS can be found at https://github.com/dockpanelsuite/dockpanelsuite.)
<!--more-->