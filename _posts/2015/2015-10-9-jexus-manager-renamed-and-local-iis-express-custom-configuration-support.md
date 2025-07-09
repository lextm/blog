---
layout: post
title: "Jexus Manager: Renamed and Local IIS Express Custom Configuration Support"
description: "This post is about why Jexus Manager is renamed and how it supports IIS Express custom configuration."
tags: Jexus-Manager IIS
permalink: /jexus-manager-renamed-and-local-iis-express-custom-configuration-support-8cff599d012b
excerpt_separator: <!--more-->
---
I just renamed the first build of Beta 3 back to Jexus Manager 2.0. The removal of "for IIS Express" does not mean IIS Express support is cut (but significantly enhanced if you read further). This change is intentioned, because now in fact this tool supports much more than IIS Express.
<!--more-->

## The Name Change

Yep, a quick glance can let you see the changes. From top to bottom we have three servers opened,

* Local IIS Express global configuration file
* Local IIS
* Local Jexus web server simulator

Thus, it is time to get rid of the IIS Express limitation, and embrace all the best web servers for ASP.NET!

## IIS Express Custom Configuration

If you happen to use Visual Studio 2015 (I hope you did), you will find [the latest build](https://devblogs.microsoft.com/dotnet/new-asp-net-features-and-fixes-in-visual-studio-2015-rc/) quite useful.

Microsoft finally finds it too complex to put all web projects with IIS Express enabled in the global configuration, and decides that each solution should have its own config file living in the .vs folder (of course you can switch back to global by project settings).

Then how can Jexus Manager help you manage such custom configuration files? Well, now you can use "File | Connect to a Server…" menu item to directly add such files to Jexus Manager as they are new server instances. It is never this easy to enjoy the fun again.

Stay tuned for more news on Beta 3.
