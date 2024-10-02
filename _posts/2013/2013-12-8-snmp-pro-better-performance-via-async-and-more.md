---
layout: post
title: "#SNMP Pro: Better Performance via Async and More"
description: "This post talks about how I improved the performance of #SNMP Pro Editions."
tags: SNMP
permalink: /snmp-pro-better-performance-via-async-and-more-e108ac3499b4
excerpt_separator: <!--more-->
---
At Microsoft MVP Summit a few weeks ago, I sat in [Lucian's Async sessions](http://blogs.msdn.com/b/lucian/archive/2013/11/23/talk-mvp-summit-async-best-practices.aspx) and really enjoyed the contents. (In fact, I were at the same sessions early this February, but at that time I were not able to do much async programming as I wished.) So finally this weekend I started to review #SNMP Pro Editions to see in which parts I could apply the optimization.
<!--more-->

So most of the long running functions have been converted to methods that return Task<T>, so that the UI forms can await on them. This simplifies the code base a lot as well, as I can now use async-await throughout the lines and get rid of old style nested sections. However, that does not contribute to the most of performance gain surprisingly. Why?

OK, let's start from my base line. The previous build of #SNMP MIB Compiler Pro can compile 1268 MIB documents in 85812-ms (roughly 1.5 minutes). Although this result is much better than the open source edition (yes, that's awesome as the Pro edition adds so many more validation and extra compilation features), it is not as good as I want.

I used Parallel.ForEach to allow compilation in parallel, but still the gain is little. Well, have to launch a profiler? Wait!!! It was before I launched the profiler that I found a serious problem.

Now the compiler uses a registry instance (ErrorRegistry) to collect all errors and warnings and raises events for UI to consume. Well, when an event is raised and the event handler is called, shouldn't the handler be finished as quickly as possible? Sorry, that's the problem in my code base, where the event handler goes pretty slow and it writes log entries to the UI synchronously!!! Thus, even if the compilation is fast, the whole process is slowed down due to error reporting.

I thought it would be pretty easy to fix the issue, but wrap such error reporting into Task instances and execute them asynchronously. But that fix won't work, as the log entries then appear on UI in an unpredictable order, simply because the Task instances are executed in that way. A dirty hack I used finally is to put all log entries into a ConcurrentQueue and then send them to UI in sequential order. That perfectly resolves the issue and leads to a performance result I could not believe.

Yes, now for 1268 files it only uses 13613-ms (more than 5X).
