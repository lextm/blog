---
layout: post
title: "SquareRoot Puzzle: Digest #SNMP Samples, Part 1 Summary"
description: "This post is about #SNMP sample projects."
tags: SNMP
permalink: /squareroot-puzzle-digest-snmp-samples-part-1-summary-aa6e8a834f82
excerpt_separator: <!--more-->
---
Many samples are shipped in #SNMP Suite. But why they are that useful?
<!--more-->

## The Command Line Tools

The command line tools are small samples showing you only a few aspects of #SNMP Library. For example, snmpget tells how to send GET messages in all SNMP versions, and handle the response messages. snmpset, snmpbulkget, snmpgetnext and so on serves similarly.

Topics covered are,

1. How to send GET, SET, GET NEXT, GET BULK messages.
1. How to handle response messages.
1. What are the differences from SNMP v1/v2c and v3.
1. How to do WALK operation.
1. How to monitor incoming TRAP/INFORM messages.

## The Agent

If you know the daily work of a hardware engineer, you see how important a reference design is. If the vendor provides you a reference design about a chipset, you can simply modify a few parts and use the main part if your product. This saves you a lot of efforts.

#SNMP Agent is a .NET based reference design for you, and you can make your own SNMP agent out of it by adding the features you need.

You must notice that this reference design is interesting, as it uses a managed pipeline to handle SNMP messages. This is similar to what ASP.NET does for HTTP messages. I want you to feel like home.

Topics covered are,

1. How to monitor incoming messages.
1. How to do authentication.
1. How to do handler mapping.
1. How to query objects.
1. How to log operations.

## The Compiler

The Compiler sample mainly shows you how to compile MIB documents (*.mib or *.txt) to module files (*.module) that the Browser expects.

It rises when I started to test out hundreds of MIB documents. Though not feature complete yet, it provides basic things such as error reporting.

Topics covered are,

1. How to compile MIB documents.
1. How to report errors.

## The Browser

At the very beginning, the Browser contains the Compiler. But after a while we split them, so now it only loads module files (*.module) and provides functions such as MIB tree navigation, trap monitor, basic SNMP operations.

Topics covered are,

1. How to load module files.
1. How to build the MIB tree.
1. How to listen to traps.
1. How to do basic operations.
