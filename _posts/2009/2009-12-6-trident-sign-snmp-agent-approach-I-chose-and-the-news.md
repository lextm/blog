---
layout: post
title: "Trident Sign: SNMP Agent Approach I Chose and The News"
description: "this post is about how I implemented the SNMP agent with a different approach"
tags: SNMP
permalink: /trident-sign-snmp-agent-approach-i-chose-and-the-news-7a95902b8d83
excerpt_separator: <!--more-->
---
When the first time someone asked me if #SNMP library can be used to develop a full feature SNMP agent, I was not sure. I know it must be a long way to go on agent side, because there are so many pieces we need to implement.
<!--more-->

Interesting that finally I can work on the agent side extensively. Now the small TestAgent sample grows over the weekends, and today it becomes a small but usable SNMP v1 agent. It can now handle v1 GET, SET, GETNEXT messages. Besides, it can send out a test TRAP message. Though I only implemented six basic objects, it is really promising that we have an architecture ready.

I have to admit that I did not have a blue print in the beginning, though I have been thinking about the elements for almost a year. Refactoring is always my friend, so that I can feel free to code first, and refactor next. And I also borrow some ingredients from dear ASP.NET. The concept of HTTP processing pipeline is amazing and it makes a lot of extensions possible. I at last chose this approach and refactor the code base accordingly.

If you take a look at SnmpApplication, SnmpContext, IMembershipProvider, IMessageHandler, you will find them familiar (just like HttpApplication, HttpContext and so on). But they are still in early stage, and subject to heavy changes in the next few weeks.

Then how to shape this TestAgent (snmpd) to suit your need? You can write your own membership provider to authenticate requests, and write your own message handlers to handle SNMP messages. Also you can implement more objects and store them in the object store. The store is really rough at this moment, but we can make it better in the future.

That's all I can write up-to-now, because after the Oct 1st release of #SNMP Suite 3.1, we really come across a lot of new things. I did not yet have anything important to write about the compiler yet, and hope this agent project can attract your attention.

Please feel free to let me know how you think about the future of #SNMP, I did not yet have a detailed plan for 4.0 release finalized. We still have time to investigate in this field, so stay tuned.
