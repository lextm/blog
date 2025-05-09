---
description: Explore how Jexus Manager extends its capabilities to manage IIS Express through Microsoft.Web.Administration namespace implementation, offering a familiar interface for web server configuration.
excerpt_separator: <!--more-->
layout: post
permalink: /jexus-manager-for-iis-express-7620e9e976d0
tags: iis jexus-manager windows
categories: [Tools and Platforms]
title: Jexus Manager for IIS Express
---
You probably know Jexus Manager has been out for a while. Since I decided to implement Microsoft.Web.Administration namespace on my own and mapped Jexus settings to that model, it is technically possible to develop other mappings, such as the ones for IIS and IIS Express.

<!--more-->

Therefore, in the past few days (plus a few days in this summer) I finally finished the mapping for IIS Express, and now Jexus Manager can start to manage IIS Express. Below is a screen shot showing the initial achievements,

![img-description](/images/jexus-manager.png)
_Figure 1: Jexus Manager for IIS Express._

More information is going to be published in the next few weeks. I plan to do a public beta soon. Yes, it is a little bit slower than the original roadmap, but stay tuned.

[Update on Nov 16]
Alpha 1 is now available.
It is very buggy, so don't use it too seriously yet.

[Update on June 7, 2015]
Alpha 6 is available at the same location. Much more stable.

[Update on Sept 5, 2015]
Beta 1 is available at the same location. Major features completed.

[Update on Oct 3, 2015]
Beta 2 is available at the same location. Many core classes are rewritten to achieve better compatibility with Microsoft's MWA. Extend support for IIS 7/8/10 Express.

[Update on Oct 14, 2015]
Beta 3 is available at the same location, with IIS Express support enhanced, full IIS read-only mode previewed, and Jexus support added back.

[Update on Feb 10, 2016]
The documentation site https://jexusmanager.com is now online.

[Update on June 26, 2016]
[Jexus Manager is open source]({% post_url 2016/2016-6-26-jexus-manager-is-now-open-source %})
