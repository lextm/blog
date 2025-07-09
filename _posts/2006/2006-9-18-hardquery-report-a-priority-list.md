---
layout: post
title: "HardQuery Report: A Priority List"
description: "This post describes how different features are prioritized in HardQuery."
tags: Code-Beautifier-Collection Delphi
permalink: /hardquery-report-a-priority-list-3cc5649c8265
excerpt_separator: <!--more-->
---
(CSDN Sept 18, 2006)

I have just listened to delphi Hour recordings these days while programming HardQuery. Jacob Thurman mentioned a priority list about Castalia in #3. His list is sorted by language. 1st is delphi, C# 2nd, and C++ 3rd. It is the first time I know of this list, and then I start to make a similar list for CBC. My list is like this,
<!--more-->

Sorted by Language:

* C#,
* Delphi,
* C++,
* BASIC

I put C# on the top because CBC is mainly written in C#. There are two reasons:

1. I build this tool first to please myself because BDS lacks certain features implemented by Visual Studio. I need to read others' code (C#, delphi, C/C++, XML) so an enhanced code formatter for all these languages is quite useful. Remember, the formatter is the very first part of this tool in the beginning.
1. CBC before 5.0 was built on SBT architecture directly, and CBC version after 5.0 includes a lot of SBT features. That tool targets on C#Builder mainly. I try to add more delphi-targeting features, but it takes time.

I used C/C++ very often when I was an undergraduate. However, now I rarely use it. As a result, C/C++ is near the bottom. Since many features for C# can be easily adjusted for C/C++, so C/C++ is above BASIC.

BASIC support is very limited, because it is not fully supported by the IDE itself.
