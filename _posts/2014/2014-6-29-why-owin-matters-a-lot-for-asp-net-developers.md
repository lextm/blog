---
description: Visual explanation of OWIN's importance for ASP.NET developers, demonstrating how its architecture enables applications to run across diverse platforms and web servers including Jexus on Linux.
excerpt_separator: <!--more-->
layout: post
permalink: /why-owin-matters-a-lot-for-asp-net-developers-3377d9d15f02
tags: .net asp.net iis jexus-manager linux
categories: [Tools and Platforms]
title: Why OWIN Matters A Lot for ASP.NET Developers
---
There are many articles discussing about OWIN even before ASP.NET vNext was announced. So why does it matter? Well, I try to provide a diagram nobody else yet drew.
<!--more-->

![img-description](/images/owin.png)
_Figure 1: OWIN ecosystem._

Got it now? From Microsoft's official documentation we can see their OWIN/Katana components (items in blue) help create decoupled layers, but you probably don't realize that many third party components (items in grey) are already out there to bring your web applications to a variety of computing platforms you never imagined. For example, can you imagine that a MVC 4 powered web app to run flawlessly on Jexus/Ubuntu on a Raspberry Pi board? Yes, that becomes reality right now.

OWIN focused on app frameworks and middleware in the past few months. The rising of Web server support, like what Jexus 5.6 (currently in beta) offers, is going to give more opportunities to ASP.NET developers.

Learn it now, or you will be left behind :)
