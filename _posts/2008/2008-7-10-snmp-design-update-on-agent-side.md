---
layout: post
title: "#SNMP Design: Update on Agent Side"
description: "This post is about the update on #SNMP agent side support."
tags: SNMP
permalink: /snmp-design-update-on-agent-side-7d086531037c
excerpt_separator: <!--more-->
---
For a long time, #SNMP focuses on SNMP manager side. Therefore, when one user asked if he/she could send out TRAP with #SNMP, I was surprised.

And today, I am so glad to see two votes on my poll that my work last night is not meaningless.
<!--more-->

If you check out the latest source code, you can see a new project named TestSendTrap. This project illustrates how to send a TRAP with #SNMP. I hope it is a good start on #SNMP agent side support.

The development last night went on quite well because TrapMessage class and TrapV1Pdu already provides the skeleton. All I needed to do is copy one constructor from GetRequestMessage and then paste into TrapMessage. After a few modification, a new constructor for TrapMessage was there. This constructor helps you to construct a TrapMessage from all information you want to send (including enterprise, generic, specific, and so on). At last, a Send method was added to TrapMessage, too. You can simply call this method to send the TrapMessage instance out via UDP.

> (please notice I renamed TrapMessage to TrapV1Message because there comes a TrapV2Message)

This TestSendTrap project can be tested against TestTrap project and it worked fine last night.

After all, it is not too hard to add agent side support into #SNMP. However, because of the complexity of SNMP agents, there is a lot to be done. Stay tuned.
