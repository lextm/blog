---
layout: post
title: "BigDipper Light: Asynchronous Calls Coming"
description: "This post is about the asynchronous calls in #SNMP 7."
tags: SNMP
permalink: /bigdipper-light-asynchronous-calls-coming-30eaee7f4b88
excerpt_separator: <!--more-->
---
It was at the very beginning that users call for asynchronous GetResponse. Well, I did not provide them as I was not happy to provide the same copy of code several times in several places. Besides, .NET Framework offers so many approaches to make synchronous calls in asynchronous way.

But now we are working on our 7.0 release, and with new extension methods there is no longer a need to duplicate code undesirably, so why not give asynchronous calls a chance to shine? Here it is.
<!--more-->

In the latest change set, two methods are added to SnmpMessageExtension. They are BeginGetResponse and EndGetResponse. Because I follow .NET Framework's async pattern, you should be familiar with how to call them correctly.

Note that comparing to GetResponse, the timeout parameter is not present. For asynchronous calls, I think it is no longer necessary to pass timeout in.

The current implementation is subject to change, as the two methods are early experiments. They will be further enhanced so as to meet your high expectations.

Stay tuned.
