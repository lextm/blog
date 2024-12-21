---
layout: post
title: The Basic Facts About IIS/ASP.NET Process/Thread Identities
description: A post about the basic facts about IIS/ASP.NET process/thread identities that can help you understand the root cause of some issues.
tags: IIS .NET ASP.NET
permalink: /the-basic-facts-about-iis-asp-net-process-thread-identities-835eaac876a0
excerpt_separator: <!--more-->
image:
  path: /images/cloudy-day-montreal.jpg
  alt: Copyright © Lex Li. A cloudy day in Montreal.
---

Developers usually ignore the facts about process/thread identities when application frameworks hide them away. However, some time later in the development/testing problems/issues occur and bite them badly. So this post tries to provide a few basic facts, and hope it might lead you to the right direction.
<!--more-->

## The Process Identity

![img-description](/images/requests-worker-process.png)
_Figure 1: Two HTTP requests in a single IIS worker process._

We all know that IIS has application pools, and each pools has its own worker processes. So naturally, [the pool identity we choose](https://docs.microsoft.com/iis/configuration/system.applicationhost/applicationpools/add/processmodel#configuration) for a pool is used to initialize the worker processes, as process identity.

But there seems to be no direct setting to control thread identities, so when two HTTP requests come from different users, what are the thread identities then?

> Note that typical code to access this identity in C# is as below

``` csharp
var processIdentity = System.Security.Principal.WindowsIdentity.GetCurrent();
```

## The Thread Identity

We cannot answer that without assuming an authentication method, because that controls how IIS decides the thread identity.

If the simplest [anonymous authentication](https://docs.microsoft.com/iis/configuration/system.webserver/security/authentication/anonymousauthentication#configuration) is used, IIS might use `IUSR`, the default anonymous account, as thread identity.

> You might prefer application pool identity, so Microsoft allows that.

If we use Windows authentication, then IIS analyzes who sent the request, and use that user account as thread identity.

> For other authentication methods, you can dig out the thread identity by running a few simple experiments.

OK. Now we can use the knowledge above to solve a few real world puzzles.

> Note that typical code to access this identity in C# is via the properties,

* [`System.Web.UI.Page.User`](https://learn.microsoft.com/dotnet/api/system.web.ui.page.user) for ASP.NET WebForms
* [`System.Web.Mvc.Controller.User`](https://learn.microsoft.com/dotnet/api/system.web.mvc.controller.user) for ASP.NET MVC
* [`System.Web.Http.ApiController.User`](https://learn.microsoft.com/dotnet/api/system.web.http.apicontroller.user) for ASP.NET Web API

## Puzzle 1: Why IIS_IUSRS and IUSR need to read my web content folder?

Your web content folder contains two pieces of data,

* IIS configuration (`<system.webServer>` tag in `web.config` files)
* Other things.

So when the worker process is created, IIS needs to load IIS configuration. At that moment, the pool identity (process identity) reads the folder. We might only allow the actual pool identity to read this folder, but sometimes you might simply allows the group `IIS_IUSRS` (as all pool identities are in this group).

But when a request comes, IIS needs to load the actual web pages (or other contents) to generate a response. Then the thread identity is used to read the folder (`IUSR` in anonymous case).

## Puzzle 2: What is impersonation?

As the process and thread identities can be different, it is always confusing which is used to access a resource (SQL Server, remote file share, and so on).

> If you know the actual Win32 function calls and their parameters under the hood, then you can see clearly, but not everyone has the luxury.

Then product documentation and existing discussions can help you better understand the rules. For example, in an ASP.NET 4.x web app with the simplest SQL Server connection with Windows authentication (**WARNING, a lot of details are ignored**), usually the process identity is used to connect to the backend database instance.

But what if you want to use the thread identity to do queries, and let unauthorized users fail? Then you can use [impersonation](https://support.microsoft.com/en-ca/help/306158/how-to-implement-impersonation-in-an-asp-net-application).

``` xml
<identity impersonate="true" />
```

> Note that we only discuss "Impersonate the IIS Authenticated Account or User" here, as other cases are too complicated for beginners.

So that's what magic is really behind impersonation, by granting you control on which identity to use for a certain API call. Use it smartly or you end up with more puzzles.

## The End

If you hit identity related issues, go back to the basic diagram and try to analyze your web apps. Often the hint is right there beside you. Good luck.
