---
layout: post
title: "#SNMP Design: A Little Bit Broadcasting"
description: "This post talks about UDP broadcasting feature of #SNMP library."
tags: SNMP
permalink: /snmp-design-a-little-bit-broadcasting-954d2b48c1c6
excerpt_separator: <!--more-->
---
Maybe you have this question just like me. If I already know there is a lot of SNMP enabled devices in my network, how can I add them easily? Yes, when I am not the administrator, I cannot have a list of IP addresses at hand. So, there is no hope, isn't it?
<!--more-->

In the past few weeks, a serious #SNMP user have been working with me on this topic (YttriumOx, isn't that you?). And finally, this feature is done today. I am happy to announce that now you can try Manager.Discover to find those devices. The IDictionary returned by this method contains an IP address list you expect. The TestDiscovery demo can guide you.

But I have to say it is not perfect (maybe some agents just ignore the broadcast packet). I find that I cannot get a response from the Windows Vista SNMP agent on my own computer. Maybe Microsoft knows why.

Also I'd like to state here that another major release is coming. Yes, the 1.5 (TwinTower) release is 90% done. All I need to do now is integrate all parts and clean up the code base again. Stay tuned.
