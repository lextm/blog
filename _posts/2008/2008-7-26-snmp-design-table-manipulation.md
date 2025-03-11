---
layout: post
title: "#SNMP Design: Table Manipulation"
description: "This post talks about the table manipulation in #SNMP."
tags: SNMP
permalink: /snmp-design-table-manipulation-6f8353bc9ebc
excerpt_separator: <!--more-->
---
I believe the table manipulation is one of the hardest things in SNMP world. Therefore, I have tried my best to make it simple for #SNMP users.

Have you tried Manager.GetTable method? In most cases, a simple call to this method provides you the rows and columns. But I want you to pay attention to some points.
<!--more-->

## Table OID

The OID you pass to this method must be a valid OID for a table. If you pass in an entry OID or other, I cannot guarantee you get what you want.

## Sparse Table

Some SNMP agent does not fill in gaps inside tables. In such cases, #SNMP cannot generate a correct output matrix so the result is wrong. I am already aware of this bug but I do not have time to further investigate this issue at this moment.

## The Implementation

The current implementation of GetTable is based on GET NEXT operation. Thus, it is not the most efficient but I hope I can tune it later.

Stay tuned.
