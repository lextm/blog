---
description: Learn about the new ASP.NET Core Diagnostics tool that helps troubleshoot deployment issues with ASP.NET Core on IIS and IIS Express environments.
excerpt_separator: <!--more-->
image:
  alt: Copyright © Lex Li. A flight to New York City.
  path: /images/flight-canada.jpg
layout: post
permalink: /asp-net-core-diagnostics-for-iis-iis-express-stories-behind-90b4e8229aad
tags: .net asp.net iis microsoft visual-studio
categories: [Tools and Platforms]
title: ASP.NET Core Diagnostics for IIS/IIS Express, Stories Behind
---
ASP.NET Core on IIS/IIS Express shouldn't be hard, as they all come from Microsoft. However, we all know it has been a mess since the beginning, as I blogged multiple times from different angles, in the following posts like [this]({% post_url 2018/2018-3-30-what-should-you-check-when-visual-studio-cannot-debug-asp-net-core-project %}), [this]({% post_url 2018/2018-6-15-the-horrible-story-of-publishing-net-core-web-apps-for-beginners %}), and [this]({% post_url 2017/2017-6-5-how-visual-studio-launches-iis-express-to-debug-asp-net-core-apps %}).

<!--more-->

So what should a developer do when a related error happens? Going through all the materials and tons of posts on Stack Overflow? That's both a waste of time and also a painful process, because even for a single error code (like 502.5) there are at least four possible causes (while Microsoft documentation only covers one).

I have been thinking about this for a while (since June 2017 maybe), but I wasn't quite familiar with all the necessary details yet, until last month at Microsoft campus. Again, thanks for all the new knowledge I gained from the MVP Summit sessions, and the passions from other participants, so that this year I was able to create [ASP.NET Core Diagnostics for IIS/IIS Express](https://docs.jexusmanager.com/tutorials/ancm-diagnostics.html) on the Hackathon day.

Similar to other diagnostics (like SSL), this new diagnostics tool focus first on data collection, where it checks,

- Whether ASP.NET Core module (ANCM) is installed, and what is the version number.
- Whether Visual C++ 2015 runtime is installed, and what's the version number.
- Whether the application pool is using `No Managed Code`.
- Whether a valid handler is registered.
- What's the web app runtime version.

Of course, whenever possible it also reports typical errors, such as version mismatch between ANCM and the web app runtime. Such should already apply to most 500 and 502.5 scenarios.

I am still trying to improve this tool so that it can cover more cases, and dig up more useful information in the report, so let's see how far we can go from here.

Stay tuned.
