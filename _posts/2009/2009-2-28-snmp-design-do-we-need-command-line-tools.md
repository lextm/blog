---
layout: post
title: "#SNMP Design: Do We Need Command Line Tools?"
description: "This post is about the command line tools in #SNMP."
tags: SNMP
permalink: /snmp-design-do-we-need-command-line-tools-2fbf1c72e82
excerpt_separator: <!--more-->
---
It is sad that Net-SNMP only has command line tools, but they are really powerful and easy to use. Do we need similar tools in #SNMP Suite? Why not? But how?
<!--more-->

I really hate to write command line tools because it is always hard to parse the arguments. However, Miguel (Mono lead) posted something wonderful here which attracted my attention. It is a discussion about command line parser so I soon decided to give Mono.Options a try.

And it works perfect! So I have just checked in the latest TestGet sample, who works similar to Net-SNMP snmpget. However, the command line syntax is slightly different.

For example,
Net-SNMP: snmpget -c public -V v2c 127.0.0.1 1.3.6.1.2.1.1.1.0
#SNMP : snmpget -c=public -V=v2 127.0.0.1 1.3.6.1.2.1.1.1.0

Well, in fact #SNMP accepts more types of command line input because of Mono.Options, so please play with it and leave me your comments.

Next step I am going to update other samples. Stay tuned.
