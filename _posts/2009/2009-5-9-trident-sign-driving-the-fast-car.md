---
layout: post
title: "Trident Sign: Driving the Fast Car"
description: "This post is about the progress of SNMP v3 support."
tags: SNMP
permalink: /trident-sign-driving-the-fast-car-1d9139a75689
excerpt_separator: <!--more-->
---
I am rushed to my feet to explore on SNMP v3. Actually this time with good materials such as Essential SNMP, Net-SNMP agent, and Snmp#Net, the progress is unexpectedly smooth.
<!--more-->

I plan to provide a detailed report once I finish the first revision of full SNMP v3 support. Now I just focus on snmpget command line tool and already finish noAuthNoPriv and authNoPriv modes. Tomorrow I will try to finish authPriv mode.

``` bash
snmpget -v=3 -l=noAuthNoPriv -u=lextm localhost 1.3.6.1.2.1.1.1.0
snmpget -v=3 -l=authNoPriv -u=lexli -a=MD5 -A=testpass localhost 1.3.6.1.2.1.1.1.0
snmpget -v=3 -l=authNoPriv -u=lextudio -a=sha -A=passtest localhost 1.3.6.1.2.1.1.1.0
```

Above are the test command lines I use to test snmpget against Net-SNMP agent, and you may notice that I choose a style similar to Net-SNMP snmpget.

I do not yet have a driver license, but I think now I have control of this v3 fast car. :)

Stay tuned.
