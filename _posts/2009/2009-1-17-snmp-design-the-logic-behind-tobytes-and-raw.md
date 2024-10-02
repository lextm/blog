---
layout: post
title: "#SNMP Design: The Logic Behind ToBytes and _raw"
description: "This post is about the ideas behind the design of ToBytes and _raw."
tags: SNMP
permalink: /snmp-design-the-logic-behind-tobytes-and-raw-649293790e97
excerpt_separator: <!--more-->
---
Well you must notice this thread and my promise there. So in this post I am going to talk about the _raw fields and why they appear in every basic data types.
<!--more-->

OK, first do you know that every packets passed during SNMP communication is constructed by raw bytes? It is not hard to understand that because bytes are common entities every programming languages supports. So every objects of ISnmpData has a corresponding raw bytes representation.

Let's start with the simplest type, Null. What is its raw bytes part? {0x05, 0x00}. 05 is Null's type code defined in SNMP, while 00 means this data object has a length of 0. You may notice that Null class does not have a _raw field, as its length is always 0.

Now move on to another type, {0x04. 0x01, 0x61}. What's that? 04 stands for OCTET STRING, so it is an OctetString object, whose length is 1 and the data is `a` (ASCII value 0x61 or 97). But because OctetString may contain such strings or other data, so it has a _raw field.

The simplest conclusion includes the following key points,

1. _raw only contains data of this object. In order to generate an object's byte form, you must call ToBytes so type code and length information are added for you.
1. If you want to convert byte form to an object, DataFactory class must be used. Constructors that take `raw` only work on data, so never pass in the byte form.
1. If no direct conversion between two types is provided, you can simple grab one object's _raw bytes, and pass that to another type's constructor that takes `raw`.

Well, don't know if this time I make things clearer. I will soon document this topic in our specifications in a formal way. Stay tuned.
