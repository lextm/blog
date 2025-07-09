---
layout: post
title: "#SNMP Design: Time for Parser Details, Part Five"
description: "This post talks about the exceptions the compiler may raise and what they mean."
tags: SNMP
permalink: /snmp-design-time-for-parser-details-part-five-39f92e7fdff6
excerpt_separator: <!--more-->
---
What exceptions I may get and what do they mean?

After avoiding using exceptions for years, I finally get addicted to it and find out how to put them under my control. So please refer to this post once you meet an exception while working with #SNMP.
<!--more-->

## ArgumentNullException

You meet this exception only if you mistakenly pass a null reference into one of #SNMP functions. The exception message and stake trace can help you locate the bug.

## ArgumentException

This exception is thrown by #SNMP functions if a wrong argument is found. For example, strings in wrong patterns, or arrays with wrong length. The exception message and stake trace can help you locate the bug.

## SharpMibException

The experimental parser throws exceptions of this kind whenever it cannot parse a symbol in the MIB document. This exception can tell you which symbol is wrong. File name, line number, and column number can help you find the issue.

However, because this parser is only tested again Net-SNMP bundled 70 MIB documents, so I know it may fail on other standard MIB documents. Please provide me reports once you meet this exception type on a standard MIB document. I'd like to analyse that document and improve the parser.

## OutOfMemoryException

Once you meet this exception, I am sure that it is caused by the parser. Please fire me reports like the above item so I can fix the bugs.

You may wonder why this kind of exception may be raised by a managed library. The reason is quite simple, sometimes the code enters a loop and cannot get out, so all resources are consumed by this loop and never get a chance to be released. I have been trying to fix such loops as many as possible but I am afraid that I haven't fixed them all.

Other #SNMP exceptions will be talked about in another post. Stay tuned.
