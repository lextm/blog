---
layout: post
title: "CatPaw Rumors: More Mono Support Coming"
description: "This post is about #SNMP Mono support"
tags: SNMP Mono
permalink: /catpaw-rumors-more-mono-support-coming-fb16f90d7c89
excerpt_separator: <!--more-->
---
Do you want to use our browser and compiler on Mono too? Yes, I believe most of you want a modern UI MIB browser and compiler on Mono/openSUSE. So is it possible that we ship something like that?
<!--more-->

I thought it was impossible as I chose to depend on DockPanel Suite. However, the fact is if we give up certain features, it is technically feasible to build a lite version of DPS to port our browser and compiler to Mono/openSUSE, so in 5.0 Beta 2 we will for the first time ship them as Mono compliant.

That was what I achieved last night. I removed nearly all Win32 PInvoke from DPS and now included this lite version in our source code package. The limitation now is that all panels in the browser and compiler cannot be dragged or moved.

This can be an interesting way to go Mono. But more Mono issues/bugs arise and I fought hard to find workarounds. Well, I must say the final result is promising that we bring as many features to Mono as possible now, but both the tools look poor.

More bug reports are now fired to Mono team, and hope they can provide fixes soon (before we ship 5.0 final is preferred, but I know that's hard).

Why complaining that Mono is not mature enough as a deployment platform? If you don't report issues, how can Mono guys fix them? Go! Mono.

Stay tuned.
