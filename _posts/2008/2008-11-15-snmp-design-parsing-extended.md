---
layout: post
title: "#SNMP Design: Parsing Extended"
description: "This post is about the improvement in MIB parser."
tags: SNMP
permalink: /snmp-design-parsing-extended-483997023960
excerpt_separator: <!--more-->
---
It is not the first time that I see posts on #SNMP discussion board contain messages formed by hex numbers. Yes, one of them is this thread . How did I involve in this thread? I have to carefully analyse the numbers and then understand their meanings.
<!--more-->

Suddenly a new idea pops up. Why not use MessageFactory to parse the string directly? The simplest way may be,

``` csharp
string bytes = "30 29 02 01 00 04 06 70 75 62 6C 69 63 A0 1C 02" + Environment.NewLine
+ "02 05 7C 02 01 00 02 01 00 30 10 30 0E 06 0A 2B" + Environment.NewLine
+ "06 01 02 01 21 01 01 05 00 05 00";
ISnmpMessage[] message = MessageFactory.ParseMessages(bytes);
```

But currently ParseMessages does not yet support string type yet.

It is a small trick, so certainly will be available really soon. Stay tuned.
