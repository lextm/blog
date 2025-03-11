---
layout: post
title: "#SNMP Design: Build My Own Lexer"
description: This post talks about how I build my own lexer.
tags: SNMP
permalink: /snmp-design-build-my-own-lexer-c45cd940e87a
excerpt_separator: <!--more-->
---
Suddenly I found that MIB support is much harder than other parts. Why? You cannot imagine parsing binary data looks so easy right now.

According to Essential SNMP, MIB files are ASN.1 format text files. In order to parse them, a lexer and a parser is necessary. Though I have built code to parse BER packets (GET, SET, GET NEXT, and TRAP), I had no idea how to parse text.
<!--more-->

Malcolm has created a parser and lexer, but the code is for general purpose, and not commented well, so I think I cannot understand the algorithm so that I cannot fix bugs if some come. Therefore, the future is clear.

Have to say I am now really a programmer, so I know exactly what I should implement. This morning, finally I got SNMPv2-SMI parsed without an error. Wow, I made it.

Now I am going to research further into other MIB files in order to make sure I can set up a MIB object tree required by #SNMP 1.0 release.

I believe I could implement something as powerful as MIB browser and compiler once I get this lexer and parser done completed. So stay tuned.
