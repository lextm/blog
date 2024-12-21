---
layout: post
title: "TritonMate Words: License Change on SNMP Engine Support"
description: "This post is about the license change on SNMP Engine support related source files."
tags: SNMP
permalink: /tritonmate-words-license-change-on-snmp-engine-support-e7410b98e8e
excerpt_separator: <!--more-->
---

If you follow #SNMP project closely, [you should already know]({% post_url 2012/2012-2-4-tritonmate-words-upcoming-change-to-sharpsnmplib-mib-dll-license %}) that the license for SharpSnmpLib.Mib.dll has been changed from Lesser GPL to BSD 3 Clause.

Now another change is coming, as documented in KB600012.

<!--more-->

SharpSnmpLib.Engine.dll assembly in fact contains two namespaces, Pipeline and Objects, which were originally part of snmpd project (released under MIT/X11), and later moved to SharpSnmpLib.dll (released under Lesser GPL). However, the nature of agent development usually requires modifications on the classes under these two namespaces, so as to customize the agent behaviors. Lesser GPL requirements can be a roadblock for commercial shops who would like to play with it.

I don't plan to sell commercial licenses for these two namespaces, as they are still in early development phase, and does not meet strict quality standards yet, so even if we sell them, supporting the users can be too huge a burden. Now you can feel free to shape them to whatever you like and hope you like this change.

Remember to go to our master branch, as that's for our 8.0 release, and covered by this license change. The previous releases (6.\*, and 7.0) are still covered by our previous licensing model.

https://github.com/lextudio/sharpsnmplib

Stay tuned.
