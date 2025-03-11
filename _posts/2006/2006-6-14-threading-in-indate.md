---
layout: post
title: "Threading in InDate"
description: This post is about .NET multi-threading used in InDate feature.
tags: Code-Beautifier-Collection Delphi
permalink: /threading-in-indate-28d940bc7503
excerpt_separator: <!--more-->
---
(June 14, 2006)

It is not hard to see the InDate feature in N3 Update 1 RC 3 has some problems.
<!--more-->

When you use Options | Update… to get update, BDS IDE freezes/locks. Since it takes long to do a update checking and download, this locking state is very unpleasant.

Today, for the very first time I study .NET threading, and partially solve this big problem and left a small one.

Now InDate on my computer does not lock BDS IDE while it is checking the blog or downloading.

The problem remaining is that when working, InDate dialog locks. I have to find some way to solve it. It requires further study on threading and WinForms components.
