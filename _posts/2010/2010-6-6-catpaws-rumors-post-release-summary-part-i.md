---
layout: post
title: "CatPaw Rumors: Post Release Summary Part 1"
description: This post is about the future of Manager and Messenger classes.
tags: SNMP
permalink: /catpaw-rumors-post-release-summary-part-1-5dc1f4a327a3
excerpt_separator: <!--more-->
---
There are still pieces unmentioned for our 5.0 release. One of that is the future of Manager and Messenger classes.
<!--more-->
If you dig into our latest browser implementation, you will see Manager class is no longer used there. It is kind of a sign that we will get rid of this small but useful class in real world applications.

Manager was one of the early classes present in #SNMP library as it was a nice way to encapsulate all manager side functions into it (Level 3). However, soon we noticed it does not provide enough interfaces for advanced users. Messenger was added then to provide a medium level of encapsulation (Level 2). Note that you can always make use of ISnmpMessage derived classes directly which provides the lowest level of encapsulation (Level 1).

The usage of Manager becomes less, simply because our browser goes bigger and it requires more powerful things. Similarly this applies to Listener class and the agent. Therefore, in 5.0 release we started to review the design of Manager and Listener, and accordingly actions were taken. For example, bindings were introduced into the Listener class, and listener adapters were obsolete with SNMP processing pipeline introduced. Manager will face a similar attack in our 6.0 release, and it will be refactored or redesigned.

Messenger also faces demanding requests of changes. For example, it only supports v3 WALK now, and no more v3 related interfaces are yet added. So simply speaking if you are doing SNMP v3 with #SNMP, you can only use our Level 1 interfaces. How to find a set of Level 2 interfaces who are easy to use? How to bring something new to our Level 3 interfaces?

5.0 release was a nice milestone for #SNMP, as we found new approaches to do SNMP v3 better compared to old releases. But we were not able to make v3 support easier to use from API aspects. That becomes our focus on 6.0 release and wish something wonderful is there in front of us.

Well, finally leave you a few points to pay attention to,

1. Check out our samples to see how Level 1, 2, 3 interfaces are in use. For advanced users, please master our Level 1 interfaces as you usually need them.
1. For SNMP v1/v2c centric applications, if you want to migrate them to support v3, you must heavily utilize our Level 1 interfaces for v3. This can be hard as our own samples show, but it is doable.
1. For everyone, please post questions/provide feedback via our discussion board.

Stay tuned.
