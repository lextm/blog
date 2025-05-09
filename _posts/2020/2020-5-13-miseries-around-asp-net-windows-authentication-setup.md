---
description: Comprehensive guide to ASP.NET Windows authentication setup, explaining common issues, IIS configuration details, and advanced topics for proper implementation.
excerpt_separator: <!--more-->
image:
  alt: Copyright © Lex Li. TELUS Garden Offices in Vancouver.
  path: /images/telus-garden.jpg
layout: post
permalink: /miseries-around-asp-net-windows-authentication-setup-14e2e8522ad2
tags: asp.net iis windows microsoft
categories: [Frameworks and Libraries]
title: Miseries Around ASP.NET Windows Authentication Setup
---
ASP.NET developers should have some IIS knowledge. But how much can be enough to fully understand the concepts of Windows authentication? Well, based on the questions from Stack Overflow, I bet the answer is quite lot. A complex topic like this requires extensive knowledge beyond ASP.NET/IIS, and if you don't fully understand some Windows/AD processes behind the scene puzzles are everywhere. This post might not be able to cover everything, but can leave you hints on what to explore further.

<!--more-->

## ASP.NET Settings

Surprisingly it is simple to set on ASP.NET side that you want to enable Windows authentication, as it is just merely a piece of setting in your `web.config`,

``` xml
<configuration>
 <system.web>
  <authentication mode="Windows"/>
 </system.web>
</configuration>
```

So, as long as IIS gives ASP.NET runtime a valid Windows user, that user's information will be wrapped up and served to properties such as [`Page.User`](https://docs.microsoft.com/dotnet/api/system.web.ui.page.user?view=netframework-4.8), [`Controller.User`](https://docs.microsoft.com/dotnet/api/system.web.mvc.controller.user?view=aspnet-mvc-5.2) and [`ApiController.User`](https://docs.microsoft.com/dotnet/api/system.web.http.apicontroller.user?view=aspnetcore-2.2).

## IIS Settings

OK, now most ASP.NET developers should move on to IIS (or IIS Express), as [the official documentation](https://support.microsoft.com/en-us/help/323176/how-to-implement-windows-authentication-and-authorization-in-asp-net) asks for some changes there.

> Note that the article still points to IIS 5/6. IIS 7 and above needs [a few different steps](https://learn.microsoft.com/iis/configuration/system.webserver/security/authentication/windowsauthentication/#setup) in IIS Manager, but I think you can figure that out.

So finally on IIS, only Windows authentication is enabled in `applicationHost.config`,

``` xml
<configuration>
 <system.webServer>
  <security>
   <authentication>
    <anonymousAuthentication enable="false">
    <windowsAuthentication enable="true">
   </authentication>
  </security>
 </system.webServer>
</configuration>
```

## Other Possibilities

Now let's visit some other scenarios and test your IIS knowledge.

What if we didn't enable Windows authentication on IIS, but use the default settings? Will ASP.NET side break?

> Equivalent to

``` xml
<configuration>
 <system.webServer>
  <security>
   <authentication>
    <anonymousAuthentication enable="true">
    <windowsAuthentication enable="false">
   </authentication>
  </security>
 </system.webServer>
</configuration>
```

You can do your experiment, but probably to your surprise that ASP.NET side still works, but all those `User` properties now show `IUSR` or the application pool identity (or another account that you configured).

That's simply because [IIS anonymous authentication](https://docs.microsoft.com/iis/configuration/system.webserver/security/authentication/anonymousauthentication#how-to-change-anonymous-authentication-credentials-from-the-iusr-account) generates a user token for the anonymous user account, and ASP.NET runtime wraps up that anonymous account instead.

> The logic behind anonymous authentication is that everyone that accesses your site is considered to be using the same account.

## Exercising Your Knowledge

So what happens if we disable all IIS authentication methods and enable digest authentication? I think you've already known the answer, haven't you?

## Advanced Topic - IIS 7+ Integrated Pipeline and More

In certain cases, you need to access the Windows user information outside of pages and controllers,

* Events in `Global.asax` (e.g., `Application_AuthenticateRequest`).
* Custom HTTP modules.

In such cases, options like `HttpContext.Current.User` might be your friend, but you need to be aware of the [IIS integrated pipeline](https://learn.microsoft.com/iis/application-frameworks/building-and-running-aspnet-applications/aspnet-20-breaking-changes-on-iis) and how it affects the user information. In short, since ASP.NET pipeline is now integrated with IIS pipeline, you might see `HttpContext.Current.User` is not set as expected in some early events, as IIS does not yet authenticate the user credentials and the user identity object is not yet initialized or passed on.

## Site Notes

You might also revisit what is impersonation from [my old post]({% post_url 2019/2019-7-1-the-basic-facts-about-iis-asp-net-process-thread-identities %}).
