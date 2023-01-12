---
layout: post
title: "Trident Sign: SNMP v3 Packet Format"
description: "This post is about the packet format of SNMP v3."
tags: SNMP
permalink: /trident-sign-snmp-v3-packet-format-636565d73d8d
excerpt_separator: <!--more-->
---
RFC 3412 is the document who defines SNMP v3 packet format. This format is much more complicated than v1 and v2c, and it took me a long time to carefully analyze the structure.

http://www.ietf.org/rfc/rfc3412.txt
<!--more-->

Well, actually parsing the entities from packets are easy, as the data types are the same. But v1 and v2c share the same format, which contains a small number of entities, while v3 packets have more entities to provide authentication and privacy features. Then it is rather hard to enhance GetRequestMessage class to support v3, without breaking existing v1 and v2c test cases.

Suddenly, I noticed that I can find v1 and v2c fields from v3 format.

http://www.tcpipguide.com/free/t_SNMPVersion3SNMPv3MessageFormat.htm

For example, community name is just like message user name, and PDU is part of scoped PDU. Therefore, finally I inserted a suite of segment classes into the library. For example, header segment contains necessary fields for v3, but it becomes null for v1 and v2c; security parameters segment becomes community name for v1 and v2c; scope PDU downgrades to PDU.

Well, luckily I still have enough test cases available to ensure my changes do not break existing code. Cool
