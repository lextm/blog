---
layout: post
title: "A WordPress on Windows Azure Web Site 502 Issue and Possible Fix"
description: "This post talks about a 502 issue I met on my WordPress blog hosted on Windows Azure."
tags: Azure
permalink: /a-wordpress-on-windows-azure-web-site-502-issue-and-possible-fix-e9c8bf77e360
excerpt_separator: <!--more-->
---
> First I claim that this fixed the 502 issue for my own blog (this page you visit). Due to the complexity of WordPress/PHP/IIS/Windows Azure, you might hit another 502 issue caused by another cause and that won't be resolved by following this post.

I lost my blog recently after migrating contents from Blogger to WordPress on Windows Azure. Yes, it is just the typical 502 error page.

> "502 - Web server received an invalid response while acting as a gateway or proxy server."
<!--more-->

Fiddler capture does not provide more hint except that it shows the 502 came from ARR on IIS 8. As I am IIS MVP, I know it won't be an easy issue to resolve without collecting more logs. However, this is Windows Azure we are talking about. So certain logs are not available to me, and my subscription does not provide me technical support on such issues (only billing issues can be supported).

As a result, I had to recall what were the changes I made before such issues appeared. Well, luckily I remembered that I upgraded it to Standard, and turned the application to 64 bit. Thus, now I set it back to 32 bit, and WOW my blog is back.

Anyway, if you happen to meet the same issue, try to set to 32 bit. I guess there might be some bitness related incompatibility, but I don't have any time to further analyze it.
