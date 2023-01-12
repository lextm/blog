---
layout: post
title: "#SNMP Design: Library Update"
description: "This post talks about the update of #SNMP library."
tags: SNMP
permalink: /snmp-design-library-update-4c705cee683e
excerpt_separator: <!--more-->
---
After the Refresh release (1.1), I did change #SNMP basic API again, and some of them are significant,

All Manager methods require an extra port number argument. Even though normally you can use 161, in some cases you may want to use another.
More SNMP v2c related classes are added. You can check how many work items have been closed during these weeks. Wow.
At last, by using InternalsPublicTo attribute, I successfully split all unit tests into a separate assembly.
Now you can try to discover SNMP enabled devices in your network by calling Manager.Discover. A new demo project is added as well.
That's all for this time. Stay tuned.
<!--more-->