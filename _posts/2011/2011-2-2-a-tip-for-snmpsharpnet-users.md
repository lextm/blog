---
layout: post
title: "A Tip for SnmpSharpNet (SNMP#NET) Users"
description: "This post is about a tip for SnmpSharpNet (SNMP#NET) users."
tags: SNMP
permalink: /a-tip-for-snmpsharpnet-snmp-net-users-6a23a02b71e
excerpt_separator: <!--more-->
---
Well, I believe you have the habit of reading release notes and pay attention to what was written in SnmpSharpNet's one.

Then you should know that in almost all cases Dispose or using must be used for UdpTarget objects. However, many users ignored this tip and experienced socket problems.

Luckily #SNMP uses a different design which is free of such issues, so you can feel free to try it out.
<!--more-->