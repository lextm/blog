---
layout: post
title: "TritonMate Words: Compiler Update So Far"
description: "This post is about the status of the new compiler for #SNMP."
tags: SNMP
permalink: /tritonmate-words-compiler-update-so-far-d5050e21d4e6
excerpt_separator: <!--more-->
---
Here comes some good news on the ANTLR based compiler,

* The port from ANTLR v2 to v3 is complete, and now we have the first open source SMI grammar file for ANTLR 3, http://code.google.com/p/sharpsnmplib/source/browse/SharpSnmpLib/Mib/Smi.g (smi_no_action.g is the Java version without actions).
* I contacted Nigel Sheridan-Smith, and he confirmed that his previous work is open source under BSD license, and he also accepts LGPL.
* My modifications of this grammar then is also released under BSD license and LGPL.
* As we cannot contact Vivek Gupta (no contact method can be found), we can only assume he published the original ASN.1 grammar in public domain (since he published it on ANTLR sample section, where most grammars are either under BSD or in public domain).

Then we can see what are the features implemented right now in this new compiler,

* MSBuild compliant error and warning messages.
* More accurate parsing on macros and other complex SMI entities.
* Automatic ANTLR grammar to C# code generation at compile time.

Now the challenge is how to keep improving it and make it a better tool for MIB authors. Of course, the code base is still messy, and I am going to do more cleanup in the coming weeks.

Happy Chinese New Year :)
<!--more-->