---
layout: post
title: "#SNMP Design: Experimental CF 3.5 Port"
description: "This post is about the experimental .NET Compact Framework 3.5 port of #SNMP Library."
tags: SNMP
permalink: /snmp-design-experimental-cf-3-5-port-69bd866592b2
excerpt_separator: <!--more-->
---
Because of this discussion thread, I think it is time to try .NET CF 3.5 a little bit. Luckily SharpDevelop 3 makes things easier when I don't have Visual Studio non-Express editions at hand. So let's see what I have done.
<!--more-->

First, it was easy to create an empty CF 3.5 project in SD3. Then I added all #SNMP Library source files into it. Well, compiling that project provides me a lot of errors and I have tried everything I can imagine to fix,

1. Cannot compile because an MSBuild targets file is missing. Installing .NET Compact Framework 3.5 and its Power Toys can help.
1. No BackgroundWorker component in CF. To fix it I have to use Mono version of this component.
1. UdpClient misses two important methods. To fix this, Mono source code is used again in UdpClientExtensions.cs.
1. Socket and UdpClient miss some properties. This time I have to use conditional defines to work around them.
1. A few elements are not available. Conditional defines must be used again.
1. Some classes are missing. So empty classes (mocks) are created to make sure the source code still compiles.

Therefore, if you want to use this CF port, you may install SD3, .NET Compact Framework 3.5 and its Power Toys at first and then open the CF solution file. At this moment, the only thing missing is how to open and compile this project in Visual Studio. But anyway now you can check out every bits from the repository and have a test. Please feel free to report any bug. :)
