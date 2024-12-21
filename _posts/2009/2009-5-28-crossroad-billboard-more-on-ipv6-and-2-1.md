---
layout: post
title: "CrossRoad Billboard: More on IP v6 and 2.1"
description: "This post is about a bug in the latest CrossRoad release."
tags: Code-Beautifier-Collection Delphi
permalink: /crossroad-billboard-more-on-ip-v6-and-2-1-3b924cecacef
excerpt_separator: <!--more-->
---
Here is the technical details about work item 4016 and release 2.1.
<!--more-->

## Background

I bought my laptop in 2007, which ships with Windows Vista Home Basic, so from then on I have worked on IP v6 enabled platforms (Windows Vista and Windows 7).

Before the release of 2.0 final, when I tried to make the library IP v6 compatible, I had a lot of tests executed on Windows 7. So I didn't realize that such tests are not enough.

Yes, I did learn a few key points about Windows XP and Windows Server 2003 in March. But I simply neglected them that day and left the bug there. (Next time surely I will do some tests on Windows XP.


## Report

BACON report this bug on April 29th (three days after the release day), which soon drew my attention.

This is one of the best bug reports I ever saw, in which not only the problem description was comprehensive, but the solution was presented as well. Soon we closed the work item (on May 1).

I must thank BACON again as he/she did a great job.

## Extra

The report was about the library, but in fact there was another relevant issue in the browser.

When I designed the notification panel, it also made use of IP v6 so that all TRAP and INFORM messages can be correctly handled. If we only fixed the library, the browser would still fail to work.

The good news is that both issues are addressed, and 2.1 contains both patches.

## Side Notes

First, what if your application only targets Windows 6.0 (Vista and Server 2008) and the upcoming Windows 7 (Windows Server 2008 R2 as well)? Do you need to upgrade? I think you can continue using release 2.0.

Second, as I removed most obsolete items in 2.1 release, please compile your code against 2.0 and follow the migration suggestions. After those changes, you can move on to compile against 2.1.

If you meet any problem with 2.0/2.1, feel free to let me know via this blog or the discussion board.
