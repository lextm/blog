---
description: This article is about the upcoming update of CBC.
excerpt_separator: <!--more-->
layout: post
permalink: /hardquery-report-release-2-update-1-rc-2-is-ready-bf3d18b015db
tags: delphi code-beautifier-collection
categories: [Tools and Platforms]
title: 'HardQuery Report: Release 2 Update 1 RC 2 is ready'
---
(CSDN Nov 27, 2006)

First I wanna say sorry for those who have downloaded the half-cooked RC 2 published some time during the last week. There were something wrong so you might have seen a lot of trouble. And today the real RC 2 is available finally.
<!--more-->

The main addition is an easter egg. Since I built up CBC using Sharp Builder Tools' code and this egg was also created with Sharp Dev Tools, I think I owe David Hervieux so much. David The Creator, now I put one of your photo in the About form, and wish you enjoy it somehow.

Also now I have also used MSBuild to build all C# projects, and NAnt to manage anything else, so if you wanna compile CBC from source code you have to install .NET 2.0 along with MSBee targets for .NET 1.1. It is too complicated so I would like to write another article on that.

BTW, I add an option in the Framework tab in the Preferences Dialog. If you check it, and next time BDS starts, CBC will tell you how long it takes to load all the pluses. Since it is a feature for debugging and tuning, it is turned off by default.
