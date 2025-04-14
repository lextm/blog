---
description: 'This post is about the design of static methods in #SNMP.'
excerpt_separator: <!--more-->
layout: post
permalink: /snmp-design-static-methods-8fda0d466c89
tags: work-life
categories: [Miscellaneous]
title: '#SNMP Design: Static Methods'
---
There are many static methods available now in Manager and Agent classes, but actually they have no relationship with either Manager or Agent. Therefore, I think it is better to move them into an isolated helper class. That's why Messenger class was added lately. It's also a good time to implement shared Socket object in this single entry for static methods.

What's your opinions about static methods? I believe a fully object oriented design should avoid them, but I couldn't help give them birth.

Next step I am going to separate default object registry from other object registries.
<!--more-->