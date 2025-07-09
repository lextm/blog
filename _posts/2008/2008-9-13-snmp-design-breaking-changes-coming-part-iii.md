---
layout: post
title: "#SNMP Design: Breaking Changes Coming, Part III"
description: "This post talks about the breaking changes in #SNMP Library."
tags: SNMP
permalink: /snmp-design-breaking-changes-coming-part-iii
excerpt_separator: <!--more-->
---
> (This post is updated on September 27th heavily.)

If you notice, both SNMP data type `OCTET STRING` and `Opaque` can be viewed as byte array type in .NET. Maybe you wonder why `OCTET STRING` is not viewed as `System.String`, the reason is simple. `System.String` does have one more property than a byte array, `Encoding`. It seems when SNMP was designed, it does not provide a default encoding for `OCTET STRING` explicitly (and sometimes it is even used just like a byte array when you store MAC address bytes in it).
<!--more-->

Therefore, a problem has been there for a long time. Which encoding should be used there if an `OctetString` instance comes. In the old Change Sets, the answer is ASCII and there is no way in them to change it to Unicode or others.

It is in the latest few builds, I start to provide a way so that you can explicitly state which encoding you prefer.

As a reference at first, there are new methods and properties in `OctetString` class you should pay attention to,

1. `public OctetString(string str, Encoding encoding)`. You may provide a specific `Encoding` so that the internal bytes are what you expect.
1. `public string ToString(Encoding encoding)`. According to `Encoding` provided, the internal bytes are decoded to a correct string.
1. `public Encoding Encoding`. This is a read only property that illustrates what encoding is assigned to this `OctetString` instance.
1. `public static Encoding DefaultEncoding`. This is a property to define default encoding used for all `OctetString` instance if no encoding is assigned via the constructor described in item 1. The default value of this property is `Encoding.ASCII`.
1. `public OctetString(string str)`. `OctetString.DefaultEncoding` is used to generate internal bytes from `str`.
1. `public string ToString()`. `OctetString.Encoding` is used to generate a string from internal bytes.

Now let's review a few common scenarios and discuss what you may do to customize `OctetString`'s behaviors.

## Default ASCII Way
If you don't touch the properties and methods related to `Encoding`, then you are in a pure ASCII way. It should behave the same as old releases of #SNMP (0.5, 1.0 and 1.1).

## Default Encoding.* Way
If you change `DefaultEncoding` to any other `Encoding` types, and don't touch the properties and methods related to `Encoding` later, you are in a pure `Encoding.*` way.

## Basic Hybrid Way
If some of your devices require ASCII while others require Unicode (aka UTF-16), then you may find it a little bit difficult. My suggestions are,

Whenever you need to construct an `OctetString` object, specify its encoding explicitly. Whenever you need to use an `OctetString` object, check its `Encoding` before calling `ToString()`. If the `Encoding` is not correct, call `ToString(Encoding)` explicitly.

## Last Word
I understand the current implementation is not perfect yet. When #SNMP parses incoming packets, it always use `DefaultEncoding` to construct `OctetString` objects from raw bytes. This is not optimal for hybrid cases. Hope a better way can be found soon.

No matter what, please report any critical issues or your suggestions in this field.
