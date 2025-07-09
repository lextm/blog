---
layout: post
title: "#SNMP Design: Turn On The Light"
description: "This post talks about MIB browser improvement and other bug fixes."
tags: SNMP
permalink: /snmp-design-turn-on-the-light-dd9ad54c79bf
excerpt_separator: <!--more-->
---
To develop a MIB browser was my ultimate goal on #SNMP. However, at this moment, I find that the hardest thing in fact is the MIB compiler. Why? If you notice, a #SNMP MIB Browser is already on its way to hit you.

Day by day, I keep adding new code to make it more powerful. Yesterday, I have completed the MIB tree panel user interface. So for the first time you can see what MIB objects are parsed from the 70 Net-SNMP MIB documents, and see their types (Object, Table, Entry, Column, and others).

A few bugs were found during the development and fixed immediately. Luckily these issues should not affect normal SNMP operations, and they only affects #SNMP MIB Browser.

Another good news is that I am going to publish the source code of this #SNMP MIB Browser under a more friendly license, the BSD license.

Stay tuned.
<!--more-->