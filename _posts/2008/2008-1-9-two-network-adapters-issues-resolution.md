---
layout: post
title: "Two Network Adapters Issues Resolution"
description: This post is about how to resolve issues when you have two network adapters installed.
tags: SNMP Windows
permalink: /two-network-adapters-issues-resolution-7d9e80034b59
excerpt_separator: <!--more-->
---
If you have two network adapters (NICs) installed, there should be a few issues. At this moment, I have two installed. One of them connects me to the corporate intranet and the other connects to an internal router connected to a few SNMP enabled devices.
<!--more-->

Because both adapters requires DHCP enabled, I can only access to intranet or the internal router one at a time. This limitation cannot be removed, because there should be only one default gateway.

My virtual machine based development environment makes it even worse.

* I have my virtual disk on the storage server in the corporate intranet, so my host machine must be able to access the intranet (otherwise Virtual PC fails to load the virtual disk).
* When I debug my applications inside the Virtual PC, the applications must be able to access the devices behind the internal router.

The only possible approach is to configure the host to use intranet gateway IP by default, and the guest to use the router IP as gateway.

How to achieve this? Modify your Windows routing table manually!

``` text
route -f
route -p ADD 0.0.0.0 MASK 0.0.0.0
```

I wrote two batch files on the guest with different gateway IPs, so I can switch between them. the effect is that sometimes I only access the intranet from the guest while sometimes the internal network. On the host you can do similar batch files if necessary.

One more thing you should notice is that you might need to manually set the DNS server IP somewhere if errors occur. Good luck.
