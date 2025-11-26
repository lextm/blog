---
description: Important considerations when using Hangfire with IIS, explaining thread model incompatibilities, potential issues with idle shutdown, and recommended architectural alternatives.
excerpt_separator: <!--more-->
image:
  alt: Copyright © Lex Li. PY1 Pyramid show at Montreal.
  path: /images/py1-pyramid.jpg
layout: post
permalink: /unpleasant-facts-about-hangfire-632a3228ff8a
tags: asp.net iis .net
categories: [Frameworks and Libraries]
title: Unpleasant Facts about Hangfire
d2: true
---
When people choose to use a framework, they are not only enjoying the benefits it brings, but also take ownership of the evil associated. Hangfire is one of such frameworks with problematic default configuration, so be caution.
<!--more-->

## The Thread Model: Hangfire Threads are Aliens

```d2
direction: right

IIS: {
  label: "IIS Services"
}

W: {
  label: "w3wp.exe"
  direction: down

  ASP1: {
    label: "ASP.NET Thread"
  }
  ASP2: {
    label: "ASP.NET Thread"
  }
  H1: {
    label: "Hangfire Thread"
    style.fill: "#d9d9d9"
  }
  H2: {
    label: "Hangfire Thread"
    style.fill: "#d9d9d9"
  }
}

IIS -- W.ASP1
IIS -- W.ASP2
```
_Figure 1: Threads inside w3wp.exe._

Microsoft designs IIS to be a multi-process system, and web applications are hosted in worker processes (w3wp.exe). So if you try to run a typical ASP.NET web application, within the worker process several threads are initialized. IIS/ASP.NET runtime are aware of such threads, so as to assert the health of the application.

This design has been used for a very long time (since 2003), so it works well with many IIS features. For example, IIS shuts down a worker process if it hasn't been processing incoming requests for a certain amount of time (idle shutdown timeout). This applies to the pink threads above in the diagram.

However, a web application with Hangfire configured usually spins off extra threads so as to schedule/execute background tasks, like the grey ones in the diagram above. Those threads are not managed by IIS/ASP.NET, and they are not processing incoming requests. Therefore, IIS idle shutdown will kill the worker process even if certain Hangfire threads are still processing scheduled tasks.

Well, [Hangfire documentation](https://docs.hangfire.io/en/latest/deployment-to-production/making-aspnet-app-always-running.html) tells that you can change IIS settings as workarounds, but does it mention that always running has its side effects? No.

## The Recommended Approaches

If you don't mind all issues brought by the default Hangfire configuration, keep using it.

If you do want to go a more reliable way,

* Hangfire [allows you to run Hangfire server in a separate process](https://docs.hangfire.io/en/latest/background-processing/placing-processing-into-another-process.html), which is a better approach.
* You can develop your own Windows service application on Windows Server machines to run scheduled tasks if you like.
* On a cloud platform such as AWS/Azure, run scheduled tasks in the right service (Lambda or Azure Functions).

  > Azure App Service has a feature called WebJobs, which is also OK for certain simple scenarios.
