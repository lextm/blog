---
description: Troubleshooting guide for Microsoft.Web.Administration version conflicts between IIS and IIS Express - learn how to properly reference version 7.0.0.0 vs 7.9.0.0 in your .NET applications
excerpt_separator: <!--more-->
layout: post
tags: .net iis windows microsoft
categories: [Programming Languages]
title: Microsoft.Web.Administration of IIS Express
---
[I blogged]({% post_url 2015/2015-5-29-whats-microsoft-web-administration-and-the-horrible-facts-you-should-know %}) about `Microsoft.Web.Administration` a long while ago, but intentionally I left a small topic aside. However, it remains a misery sometimes painful to developers, so here comes a dedicated post.

<!--more-->

## Version 7.0.0.0 in Global Assembly Cache

If you plan to write a .NET Framework application to consume `Microsoft.Web.Administration` API, you probably notice that Visual Studio resolves that reference to an assembly in GAC,

![img-description](/images/mwa-7.0.0.0.png)
_Figure 1: Microsoft.Web.Administration in full IIS._

This 7.0.0.0 version appears in GAC, as long as you enable full IIS on this Windows machine.

## Version 7.9.0.0 in Global Assembly Cache

The 7.0.0.0 version worked pretty fine for years, but suddenly things started to break. For example, if you don't force the reference in your project file to this specific version `7.0.0.0`, you might find that Visual Studio/MSBuild resolves a version of `7.9.0.0` from GAC instead.

- Where does this version come from?

  Well, it is part of IIS Express installation.

- Does it bring any harm?

  This assembly by default reads/writes the IIS Express configuration file, so your code suddenly behaves differently (not against full IIS any more).

## Solution

Since you probably don't want to uninstall IIS Express (you might need it some day), the remaining option at compile time to resolve the issues is to force your application to use version `7.0.0.0` as reference explicitly.

And then use assembly redirection in `app.config` (or `web.config`) to load only version `7.0.0.0` at runtime.

> But if your web app is being hosted on IIS Express, you might need [further changes](https://stackoverflow.com/a/11558360/11182) to IIS Express specific `aspnet.config`.
