---
layout: post
title: "Jexus Manager: The Open Source Plan"
description: "This post is about the open source plan of Jexus Manager."
tags: Jexus-Manager
permalink: /jexus-manager-the-open-source-plan-4977676be99e
excerpt_separator: <!--more-->
---
I was at Jiaodong Development Conference 2015 last Saturday, giving a talk on Jexus web server. One important announcement I made there, was to open source Jexus Manager source code. It was not a sudden decision, as when I demonstrated this product to geeks such as Scott Hanselman, he really thought that open sourcing it would be a good option.
<!--more-->

It is relatively easy to make a decision than carrying out the plan. Different from most of my previous projects, Jexus Manager was not initially open sourced, due to a few reasons,

1. Jexus web server is not open source.
1. The development involves a few technologies I didn't know well at that time, so the code is messy.
1. Even at this stage of 2.0 Beta 3, the code quality is not as high as I wanted.

Thus, to release the code in 2016 as truly open source, I will have to stop developing new features for a short while, clean up the code base, and add necessary documentation. Hope the following schedule can be hit without further delay.

## Schedule

2016 Q1: Clean up my open source implementation of Microsoft.Web.Administration and release it at GitHub. It features the following,

* Fully in C# (Microsoft's implementation binds to native COM)
* Cross platform (can run on OS X and Linux, for Jexus web server)
* Unit test cases covered
* Fix a few issues of Microsoft's implementation
[Updated on Jan 16, 2016: Now at GitHub https://github.com/jexuswebserver/Microsoft.Web.Administration under MIT license.]

[Updated on Feb 10, 2016: The NuGet package is at https://www.nuget.org/packages/Microsoft.Web.Administration.Jexus/11.0.0-beta.]

2016 Q2: Clean up my open source implementation of Microsoft.Web.Management and release it at GitHub. Since I haven't yet implemented all classes, the open source version will have many gaps for the community to fill in.

2016 Q3: Clean up and release all the remaining code of Jexus Manager.

[Updated on June 26, 2016: Jexus Manager [is now fully open source](jexus-manager-is-now-open-source-a48fef80a6e7)]

Stay tuned.