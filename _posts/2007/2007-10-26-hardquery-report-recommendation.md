---
layout: post
title: "HardQuery Report: Recommendation"
description: This post talks about the future of HardQuery.
tags: Code-Beautifier-Collection Delphi
permalink: /hardquery-report-recommendation-8148575027cf
excerpt_separator: <!--more-->
---
Dear users, although I am trying to release a new update for HardQuery series (5.3.4.1001 is the first Release Candidate), there is something I won't fix in this update (or later updates).
<!--more-->

## No Vista support in HardQuery

I have to say I made a lot of changes in order to make GrapeVine Vista compatible. And according to my analysis, porting those changes back to HardQuery will take a rather long time (several months). Because CodeGear starts to ship its latest and most stable IDEs in 2007 and surely will continue in 2008, I believe migrating to its RAD Studio 2007 and later Tiburon should be a better way than continuing using Delphi 2006 or lower.

If you want to use Delphi 2006 or lower, please install them on Windows 2000 or XP. In fact, those old IDEs do not support Vista officially.

## No CodeGear RAD Studio 2007 support

RAD Studio 2007 is partially built on .NET 2.0 so HardQuery which is compiled against 1.1 cannot consume the new feature of this framework. So GrapeVine should be used in order to achieve better performance and compatibility.

## Conclusion

If you want to upgrade your IDE, please take a look at GrapeVine at [CBC Homepage](http://code.google.com/p/lextudio). If you prefer to use Delphi 2006 and lower, don't install HardQuery on Vista.
