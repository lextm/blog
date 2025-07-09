---
layout: post
title: "#SNMP Pro: Syntax Validation in SharpSnmpPro.Mib"
description: "This post talks about the syntax validation support in SharpSnmpPro.Mib assembly."
tags: SNMP
permalink: /snmp-pro-syntax-validation-in-sharpsnmppro-mib-aef7a40c9af4
excerpt_separator: <!--more-->
---
SMI defines the syntax of MIB documents. One of the most important part of SMI is the syntax that governs the value of an object. For example,

``` text
testEntity13 OBJECT-TYPE
SYNTAX INTEGER (30000000..31000000 | 13750000..14500000 | 5850000..6425000 | 7900000..8400000)
MAX-ACCESS read-only
STATUS current
DESCRIPTION
"A textual description of the entity. This value should
include the full name and version identification of
the system's hardware type, software operating-system,
and networking software."
::= { test 13 }
```

The above OBJECT-TYPE definition uses a syntax that requires an INTEGER value which falls into the four intervals defined.
<!--more-->

Many MIB compilers are able to compile such objects, extract their type (INTEGER) and OID (test.13), and interpret other properties. However, they are not able to extract the full syntax and make good use of it. So what about #SNMP MIB Compiler? Does it support full syntax validation?

As the foundation of #SNMP MIB Compiler, SharpSnmpPro.Mib assembly of course provides full validation support. For example, the below test case is part of our test suite, which shows how to load a MIB document into memory, and then use the information extract (including the full syntax) to validate input data,

{% gist 6255514 %}

Clearly when this test case passes we know the syntax validation works like a charm,

This is the very first post about SharpSnmpPro.Mib assembly. I am going to write more about it once the API set is further finalized.
