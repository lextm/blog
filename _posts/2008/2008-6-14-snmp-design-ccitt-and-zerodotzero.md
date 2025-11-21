---
description: This post talks about the difference between ccitt and zeroDotZero.
excerpt_separator: <!--more-->
layout: post
permalink: /snmp-design-ccitt-and-zerodotzero-f87da8b8c3b6
tags: snmp windows
categories: [Technologies and Concepts]
title: '#SNMP Design: ccitt and zeroDotZero'
---
According to comments inside SNMPv2-SMI, zeroDotZero is used as "a value used for null identifiers". However, when I tested #SNMP against Microsoft SNMP agent for Windows Vista Home Basic, I found that this agent returned `ccitt` when the identifier is `null`.

I didn't have chance to test other agents, so I don't know whether right now I need to fix #SNMP to replace occurrences of `ccitt` with `zeroDotZero`. But this issue is logged here as #2366 under Issue Tracker.
<!--more-->