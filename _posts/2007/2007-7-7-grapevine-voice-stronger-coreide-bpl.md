---
layout: post
title: "GrapeVine Voice: Stronger coreide.bpl"
description: "This post describes about GrapeVine release and the breaking changes observed."
tags: Code-Beautifier-Collection Delphi
permalink: /grapevine-voice-stronger-coreide-bpl-b49696307989
excerpt_separator: <!--more-->
---

When I switched to CodeGear RAD Studio 2007 IDE (BDS 5), I found that an exception occurred after closing the IDE if CBC was installed. Yep, it seemed that some pluses had bugs.

Today I tried again. After disabling WiseEditor, NFamily, and Utilities pluses, the exception had gone. So I will try to locate which features cause the exception. Luckily CBC has a flexible plug-in architecture, so every feature can be turned on/off easily. I believe soon the bug will be found and fixed.

You can see that CodeGear has improved the IDE a lot. Delphi 2006 ignores the bug while Delphi 2007 catches it. In fact there are hundreds of bug fixes and improvements.

Stay tuned.

(Updated: A few features have been disabled from this version, because some are already obsolete or need reimplementation. I promise that when GrapeVine ships the problems would be solved.)
<!--more-->