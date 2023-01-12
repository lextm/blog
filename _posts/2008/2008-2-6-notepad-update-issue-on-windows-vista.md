---
layout: post
title: "Notepad++ Update Issue on Windows Vista"
description: This post talks about the update issue of Notepad++ on Windows Vista.
tags: Windows
permalink: /notepad-update-issue-on-windows-vista-f97c4148d6a1
excerpt_separator: <!--more-->
---
Because auto update feature has been added to Code Beautifier Collection (http://code.google.com/p/lextudio) since 2006, I am able to compare other products with my small project to see if their auto update implementation is better or not.

Just one or months ago, auto update feature was added in Notepad++. However, compared to CBC N++'s update executable is launched every time N++ launches. This implementation is OK on Windows XP. But on Windows Vista, it is terrible.

N++ update executable requires elevation. This means even if no update is available I have to elevate it in order to use N++. Because my InDate implementation does not require elevation and do work well, I wonder why N++'s author implements an update executable like this.

(Update: I am using 4.8.2 now and this bug is fixed. Well done.)
<!--more-->