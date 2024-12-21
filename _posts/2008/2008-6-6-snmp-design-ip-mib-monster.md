---
layout: post
title: "#SNMP Design: IP-MIB Monster"
description: "This post talks about the progress of #SNMP 0.9 release."
tags: SNMP
permalink: /snmp-design-ip-mib-monster-9a40366c13d8
excerpt_separator: <!--more-->
---
It is really a challenge to parse IP-MIB. Why? This file contains 185,928 bytes so a lot of definitions. Therefore, after parsing this file, I got 293 more nodes in the MIB tree.
<!--more-->

A few issues were introduced because I did not take enough care of TEXTUAL-CONVENTION in the past and there was a big bug in the lexer which is triggered by this big MIB document.

In all, nine MIB documents can be parsed by the experimental parser. A nice start, isn't it?

Stay tuned.

BTW, a developer has just contacted me to ask why he cannot open #SNMP projects in his Visual Studio. I'd like to mention that those projects are in Visual Studio 2008 format so can only be opened in Visual Studio 2008 and SharpDevelop 3.0.

Sorry that I have got addicted to C# 3.0 and have no plan to bring #SNMP back to C# 2.0.
