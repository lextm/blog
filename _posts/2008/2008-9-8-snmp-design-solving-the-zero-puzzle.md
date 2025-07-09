---
layout: post
title: "#SNMP Design: Solving the Zero Puzzle"
description: "This post talks about the solution to SNMP zero puzzle."
tags: SNMP
permalink: /snmp-design-solving-the-zero-puzzle-ad094d078cfd
excerpt_separator: <!--more-->
---
It is happy that now I have "Understanding SNMP MIBs" at hand. The solution to the zero puzzle can be found on page 394 and 395 (Appendix A). I don't want to bother you with the details which most of you may not be interested in, but a small hint can be provided that the encoding (ToBytes) algorithm in #SNMP needs to be updated ASAP(Malcolm's code works fine for iso subtree, but not correct for both ccitt and joint-iso-ccitt subtrees).

An interesting thing is that according to the standard, .0 and .0.0 share the same byte form (OH, this causes serious confusion!). Therefore, whenever {0x06, 0x01, 0x00} is received it should be translated to .0.0 by default. As a result, a new rule is going to be added in ObjectIdentifier constructors that the length of the shortest identifier is two (then .0 is not supported, and the ambiguity is resolved).

The complete fix will be available later in the repository. Stay tuned.
<!--more-->