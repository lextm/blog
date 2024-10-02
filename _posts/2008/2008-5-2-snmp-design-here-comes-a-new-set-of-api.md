---
layout: post
title: "#SNMP Design: Here Comes A New Set of API"
description: This post talks about the new API of #SNMP.
tags: SNMP
permalink: /snmp-design-here-comes-a-new-set-of-api-ededcefba0e0
excerpt_separator: <!--more-->
---
To keep you update, I have just published a new build (version number 0.5.010502.335) of #SNMP here. The biggest change is the API it provides. Compared to older builds, this build removes a lot of weak typed classes (such as the over-powerful Universal and SnmpBER created by Malcolm).
<!--more-->

Strong typed classes can make the users easier to see what properties and methods are available. And right now, with the help of Manager component, SNMP operations like GET, SET, and TRAP can be done as easy as possible.

I am working on other operations like table manipulation and MIB parsing. Once they are added to Manager, I believe it is time to release a 0.9 release of #SNMP.

You may notice that nearly all Malcolm's code has gone. No. The code is extracted and moved into smaller classes by heavy refactoring.

By the way, I don't have enough time to write a few demos or documents in order to show how to make use of every bit, but there are lots of unit test cases embedded, so you can understand how to use the API from them. I plan to write a few posts in May to illustrate #SNMP's power.

Stay tuned.
