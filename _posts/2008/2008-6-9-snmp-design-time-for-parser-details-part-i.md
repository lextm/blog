---
layout: post
title: "#SNMP Design: Time for Parser Details, Part One"
description: "This post talks about the #SNMP compiler details."
tags: SNMP
permalink: /snmp-design-time-for-parser-details-part-one-4a46ff24093a
excerpt_separator: <!--more-->
---
This morning I changed to version number of #SNMP to 0.9 after checking in latest update on MIB support. Compared to my plan, there is nothing big to add before NineHeaded release.

So what would be contained in these posts? I'd like to share some implementation details interesting with you.
<!--more-->

## Why it is an experimental parser and what it can do?

This must be answered at first to clear the clouds. I am working on a MIB parser because right now there is no need to dig as deep as possible. You can look at ObjectTree.cs and see that only a few entities inside the MIB module are used to construct the tree. Therefore, in the first stage of the parser, I am only curious about how to parse out those entities.

And that's why you can see lots of empty classes such as Macro and TextualConvention. They are not critical entities I need at this moment.

Compared to a commercial MIB compiler, this parser is still a toy. It cannot tell all bugs in the MIB documents, and it cannot tell you all information containing inside. But I believe I could make a compiler later if I can spend more time on MIB language.
