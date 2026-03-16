---
description: "Discover the history behind the misleading 'WebSockets is unsupported' error in ASP.NET applications and learn how to properly configure your web.config file to enable WebSocket functionality, even in newer .NET Framework versions."
image:
  path: /images/rainy-day-union-station.jpg
  alt: Copyright © Lex Li. Rainy day at Union Station, Toronto.
excerpt_separator: <!--more-->
layout: post
tags: asp.net iis windows
categories: [Frameworks and Libraries]
title: "The History Behind 'WebSockets is Unsupported' Error in ASP.NET"
---
Two weeks ago [I was answering a question on Stack Overflow](https://stackoverflow.com/questions/79030952/asp-net-4-8-exception-message-websockets-is-unsupported-in-the-current-applica/79041024#79041024) and noticed that the question was not the first time someone encountered the error message "WebSockets is unsupported in the current application configuration." Even [when this was reported to Microsoft developers via GitHub in 2016](https://github.com/SignalR/SignalR/issues/3699), no one investigated it further. So, I decided to dig deeper, and figured out some interesting history behind this error message.
<!--more-->

## The Error Message

It should be very rare that you see this error message in your ASP.NET application. The error message is,

``` text
Exception information: 
    Exception type: InvalidOperationException 
    Exception message: WebSockets is unsupported in the current application configuration. To enable this, set the following configuration switch in Web.config:

<system.web>
  <httpRuntime targetFramework="4.5" />
</system.web>
```
People might be confused by the error message, as it suggests that you should set the `targetFramework` attribute to `4.5` in the `<httpRuntime>` element, even when you are using .NET 4.8. Why the hint in that the error message is not accurate?

## The History

ASP.NET 4.5 was a significant release, as it introduced a lot of new features, including the support for WebSockets. In a similar time frame, Microsoft also introduced WebSocket support in IIS 8.0. Therefore, if you are a long time ASP.NET developer, you have a lot to catch up with.

Things got more complicated if you ever use compatibility mode in your application. The compatibility mode is a feature that allows you to run your application in a lower version of the .NET Framework, even when you are using a higher version. This is useful when you have a legacy application that you cannot upgrade to the latest version of the .NET Framework. For example,

``` xml
<system.web>
  <httpRuntime targetFramework="4.0" />
  <compilation targetFramework="4.0" />
</system.web>
```

This configuration tells ASP.NET to run your application in .NET 4.0 mode, even when you are using .NET 4.5 (or a newer version like 4.8). This is a common practice in many enterprises, as they have a lot of legacy applications that cannot be upgraded easily.

Therefore, when you try to use WebSockets in your application, ASP.NET will check the `targetFramework` attribute in the `<httpRuntime>` element. If it is not set to `4.5`, it will throw the error message "WebSockets is unsupported in the current application configuration." While this might be clear to developers who migrated to .NET Framework 4.5 a long time ago, it is not so clear to developers who are new to ASP.NET and start with .NET Framework 4.6 and above.

## Solution

Well, the solution is simple.

You might just set the `targetFramework` attribute to `4.5` in the `<httpRuntime>` element in your `Web.config` file. For example,

``` xml
<system.web>
  <httpRuntime targetFramework="4.5" />
  <compilation targetFramework="4.5" />
</system.web>
```

But wait, if you are using .NET Framework 4.6 and above, you should set it to the exact version instead.

``` xml
<system.web>
  <httpRuntime targetFramework="4.6" />
  <compilation targetFramework="4.6" />
</system.web>
```

This should solve the error message, and you can continue to use WebSockets in your ASP.NET application.

## Side Notes

Should Microsoft update the error message to reflect the current version of the .NET Framework? I think so. But it is not a big deal as long as someone can figure out the solution quickly. And now you know the history behind this error message.

Well, GitHub search pointed out that [this issue was first reported and resolved in 2013](https://github.com/SignalR/SignalR/issues/1315). The lesser frequent an issue is, the more likely it will be forgotten.
