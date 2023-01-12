---
layout: post
title: "#SNMP Design: Oh, 63 Seconds!"
description: This post is about the latest performance analysis of the MIB parser.
tags: SNMP
permalink: /snmp-design-oh-63-seconds-70998d527347
excerpt_separator: <!--more-->
---

1465474 milliseconds is a long time to load 1000+ MIB documents into the current browser in #SNMP (see [this post]({% post_url 2008/2008-10-1-snmp-design-the-first-performance-analysis %}). Do you think 24 minutes is a reasonable amount of time? I feel it too long.

<!--more-->

When I wrote [this post]({% post_url 2008/2008-10-2-snmp-design-compiler-design-proposal-for-crossroad %}) about the new design for CrossRoad, I understood that it could boost the performance. So the Turbo comes now. I am going to check in the latest changes in a few minutes, which is able to unbelievably do the same thing in 63410 milliseconds/63 seconds. 23x is a really nice result for a prototype, considering I only made use of existing Compiler and ObjectTree implementation.

It is sad that the browser cannot enjoy this turbo engine until I integrate it with the current browser. This integration may take a few weeks because Steve not yet finish the merging. As a result, I have plenty of time to improve the prototype lately.

In the next few months, I will refine this prototype until it is ready for CrossRoad release. But from now on, you can also play with it to see what is the magic. Stay tuned.

(Updated: One night later it only takes about 20–30 seconds to load 1000+ MIB documents. What I have done is simply move a few methods from Assembler to ObjectTree. It is hard to explain why this leads to another 2x boost.)
