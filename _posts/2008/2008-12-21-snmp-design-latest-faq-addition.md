---
layout: post
title: "#SNMP Design: Latest FAQ Addition"
description: "This post is about the latest FAQ addition."
tags: SNMP
permalink: /snmp-design-latest-faq-addition-af988ee9a64e
excerpt_separator: <!--more-->
---
## 1. Why when I compile the source code an error is displayed about AssemblyInfo task?
Answer: Please open readme.txt in the source code package to see what is missing on your computer.

## 2. Which language does this library support?
Answer: Technically speaking, all .NET languages are supported, such as C#, VB.NET, Delphi Prism , C++/CLI, IronPython, IronRuby, and so on.

## 3. Is this library thread safe?
Answer: Not yet. Please use static methods in Manager or Agent component which should be thread safe.

## 4. How to diagnose problems?
Answer: A general approach is like this,

* Does this problem reproducible?
* Do other libraries behave the same? Please test with Net-SNMP which is also open source.
* Does the latest build in the repository work?
* Is this a known issue ?
* Prepare extra information (a Wireshark or Network Monitor log for network traffic, stack trace for exceptions, MIB file for parser errors). Then open a bug report here with the log file attached.

## 5. Why some methods are marked as Obsolete?

Answer: After 1.5 release, #SNMP Library API will be changed a little bit. Therefore, some methods are obsolete from now on. Please avoid using them from now on.
<!--more-->