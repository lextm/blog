---
layout: post
title: "If You Cannot Install/Uninstall IIS 7"
description: "This post is about how to resolve IIS 7 installation issue."
tags: Windows IIS
permalink: /if-you-cannot-install-uninstall-iis-7-292f3d582837
excerpt_separator: <!--more-->
---

IIS 7 (7.0 on Windows Vista and Windows Server 2008, or 7.5 on Windows 7 and Windows Server 2008 R2) installation depends on Windows CBS. This is a bless but also a curse. If you find installing or uninstalling IIS 7 failed with an error message, please blame CBS in most of the cases.

<!--more-->

Then why may CBS ever be corrupt without any hint? Possible causes are listed below,

1. You have run a "so called" registry optimization software. I believe the vendors neither fully test such products nor have a close enough relationship with Microsoft to learn about every registry keys. So stay away from them.
1. You have hardened the box. In some firms (financial firms especially), such hardening is mandatory for every server boxes. However, if the process is not Microsoft certified and indeed some registry or permission is changed wrongly, you will end up with lots of problems including this IIS one.
1. Windows Update process ended abnormally and broke CBS (like turning off Windows protection when Windows Update is in progress).
1. Many others…

About how to resolve the issue, you might go on to read [part II]({% post_url 2012/2012-7-15-if-you-cannot-install-uninstall-iis-7-part-ii %}).
