---
layout: post
title: "CBC TechNote: Why I choose JCF and AStyle"
description: A post about why I chose JCF and AStyle as code beautifiers for CBC.
tags: Code-Beautifier-Collection Delphi
permalink: /cbc-technote-why-i-choose-jcf-and-astyle-b4cf28311f72
excerpt_separator: <!--more-->
---
(Originally published to CSDN on Nov 03, 2005)

First thing I want to commit is that I knew little about source file parsing, so I gave up this idea in the beginning. David did the same. He used AStyle in his SBT. And I followed his approach. How I advanced a little was that I used JCF, too.

There are a lot beautifiers all over the world if you use a search engine to search, both open-source/freeware or commercial products.
<!--more-->

For Delphi source files, an IDE plug-in named Delphi Formatter Expert is quite famous in "Chinese Delphi Community". However, it is free but no source available. Since Delphi 8 for .NET was released, this expert have been out-of-date. But in China, a lot guys are still on Delphi 5/6/7, so they don't bother.

For me, a guy full of adventurous ideas, Delphi 7 was too old. So, I tried my best to modify DelForExp but failed. Then I found JEDI Code Format hosted by Anthony.

Luckily, JCF provides me a command line tool named `jcf.exe` which run very similarly to AStyle. JCF is under Mozilla license, while AStyle is under GPL, so both are free and open-source.

AStyle is so powerful that it formats Java/C/C++/C# files. Also, it implements useful build-in styles. So I make no second choice (a BCB plug-in, SourceFormat, utilizes another C++ beautifier, but I never try it).

Compared to AStyle, JCF lacks of build-in styles, but it provides an alternative mechanism. You can use a cfg file to store your style, and call it whenever formatting. I would employ this feature to provide CBC users with some more styles (but this styles will be built-in CBC then) in future versions.

If you know much about some better beautifiers, please contact me and let me know. Then maybe I choose another.
