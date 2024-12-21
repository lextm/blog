---
layout: post
title: "#SNMP Design: Time for Parser Details, Part Three"
description: "This post is the third part of the parser design series."
tags: SNMP
permalink: /snmp-design-time-for-parser-details-part-three-99e23346a7f8
excerpt_separator: <!--more-->
---
## How to parse so many file in order? And how can I add more files to ObjectRegistry?

Even though right now the parser is still experimental, ObjectRegistry parses over sixty documents at startup. In this way you don't need to have basic documents at hand before using #SNMP. Hope this helps.
<!--more-->

So back to the first question, how to order those files is in fact EASY. If you take a look at the source code, you can see I cache all documents/modules in a list, and parse them until all their dependencies are parsed ahead.

Three functions are involved in the order process. They are Parse, ParsePendings, and ParseModule in ObjectTree.cs. The basic logic is that every time Parse is called, ParsePendings is triggered to initiate an attempt to parse all pending modules. Therefore, inside ParsePendings, ParseModule is called so many times in a horrible loop. The loop exits only if no module is pending or no more pending module can be parsed.

Then comes the second question. And the answer is also simple. Please use LoadFile and/or LoadFolder in ObjectRegistry.cs.

Please notice that the parser may throw exceptions on a few MIB documents. In those cases, please send me a copy of the MIB documents so I can debug the parser. Thank you in advance.
