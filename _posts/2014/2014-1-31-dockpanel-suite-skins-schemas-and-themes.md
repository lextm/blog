---
layout: post
title: "DockPanel Suite: Skins, Schemas, and Themes"
description: "This post talks about the history of skins, schemas, and themes in DockPanel Suite."
tags: .NET DockPanel-Suite
categories: [History, .NET]
permalink: /dockpanel-suite-skins-schemas-and-themes-a080747aa1c8
excerpt_separator: <!--more-->
---

In the adventure of VS2012 Light theme support, I have gained further knowledge on how DPS works internally. Thus, I summarized what I learnt [in this blog post]({% post_url 2013/2013-5-4-dockpanel-suite-a-summary-on-visual-studio-2012-light-theme %}). What I missed was a detailed explanation on the confusing terms used throughout the code base. Hope this post is not too late for anyone who would like to customize DPS look and feel.

<!--more-->

## The History of Schemas

The term schema was invented by Weifen Luo when both VS2003 and 2005 need to be supported. If you check out release 2.2 and go to Extender.SetSchema function you can see that when a new schema is applied, the function sets three factory objects to the Extender and the whole look and feel is changed.

Of course there was nothing called skins nor themes.

## The History of Skins

The term skin was introduced in release 2.3 by Steve Overton. It was not heavily emphasized in 2.3 release, but was made visible in release 2.5 (DockPanelSkin Demo button in the sample).

By setting a new skin, the look and feel changes even if you don't change the schema. Thus, it becomes easy enough to create sub-schemas and the door of customization is opened.

## The History of Themes

I attempted to refine the customization interface in 3.0 branch so as to resolve two issues,

- Schema is not something easy to drop in. To develop a new schema and apply, you have to touch too many places in the code base and that's too bad for beginners.
- Skin has been too weak. You cannot create a VS2012 Light theme with a new skin, because the old schemas do not cover the new elements introduced by Microsoft.

So ITheme interface and the three default themes were created, and the following advantages are achieved,

- To change the whole look and feel, you simply create a new theme that derives from ITheme. Existing themes can be forked as templates.
- To apply a new theme, you simply hook it to DockPanel.Theme. You no longer need to modify multiple spots.

Thus, themes are nothing new, but better schemas with unified API. Of course, skins are still supported by themes, so you can change skins so as to achieve sub-themes.
