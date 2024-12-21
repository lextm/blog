---
layout: post
title: "TritonMate Words: ifTable Implementation"
description: "This post talks about the implementation of ifTable in TritonMate."
tags: SNMP
permalink: /tritonmate-words-iftable-implementation-c15a6b8a587f
excerpt_separator: <!--more-->
---
#SNMP has a reference design of SNMP agent, which should have been known for a while. But up to now the problem is inside of it there is no real-world SNMP table example. Yes, that is a big problem. The sysORTable might be an example, but it is faked, and it is not available by default in most MIB browsers (due to the MIB document versioning issues). So even if you want to try it out, it might take extra efforts.
<!--more-->

Today, I finally finished implementing the ifTable (.1.3.6.1.2.1.2.2) which should be available everywhere, and what's more interesting is that this table is real, not faked. When you use a MIB browser to monitor it (either #SNMP MIB Browser, iReasoning MIB Browser, or any other), you will see numbers updated as expected. Right, the objects are indeed tied to the underlying network interfaces, via NetworkInterface class of .NET Framework.

The changes are available in this change set,

https://github.com/lextudio/sharpsnmplib/tree/3ab8108b08516ca5eb2e6f654c33540350acc0c1

I might move on and implement more tables to explore what kind of difficulties might appear. Please do let me know if you meet any difficulties in your work, so we can troubleshoot them together.

Stay tuned.
