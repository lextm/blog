---
layout: post
title: "TritonMate Words: #SNMP 9.0 Plan"
description: "This post is to announce the plan of #SNMP Library 9.0."
tags: SNMP
excerpt_separator: <!--more-->
---
#SNMP Library 8.5 has been published for a while (Feb 22, 2015).

If you did not yet try it out, it can be easily acquired from NuGet. The focus was primarily set on repackaging, so most of the APIs are not touched. However, you should notice that both .NET 3.5 and Compact Framework are now no longer in supported platform list. .NET 4.0 + KB2468871 becomes the new minimal.
<!--more-->

Microsoft is going to retire .NET 4.0 soon (Jan 2016), so #SNMP Library will follow in its next release, aka LordGate (9.0).

At that time, .NET 4.5 will be the minimal. One key change will be support for async/await. An example is

``` csharp
Socket socket = new Socket(AddressFamily.InterNetwork, SocketType.Dgram, ProtocolType.Udp);
GetRequestMessage message = new GetRequestMessage(0x4bed, VersionCode.V2, new OctetString("public"), new List<Variable> { new Variable(new ObjectIdentifier("1.3.6.1.2.1.1.1.0")) });

var users1 = new UserRegistry();
var response = await message.GetResponseAsync(new IPEndPoint(IPAddress.Loopback, 16100), users1, socket);
```

Yep, BeginGetResponse/EndGetResponse will no longer be needed.

Other changes planned are,

* Change security cache mode from FIFO to LRU.
* Add SNMP session support.
* (Possibly) .NET Core and Universal App support.

More details will be posted in future posts under "LordGate Notes" series. Stay tuned.
