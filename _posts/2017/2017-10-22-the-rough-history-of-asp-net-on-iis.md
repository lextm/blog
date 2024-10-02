---
layout: post
title: The Rough History of ASP.NET on IIS
description: This post is about the rough history of ASP.NET on IIS.
tags: Visual-Studio .NET
categories: [History, .NET]
permalink: /the-rough-history-of-asp-net-on-iis-8f49e2bcefcd
excerpt_separator: <!--more-->
---

> It all happened when I tried to answer [this Stack Overflow question](https://stackoverflow.com/questions/35639205/what-is-kestrel-vs-iis-express/46878663#46878663).
>
> The version below is last updated on Apr 10, 2023.

## The Birth of ASP.NET

Scott Guthrie joined Microsoft in 1997 and started to build something that enables rapid web application development. He mentioned more technical details in several occasions that the initial project was written in several programming languages (including Java) as experiments, and when .NET Framework/C# was selected to be the new platform for Windows development inside Microsoft, the framework he worked on was rewritten in C# and included as ASP.NET.

<!--more-->

> This version of ASP.NET introduced the HTTP request processing pipeline (classes around `HttpApplication`) as well as the UI control framework, which later is called WebForms (when ASP.NET MVC was introduced).

Two pieces of important software were required by ASP.NET developers,

- Cassini, later became ASP.NET Development Server in Visual Studio. It is a fully managed web server written in C# based on `HttpListener`. Of course, since it was designed for development only, many features were never implemented.

  > As Microsoft made the source code of Cassini available for the public, there are third parties who forked the code base and added more features, which started the Cassini family.

- ASP.NET support on IIS (revision 1). Because IIS was 4.0 and 5.0/5.1 at that time, which has nothing like application pools, ASP.NET even has its own worker process (`aspnet_wp.exe`), that hosts ASP.NET's own processing pipeline outside of IIS's pipeline.

So, web apps were developed on Cassini, and then deployed to IIS.

> The war of web browsers was just over (IE beat Netscape), but the war of web servers continued, so naturally ASP.NET became a selling point for IIS.

## IIS 6 and IIS 7

The introduction of application pools in IIS 6 required some changes on ASP.NET side, so `aspnet_wp.exe` became obsolete and replaced by `aspnet_isapi.dll`. This hooks up ASP.NET processing pipeline to IIS via the classic ISAPI approach. That can be seen as ASP.NET support on IIS revision 2. So ASP.NET apps are being hosted in IIS worker processes (`w3wp.exe`) for the first time. This was later called the IIS classic pipeline.

The introduction of integrated pipeline in IIS 7 and above required further changes, which replaced `aspnet_isapi.dll` with `webengine.dll` (.NET Framework 2.0/3.0/3.5) and `webengine4.dll` (.NET Framework 4.x). That can be seen as ASP.NET support on IIS revision 3. ASP.NET and IIS pipelines are unified in this pipeline mode.

> If you want to dive deeper into this, Microsoft documented the pipeline modes in [this article](https://docs.microsoft.com/iis/application-frameworks/building-and-running-aspnet-applications/aspnet-integration-with-iis#aspnet-integration-architecture) with great diagrams.

## IIS Express and OWIN

WCF and ASP.NET MVC were introduced to enrich web apps/services development, but they also make the web stack complicated and monolithic. In that situation, Cassini started to show its age (and other problems), and was gradually replaced by IIS Express (a user mode lite IIS).

When ASP.NET Web API and SignalR were developed, Microsoft engineers started to develop the OWIN based pipeline and utilize the middleware concepts to decouple different components of the web framework. That attempt worked quite well for Web API and SignalR scenarios and enabled cool things like self hosting. However, later they found it difficult to migrate WebForms and MVC to this new pipeline without breaking compatibility. Therefore, a platform upgrade was unavoidable.

> Thus, in many cases, when people blame that IIS is slow, they should blame ASP.NET in fact. IIS itself without ASP.NET is pretty fast and stable, while ASP.NET was not developed with enough performance metrics in mind (as WebForms focuses quite a lot on productivity and RAD).

## ASP.NET Core, Kestrel, and ASP.NET Core Module

Then in November 2014, ASP.NET 5 (later renamed to ASP.NET Core) was announced and became a cross platform technology. Obviously Microsoft needed a new design to support Windows, macOS, and Linux, where all major web servers, nginx/Apache (or other web servers) should be considered besides IIS.

I think many would agree that Microsoft learned quite a lot from Node.js, and then designed and developed Kestrel. It was initially based on `libuv` and moved to fully managed sockets in .NET Core 2.1. As a light weighted web server like Cassini, it later includes more features that usually appear only in a full web server. So, it is no longer a toy server.

Then why cannot you just use Kestrel? Why IIS Express and potentially IIS, nginx, or Apache are still needed? That primarily is a result of today's internet practice. Most web sites use reverse proxies to take requests from your web browsers and then forward to the application servers in the background.

- IIS Express/IIS/nginx/Apache are the reverse proxy servers
- Kestrel/Node.js/Tomcat and so on are the application servers

[Microsoft has its documentation here](https://docs.microsoft.com/aspnet/core/fundamentals/servers/kestrel).

Microsoft developed HttpPlatformHandler initially to make IIS a good enough reverse proxy for Java/Python and so on, so planned to use it for ASP.NET Core. Issues started to appear during development, so later Microsoft made ASP.NET Core Module specifically for ASP.NET Core. That's ASP.NET support on IIS revision 4, which is later called out-of-process hosting mode.

Starting from ASP.NET Core 2.2, ASP.NET Core Module for IIS (version 2) can host .NET Core environment inside IIS worker process (w3wp.exe), quite similar to ASP.NET 2.x/4.x. This mode is called ["IIS in-process hosting"](https://learn.microsoft.com/aspnet/core/host-and-deploy/aspnet-core-module#in-process-hosting-model). It can be considered as ASP.NET support on IIS revision 5.

One recent update is that ASP.NET Core/Kestrel can be used to host reverse proxy functionalities itself, as [the open source YARP project revealed](https://microsoft.github.io/reverse-proxy/).

Kestrel/YARP is now widely used inside Microsoft Azure to replace IIS ARR in many scenarios as reported, so literally now you can host your own production web apps with Kestrel/YARP without any other web server (IIS/nginx/Apache) in front as well.

> Look for other interesting posts like this one? You can visit [the .NET Legends page]({% post_url 2017/2017-11-2-all-in-one-for-the-legends-of-net-materials %}).
