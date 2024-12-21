---
layout: post
title: "Some Gaps in Microsoft ASP.NET/IIS Stack and Why Jexus Steps In for The Community"
description: This post is about some gaps in Microsoft ASP.NET/IIS stack and why Jexus projects were created.
tags: Jexus-Manager .NET
permalink: /some-gaps-in-microsoft-asp-net-iis-stack-and-why-jexus-steps-in-for-the-community-e5a6f79fec99
excerpt_separator: <!--more-->
---
> Update: ASP.NET Core 2.0 today is mature enough as the official migration path for ASP.NET 4.x apps on .NET Framework. Thus, spend some time on ASP.NET Core please.

ASP.NET/IIS has been the core for server side .NET developers for years, and through the years many products come and go, but there are several gaps unfilled. This post reveals some of them that I personally think are critical or significant. The Jexus projects (Jexus web server and Jexus Manager) attempt to address some of them and more are coming in the future releases.
<!--more-->

## IIS Manager for IIS Express

IIS Express is introduced to replace Cassini, and it shares a large amount of code with full IIS. However, IIS Manager cannot be used to manage IIS Express.

Microsoft attempts to solve this by

1. Allowing some important settings to be configured in VS. That's quite a limited set of settings.
1. Providing command line tools (appcmd and so on). That's still not easy to use, as not everyone knows the command line tools.

IIS Manager could not be easily changed to support IIS Express because it has a tight dependency on IIS itself in every design (module organization, MWA dependency, permission control).

IIS Express has its own Microsoft.Web.Administration.dll (version 7.9, installed in GAC), which sometimes introduces even a bigger problem (affecting apps who want to use full IIS's MWA).

Thus, Jexus Manager was created to fill this gap, providing both a fully managed MWA clone which works without native dependencies, and GUI that emulating IIS Manager.

## ASP.NET 4.* Web Applications on Linux

Microsoft focuses on ASP.NET 5 and .NET Core 5, while we do see many existing projects remain on ASP.NET 4.*. Before there is a better way to convert ASP.NET 4.* apps to 5, it would be beneficial if we could run ASP.NET 4.* apps directly on Linux.

Luckily Jexus web server has been there for years. By using Mono's ASP.NET 4.* stack, many ASP.NET 4.* apps can run on Linux/Jexus with moderate modification (to adapt to Linux file system and so on mainly).

We are working on MWA support in Jexus, so that in future releases you might even use your Windows's copy of web.config with IIS configuration on Linux/Jexus. That should save you lots of efforts converting settings from IIS to another web server.

## Kestrel Limitation

The current approach of ASP.NET 5 is to Kestrel for CLR hosting, and another web server for reverse proxy. This gives ASP.NET 5 flexibility on Linux, but also makes knowledge of IIS useless on Linux.

Jexus web server adds support for ASP.NET 5 recently, which also works similar to IIS, and helps extend your investment on IIS knowledge to Linux.

(To be updated once Microsoft makes further announcements.)
