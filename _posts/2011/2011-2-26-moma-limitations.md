---
layout: post
title: "MoMA Limitations"
description: "This post is about MoMA tool limitations."
tags: Mono
permalink: /moma-limitations-e5438c2c1187
excerpt_separator: <!--more-->
---
To port a Windows/.NET application to Linux/Mono, you must have too many skills and a lot of patience. Though Mono team invent MoMA and keep improving it, there are still some areas MoMA cannot cover. These are the limitations you should pay special attention to. I found them during porting #SNMP to openSUSE/Mono.
<!--more-->

First, if MoMA reports one assembly contains missing/TODO/not implemented APIs, you still have some possibility to use it on Linux/Mono without a problem. A typical example is Microsoft Unity. I use Unity in #SNMP, but the part of Unity #SNMP relies on seems to be working fine on Mono, although MoMA reports several issues.

Second, MoMA is not yet able to analyze some compatibility issues, such as the ones listed in this guideline page,

http://mono-project.com/Guidelines:Application_Portability

You must pay more attention to the guidelines, as this kind of issues are harder to identify and fix.

So "check out your source code on Linux, build it in MonoDevelop and run your application" can be a good start. A crash can indeed tell you more than all the written words, and reveal how uniqueness your application is.

Good luck.
