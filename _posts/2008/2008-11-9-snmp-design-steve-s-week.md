---
layout: post
title: "#SNMP Design: Steve's Week"
description: "This post is about Steve's work in the past week."
tags: SNMP
permalink: /snmp-design-steves-week-f052a50ac4f
excerpt_separator: <!--more-->
---
This week Steve provided a new Change Set , which makes the Browser nearly complete. Therefore, I think it is time to release a new RC for TwinTower in November so a final 1.5 release by the end of 2008. This is really overdue to my original plan but I am the one you should blame. So leave Steve alone :)
<!--more-->

I hope soon the development can be sped up but now I really have no news to update. Is it true? Oh, wait a minute. There is actually something worth mentioning that Steve started to work on the Library.

When you navigate to Manager.cs, probably you find it confused to see two Walk methods there, the classic one and a new SteveWalk. It is amusing that Steve tried to enhance it but rather create a new method instead of deleting mine. I guess it is because he did not find a unit test case there to guarantee his should not break anything existing. Therefore, a new Work Item is added so a new case may be added to test about Walk. Oh if I had applied TDD everywhere, it would be this confusing today. So sorry, guys. I can confirm here that Steve is going to delete the classic one soon and then the confusion will go away.

I really start to think about things beyond TwinTower lately because there are still so many pieces ahead. For example, the Compiler and Browser "separation and integration", SNMP v3 packets, agent side, and so on. I think it is even possible to build the Compiler and Browser based on Visual Studio Shell or SharpDevelop in order to provide a modern MIB editor to attract users. But that will take a longer time to achieve certainly.

Stay tuned and see you next weekend.
