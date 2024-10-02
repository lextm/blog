---
layout: post
title: "#SNMP Design: Under The Surface"
description: "This post talks about the low level functions exposed by those message classes."
tags: SNMP
permalink: /snmp-design-under-the-surface-7374b30a15e8
excerpt_separator: <!--more-->
---
How to use #SNMP Library in your applications? I suggest you drag a Manager component into your WinForms or WebForms. This Manager instance allows you to configure default SNMP protocol version to be used and the global timeout count in milliseconds. Then wherever you need to do SNMP operations, simply call Get, Set, or GetTable with appropriate parameters. But what's more? Is it possible to manipulate PDU level data? Is it possible to play with bytes?

The general answer is, no surprise, YES. I provides several ISnmpMessage derivatives to serve you. Take GetRequestMessage as an example. You can create an instance from raw bytes you received from the peer and get access to parsed properties (such as variable bindings) easily. Or you can create an instance from known properties, and send out raw bytes from ToBytes.

In my opinions, starters can easily accomplish basic works with the Manager. And hope advanced users enjoy the low level functions exposed by those message classes.
<!--more-->