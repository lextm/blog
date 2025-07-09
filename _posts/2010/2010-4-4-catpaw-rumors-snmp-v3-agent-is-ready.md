---
layout: post
title: "CatPaw Rumors: SNMP v3 Agent Is Ready"
description: "This post is about SNMP v3 Agent"
tags: SNMP
permalink: /catpaw-rumors-snmp-v3-agent-is-ready-fd7b5819093b
excerpt_separator: <!--more-->
---
In #SNMP Suite release 4.0 we delivered an SNMP agent which supports v1 and v2c. How far away are we from v3 support?
<!--more-->

The first missing piece is the discovery process. How to respond to v3 discovery message was a question raised on the discussion board before we released 4.0. At that time I was not sure how hard it is. Soon I found it is not that difficult, and adding a few lines in v3 membership provider is all it requires. In this way we resolved work item 6128 and advanced the agent a little bit.

The second piece is to support v3 modes. This is relatively easy, because our MessageFactory implementation already helps parse the messages. However, if decryption of messages is taken into consideration, the problem arises. What if we cannot get the scope part of the message? That means we lost all information such as PDU. Interesting that after we introduced malformed message, everything becomes easy.

Currently we did not yet complete v3 support in snmpd, as there are many details to review in order to improve RFC compliance. But this can be deferred to future builds. My next focus is v3 support in the browser. In release 4 I already did some fundamental tasks, and now it is time to fill in the blanks.

Stay tuned. More will come in this beautiful spring.
