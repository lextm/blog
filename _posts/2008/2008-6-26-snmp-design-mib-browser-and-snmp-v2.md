---
layout: post
title: "#SNMP Design: MIB Browser and SNMP v2"
description: "This post talks about MIB Browser and SNMP v2 support."
tags: SNMP
permalink: /snmp-design-mib-browser-and-snmp-v2-74a48ec539ce
excerpt_separator: <!--more-->
---
I was thinking about what demo should be added in UnicornHorn and today I finally made up my mind. Why not create a simple MIB Browser? Yes, it is quite possible because I ready had the basis there in NineHeaded.

If you notice, in change set 13748 I have enabled SNMP v2 support on GET and SET operations. This was requested by a user named Peter. However, please notice that this support is still experimental. Although #SNMP can correctly handle new error codes introduced in SMI-II, it cannot yet process SNMP exceptions. Thus, exceptions like "no such instance" cannot be treated correctly by #SNMP at this moment.

It is happy to hear from my users here, and if you have any question about #SNMP, put it down.
<!--more-->