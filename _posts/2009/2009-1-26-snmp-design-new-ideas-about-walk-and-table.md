---
layout: post
title: "#SNMP Design: New Ideas about Walk and Table"
description: "This post is about new ideas on how to implement SNMP walk and table."
tags: SNMP
permalink: /snmp-design-new-ideas-about-walk-and-table-a9c9113b2229
excerpt_separator: <!--more-->
---
I discussed with Steve several times before we shipped TwinTower. We agreed that it is a big task to finish through multiple releases, so TwinTower only contains a new implementation of Walk from Steve.
<!--more-->

We are going to investigate more in this field, but at first I would like to ask a simple question, "why Net-SNMP does not get a table unless it has the MIB?"

You may wonder why I asked this question, as #SNMP can get such a table even if the MIB is not loaded. I have to confess I underestimate the role of MIB in the past. :(

In fact, SNMP table is a complex thing. When you understand more and more MIB documents, you will notice there are many complex tables who have a lot of indices. Therefore, without an MIB definition, it is impossible to get a complex table as its walk result may be very very weird.

I will try to post more details later after I heavily improve our MIB parser/compiler. I believe only when the parser is ready and we can extract enough information from MIB documents, we are ready to advance support on SNMP tables.

Stay tuned.
