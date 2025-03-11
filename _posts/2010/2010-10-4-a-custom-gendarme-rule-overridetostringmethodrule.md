---
layout: post
title: "A Custom Gendarme Rule: OverrideToStringMethodRule"
description: This post is about a custom Gendarme rule.
tags: Mono
permalink: /a-custom-gendarme-rule-overridetostringmethodrule-fc52ebb18c78
excerpt_separator: <!--more-->
---
I started to use GitHub as I would like to write patches for the software I use the most and love the most. So today I finally checked in a patch for Gendarme,

http://github.com/lextm/mono-tools
<!--more-->

This new rule named OverrideToStringMethodRule, and it analyzes all classes in your assemblies to see if they override ToString method.

Well, it can be a very annoying rule for someone. Yes, I confess that for UI related classes it is not critical to do so. But if you ever design a framework for other to use, which is kind of complex, you have to somehow override ToString method. Only in this way when your users try to debug code, they can enjoy the ease you provide because for example Visual Studio can display a lot of information in its tool tip or Watch panel for the objects and they don't even need to expand their members for more details.

I have been using this rule for a long time for #SNMP, and I hope you find it helpful.
