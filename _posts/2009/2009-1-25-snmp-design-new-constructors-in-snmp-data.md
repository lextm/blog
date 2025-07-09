---
layout: post
title: "#SNMP Design: New Constructors in SNMP Data"
description: "This post is about the new constructors in SNMP data types."
tags: SNMP
permalink: /snmp-design-new-constructors-in-snmp-data-855781525f07
excerpt_separator: <!--more-->
---
Dramatic changes happened today in the repository, but you may not notice. Ha, it is normal because I only touched API you won't use, generally speaking.
<!--more-->

This time I started to hide constructors such as public Counter32(byte[]) and expose public Counter32(int, Stream) instead. Why? After a review, I found that all the times, I created new MemoryStream objects from bytes who indirectly come from MemoryStream. So I believe passing MemoryStream directly is better.

Therefore, now everything starts with MemoryStream and ends with bytes, while nobody plays the middle man again.

By the way, now I am enjoying the Chinese spring festival. Simply wish that I could work out a plan for 2.0 release during these days. Stay tuned.

Updated:

You may notice that in our latest repository a lot of methods are removed while new methods added. And a key change is that ISnmpMessage is no longer derived from ISnmpPdu. I consider this a reasonable change as messages are not PDU in fact.
