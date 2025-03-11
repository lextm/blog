---
layout: post
title: "Save CPU Utilization In An Empty Loop"
description: "This post describes how to save CPU utilization in an empty loop."
tags: .NET
permalink: /save-cpu-utilization-in-an-empty-loop-e9b4a265d874
excerpt_separator: <!--more-->
---
Sometimes you need to kill some time by running an empty `for` or `while` loop. The only problem is that the CPU utilization will soon reach 100% for a single core CPU or 50% for a duel-core. Oh, my Goodness, it is horrible.

How to solve the problem and protect your/and your users' CPU? A simple walk around is there. Just write `Thread.Sleep(??);` inside the loop. In my case, I let it sleep for 500-ms. In this way, the utilization can be reduced to a quite small number.
<!--more-->
