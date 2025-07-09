---
layout: post
title: "#SNMP Pro: A Sneak on Upcoming Compiler Pro"
description: "In this blog post I am going to demonstrate how the Pro edition of #SNMP MIB Compiler is different from the open source edition."
tags: SNMP
permalink: /snmp-pro-a-sneak-on-upcoming-compiler-pro-4a188285867b
excerpt_separator: <!--more-->
---
In this blog post I am going to demonstrate how the Pro edition of #SNMP MIB Compiler is different from the open source edition.
<!--more-->

## Brand New Look and New Menu Items
Besides, the theme has been changed from Visual Studio 2005 to Visual Studio 2012 Light theme. Of course this is powered by DockPanel Suite 3.0 (currently in alpha).

By cloning Visual Studio look and feel, you can see from the screen shots that more menu items are added (and also more icons on the tool bar). The new ones provide the following functionality,

* Close current solution (which contains the MIB documents you are working on).
* Abandon compilation result (which clears the contents in Module List panel and allow you to recompile all documents in solution).

They might not sound fancy, but once you start to write your own MIB documents, and edit others' work, you will find them very useful to keep the workflow smooth. As without them you will have to restart the whole compiler often.

The MIB documents can now be edited directly in the compiler. With syntax highlighting and the improved compiler back end, the Output panel always generates accurate errors/warnings.

By double-clicking on an error or warning, you will be redirected to the problematic file, and more friendly at the correct line and column.

## Rich Metadata Extraction and Accurate Error Reporting
Starting from 2008, the #SNMP MIB Compiler is capable of extracting OIDs from MIB documents. This serves #SNMP users well, as they can easily translate OIDs to names and vice verse. This might meet 80%-90% daily needs as most SNMP users won't touch the metadata on an object or a type.

However, if your work is to develop a commercial SNMP agent or manager, you need the following features seriously,

* Type information extraction so that for every objects we know their basic types (Counter32, OCTET STRING, and so on), and also know about the intermediate types (such as DisplayString). As constraints can be added at each level, those constraints should be extracted too, so as to build data validation. [in progress]
* Cross module dependency resolution, type resolution, and entity validation. They can provide more accurate error reports and help fix broken MIB documents. [in progress]
* MIB to C# compilation, which is similar to Net-SNMP's mib2c utility (who compiles MIB documents to C code). The output C# source files can be used to turn snmpd sample to a simulator for those MIB documents. [Not yet implemented]
* Alternative compiler input and output. You might need SMIv1/v2, plus SMIng as input, while YAML, XML, database file and others as output. [Not yet implemented]
* Wizards to generate MIB document building blocks. [Not yet implemented]
* Better integration with the #SNMP MIB Browser. [Not yet implemented]

If you like to join the beta test program (which might start in May), please write to support@lextudio.com.

Stay tuned.
