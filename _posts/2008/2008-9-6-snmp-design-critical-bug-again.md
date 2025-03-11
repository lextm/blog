---
layout: post
title: "#SNMP Design: Critical Bug Again"
description: "This post talks about a critical bug."
tags: SNMP
permalink: /snmp-design-critical-bug-again-f3a5dafd1d02
excerpt_separator: <!--more-->
---
A critical bug was just noticed by Steve, and he isolated it into a test case. I did have a quick fix earlier today, but now it seemed a bad approach. Finally, I further isolated this bug into a few new test cases in ObjectIdentifier class. Exactly, the bug is inside ToBytes. Happily, this time I need to dig deeper to provide a complete fix (the quick fix is in fact useless).

Hope I can finish this tomorrow. Stay tuned. (I will also contact Malcolm, too, because his SNMP tool does have similar issue.)
<!--more-->