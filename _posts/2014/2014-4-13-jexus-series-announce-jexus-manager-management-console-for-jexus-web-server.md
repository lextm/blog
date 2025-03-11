---
layout: post
title: "Jexus Series: Announce Jexus Manager, Management Console for Jexus Web Server"
description: "This post talks about Jexus Manager, a management console for Jexus Web Server."
tags: Code-Beautifier-Collection Delphi
excerpt_separator: <!--more-->
---
As illustrated in early posts, Jexus web server is more similar to IIS, if we compare other famous web servers available on Linux. To better assist ASP.NET developers and professionals to migrate their web applications to Jexus, I have been developing a management console in the past few weeks. Today it is time to reveal this utility, aka Jexus Manager, to general public.
<!--more-->

Well, kind of familiar, right? Yes, Jexus Manager (JxMgr for short) client is a Windows Forms based application that looks almost the same as Microsoft IIS Manager. This design features the following advantages,

1. If you already know how to use IIS Manager, you know how to use Jexus Manager.
1. If you don't know IIS Manager, you can still find the UI easy to learn, as IIS help links are embedded to lead you to the tons of articles Microsoft published.
1. Even if you are a beginner of Jexus, you don't need to spend tons of time learning how to write configuration files in INI format or remember which options to use. In the UI, the same settings can be easily learned and configured.
Jexus Manager Homepage is at https://jexusmanager.com. (Update: 1.0 RC1 has retired. RC2 will be available on April 26.)

## Components

Jexus Manager has two components, client and server.

Jexus Manager server (aka RemoteServicesHost.exe) is a console application that should be deployed along with Jexus. It is an Owin based ASP.NET Web API 2 app that requires root permissions to run, and monitor a TCP port that users can configure at startup.

Jexus Manager client (aka JexusManager.exe) is a Windows Forms application that can run on any machine (Windows+.NET, OS X/Linux+Mono), which remotely connects to server side and enables remote management of Jexus servers.

## History/Roadmap

* 0.1 release (initial release in mid March 2014), bridged Microsoft.Web.Administration API with Jexus server configuration files.
* 0.5 release (first private beta in early April 2014), finished most of Jexus Manager client and can manage local Jexus server.
* 0.9 release (first public beta in mid April 2014, current release), finished Jexus Manager server, and can manage remote Jexus servers.
* 1.0 release, RC is expected in early May 2014, while RTW in mid May 2014. Feature tuning and bug fixes beyond 0.9.
* 2.0 release, RC is expected in early Oct 2014, while RTW in late Oct 2014. Full Microsoft.Web.Administration implementation with both IIS and Jexus back ends. Jexus Manager can then manage both IIS and Jexus instances.
* 2.1 release, RC is expected in early Feb 2015, while RTW in late Feb 2015. Added diagnostics for both IIS and Jexus.

## Price and Licensing

Jexus Manager release 1.0 is going to be free but not open source. Users might need to pay a license fee for Jexus Manager 2.0 and above.
