---
layout: post
title: "#SNMP Design: Soaring"
description: "This post talks about the progress of #SNMP library."
tags: SNMP
permalink: /snmp-design-soaring-e000d37de4c5
excerpt_separator: <!--more-->
---
It is really hard to focus on the browser design because it is a complex task. I got a lot of pains last weekend on the agent profile section, and had to stop to do other stuffs.

The final result, surprisingly, is awesome. I finally implemented what are missing in SNMP v2c support. Yes, now you can use Counter64, and there is even a basic Opaque type. However, even though REPORT, INFORM, and GETBULK messages are there in the repository, they are not tested. I coded them simply according to the book, "Understanding SNMP MIBs", so maybe something is not right.

In all, right now the SNMP v2c support in #SNMP library is still experimental. Please play with it and provide me suggestions if you are interested. Stay tuned.
BTW, I'd like to say thank you to all guys who left kind words and suggestions in the Discussion board. You did help a lot.
<!--more-->