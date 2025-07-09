---
layout: post
title: "#SNMP Design: Oh, Dear Compiler"
description: This post is about the latest progress of the MIB compiler.
tags: SNMP
permalink: /snmp-design-oh-dear-compiler-44369d113f58
excerpt_separator: <!--more-->
---
I cannot believe that a prototype of the proposed MIB compiler is now working on my computer. And during the process of developing it, I merely added a few new classes and methods, but no API change was made since Change Set. Nice, I think Steve is happy to hear this.
<!--more-->

All Net-SNMP MIB files was compiled to *.module files a few minutes ago, and now the 1000+ MIB documents are being processed. Although the compiling still takes a long time, I expect that the browser can load 1000+ *.module files in a few seconds. If later I can prove this, then I think I have already solved the performance issue and go beyond my original design of the browser and the library.

In the old design,

* Net-SNMP MIB documents are bundled in the library and parsed every time a ObjectRegistry is created.
* The browser accepts MIB documents directly, and parses them every time to form a tree.

If the compiler works as expected, then these changes can happen immediately,

* Only *.module files are needed by the library to create a basic tree.
* The browser can use *.module files by default, and compile MIB documents to *.module files whenever a new document is added.

Isn't that wonder? I am going to prepare a performance report of this compiler prototype soon. Also, I hope I can create a GUI for this command line compiler, too. Luckily if all these new stuffs do not break the existing interfaces the browser relies on, I can make sure they won't delay TwinTower.
