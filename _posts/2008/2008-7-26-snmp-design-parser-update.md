---
description: This post talks about the update of the MIB parser.
excerpt_separator: <!--more-->
layout: post
permalink: /snmp-design-parser-update-51fa55793986
tags: linux snmp
categories: [Operating Systems]
title: '#SNMP Design: Parser Update'
---
I know that it is impossible to write a perfect MIB parser in a few months, but I am still satisfied about the simple parser I wrote for #SNMP library in May and June as it successfully parses 70 Net-SNMP bundled MIB documents without an exception.
<!--more-->

However, I know there are bugs inside because Net-SNMP bundles nice MIB documents with consistent format. Yes, other MIB documents may cause an exception just because its format is cripple. That's my fault, because I never knew how ugly a MIB document might be.

During the development of #SNMP MIB Browser (especially the MIB tree feature), I have to enhance the parser from time to time to parse a few MIB documents downloaded from the Internet. Luckily, the changes are small, so I think my original design is not too bad.

And today, I can announce that this parser can parse over 100 different MIB documents without an exception. Stay tuned.
