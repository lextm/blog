---
layout: post
title: "#SNMP Design: The First Performance Analysis"
description: This post is about the first performance analysis of the MIB parser.
tags: SNMP
permalink: /snmp-design-the-first-performance-analysis-fa3b7f884253
excerpt_separator: <!--more-->
---
I never take a look at performance counters until it is time. And now it is time for #SNMP. According to my latest analysis, it takes about 24 minutes (1465474-milliseconds) to load 1000+ MIB documents in the browser. This is horrible. So where is the bottleneck?
<!--more-->

A further evaluation is now under way. Luckily I have split the compiler into two parts, front-end (parser) and back-end (assembler), so it is easier to time the operations separately.

Out of my expectation, the parser works fine. The time it takes to parse a MIB document is about tens of milliseconds (min: 0-ms, max: about 733-ms for POWERNET-MIB). So it is the assembler that has poor performance. It takes hundreds or more of milliseconds (min: 0-ms, max: 57096-ms for VBRICK-BOX2-MIB) to assemble all entities of a MIB document to the tree.

Now I realize the issue and I start to explore it. Hope I can tune it soon.

What about the schedule? Although RC2 is already out, 1.5 release is not yet ready. Steve will work hard to merge all changes later to provide a stable browser. Then an evaluation report will be provided so we can discuss what are missing. If we think all basic functions are there, then 1.5 RC3 will be delivered immediately. One or two weeks after RC3, we can ship the final release of TwinTower. It takes much longer than expected, but we already finish more (such as SNMP v2c support, basic Agent component, and so on).

Stay tuned.

BTW, don't be panic about the performance issue. Not everyone has 1000+ MIB documents, isn't it? :) Up-to-now, I am the only one who suffers.
