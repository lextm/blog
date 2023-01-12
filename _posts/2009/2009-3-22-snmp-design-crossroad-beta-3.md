---
layout: post
title: "#SNMP Design: CrossRoad Beta 3"
description: "This post is about the new beta of #SNMP MIB Browser and Compiler."
tags: SNMP
permalink: /snmp-design-crossroad-beta-3-ce39689c01f9
excerpt_separator: <!--more-->
---
I started to publish beta packages for 2.0 a few weeks ago and today Beta 3 is available. What's the drive of this new package? Well, I will share with you my story.
<!--more-->

This week I got a task to check if Windows x64 SNMP agent delivers 64-bit specific objects. So I moved on and compared MIB documents from both x86 and x64 boxes. No doubt that they are exactly the same. But how to tell if this is a x64 box? I guess 1.3.6.1.2.1.1.1.0 can tell so I should have a check.

When I was still at Cisco, using a commercial MIB browser is always a few clicks away. But now what I could use? Well, luckily I have #SNMP MIB Browser. Then I simply downloaded and launched #SNMP MIB Browser (CrossRoad Beta 2) on the boxes. It should help import the MIB documents and tell me which values are on them.

But this short process also revealed a few critical problems. They are,

1. #SNMP MIB Browser and Compiler failed to launch because I need to update their app.config files. Luckily I realized this issue without using a debugger.
1. I could not compile http.mib because of the last character, which is strange. This is a known issue. Simply delete this character, then #SNMP MIB Compiler can compile it.
1. I need to load newly-compiled MIB documents one by one. I thought it would not be hard when I coded it like that, but surely I was totally wrong. It worked terrible that I was 100% percent bored. I promised that I would spend time this weekend to fix that.

Interesting that now I am done. I think next week if I need to use a MIB browser I shall have a better one. Do you like the new beta? If you have any comments, please feel free to let me know.
