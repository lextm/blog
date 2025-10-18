---
description: Visual explanation of OWIN's importance for ASP.NET developers, demonstrating how its architecture enables applications to run across diverse platforms and web servers including Jexus on Linux.
excerpt_separator: <!--more-->
layout: post
permalink: /why-owin-matters-a-lot-for-asp-net-developers-3377d9d15f02
tags: .net asp.net iis jexus-manager linux
categories: [Tools and Platforms]
title: Why OWIN Matters A Lot for ASP.NET Developers
mermaid: true
---
There are many articles discussing about OWIN even before ASP.NET vNext was announced. So why does it matter? Well, I try to provide a diagram nobody else yet drew.
<!--more-->

```mermaid
flowchart LR
    subgraph HS[Hosts]
        direction TB
        HS1[Windows]
        HS2[Linux]
        HS3[BSD]
        HS4[...]
    end

    subgraph WS[Web Servers]
        direction TB
        WS1[IIS]
        WS2[Jexus]
        WS3[...]
    end

    subgraph AD[Server Adapters]
        direction TB
        AD1[Host.IIS]
        AD2[Host.SystemWeb]
        AD3[Host.Jexus]
        AD4[...]
    end

    subgraph MW[OWIN Middleware]
        direction TB
        MW1[Katana]
        MW2[Nowin]
        MW3[...]
    end

    subgraph AF[Application Frameworks]
        direction TB
        AF1[MVC]
        AF2[Web API]
        AF3[SignalR]
        AF4[Nancy]
        AF5[...]
    end

    classDef ms fill:#4d91ff,color:#fff,stroke:#1f4ab8,stroke-width:1.5px;
    classDef third fill:#d1d1d1,color:#333,stroke:#888,stroke-width:1.5px;

    class AF1,AF2,AF3,MW1,MW2,AD1,AD2,WS1,HS1 ms;
    class AF4,AF5,MW3,AD3,AD4,WS2,WS3,HS2,HS3,HS4 third;

    style AF fill:#ffffff,stroke:#4d91ff,stroke-width:2px;
    style MW fill:#ffffff,stroke:#4d91ff,stroke-width:2px;
    style AD fill:#ffffff,stroke:#4d91ff,stroke-width:2px;
    style WS fill:#ffffff,stroke:#4d91ff,stroke-width:2px;
    style HS fill:#ffffff,stroke:#4d91ff,stroke-width:2px;
```
_Figure 1: OWIN ecosystem._

Got it now? From Microsoft's official documentation we can see their OWIN/Katana components (items in blue) help create decoupled layers, but you probably don't realize that many third party components (items in grey) are already out there to bring your web applications to a variety of computing platforms you never imagined. For example, can you imagine that a MVC 4 powered web app to run flawlessly on Jexus/Ubuntu on a Raspberry Pi board? Yes, that becomes reality right now.

OWIN focused on app frameworks and middleware in the past few months. The rising of Web server support, like what Jexus 5.6 (currently in beta) offers, is going to give more opportunities to ASP.NET developers.

Learn it now, or you will be left behind :)
