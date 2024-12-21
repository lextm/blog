---
layout: post
title: "TritonMate Words: Story on RFC 3414 Support"
description: "This post is about the story of adding RFC 3414 support in #SNMP."
tags: SNMP
permalink: /tritonmate-words-story-on-rfc-3414-support-5a7ff6448e7b
excerpt_separator: <!--more-->
---
Back in May 2009 when I was working on initial SNMP v3 support, I think the discovery process was rather simple. Since then that piece of code have been working well. It seems to me that choosing Net-SNMP agent/utilities as reference is a good idea. However, observing discovery process by capturing message dumps was in fact a stupid idea, because the observation could be incomplete and corner cases could be neglected.

Finally we received an in-depth bug report in October.
<!--more-->

I did not pay much attention to it, and thought that this Cisco agent was not properly configured. But thanks to HiMik74, who appears to be demanding and detail-oriented, more evidence had been collected and the whole picture became clearer every time we had new packet captures.

So what's so special about this Cisco SNMP agent and RFC 3414? Let's first review what Net-SNMP agent behaves during v3 discovery with its own utility,

1. The utility (snmpget) sends an empty GET request to perform discovery.
1. The agent responds with a REPORT message which not only contains the agent's engine ID, but also the engine time data.
1. Finally the utility can construct a new GET request with engine ID and time data filled.
1. The agent happily responds with the data the utility asks for.

Is this behavior correct according to RFC 3414? Nope! The standard document actually said,
http://tools.ietf.org/html/rfc3414#section-4, that at step 2 only engine ID should be returned by the agent. Well, I have to take off my hat to the Cisco engineers who implemented SF 300's firmware. They strictly followed the RFC and this agent expects the following conversation to be carried out,

1. The utility (snmpget) sends an empty GET request to perform discovery.
1. The Cisco agent responds with a REPORT message which only contains the agent's engine ID.
1. The utility can construct a new GET request with engine ID filled, which does have empty time data.
1. The agent this time replies with another REPORT message which contains the time data.
1. The utility constructs a new request with time data filled.
1. The agent happily responds with the data the utility asks for.

Net-SNMP's utilities are smart enough to perform this kind of conversation, as I think they have been played with such devices for a long time. As a result, my task then was to educate #SNMP's utilities to perform the same steps, and yesterday I finished the fix.

Except the fix to support the longer discovery process, there is another fix added to support all Request messages to be sent at step 1. I stupidly thought that only GET requests should be sent, but RFC3414 indicates that in fact other types of Request messages must also be supported. Luckily soon we received a new bug report which provides evidence.

After two months of investigation, #SNMP reaches better compliance with RFC3414, and have two critical issues fixed. Thus, it is time to cut a new maintenance release (7.6 or another number).

My focus will shift back to the compiler, as I received all books related. The major task of TritonMate will be carried out in the next few weeks.
