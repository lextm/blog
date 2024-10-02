---
layout: post
title: "#SNMP Design: Time for Parser Details, Part Two"
description: "This post is the second part of the parser details."
tags: SNMP
permalink: /snmp-design-time-for-parser-details-part-two-f722930f5c8e
excerpt_separator: <!--more-->
---
## Why TDD really helps?

You can see that a lot of new NUnit test cases added. I created one test case for every MIB document I was going to parse. In this way I could estimate my progress.

Do you know how this estimate keeps me on always? Whenever one more red node turns green, I know I am one step closer to the goal. Try this approach yourself and I believe you fall in love with it soon.

In #SNMP MIB case, TDD works perfect. The first few MIB documents take me about ten days, while the rest only take one.

SharpDevelop's wonderful integration with NUnit makes it possible to debug into test cases. And this feature significantly saves my time on debugging. Even though SharpDevelop's debugger is not as powerful as Visual Studio and NUnit for #D is not as beautiful as ReSharper's NUnit session panel, this free C# IDE does provide what a C# developer requires. Thank you, #D guys. Thank you all for this TDD IDE.

BTW, since I started to use TortoiseSVN to access CodePlex.com, I found that SharpDevelop's SVN support really neat and useful.
<!--more-->