---
layout: post
title: "#SNMP Design: Locating Boxing The Standard Way"
description: "This post talks about how to locate boxing instructions in #SNMP library."
tags: SNMP
permalink: /snmp-design-locating-boxing-the-standard-way-13eb1cecfd6b
excerpt_separator: <!--more-->
---
I bought a lot of C# books this year to investigate under the surface when Effective C# does not provide me more insight. So now the "CLR via C#" is open in front of me, and I am on page 133. The Importance banner for the very first time attracts my attention to ILDasm.exe. Yes, in the past I never use this tool, so I never know how many box instructions are there inside #SNMP.
<!--more-->

Goodness, the count for Change Set 15686 is 191. So is it a large number? After a few clean up, I reduce this number to 16. Therefore, 191 is relatively large (more than 10x). But the clean up requires a lot of ISnmpData derivatives be changed from value type to reference types (right now I don't know if this change is wise).

I don't know if there is any way to clean up the remaining items, because they are closely related to enumerations. It seems that there is no way to call enum.ToString without a box instruction, so I leave them alone.

Any way, the most important thing is that now I understand boxing and unboxing much better.
