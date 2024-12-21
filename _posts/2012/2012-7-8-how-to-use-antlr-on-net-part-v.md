---
layout: post
title: "How to Use ANTLR on .NET, Part V"
description: "This post is about how to use ANTLR on .NET."
tags: .NET ANTLR
permalink: /how-to-use-antlr-on-net-part-v-93a94e02d789
excerpt_separator: <!--more-->
---
Debugging
<!--more-->

I already shared an important tip with you in part IV, so that if you find a portion cannot be parsed properly you should use the Java grammar in ANTLRWorks to debug. This can help locate grammar bugs and allow you to fix them quickly.

However, sometimes you do need to debug SmiLexer and SmiParser classes in Visual Studio (or another IDE). Since we use ANTLR MSBuild targets to convert the grammar file at compile time, you might find it not easy to set break points. In that case, you can simply open obj/Debug/SmiLexer.cs or SmiParser.cs (for Debug build) and set break points in the file and debug as usual.

The ANTLR code generator does a good job of leaving hints in the source code to aid you. The following method is an example,

{% gist 3198483 %}

where you can find the comments show which portion of the grammar was translated to which part of the code. You can almost debug the code without reading the grammar file.

> This is a short post compared to previous ones, simply because at this moment I could not yet think of other useful tips. Might update it periodically in the future. Stay tuned.
