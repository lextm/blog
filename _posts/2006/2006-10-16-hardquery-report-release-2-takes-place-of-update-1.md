---
layout: post
title: "HardQuery Report: Release 2 takes place of Update 1"
description: This post reports the progress of HardQuery and possibly a second release.
tags: Code-Beautifier-Collection Delphi
permalink: /hardquery-report-release-2-takes-place-of-update-1-1c26ab8a9617
excerpt_separator: <!--more-->
---
(CSDN Oct 16, 2006)

Since no serious bugs are found lately, it will be wield to release an update version when there is nothing to update. In fact, recently I've added a lot of new features and made important changes in LeXDK. A Release 2 version of HardQuery may sound better.
<!--more-->

New features are listed in previous threads, so now, I am focusing on PropertyService unit, a Registry pattern implementation.

When I made AStyle AddIn for SharpDevelop, I found out how to make use of Editor Buffer, that was how I added Undo support in HardQuery Final. This time I find out how SharpDevelop manages preferences through its PropertyService unit. I am not cloning it.

Because now I know how to build a Hashtable, and get a new deeper Serialization unit from Code Project, both techniques are used inside my PropertyService.

However, simple options are conveniently managed in this way, while complex objects are not correctly serialized and deserialized. Luckily, I could use an alternative way. Go and dig in the code. Then you will see how I make it.

Today or tomorrow I shall post a Release 2 Milestone 5 on GForge for you to try.

Stay tuned.
