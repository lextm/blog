---
layout: post
title: "Analysis on a #SNMP Library Memory Leak Report with JetBrains dotMemory"
description: "This post is about how I analyzed a memory leak report on a #SNMP Library with JetBrains dotMemory."
tags: .NET Visual-Studio
permalink: /analysis-on-a-snmp-library-memory-leak-report-with-jetbrains-dotmemory-9199f8a98955
excerpt_separator: <!--more-->
---
A few days ago, I got a report on possible #SNMP memory leak. The report itself contains very useful information, so that I was confident on reproducing it.
<!--more-->

Today, I [added two test cases](https://github.com/lextudio/sharpsnmplib/commit/914a74ab6041d5b8198b60325ddf4da9c0853c88) in the code base, and then use JetBrains dotMemory Unit to execute it following [this guide](https://www.jetbrains.com/dotmemory/unit/help/Comparing_Snapshots0.html).

JetBrains has made the steps very intuitive, so that I can compare the two snapshots easily to see which new objects were created when 100 requests were sent and ended with exceptions.

However, all new objects come from either JetBrains unit test executor, NUnit, or dotMemory Unit framework, and none comes from #SNMP Library.

I think I will play with dotMemory more in the future, as it turns out to be a very useful piece of software with unit testing integration.
