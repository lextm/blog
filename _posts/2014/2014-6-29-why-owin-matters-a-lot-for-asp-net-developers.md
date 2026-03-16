---
description: Visual explanation of OWIN's importance for ASP.NET developers, demonstrating how its architecture enables applications to run across diverse platforms and web servers including Jexus on Linux.
excerpt_separator: <!--more-->
layout: post
permalink: /why-owin-matters-a-lot-for-asp-net-developers-3377d9d15f02
tags: .net asp.net iis jexus-manager linux
categories: [Tools and Platforms]
title: Why OWIN Matters A Lot for ASP.NET Developers
d2: true
---
There are many articles discussing about OWIN even before ASP.NET vNext was announced. So why does it matter? Well, I try to provide a diagram nobody else yet drew.
<!--more-->

```d2
direction: right
grid-rows: 5

AF: {
  label: "Application Frameworks"
  grid-columns: 5
  MVC: {
    label: "MVC"
    style.fill: "#cfe0ff"
  }
  WebAPI: {
    label: "Web API"
    style.fill: "#cfe0ff"
  }
  SignalR: {
    label: "SignalR"
    style.fill: "#cfe0ff"
  }
  Nancy: {
    label: "Nancy"
    style.fill: "#dddddd"
  }
  OtherFrameworks: {
    label: "..."
    style.fill: "#dddddd"
  }
}

MW: {
  label: "OWIN Middleware"
  grid-columns: 3
  Katana: {
    label: "Katana"
    style.fill: "#cfe0ff"
  }
  Nowin: {
    label: "Nowin"
    style.fill: "#cfe0ff"
  }
  OtherMiddleware: {
    label: "..."
    style.fill: "#dddddd"
  }
}

AD: {
  label: "Server Adapters"
  grid-columns: 4
  HostIIS: {
    label: "Host.IIS"
    style.fill: "#cfe0ff"
  }
  HostSystemWeb: {
    label: "Host.SystemWeb"
    style.fill: "#cfe0ff"
  }
  HostJexus: {
    label: "Host.Jexus"
    style.fill: "#dddddd"
  }
  OtherAdapters: {
    label: "..."
    style.fill: "#dddddd"
  }
}

WS: {
  label: "Web Servers"
  grid-columns: 3
  IIS: {
    label: "IIS"
    style.fill: "#cfe0ff"
  }
  Jexus: {
    label: "Jexus"
    style.fill: "#dddddd"
  }
  OtherWebServers: {
    label: "..."
    style.fill: "#dddddd"
  }
}

HS: {
  label: "Hosts"
  grid-columns: 4
  Windows: {
    label: "Windows"
    style.fill: "#cfe0ff"
  }
  Linux: {
    label: "Linux"
    style.fill: "#dddddd"
  }
  BSD: {
    label: "BSD"
    style.fill: "#dddddd"
  }
  OtherHosts: {
    label: "..."
    style.fill: "#dddddd"
  }
}
```
_Figure 1: OWIN ecosystem._

Got it now? From Microsoft's official documentation we can see their OWIN/Katana components (items in blue) help create decoupled layers, but you probably don't realize that many third party components (items in grey) are already out there to bring your web applications to a variety of computing platforms you never imagined. For example, can you imagine that a MVC 4 powered web app to run flawlessly on Jexus/Ubuntu on a Raspberry Pi board? Yes, that becomes reality right now.

OWIN focused on app frameworks and middleware in the past few months. The rising of Web server support, like what Jexus 5.6 (currently in beta) offers, is going to give more opportunities to ASP.NET developers.

Learn it now, or you will be left behind :)
