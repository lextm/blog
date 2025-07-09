---
layout: post
title: "#SNMP Design: The Puzzle of Zero"
description: "This post talks about the zeroes in SNMP protocol."
tags: SNMP
permalink: /snmp-design-the-puzzle-of-zero-d26d9979f6
excerpt_separator: <!--more-->
---
It is hard to translate .0.0 and .0 into bytes, isn't it? According to AdventNet's implementation, both of them should be translated to {0x06, 0x01, 0x00}. So is this the correct answer? If it is, now I have a good explanation for a long existing bug here (maybe it is resolved as .0 simply because .0 and .0.0 share the same bytes).

I think I need to borrow "Understanding SNMP MIBs" from a friend tomorrow to see if there were more details I simply ignored last time. Even though it is a great book, I don't know if it can solve all questions I have (although most of them are gone).

Once this puzzle is resolved, I may have a chance to close two more bugs in the list. Stay tuned.
<!--more-->