---
layout: post
title: "TritonMate Words: BytesViewer, Yet Another Sample"
description: This post talks about the new sample, BytesViewer, which is a very useful tool for learning and troubleshooting.
tags: SNMP
permalink: /tritonmate-words-bytesviewer-yet-another-sample-3c83c897ccf7
excerpt_separator: <!--more-->
---
For a very long time, no new samples have been added to #SNMP code base, because the existing samples already demonstrate most of the features a developer might need. However, I think the new comer, named BytesViewer, is a very useful tool, both for learning and troubleshooting.
<!--more-->

## The Problem
In Wireshark we can easily analyze SNMP packets. But what if at hand we don't have a full capture file? When all we have is `30 42 02 01 01 04 06 70 75 62 6C 69 63 A4 35 06 08 2B 06 01 04 01 80 … …`, it is no longer easy to utilize Wireshark.

I often met such problems when handling issue reports from users, and the best approach I found in the past was to write a corresponding test case in MessageFactoryTestFixture.cs and debug the test case. That was convenient enough to locate the root cause, but no user would like to do the same.

## The BytesViewer
The new sample is friendly to users, as it transforms a boring test case in MessageFactoryTestFixture.cs to a navigable tree view. For example, I copy the same bytes from TestReportFailure test case into the top text box, and also type the user information in the items on the tool bar. Then by clicking Analyze button, I immediately know the message in details.

Hope you like this new sample and learn more about SNMP message format from the bytes.

Stay tuned.
