---
layout: post
title: "#SNMP Design: Breaking Changes Coming, Part II"
description: "This post talks about the breaking changes coming in the next release."
tags: SNMP
permalink: /snmp-design-breaking-changes-coming-part-ii-398acc62f573
excerpt_separator: <!--more-->
---
In this part, I am going to talk about IDisposable. If you have mastered the Dispose Pattern designed first for Java and now for .NET, you already notice in the past, a lot of #SNMP types implement this interface. However, my latest research shows that it is unnecessary.

Why? Your type must implement IDisposable only if one of the fields implements it. So, a simple approach is used. Remove those UdpClient from fields, move them into methods that use them, and catch them inside using clause. Done. At last, I can clean up a lot of code to make things simpler.

Thus, you may get compiler errors if you have used those ISnmpMessage derivatives directly with using clause because the using clause can be deleted now.

I do not know yet if there could be a Part III because I think I can freeze the library code for 1.5 today.
<!--more-->