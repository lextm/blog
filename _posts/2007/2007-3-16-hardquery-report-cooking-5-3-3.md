---
layout: post
title: "HardQuery Report: Cooking 5.3.3"
description: This post is about the progress of HardQuery, specifically related to migrating from NAnt to MSBuild.
tags: Code-Beautifier-Collection Delphi
permalink: /hardquery-report-cooking-5-3-3-da1bb8fdb78f
excerpt_separator: <!--more-->
---
I have to confess that before I started to replace NAnt script with MSBuild script I never thought it costed me so much time.

I spent a half day on learning the MSBuild syntax. After that I worked hard on the transition. Yes, it was really hard because there was so much to be learned. The problem was that I had few examples to follow, and sometimes I had to try many times.

The result is so pleasing that it worths the while. After that I can clean up the code base finally. Yes, this time many temporary files are removed forever. The NAnt scripts are deleted, too. The solution tree has been revised for the fourth time which leads to a simple and maintainable structure for the first time.
<!--more-->

After this big change, I have the RC 2 ready to be shipped. The sas thing is that I did not release RC 1. Yes, what a pity. But I believe this new version will be much better.

Luckily I learned a lot from the work. It was unexpected that I named this stage of CBC HardQuery, while in fact the journey is really hard and I study a lot of different techniques, such as Sandcastle, MSBuild, MSBee, and so on.

You can download the latest build here.

Stay tuned.
