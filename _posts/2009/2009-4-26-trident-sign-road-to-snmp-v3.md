---
layout: post
title: "Trident Sign: Road to SNMP v3"
description: "This post is about the plan to work on SNMP v3 features."
tags: SNMP
permalink: /trident-sign-road-to-snmp-v3-6aac30a6040
excerpt_separator: <!--more-->
---
We shall finally come to work on SNMP v3. But how to go there step by step? I have a list below and hope that following it we can reach the land.

1. Configure Net-SNMP agent so that I can test #SNMP against it.
1. Develop an SNMP v3 compliant manager to talk to that agent.
1. Design necessary agent parts so that it can perform basic functions like its Net-SNMP counterpart.

Good news is that I just finished the first critical task. Well, that's a good start. Cooking Trident must be cooler :)

## Updated:

You must wonder how to configure Net-SNMP agent, so here are the links you must read,

* http://docstore.mik.ua/orelly/networking_2ndEd/snmp/ch07_01.htm
* http://docstore.mik.ua/orelly/networking_2ndEd/snmp/appf_02.htm
<!--more-->