---
layout: post
title: "Roadmap of Stage 2.4"
description: "This post talks about the roadmap of #SNMP 2.x."
tags: SNMP
permalink: /snmp-design-instance-property-octetstring-encoding-8f355c053e9a
excerpt_separator: <!--more-->
---
It was in the latest Change Set 15756 that I added a static property DefaultEncoding to OctetString class. Soon, as a user commented in this thread, that was not enough if both ASCII and Unicode strings are required in the management system (especially for "community name"). Therefore, now I am working on a new approach.
<!--more-->

The idea is simple. Why not provide an instance property to OctetString for encoding? In this way, you can configure every objects of this class. I believe this is the most flexible way I can think of now. I will check in a new Change Set tonight so you can play with it and provide me feedbacks.

What's more, in order to make it much easier to send both ASCII and Unicode community strings to different SNMP agents in one application easily, I am going to change static methods in Manager component once again. This time, the community names will be passed in as OctetString (instead of System.String), so that you have a chance to specify encoding explicitly.

Stay tuned.
