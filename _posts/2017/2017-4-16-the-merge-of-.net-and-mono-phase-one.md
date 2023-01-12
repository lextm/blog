---
layout: post
title: "The Merge of .NET and Mono: Phase One"
description: "This post is about the first phase of the merge of .NET and Mono."
tags: .NET Mono
permalink: /the-merge-of-net-and-mono-phase-one-c157e68ce371
excerpt_separator: <!--more-->
---

> I was about to write a phase two post, but suddenly realized that I did not even have a phase one post. Thus, this is it.

When we look back at [the history of .NET and Mono](https://corefx.lextudio.com), we can see the first collaboration was around Silverlight/Moonlight (2008–2009). Microsoft only provides testing suites to Novell (who owned Mono at that time), so we could not say that gives Mono a chance to "merge" with .NET Framework. But at least, Moonlight has better compatibility to Silverlight, compared to Mono and .NET Framework.
<!--more-->

Microsoft started to open source its technology in 2008–2009 as well (MEF/EntLib/ASP.NET MVC), and Mono shipped such immediately when they became available. It was rather painful still, because Mono core runtime was not fully compatible to .NET Framework core runtime, and Mono had to ship forked versions. Microsoft teams who maintain such libraries could not help too much, as they were not that familiar with Mono and Linux in general.

.NET Framework source code was partially published by Microsoft on October 3, 2007. However, Mono guys could not even read the code, because it was made publicly under a quite restricted license, which does not fall under Open Source Definition.

Till November 12, 2014, Microsoft finally declared its open source plan for .NET Framework and .NET Core. Mono decided then to incorporate Microsoft .NET Framework source code (BCL) to replace Mono's cloned classes. From Mono 4.0 on, we have seen more and more classes adopted, and better and better compatibility.

What might happen in the next phase? We shall see soon.
