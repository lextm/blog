---
layout: post
title: "#SNMP Pro: DateAndTime Syntax Support"
description: "This post talks about DateAndTime syntax support in #SNMP Pro."
tags: SNMP
permalink: /snmp-pro-dateandtime-syntax-support-e99abc51bc2f
excerpt_separator: <!--more-->
---

Well, I blogged about syntax validation [in a previous post]({% post_url 2013/2013-8-18-snmp-pro-syntax-validation-in-sharpsnmppro-mib %}), which should be one of the coolest features for SharpSnmpPro.Mib assembly. But there is an interesting story about that untold.

<!--more-->

## The Beginning of DateAndTime Support

In fact a very long time ago OctetString class has [a special implementation of ToString](https://github.com/lextudio/sharpsnmplib/blob/cec90df0e1f557a3de3beb6c5cbb6d0a16f9c27d/SharpSnmpLib/OctetString.cs). It was not written by me, but Malcolm. Malcolm tried to use it to convert an OctetString instance to DateAndTime value. However, that was not a good way as you never know if that instance should be interpreted in that format.

Anyway, that was the start. Later I moved that logic to a separate method called ToDateString, but it was not improved in the future releases.

## Five Years After

Now five years passed, and we have syntax validation ready. Is it a good time now to support DateAndTime completely? Yes, of course.

Assume we have such an entity defined in MIB document,

```text
testEntity5 OBJECT-TYPE
SYNTAX DateAndTime
MAX-ACCESS read-only
STATUS current
DESCRIPTION
"A textual description of the entity. This value should
include the full name and version identification of
the system's hardware type, software operating-system,
and networking software."
::= { test 5 }
```

We expect it can be properly understood by #SNMP Pro, so the following test case is prepared,

{% gist 6333534 %}

Yes, that passes now with SharpSnmpPro.Mib and we know DateAndTime support is finally finished.

## IDecoder Interface

Behind the scene, the raw data we passed in is handled by a new class called DataAndTimeDecoder, which is built into to SharpSnmpPro.Mib. Its source code is as below,

{% gist 6333563 %}

At runtime, a class called DecoderRegistry will hold all the decoders (which implements IDecoder). Whenever #SNMP Pro thinks it is a must to use a decoder, it goes to the registry and picks up the one that matches the syntax.

It is very easy to write your own decoder and replace the one built-in. You can simply use DecoderRegistry.Register your decoder. Make sure you set the correct key, which is the name of the syntax, such as SNMPv2-TC::DateAndTime.
