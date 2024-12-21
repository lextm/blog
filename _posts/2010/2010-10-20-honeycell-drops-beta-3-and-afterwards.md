---
layout: post
title: "HoneyCell Drops: Beta 3 and Afterwards"
description: "This post is about the third beta release of #SNMP 6.0 and future plan."
tags: SNMP
permalink: /honeycell-drops-beta-3-and-afterwards-3f462280c700
excerpt_separator: <!--more-->
---
Beta 3 was released last weekend. But we still have more new things to add to the code base.
<!--more-->

Currently, I am busy reviewing SNMP RFC documents to better understand the details on message handling. Then all message handlers will be tuned to be standard compliant. It is not an easy task, but since Moq is found and used to build test cases, now the progress is promising. I am pretty sure that we will get high coverage this time.

Though this delays the release day for 6.0 final, I think it worths the while. At least, we can consolidate the code base heavily again to ensure less bugs remain.

If you are interested in the recent changes, you can check out the latest code from here.

BTW, there are a lot of tiny breaking changes throughout the code base during the past weeks. I will try to provide a detailed summary once we finish the release. NDepend should be able to provide us all information on breaking changes, and I will make full use of it this time.
