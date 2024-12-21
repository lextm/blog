---
layout: post
title: "#SNMP Design: Two New Issues Found"
description: "This post is about two new issues found in #SNMP."
tags: SNMP
permalink: /snmp-design-two-new-issues-found-f4f0081a76de
excerpt_separator: <!--more-->
---
Two more #SNMP issues were reported this week. And luckily both of them have workarounds.
<!--more-->

First, the parsing algorithm failed when special characters such as SUB occur in the MIB documents. It was only when I tried to parse Windows Vista MIB documents that I met it. The workaround is to remove such characters from the files.

Second, it may not be feasible if an exception is raised when you try to get a bunch of objects and only one of them fails. Therefore, I plan to improve in such an area later. For example, I can keep the Manager methods unchanged while providing new methods in GetRequestMessage so you can touch the response message directly to determine how to handle it in your way. However, this really takes time and I must consider when to provide it. The workaround is to modify GetRequestMessage yourself in an ugly way (sorry for that).

That's all for this week. Stay tuned.

BTW, if you are interested, I suggest you watch PDC 2008 recordings to know more about Microsoft platforms. They are amazing! I love Miguel's Mono session a lot. But you will find it even more funny if you watch Anders Hejlsberg's session at first. Follow my suggestion and you will see why. :)
