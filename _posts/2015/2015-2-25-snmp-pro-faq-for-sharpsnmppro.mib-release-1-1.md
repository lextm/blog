---
layout: post
title: "#SNMP Pro: FAQ for SharpSnmpPro.Mib Release 1.1"
description: This post is about some frequently asked questions about SharpSnmpPro.Mib release 1.1.
tags: SNMP
permalink: /snmp-pro-faq-for-sharpsnmppro-mib-release-1-1-b68824d9220a
excerpt_separator: <!--more-->
---
Some users wrote in to ask questions about this new release. Here I pick up a few common questions as FAQ.
<!--more-->

## Q1: #SNMP Library 8.5 requires KB2468871 to be applied for .NET 4.0 environment. Does that restriction also affect SharpSnmpPro.Mib?

Answer: Yes, it does. The trial and paid versions of SharpSnmpPro.Mib depends on #SNMP Library 8.5, so it also requires KB2468871.

If your applications do require .NET 4.0 without KB2468871, please write to support@lextm.com and a special version can be compiled and sent to you to remove this restriction. But that version depends on an earlier version of #SNMP Library. Meanwhile, Microsoft will stop supporting .NET 4.0 on Jan 12, 2016. So this special version is only supported by LeXtudio till that day. Any SharpSnmpPro.Mib user should migrate to the standard paid version before that day.

## Q2: Release 1.1 is a free update for all 1.0 users. What about the future releases?

Answer: 1.x patched versions will be free for 1.x users. That guarantees that you get all bugfixes.

Only when there is significant new features added to the library and the version number is bumped to 2.0, you need to pay the upgrade fee.

When 2.0 is available, 1.x support contract will no longer be sold.

All users with active support contracts will receive 1.x patching till the end of their support contracts.

## Q3: What about the source code? When will source code access be given?

Answer: Currently the plan is to sell a special version (with no obfuscation at all) to users who want to better understand the code base and customize it. There are some technical issues preventing me from selling the source code directly.

Stay tuned.