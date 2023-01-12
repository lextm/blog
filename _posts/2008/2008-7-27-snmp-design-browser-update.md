---
layout: post
title: "#SNMP Design: Browser Update"
description: "This post talks about the update of the MIB browser."
tags: SNMP
permalink: /snmp-design-browser-update-9bd1942b53b7
excerpt_separator: <!--more-->
---
Since TwinTower release (1.5) is going to have a basic MIB browser, I started to finish the task step by step last week just after releasing UnicornHorn (1.0).
<!--more-->

The very first thing I try to accomplish was the MIB tree feature. The 1.0 release already has a tree structure done, so this time a module list is added.

It is easy now to add new MIB documents by clicking Add button on module panel. Parsing a problematic document will trigger a few error dialogues with detailed error information. Please pay attention to the panel because it also tells you which modules are not loaded because of dependency issues. And pending modules are listed in gray. Every time new documents are parsed, the tree panel will be updated automatically.

There is a lot of room for improvements. Some of them are,

* store new documents so no need to add new documents every time you launch the browser. (I do not yet decide where to store these documents but I promise soon it will be done.)
* allow to remove documents. (but default ones cannot be deleted.)
* provide more information about pending documents. (for example which dependencies are missing.)

But now I have moved on to design the agent profile section to store SNMP agent information. This section also needs a place to save data. Therefore, I am going to develop a common data storage for all browser features. Although I have done similar things before for Alex and CBC, this time I am not yet sure which way is better.

Stay tuned.
