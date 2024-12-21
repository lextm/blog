---
layout: post
title: "#SNMP Design: An Extra Refresh for TwinTower"
description: "This post is about another important release for TwinTower."
tags: SNMP
permalink: /snmp-design-an-extra-refresh-for-twintower-2009c8d650ce
excerpt_separator: <!--more-->
---
We did a Refresh for UnicornHorn last year and now a similar Refresh for TwinTower is on its way. Note that I am talking about the Library. The Browser and Compiler will be a separate story.
<!--more-->

Big changes are,

1. More obsolete elements. This points out what we are going to change in CrossRoad. So you should really consider migration from time to time.
1. Inheritance changes. ISnmpMessage is no longer derived from ISnmpPdu or ISnmpData. Many functions are pushed down or pulled up.
1. MIB files are removed from resources. So the library is only around 140-KB at this moment (it was 2.2MB in UnicornHorn Refresh). *.module files are included instead.
1. Table OID validation becomes stricter.

Beta 1 for 1.6 is now available here. Take a look if you are interested. Stay tuned.
