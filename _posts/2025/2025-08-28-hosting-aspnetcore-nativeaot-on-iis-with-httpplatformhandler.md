---
layout: post
title: "Running ASP.NET Core NativeAOT Web Apps on IIS with HttpPlatformHandler"
description: "Step-by-step guide to run ASP.NET Core NativeAOT apps behind IIS using HttpPlatformHandler, including web.config, publish commands, and troubleshooting tips."
tags: iis httpplatformhandler windows .net
categories: [Tools and Platforms]
excerpt_separator: <!--more-->
---

ASP.NET Core NativeAOT produces a single native executable with fast startup and no .NET runtime dependency, but it does not work with ASP.NET Core module in-process hosting mode. If you prefer IIS to serve traffic, you can use out-of-process hosting mode, or simply HttpPlatformHandler for your NativeAOT app. This post shows the architecture, the exact `web.config` to use, how to publish, and how to troubleshoot.

You can refer to Microsoft’s tutorial on Native AOT ([Native AOT deployment](https://learn.microsoft.com/aspnet/core/fundamentals/native-aot?view=aspnetcore-9.0)) for information on what application types are compatible.
<!--more-->

## Prerequisites

To follow this post, you need to have the following software installed,

* Windows 10 or Windows Server 2016 or later (IIS 10+)
* HttpPlatformHandler v1.2 (from Microsoft) or [v2.0 (from LeXtudio)]({% post_url 2024/2024-4-8-httpplatformhandler-v2 %})
* .NET 9 SDK or later

## Basic ASP.NET Core Native AOT Setup

First, use `dotnet new webapiaot` to create a new ASP.NET Core Web API project with Native AOT support.

``` shell
$ cd C:\
$ mkdir MyNativeAotApp
$ cd MyNativeAotApp
$ dotnet new webapiaot
$ dotnet publish
```

The compilation will take a while to finish, because Native AOT tools compile the app into a single native executable.

My final artifacts are located in the `bin\Release\net9.0\win-arm64\publish` folder, because I am using .NET 9 on Windows ARM64.

``` shell
$ cd C:\MyNativeAotApp\bin\Release\net9.0\win-arm64\publish
$ MyNativeAotApp.exe
info: Microsoft.Hosting.Lifetime[14]
      Now listening on: http://localhost:5000
info: Microsoft.Hosting.Lifetime[0]
      Application started. Press Ctrl+C to shut down.
info: Microsoft.Hosting.Lifetime[0]
      Hosting environment: Production
info: Microsoft.Hosting.Lifetime[0]
      Content root path: C:\MyNativeAotApp\bin\Release\net9.0\win-arm64\publish
```

The app listens on `http://localhost:5000` by default. You can change the port by setting the `ASPNETCORE_URLS` environment variable or configuring Kestrel in code.

## HttpPlatformHandler Setup

So similar to our setup for other web stacks, we will create a `web.config` file in the `publish` folder to configure HttpPlatformHandler,

``` xml
<?xml version="1.0" encoding="utf-8"?>
<configuration>
  <system.webServer>
    <handlers>
      <add name="httpPlatformHandler" path="*" verb="*" modules="httpPlatformHandler" resourceType="Unspecified" />
    </handlers>
    <httpPlatform processPath=".\MyNativeAotApp.exe" arguments="" stdoutLogEnabled="true" stdoutLogFile=".\logs\stdout.log">
      <environmentVariables>
        <environmentVariable name="ASPNETCORE_URLS" value="http://localhost:%HTTP_PLATFORM_PORT%" />
      </environmentVariables>
    </httpPlatform>
  </system.webServer>
</configuration>
```

Now we go to IIS Manager and create a new site or application pointing to the `publish` folder with a site binding on localhost port 8014. Then you can browse this site and test out the Web API.

``` shell
$ curl http://localhost:8014/todos
[{"id":1,"title":"Walk the dog","dueBy":null,"isComplete":false},{"id":2,"title":"Do the dishes","dueBy":"2025-08-28","isComplete":false},{"id":3,"title":"Do the laundry","dueBy":"2025-08-29","isComplete":false},{"id":4,"title":"Clean the bathroom","dueBy":null,"isComplete":false},{"id":5,"title":"Clean the car","dueBy":"2025-08-30","isComplete":false}]
```

## Troubleshooting

There are a few simple steps skipped above, so make sure you are familiar with IIS basics to resolve the common issues.

## Other Languages on IIS?

If you want to learn more about HttpPlatformHandler and how to host other languages (Go/Python/Java) or frameworks (Next.js/Nuxt.js), you can read [this post]({% post_url 2023/2023-4-7-the-rough-history-of-iis-httpplatformhandler %}).

## Related HttpPlatformHandler Articles

> This article is part of a series on using HttpPlatformHandler with IIS. To explore all related articles, please visit the [httpplatformhandler tag page]({{ site.baseurl }}/tags/httpplatformhandler/) for the complete collection of guides and tutorials.
