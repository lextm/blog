---
layout: post
title: "The Rough History of IIS HttpPlatformHandler"
description: "This post talks about the rough history of IIS HttpPlatformHandler and the miseries around it."
tags: .NET Visual-Studio Windows IIS HttpPlatformHandler
categories: [History, IIS]
excerpt_separator: <!--more-->
---

Due to various misinformation around this IIS out-of-band component, I think it's worth the while to write about its history so you know what others are talking about and how some of them made mistakes.

<!--more-->

## The Start of Windows Azure

When Microsoft entered the cloud computing market, it was a big challenge to support non-Microsoft technologies on Windows Server so that this platform can expand its reach to a broader audience.

That effort happened to align with a few important changes on IIS itself, where FastCGI support was added so that PHP applications can be hosted on IIS via that interface in 2006. Zend Technologies Inc. and PHP community were willing to help on PHP for Windows while Microsoft provided support.

While this was a big step forward, soon people discovered the difficulty to extend the excitement to other programming languages. For example, wfastcgi was developed by Microsoft Python team in 2012 to enable FastCGI support for Python. iisnode was developed by Tomasz Janczuk initially in 2012 to enable FastCGI support for Node.js, and later handed over to Microsoft Azure team.

But the FastCGI approach isn't sustainable, as the Azure team cannot create and maintain more to integrate Ruby, Go, Java, and many more languages with FastCGI.

## The Reverse Proxy Disadvantages

A clear alternative at that time was to run those non-Microsoft technologies on their own application servers, and then IIS/ARR can sit in front as reverse proxy. The popularity of nginx proved the feasibility for long, but this approach comes with its own disadvantages,

1. The application server is usually running on its own, so you should not expect it to work in your familiar application pool pattern that from time to time the processes are recycled.
   > Note that language specific tools like pm2 for Node.js can help here.
1. You need complex reverse proxy rules to be defined on IIS side to ensure traffic can be properly forwarded to the application server.
1. You need to predetermine the port for your application server. It's not a big deal for your own server which just hosts one or two web apps this way, but what about an enterprise server with hundreds of web apps? It's not easy to manage the port numbers.

## The Magical HttpPlatformHandler

Building up FastCGI and ARR gave Microsoft developers enough experience on both sides of the coin, so they came back with a very smart idea and implemented a new component called HttpPlatformHandler.

It seems to work just like a reverse proxy between IIS and your application server, but the reverse proxy rules and port numbers are managed automatically and transparent. And all you need to configure is:

1. Which process should be called with, and
2. What are the right arguments to launch the application server process.

Once configuration is done, this module spins out the application server on demand and recycle it whenever needed.

> The port number in use can be either passed as one of the arguments or via an environment variable, so that your application server knows which port it should hook to.

The simplicity of this design makes the module a great success, as you no longer need any language specific FastCGI bits or ISAPI modules. HttpPlatformHandler configuration is rather simple and it works for almost all modern web stacks.

This was first used by Microsoft Azure Websites to host Java web apps, and soon released as a separate download for all IIS users in 2015.

## The Mist of ASP.NET Core Module

When Microsoft designed ASP.NET Core, HttpPlatformHandler was naturally chosen to be the integration point. However, the more features ported from ASP.NET 4.x, the more gaps identified that HttpPlatformHandler cannot fulfill all the needs.

ASP.NET 4.x has so tight integration with IIS (if you read about the integrated pipeline) that a dedicated IIS module must be developed to replace HttpPlatformHandler in order to support most of the unique features and enable a smooth migration path. Now you know this new module as ASP.NET Core module for IIS.

Almost all misinformation today can be traced back to [this announcement made by the ASP.NET Core team on GitHub](https://github.com/aspnet/IISIntegration/issues/105). Readers without knowing the entire story or reading the announcement carefully can easily assume that they shouldn't use HttpPlatformHandler in all cases but switch to ASP.NET Core module. You can see how wrong that assumption is. Author of the original announcement later clarified that the announcement was not meant to discourage overall HttpPlatformHandler usage, but to inform just the ASP.NET Core community about the new ASP.NET Core module in [this comment](https://github.com/aspnet/IISIntegration/issues/1454#issuecomment-425472537),

> "HttpPlatformHandler was only replaced by ANCM for ASP.NET Core apps, it is still maintained for other uses. You're welcome to use ANCM for other applications but we don't document or support that scenario, you would need to reverse engineer it from here."

There are a few noticeable things we can observe from ASP.NET Core module source code though (to help you better understand its sibling HttpPlatformHandler),

1. The module keeps the functionality of HttpPlatformHandler, so that it can host Kestrel processes in out-of-process mode. But you won't find the documentation from Microsoft on the port number environment variable, as ASP.NET Core/Kestrel has that knowledge built in.
1. Except the way to shut down the application server process via Control+C, it also adds a new way to shut down the process via a special URL (`/iisintegration`). This is a feature that HttpPlatformHandler does not have.
1. The module adds a lot of features to support ASP.NET Core in-process mode, which is not available in HttpPlatformHandler. This is why the module is not a replacement for HttpPlatformHandler, and it has a larger memory footprint.
1. It changed some internals such as [the 8kb internal buffer](https://github.com/aspnet/IISIntegration/issues/7). Those changes were not backported to HttpPlatformHandler.

> If you are interested in learning more about ASP.NET Core module, you might review its code base on GitHub under `dotnet/aspnetcore` repository. Methods like [`UseIISIntegration`](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.hosting.webhostbuilderiisextensions.useiisintegration) or`UseIIS` are also important.

So, HttpPlatformHandler is still fully supported by Microsoft, and its latest release v1.2 from 2015 supports all latest Windows releases. If you are hosting Python/Ruby/Go/Java/Node.js applications on IIS, give it a try and feel how simple it is to set up everything around it.

## HttpPlatformHandler v2.0 by LeXtudio

LeXtudio Inc. just released a new product, HttpPlatformHandler v2, which is a a drop-in replacement for Microsoft HttpPlatformHandler v1.2 but offer more features and bugfixes. You are welcome to give it a try.

This post talks about why we build it and how we build it. You can find more details in [this post]({% post_url 2024/2024-4-8-httpplatformhandler-v2 %}).

## Side Notes

### HttpPlatformHandler on Azure App Service

HttpPlatformHandler is also enabled on Azure App Service (Windows) by default, so if you have tested your web apps on your own IIS server, you can confidently host them on Azure App Service without many changes on configuration.

### HttpPlatformHandler on IIS Express

This special requirement is now for the first time covered by the [new open source HttpPlatformHandler v2.0 from LeXtudio]({% post_url 2024/2024-4-8-httpplatformhandler-v2 %}).

> If you do prefer Microsoft HttpPlatformHandler v1.2, I also created the necessary PowerShell scripts to help enable that on IIS Express. You can find them on [my GitHub repository](https://github.com/lextm/iisexpress-httpplatformhandler).

## References

- [PHP on IIS announcement](https://news.microsoft.com/2006/10/31/microsoft-and-zend-technologies-announce-technical-collaboration-to-improve-interoperability-of-php-on-the-windows-server-platform/)
- [wfastCGI initial commit](https://github.com/microsoft/PTVS/commit/0b944a292442dcb7a5caaffb9e3cd7542bbf190f)
- [iisnode initial commit](https://github.com/tjanczuk/iisnode/commit/2ad22f2dbc5d9721a58c006c5fb7aef18ae6b430)
- [HttpPlatformHandler initial announcement](https://azure.microsoft.com/blog/announcing-the-release-of-the-httpplatformhandler-module-for-iis-8/)
- [HttpPlaformHandler v2 by LeXtudio](https://github.com/lextudio/httpplatformhandlerv2/releases)
- [Configuration Reference by Microsoft](https://learn.microsoft.com/iis/extensions/httpplatformhandler/httpplatformhandler-configuration-reference)
- [Java Example by Microsoft](<https://learn.microsoft.com/previous-versions/azure/windows-server-azure-pack/mt125371(v=technet.10)>)
- [Python Example by Microsoft](https://learn.microsoft.com/visualstudio/python/configure-web-apps-for-iis-windows?view=vs-2022#configure-the-httpplatform-handler)
- [Python/Flask Example by me]({% post_url 2022/2022-7-10-running-flask-web-apps-on-iis-with-httpplatformhandler %})
- [Python/Django Example by me]({% post_url 2024/2024-3-30-running-django-web-apps-on-iis-with-httpplatformhandler %})
- [Python/FastAPI Example by me]({% post_url 2024/2024-3-30-running-fastapi-web-apps-on-iis-with-httpplatformhandler %})
- [Node.js Example by me]({% post_url 2022/2022-6-11-running-nodejs-web-apps-on-iis-with-httpplatformhandler %})
- [Next.js Example by me]({% post_url 2024/2024-3-31-running-next-js-web-apps-on-iis-with-httpplatformhandler %})
- [Nuxt 3 Example by me]({% post_url 2023/2023-1-16-running-nuxt-3-web-apps-on-iis-with-httpplatformhandler %})
- [Nest Example by me]({% post_url 2024/2024-4-5-running-nest-web-apps-on-iis-with-httpplatformhandler %})
- [Ruby Example by Scott Hanselman](https://www.hanselman.com/blog/announcing-running-ruby-on-rails-on-iis8-or-anything-else-really-with-the-new-httpplatformhandler)
- [Go Example by me]({% post_url 2024/2024-2-9-running-go-web-apps-on-iis-with-httpplatformhandler %})
