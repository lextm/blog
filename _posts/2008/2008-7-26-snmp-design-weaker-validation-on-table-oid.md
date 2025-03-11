---
layout: post
title: "#SNMP Design: Weaker Validation on Table OID"
description: "This post talks about the validation on table OID."
tags: SNMP
permalink: /snmp-design-weaker-validation-on-table-oid-b34c0c4d9e00
excerpt_separator: <!--more-->
---
Maybe I should not have designed Manager.GetTable that way, isn't it? The trouble I got is more. So how to change the original design at this moment? Take a look at source code of Change Set 14707, and you will see my decision.
<!--more-->

## The Old Design

Once upon a time (in this April), there was no validation in GetTable. But I added a basic case as soon as I noticed the necessity. This old validation required the OID passed to GetTable could be translated to textual form and ended with `Table`. It is such a natural rule that all tables defined in standard MIB documents follow it.

## The Problem It Brings

The old validation is too strong because not all OID can be validated like this. For example, if you try to access a table defined inside a private MIB document and probably #SNMP fails to parse this document, you are stuck! Sorry for the inconvenience.

After hearing of this critical bug, I admitted that I made a mistake when closing Issue and a solution must be presented as soon as possible.

## The New Implementation

I think a weaker validation is preferred before I fix all possible issues in the parser. Thus, a new rule is added to the validation,

* If the OID cannot be translated to textual form, it is assumed as a valid table OID (hi, this means you have to validate it yourself!).
* If the textual form is available, this validation falls back to the old design. Only if the names ended with `Table` are valid.

Hope you like this change. Stay tuned.
