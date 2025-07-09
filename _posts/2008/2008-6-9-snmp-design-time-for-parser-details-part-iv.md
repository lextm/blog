---
layout: post
title: "#SNMP Design: Time for Parser Details, Part Four"
description: "This post talks about the OID/IID textual form."
tags: SNMP
permalink: /snmp-design-time-for-parser-details-part-four-f856d990342a
excerpt_separator: <!--more-->
---
## What's the numerical and textual form of OID and IID?
Let's start with an example. When you try to know name of an SNMP enabled device, which of three references you think you prefer to use?
<!--more-->

* A: 1.3.6.1.2.1.1.1.0
* B: iso.org.dod.internet.mgmt.mib-2.system.sysDescr.0
* C: SNMPv2-MIB::sysDescr.0

Even though in SNMP all three references refer to the same object, in a glance you may feel that C is the best choice.
Why? I can provide the following reasons and hope you agree with me,

I believe only machine can understand option A well (and it must be trained well to memorize the meaning of every digit).
Option B is understandable. However, it provides too much information that nothing except the last two words is useful.
I am really sorry that because of my limited skill set, I forced every users of #SNMP to use option A during the 0.5 to 0.8 stages. Sorry. And from now on (0.9), you can use option C freely. At last, I am not going to provide option B because personally I hate that option and never use it in practice.
To summarize, option A exists as OID/IID numerical form in #SNMP, and option C exists as OID/IID textual form.
