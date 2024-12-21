---
layout: post
title: "#SNMP Design: Month Update"
description: "This post is a monthly update from the team."
tags: SNMP
permalink: /snmp-design-month-update-7a8e5b675645
excerpt_separator: <!--more-->
---
TwinTower was released about a month ago, so here is a month update from the team.
<!--more-->

## People

We have three new members on board this month. Two of them are from New Zealand, while one from France. Robert and Patrick still works on the compiler specifications, so lately you won't see much news from them. But Chris, our dear "floodman", did a lot of contribution these days. Well, as a result, a lot of changes were checked in and we already broke a lot of old interfaces to reach a higher level.

## CrossRoad Beta 1

I had tried to keep compatibility to a certain degree, but failed at last. I realized this clearly this morning so the original plan to ship a TwinTower Refresh is going to be cancelled. Instead, I published the very first beta of CrossRoad here. This Beta 1 is based on Change Set 18569.

Accumulated changes are,

1. RFC definition of Request ID in message body is honoured. Related constructors and methods are heavily updated. (Note that this is a breaking change.)
1. Chris' version of Listener and related patches integrated. This should significantly improve performance. Please stop using obsolete classes such as TrapListener.
1. The first version of #SNMP MIB Compiler is further enhanced. The GUI is now feature complete.
1. The second version of #SNMP MIB Browser now has less features but integrates with the compiler.
1. Many bug fixes and small changes.

## Remaining

If we take a look at the original plan listed here for 2.0 release, you may notice that only a few small pieces are missing besides 3708. So we are now close to a new release.

Well, before the final release we still have a lot of code to test, refactor, and tune. So please kindly advise and report issues. Stay tuned.
