---
layout: post
title: "HardQuery Report: Latest Bugs Are Fixed"
description: This post reports the latest bugs fixed.
tags: Code-Beautifier-Collection Delphi
permalink: /hardquery-report-latest-bugs-are-fixed-38dbbf43179c
excerpt_separator: <!--more-->
---
(CSDN Nov 12, 2006)

Yes, two bugs were found just yesterday. I fixed them immediately. However, today GForge is down, so I can not upload the update on it. The package on BDN Code Central is updated right now.
<!--more-->

One bug is that when you open a file without a project opened, a warning box prevents you from doing anything including closing BDS. As a result, you have to kill the process instead.

The other is that when you just install CBC, and open the C/C++/C# tab in the Preferences Dialog, you get an exception, and the global exception handler is triggered and brings you a dialog. You should click the Continue button or BDS will be closed.

I am sorry for the inconvenience.

The version number for this update is 5.3.1.1001, and it is the first RC of HardQuery Release 2 Update 1.

If you notice this time the LeXDK reference is in the VS2005 style. Yes, it is done by Sandcastle. I will soon publish an article about it.

Stay tuned.
