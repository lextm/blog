---
description: Detailed explanation of ASP.NET Core's execution model on IIS, including the relationship between w3wp.exe and Kestrel, process creation, and debugging considerations.
excerpt_separator: <!--more-->
layout: post
permalink: /a-closer-look-at-asp-net-core-execution-model-b3c332f6ed1
tags: .net asp.net iis windows
categories: [Programming Languages]
title: A Closer Look At ASP.NET Core Execution Model
mermaid: true
---
It is very important to know what process hosts your web application when it is running on IIS, as often you need to attach to that process, or troubleshoot issues related to process model.
<!--more-->

However, Microsoft does not yet seem to have a diagram for ASP.NET Core, so I created my own,

```mermaid
flowchart LR
    IN([Incoming HTTP Request])

    subgraph W[w3wp.exe]
        direction LR
        MOD[[ASP.NET Core Module]]
    end

    subgraph D[dotnet.exe]
        direction LR
        CORE[[ASP.NET Core]]
    end

    IN --> MOD --> CORE

    classDef node fill:#ffffff,stroke:#111,stroke-width:2px;
    class IN,MOD,CORE node;
    style W fill:#d9ecff,stroke:#111,stroke-width:1.5px;
    style D fill:#e4d4f1,stroke:#111,stroke-width:1.5px;
```
_Figure 1: ASP.NET Core process model (1.x and 2.0/2.1)_

If you recall Microsoft's recommendation on setting up ASP.NET Core apps on IIS, you should immediately know the `w3wp.exe` part.

1. The application pool does not have ASP.NET configured, so the worker process `w3wp.exe` will not load ASP.NET runtime.
1. The `web.config` file contains the settings of ASP.NET Core module, so `w3wp.exe` loads the module and prepare the environment to host ASP.NET Core apps.

Noticeably, `w3wp.exe` does not execute any of your code, because it serves as the reverse proxy.

Incoming HTTP requests would be delegated to the actual Kestrel web server process, where the responses are generated.

1. The process name would be `dotnet.exe` for framework dependent deployment, while it would match your application name if you use self contained deployment.
1. Kestrel process is not created if there is no incoming request. The creation when the first request comes might take a while based on the actual initialization it needs to perform.
1. Kestrel web server can run on .NET Core or .NET Framework, based on your project configuration.

> Note that ASP.NET Core on .NET Framework uses the same process model like ASP.NET Core on .NET Core, and that's significantly different from ASP.NET 4.x.

If you want to attach a debugger to Kestrel web server process, sometimes you could not see the process, because ASP.NET Core module won't initialize one if there is no incoming request.

The process model also applies to IIS Express.

When troubleshooting issues, you can always run Kestrel web server alone to see if the issue is within Kestrel or your own code.

> Note that ASP.NET Core 2.x started to introduce the in-process hosting mode, which is similar to ASP.NET 4.x on IIS, which is not covered by this post.
> You can learn more about in-process hosting mode from [this article](https://docs.microsoft.com/aspnet/core/host-and-deploy/iis/in-process-hosting).
