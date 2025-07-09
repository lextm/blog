---
layout: post
title: "HoneyCell Drops: Pipeline in Browser"
description: This post is about the pipeline in the browser.
tags: SNMP
permalink: /honeycell-drops-pipeline-in-browser-2a992a2a61c8
excerpt_separator: <!--more-->
---
Remember how we turned Agent class to an SNMP pipeline in our 5.x release? It is a nice example to show how our initial design back in 2008 ages through the years, and has to make way for new stuffs who grow and take over the responsibility.
<!--more-->

Scenarios on the Manager side are similar now. First, the Manager class is on the verge of being removed (it is officially obsolete). Second, all listener adapters are now obsolete. (It is not easy to migrate, but I will write a post for that.) And definitely the Browser has evolved accordingly.

Because we can no longer use listener adapters, the only choice remains on the table is moving to SnmpDemon and the pipeline. Yes, the same pipeline we use in snmpd. It may sound like a small change, but anything about the pipeline is in fact complex. What will be the output?

Finally support for v3 INFORM in the browser is added because the pipeline provides all necessary elements, such as v3 discovery and security model.

Yes, this change relies on new message handlers (for TRAP and INFORM) implemented and other according changes prepared.

However, v3 TRAP is still missing, as I am not yet sure how to write a proper test case before implementing it, or whether this feature is that critical.
