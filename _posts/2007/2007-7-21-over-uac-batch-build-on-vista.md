---
layout: post
title: "Over UAC: Batch Build On Vista"
description: "This post talks about how to use make.all.bat on Windows Vista with UAC enabled."
tags: Windows
permalink: /over-uac-batch-build-on-vista-13d31dee6a5d
excerpt_separator: <!--more-->
---

Because of security concerns, I reactivated UAC on Vista. And now how can I use make.all.bat to make a CBC build? In fact, it is quite easy if you become familiar with UAC.

The steps are,

Launch a cmd.exe console as Administrator,
cd to the folder containing make.all.bat,
Run make.all.bat.
Isn't it simple? Yep, in this way, you find yourself back to XP days.

Why MS provides us such a simple way (although not easy to notice)? I guess for MS guys who develop pieces on Vista, UAC is also something blocks their way. A console walk around may ease their (and my) pains.
<!--more-->