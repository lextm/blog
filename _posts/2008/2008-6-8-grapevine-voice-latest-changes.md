---
layout: post
title: "GrapeVine Voice: Latest Changes"
description: This post talks about the latest changes of CBC.
tags: Code-Beautifier-Collection Delphi
permalink: /grapevine-voice-latest-changes-f916c585230f
excerpt_separator: <!--more-->
---
It's been a long time since last time I posted about CBC. But it is still alive. Although #SNMP is now my top priority, I think improving CBC must be the second.

It is really hard for me to think about new features because I no longer use Delphi that much. Therefore, all latest changes are related to bug fixes.
<!--more-->

For example, I found a serious bug in [PSTaskDialog library](http://www.codeproject.com/KB/vista/Vista_TaskDialog_Wrapper.aspx?display=Print). And luckily I got it fixed. And then I make full use of this wonder task dialog library to replace XP dialogs everywhere inside CBC. Microsoft did a nice job by implementing task dialog API because it is much better at telling your users what happens and what to do. However, without PSTaskDialog, I won't be able to bring this invention back to XP.

I did not plan to release any binaries this month, so if you are interested please check out the latest source code from the repository.

Stay tuned.
