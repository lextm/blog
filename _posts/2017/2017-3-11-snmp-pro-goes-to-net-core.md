---
layout: post
title: "#SNMP Pro Goes to .NET Core"
description: "This post is about how we are going to make #SNMP Pro .NET Core ready."
tags: IIS
permalink: /snmp-pro-goes-to-net-core-d3b3ebdc2750
excerpt_separator: <!--more-->
---

I blogged once about [how I moved #SNMP Library to .NET Core]({% post_url 2016/2016-12-26-porting-snmp-library-to-net-core-once-again %}). It was a wonderful journey though painful initially, but now Visual Studio 2017 and .NET Core Tooling 1.0 RTM are finally available, so my team have a better tool to work on #SNMP Pro and make it .NET Core ready.

<!--more-->

Of course, we have to make a few changes so as to adapt to the new platform, and in the mean time we try to keep them minimal.

> Don't know what is #SNMP Pro? Visit [our documentation site](https://pro.sharpsnmp.com/).

We will release a new release (1.3.0 based on current roadmap) when everything is tested out and all confidence is held. But if you are interested in the preview, we now have an insider program.

Please answer the below two questions and send your answers to [our mailbox](mailto:support@lextudio.com) to enroll (yep, that simple),

- Do you have a custom NuGet server/feed where you can host our test NuGet package for this build?
- What is the lowest .NET Standard version your apps require? Is .NET Standard 1.3 OK for them?

> Note, to better support .NET Core tooling we now ship NuGet package.

Stay tuned.
