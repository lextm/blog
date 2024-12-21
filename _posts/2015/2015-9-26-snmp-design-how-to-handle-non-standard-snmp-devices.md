---
layout: post
title: "#SNMP Design: How to Handle Non Standard SNMP Devices"
description: "This post is about how to handle non standard SNMP devices with #SNMP Library."
tags: SNMP
permalink: /snmp-design-how-to-handle-non-standard-snmp-devices-ec75872ae9d
excerpt_separator: <!--more-->
---
It is quite happy to go over old posts I made in the past few years regarding #SNMP. Many topics are so generic that they also apply to other SNMP products. But one surprising fact is that I rarely discussed about those devices that fail to be standard compliant. Though rare in numbers, they still bite users/operators many times, and different product/library vendors take different approaches to handle them. It would be quite useful if I can write down some technical details for future readers. Thus, this post is the one for that purpose.
<!--more-->

Thanks for dear #SNMP users who reported the issues, and we have such a long list,

* UInt32 used in some device
* Zero length OBJECT IDENTIFIER generated in some device firmware
* Opaque/IP type encoding issue by some device
* Potential agent issue in a Samsung ML-4550 printer
* Unexpected encoding of Integer by some device
* Improper OBJECT IDENTIFIER encoding by a Canon iR C3580 printer
* Improper UInt32 type used by an H3C switch
* Improper TRAP v2 messages from some Cisco device
* Improper integer encoding

Of course it won't be a complete list as buggy firmware is everywhere. So let's drill down to see why such issues occurred based on my own assumption.

## Reason 1: Unsigned32 Type

The UInt32/Unsigned32 case was quite typical. IETF published different revisions (RFC 1442 and RFC 1902), in former Unsigned32 has its own data type code 0x47, but in the latter Unsigned32 shares the same data type code 0x42 with Gauge32.

Therefore, if a firmware was written against RFC 1442 and was never updated later to follow RFC 1902, then when it sends data to #SNMP based applications, exceptions will happen, as 0x47 is not handled at all.

We could not blame IETF in general, because any standard is a moving target until everyone is OK with its feature and nothing is going to be added. The RFC 1442 (in 1993) –> 1902 (in 1996) –> 2578 (in 1999) evolution is a good example to show how something cool at that time (SNMP v2) was being designed, proposed, and finalized. The technical difficulty to upgrade firmware in devices at that time also made many devices stuck in a state that's not standard compliant.

## Reason 2: Default Value of OBJECT IDENTIFIER

You might notice that in at least two cases the devices want to encode an OBJECT IDENTIFIER with zero byte. Developers might assume that this should be the default value to use.

However, if they carefully read the RFC documents (RFC 1902 and above), there is at least two ways,

1. Use zeroDotZero in SMI v2.
1. Use Null type in SMI v1.

## Reason 3: Encoding Algorithm Bugs

RFC documents have indicates clearly how BER should be used to generate bytes from data types in an optimized way (least bytes whenever possible). But some devices just fail to conform to this rule. They either generates extra bytes unnecessarily, or stick to an algorithm that generates fixed length byte arrays. It would be OK for SNMP libraries to decode the data, but really a waste of bandwidth.

## Reason 4: Opaque/BIT STRING Types

Opaque was a type to store raw bytes, and BIT STRING type (default in ASN.1, and allowed in RFC 1442, and forbidden in later revisions) was to store named bits. Whatever they were designed for, for now we should use OCTET STRING type instead.

## Troubleshooting Tips

Nonstandard devices can lead to various kind of issues, but would be difficult to troubleshoot without capturing network packets.

In all cases we should go down to byte level, and use tools such as Wireshark, and BytesViewer sample to analyze the raw bytes.

By finding out which part of the standards is violated, a workaround might be found.