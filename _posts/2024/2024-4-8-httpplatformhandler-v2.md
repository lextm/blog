---
layout: post
title: "HttpPlatformHandler v2"
description: "This post talks the new HttpPlatformHandler v2 and how it is built."
tags: .NET Visual-Studio Windows IIS HttpPlatformHandler
excerpt_separator: <!--more-->
---

LeXtudio Inc. just released a new product, HttpPlatformHandler v2, which is a new version of Microsoft HttpPlatformHandler. This post talks about why we build it and how we build it.
<!--more-->

## Why HttpPlatformHandler v2?

> The history of HttpPlatformHandler can be found in [this post]({% post_url 2023/2023-4-7-the-rough-history-of-iis-httpplatformhandler %}).

From various sources we can confirm that HttpPlatformHandler v1.2 was released in Jan 2015 ([here](https://www.iis.net/downloads/microsoft/category/host-applications#:~:text=HttpPlatformHandler%20v1.2%20Published,on%2001%2F15%2F2015%20by%20Microsoft) the day is showed as Jan 15, 2015). While this is a great module to bridge IIS and other application servers (Java/Python/Node.js/Go and etc), its design limitations started to show after a few years as the web has been constantly evolving,

* For example, v1.2 has a 8-KB output cache that we cannot disable, which prevents modern web features like SSE (Server-Sent Events) from working properly and can affect any Socket.IO implementation.
* On Windows ARM64, v1.2 can lead to application pool crash because it has no ARM64 build.
* There are other issues such as [this one](https://learn.microsoft.com/en-us/answers/questions/827779/iis-duplicate-http-platform-port).

Ideally Microsoft should release a new version (such as v1.3) of HttpPlatformHandler to address these issues but it didn't happen.

People started to write about switching to ASP.NET Core module as workaround, but they might quickly find out that the configuration (like the magical `ASPNETCORE_PORT` environment variable) wasn't documented publicly and Microsoft didn't provide any support for such usage.

## How We Build HttpPlatformHandler v2?

You know that in the past two years I wrote quite [a few blog posts on HttpPlatformHandler]({{ site.baseurl }}/tags/httpplatformhandler/), and I have been working on IIS topics for more than a decade (as IIS MVP or not). So why not take the challenging task to build a new version of HttpPlatformHandler? And most importantly, we can make it open-source.

But clearly Microsoft never released the source code of HttpPlatformHandler, so do we have to start from scratch? Not really. ASP.NET Core module was initially a fork of HttpPlatformHandler itself, now is both open-source and well maintained by Microsoft ASP.NET Core team. So, we started from there by creating a fork of ASP.NET Core module.

You might think all we needed to do is just renaming many things through the code base, but in fact there were quite a few places that we had to rip out ASP.NET Core specific code and added missing pieces. The most interesting part is to set up a suitable debugging environment for this IIS module, without using the massive bits Microsoft use for ASP.NET Core module. There were a few nasty bugs caused by the schema differences, but in a few days we were finally able to derive a slim module that just works for any programming languages/application servers. We ran all test cases I previously set up for those HttpPlatformHandler blog posts, and they all passed.

> For me personally, this is the second IIS module I derived from ASP.NET Core module, and I still learned something new. It's an interesting journey.

We are happy in the end we are able to keep this new module backward compatible with Microsoft HttpPlatformHandler v1.2 as much as possible. You can install it as a drop-in replacement without any code changes in your `web.config` files. That's why we confidently named it HttpPlatformHandler v2.

To recap, this v2 module from us provides the following benefits,

* Backward compatible with Microsoft HttpPlatformHandler v1.2. You can use it as a drop-in replacement.
* Bug fixes. SSE and other modern web features should work properly.
* IIS Express support (finally I know, as Microsoft never released a version for IIS Express).
* Open-source. You can check out the source code and build it yourself.

## How to Get HttpPlatformHandler v2?

The changes we make are released under MIT, and you can check out the source code and installers on [our GitHub repository](https://github.com/lextudio/httpplatformhandlerv2/releases).

The current release is marked as v2.0 RC2, as we are still testing it in various scenarios. But the module is already able to handle all the test cases my team have at hand, so we believe it's time that you try it out.

You are welcome to report any issues you find on [GitHub](https://github.com/lextudio/httpplatformhandlerv2/issues).

Stay tuned for more updates on this new project.
