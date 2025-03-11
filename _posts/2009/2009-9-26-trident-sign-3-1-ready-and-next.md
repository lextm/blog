---
layout: post
title: "Trident Sign: 3.1 Ready and Next"
description: "This post is about the 3.1 release."
tags: SNMP
permalink: /trident-sign-3-1-ready-and-next-bc522bef47fb
excerpt_separator: <!--more-->
---
I just checked in the last bit for 3.1 release. So Trident Refresh will be released after one month of baking. This is a bug fix release, so changes are rare (but some are significant),
<!--more-->

1. Work item 4988 is resolved. This issue can lead to memory leak, so all 3.0 users need to migrate to 3.1 as soon as possible.
1. `snmpset` tool is enhanced. Now it supports most argument the Net-SNMP alternative uses.
1. `snmpwalk` tool now supports `mode` switch.
1. SharpSnmpLib.Optional.dll is added. An experimental AES privacy is added. I may port more such providers from SNMP#NET in the future.
1. Message factory parser is enhanced. Bytes that cannot be parsed as SNMP messages will be thrown out in SharpMessageFactoryException.
1. StringUtility.GetAlternativeTextualForm is finally added. It can be used to generate strings such as `iso.org.dod.internet.mgmt.mib-2.system` which is asked by many #SNMP users.

I have chosen a name for our 4.0 release. That is, SquareRoot. In that release, we will see more enhancements for the Browser and the Compiler, which aim to make your life much easier than present. If we are lucky enough to have a new compiler implemented in this release, then we may get rid of some long lived issues and provide much more powerful features.

I admit that this new compiler has been delayed several times. But still at this moment I don't have anything more to share. We won't upgrade the poor-designed one existing, and we lack of resources to finish the experimental one. Maybe I should have learned ANTLR earlier and spent more time on that approach.

Anyhow, we have delivered a lot still in Trident, so we are on the way again.

Stay tuned.
