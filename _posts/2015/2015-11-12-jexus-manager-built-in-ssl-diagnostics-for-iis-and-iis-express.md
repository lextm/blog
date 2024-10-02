---
layout: post
title: "Jexus Manager: Built-in SSL Diagnostics for IIS and IIS Express"
description: "This post is about how Jexus Manager built-in SSL Diagnostics for IIS and IIS Express, and how it can help you troubleshoot SSL/TLS/HTTPS issues."
tags: Jexus-Manager IIS
permalink: /jexus-manager-built-in-ssl-diagnostics-for-iis-and-iis-express-69128ad1c4fb
excerpt_separator: <!--more-->
---
IIS 6 used to have a great troubleshooting tool called SSL Diagnostics (SSL Diag for short). It relied on the ADSI API, so this tool was not made part of IIS 7.
<!--more-->

Of course you can use the IIS 6 version if you enable IIS 6 Compatibility component on IIS 7, but it would be less convenient.

A Microsoft employee Vijayshinva Karnure developed a newer version that relied only on IIS 7+ new API, and [released it](https://www.iis.net/downloads/community/2009/09/ssl-diagnostics-tool-for-iis-7).

It works for all IIS versions (up to 10), but it does not work for IIS Express.

OK. Enough about the background, and here is the quick announcement. Yes, now for web servers opened in Jexus Manager, you can see a new action called SSL Diagnostics showed, and clicking it gives you the report. Errors are now nowhere to hide.

Note that currently I only implemented the Generate Report button. Save and Verify Store will be fixed soon. You can start playing with this new feature by downloading the latest build.

Stay tuned.
