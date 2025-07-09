---
layout: post
title: "#SNMP Design: Levelizing on Library Side"
description: "This post is about the code base cleanup of #SNMP Library."
tags: SNMP
permalink: /snmp-design-levelizing-on-library-side-7ca59c20a7cb
excerpt_separator: <!--more-->
---
> Patrick Smacchia talks a lot about levelizing in his blog. As a fan of NDepend, I followed his advice and started to levelize on the Library side of #SNMP last weekend. Due to a network outage, I could not post about that change last Sunday so here is the post.

You may already know that in previous releases, the Library contains three layers of classes (one for messaging, one for MIB and another for components). So it is relatively hard to avoid dependency loop.
<!--more-->

For example, Lextm.SharpSnmpLib.Mib depends on Lextm.SharpSnmpLib because of a few exception classes, while ObjectIdentifier in Lextm.SharpSnmpLib depends on classes in Lextm.SharpSnmpLib.Mib.


Such dependency loops are bad because it introduces coupling that endangers future changes. Therefore, finally I decided to split the single assembly into three parts.

* SharpSnmpLib.dll now only contains messaging layer. So a few methods and constructors are removed from ObjectIdentifier class.
* SharpSnmpLib.Mib.dll now contains all MIB related classes.
* SharpSnmpLib.Controls.dll now contains the components.

The change is significantly a breaking one, but it also brings in some goodness,

1. The core library (SharpSnmpLib.dll) is only 80-KB, which makes it suitable for CF deployment.
1. MIB parsing and relevant resources are moved in a separate assembly (.Mib.dll), which makes it easier to switch to another MIB parsing engine.
1. We may push down a few useful classes from the Browser to the controls assembly in the future releases.

Now a Beta 2 package for 2.0 is available here.

We are now one step closer to the 2.0 release. Stay tuned.
