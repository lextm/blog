---
layout: post
title: "Revival of LoggingService Functionality"
description: "This post is about why I revived the LoggingService functionality."
tags: .NET
permalink: /revival-of-loggingservice-functionality-29aef28c75b1
excerpt_separator: <!--more-->
---

A few years ago, I wrote a class for Code Beautifier Collection named [LoggingService]({% post_url 2006/2006-12-20-hardquery-report-using-loggingservice-class %}). At that time I decided to wrap over log4net.

However, I started to use log4net more directly in the following years, and LoggingService is no longer a convenient way. OK. Then how to make use of those old code again?

<!--more-->

1. Extension methods can be added to ILog and then I can use ILog.EnterMethod and ILog.LeaveMethod.
1. In order to add necessary indentation to the log files, I have to hack the appender.

Well, this becomes something much easier to use.
