---
layout: post
title: "CrossRoad Billboard: How to Support IP v6 in .NET/C#"
description: "This post is about how to support IP v6 in .NET/C# by using the new API in .NET Framework."
tags: SNMP .NET
permalink: /crossroad-billboard-how-to-support-ip-v6-in-net-c-d579939ce0f0
excerpt_separator: <!--more-->
---
In the past, I thought I needn't do anything to support IP v6. Well, at that moment I knew little of IP v6.

Last month I finally had a chance to study IP v6 with Windows Vista and Server 2008. From then on, I know that as a new protocol, it is not a small jump from the IP v4 boat to the IP v6 one.
<!--more-->

Last weekend I started to implement the notification panel of browser. After finding a way to list all IP addresses that I am interested, I knew it is time to add IP v6 support as there is an IP v6 address listed. But how? Interesting that this time I was driven by exceptions and Google.

Do you know the following exception messages?

* "The system detected an invalid pointer address in attempting to use a pointer argument in a call"
* "An address incompatible with the requested protocol was used"

Well, Google reveals that they are the hints that you need to search for all `Socket`/`UdpClient`` objects used and let them aware of IP v6 existence.

My changes are,

1. Specify `AddressFamily` parameter when creating a `Socket` object. From then on, this `Socket` object will only be used for IP v4 or v6.
1. Every time an `IPAddress` object is used, check its `AddressFamily` so that a proper `Socket` object can be used.

The toughest problem is how to monitor incoming packets for "All Unassigned". Ha, you must wonder why monitoring `IPAddress.Any` is not enough. OK, here is the answer.

`IPAddress.Any` is for IP v4 only. `IPAddress.IPv6Any` must be used besides to monitor IP v6 packets. So finally I have to use two `Socket` objects in this panel. One is used for IP v4, and the other for IP v6.

It is perfect that I have this notification panel completed and in the meantime IP v6 support is accomplished. .NET platform really makes the progress quite smooth.
