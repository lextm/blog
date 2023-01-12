---
layout: post
title: "Jexus Web Server and ASP.NET Cross Platform"
description: "This post is about my opinions on Jexus and ASP.NET cross platform development."
tags: .NET Mono Jexus-Manager
permalink: /jexus-web-server-and-asp-net-cross-platform-7d3c9169a906
excerpt_separator: <!--more-->
---
> Update: ASP.NET Core 2.0 is now mature enough as the official migration path for ASP.NET 4.x on .NET Framework. Thus, spend some time on ASP.NET Core please.

I was invited by Mingzhi Yi to give a talk at Jiaodong Developer Conference 2015 on 12 Dec. It was about my opinions on Jexus and ASP.NET cross platform development. This post is based on the same materials, and includes more details where necessary.
<!--more-->

## Microsoft's Cross Platform Roadmap

Microsoft's change in 2015 is astonishing to all other IT companies. Of course, such a shift to openness and open source began with Mr Ballmer's step-down, and Mr Nadella's rise as CEO, but also has been promoted heavily in many of the technology departments.

For example, the ASP.NET team in developer tools department has been open sourcing their products for a long time. Since ASP.NET MVC 1.0, all new frameworks from them are fully open sourced, such as Web API and SignalR, such as the OWIN middle Katana. They also have a good relationship with the Mono project.

The Hyper-V team has also been actively involved in open source community, such as Linux kernel, for years.

To long time Microsoft observers, it is not surprising at all to see Mr Nadella announced that Microsoft loves Linux in Oct, 2014. It is just a natural turnaround.

It is a must to go cross platform to enter new markets. For instance, many companies solely use Linux or Linux based solutions. Without buying Windows licenses, now such can deploy their ASP.NET web sites to Linux machines. Even if a company uses both Linux and Windows, now it has a chance to shift some web sites from Windows to Linux and achieve better cost control.

For public cloud computing platforms, there is also a cost reduction to use Linux to host your ASP.NET web sites, as in most cases Linux virtual machines are cheaper than Windows ones.

## .NET Core 5 and ASP.NET 5

To make web sites cross platform, the developer tools department spent a long time developing ASP.NET vNext after releasing .NET 4.5 and ASP.NET 4.5. After more than two years, the image is clear at this stage,

1. Fully rewrite the framework from scratch, and borrow a lot from node.js.
1. Use latest technologies, such as Roslyn and .NET Native.
1. Support .NET Framework but not bound to it.

That's the ASP.NET 5 we now see.

ASP.NET 5 supports Linux and OS X, where it runs on a brand new runtime from .NET team, aka .NET Core 5.

.NET Core 5 is also fully open source. The code base and all development logs can be found at GitHub, as well as other reference sites.

A significant set of changes have been carried out here, such as deletion of a large number of classes and methods. For example, some types under System.Security.Cryptography, UdpClient class under System.Net, and sync methods of the Socket class.

A class library project type is also introduced in VS 2015 whose extension is .xproj. The dependency management now changes from direct references to project.json. Such projects compile directly to NuGet packages.

ASP.NET 5 differs from its precedents too, that huge changes are introduced. For instance, System.Web, a core ASP.NET component since 1.0 initial release, is removed along with WebForms. So we will no longer need to use HttpContext to access runtime data, and no more `<system.web>` tag in web.config to configure settings. MVC/Web API/SignalR have also been merged (e.g. Web API's ApiController is now merged with MVC's Controller).

To deploy such applications, IIS and Windows can still be used, but this time HttpPlatformHandler as a separate component needs to be installed. For Linux platform deployment, nginx and Kestrel can be used.

We can see clearly that Microsoft wants the developers to migrate first from ASP.NET 4 to 5, and then move to Linux. That's in fact not a simple step, and a lot of manual conversion is required. Linux and nginx must be studied aside, while experience on Windows and IIS seems to be useless.

Well, anything simpler?

## Mono and Jexus Web Server

Mono has been an active open source project for more than a decade, which follows Microsoft .NET Framework. Miguel de Icaza has been leading it still, who became famous when he led the Gnome project. Miguel fell in love with C# and .NET when Microsoft announced it in 2000, and was eager to port such technologies to Linux. Now Mono receives support from both Xamarin and Microsoft.

Mono is more compatible with .NET Framework, differently from .NET Core's approach. After Microsoft released the reference code of .NET Framework in Nov 2014 under MIT license, Mono started to integrate the source files. More than 600 classes have now been shared between Mono and .NET Framework, and achieved better compatibility. Mono continues to use its own C# compiler (due to a few problems in Roslyn) and CLR implementation, with its own AOT approach and C# Shell. Application frameworks such as WinForms and WebForms are supported by Mono, as well as MVC 5/Web API 2/SignalR 2, which Microsoft ASP.NET team releases earlier.

On the solid foundation of Mono and Linux, Microsoft C# MVP Bing Liu decided to write his own web server since 2008, named Jexus. It grows steadily and gradually draws attention from other developers. Its 5.8.0 was released a few days ago. Jexus is written primarily in C#, and hooks to Linux kernel's epoll API. This choice gets rid of libraries such as libuv, so it achieves better performance. Currently all major Linux distributions and FreeBSD are the supported platforms.

Video 1: [Install Jexus on Ubuntu Server](http://v.youku.com/v_show/id_XMTQyMTA1OTA1Ng==.html)

Technically speaking, Jexus can compare to commercial web servers such as IIS because it features many important features,

* Support multiple web sites
* Support application pool
* Support HTTPS and WebSockets
* Support FastCGI and OWIN
* Support ASP.NET 4 apps (WebForms/MVC/Web API/SignalR)
* Support URL rewriting, reverse proxy, and compression
* Have built-in security protection, such as SQL injection prevention

Jexus has already been used in many web sites already. Many show cases can be found at its homepage.

Video 2: [MVC 5 web site exported from Visual Studio 2013](http://v.youku.com/v_show/id_XMTQyMTA2MDUzMg==.html)
Video 3: [Host MVC 5 on Jexus](http://v.youku.com/v_show/id_XMTQyMTA2MTUxMg==.html)

## Jexus Manager

For developers who are quite familiar with IIS management already, I developed a management tool called Jexus Manager to simplify Jexus management.

It runs on multiple platforms (Windows, OS X, and Linux), and supports multiple web servers (Jexus，IIS, and IIS Express), though all operations are similar to IIS Manager.

Interestingly, Jexus Manager also implements two important sets of API, named Microsoft.Web.Administration and Microsoft.Web.Management, to achieve extensibility.

## Jexus Roadmap
In the next few months, the following new features might come to Jexus,

* Support <system.webServer> tag in web.config
* Expose Microsoft.Web.Administration API to other apps on local machine
* Provide appcmd command line for management
* Support full ASP.NET 5!
* Add more options
* Provide REST API for remote management
* Provide built-in management web site
* Add commercial support contracts

BTW, Jexus Manager will become fully open source in 2016. Stay tuned.

## References

* Jexus homepage http://jexus.org
* Jexus English docs https://server.jexusmanager.com
