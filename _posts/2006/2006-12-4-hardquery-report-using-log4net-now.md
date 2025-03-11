---
layout: post
title: "HardQuery Report: Using log4net now"
description: "This post describes that I have changed the logging framework to log4net."
tags: Code-Beautifier-Collection Delphi
permalink: /hardquery-report-using-log4net-now-dfb6b817a46a
excerpt_separator: <!--more-->
---
(CSDN Dec 04, 2006)

It is hard to find what I need now when I look into the log file generated. There are a lot of lines in that file that prevent me from finding the most important one.

As a result, I have to try something better than Debug and Trace. I have tried Microsoft's shared source Enterprise Library. However, it is not easy to use it in CBC, as the assemblies are loaded by BDS.exe. So I have to search again and find log4net suitable.

In 5.3.1.1003, log4net is used to make the log file. I have to say it is easy to learn and use, although the migration costs me a lot of time. I will finish this boring task these days and release an RC 3 soon.

Stay tuned.
<!--more-->