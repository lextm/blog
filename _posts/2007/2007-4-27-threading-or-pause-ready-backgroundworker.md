---
layout: post
title: "Threading or Pause-Ready BackgroundWorker"
description: "This post describes how to make a BackgroundWorker pause-ready."
tags: .NET
permalink: /threading-or-pause-ready-backgroundworker-e0813de90f02
excerpt_separator: <!--more-->
---
It is hard to make a Thread and control it well. However, using a Backgroundworker is much easier until you need to pause/resume it.

Can we make a `BackgroundWorker` pause-ready? Yes. I have joined [a discussion](http://forums.microsoft.com/MSDN/showpost.aspx?postid=1529756&siteid=1&&notification_id=2712442&message_id=2712442&agent=messenger) on the MSDN Forums. It seems that we approach to a solution finally. I have contributed the code samples. And in fact I have used the code in a big project. It runs just Okay.

Generally speaking, I will resort to `BackgroundWorker` in the future.
<!--more-->
