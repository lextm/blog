---
layout: post
title: "Experimental Support for recycleOnFileChange in HttpPlatformHandler v2"
description: "Discover how the recycleOnFileChange feature—critical for automating process restarts in Node.js, Python, Java, and Go web apps hosted on IIS—was reintroduced in HttpPlatformHandler v2 after user feedback. Learn about the historical connection to ASP.NET Core Module, why this feature matters for non-.NET apps, and how GitHub Copilot accelerated the C++ implementation."
tags: httpplatformhandler iis nodejs recycleOnFileChange windows
categories: [Tools and Platforms]
excerpt_separator: <!--more-->
---

If you host Node.js, Python, Java, or Go web applications on IIS using HttpPlatformHandler, you may have encountered the need to automatically restart your backend process when deploying new code or updating configuration files. The `recycleOnFileChange` setting in `web.config` was designed for this purpose, but recent user feedback revealed it was not working as expected in HttpPlatformHandler v2. This post explores the technical and historical reasons behind this, and how the feature was brought back with the help of GitHub Copilot.

<!--more-->

## The Forked Legacy: HttpPlatformHandler and ASP.NET Core Module

The story of `recycleOnFileChange` is deeply tied to the history of HttpPlatformHandler and its relationship with the ASP.NET Core Module (ANCM). Microsoft never released the source code for the original HttpPlatformHandler v1.x, but when they began work on ASP.NET Core, they needed a native IIS module to host .NET Core applications. Instead of starting from scratch, Microsoft forked the internal codebase of HttpPlatformHandler to create the ASP.NET Core Module. This fork inherited much of the original logic, including support for features like `recycleOnFileChange`—at least in the configuration schema.

When I received the user report about `recycleOnFileChange` not working in HttpPlatformHandler v2, I traced the implementation back to the [ASP.NET Core module source](https://github.com/aspnet/AspNetCoreModule/blob/dff0db80ca2092f1f6e6dbcd327d4e8d83075729/src/AspNetCore/Src/aspnetcoreconfig.cxx#L386). There, I found proof that Microsoft had explicitly disabled this feature in early versions of the module. The reason for this, as discussed in [dotnet/AspNetCore.Docs#1990](https://github.com/dotnet/AspNetCore.Docs/issues/1990), is that while the configuration schema still includes `recycleOnFileChange` for compatibility, it is ignored at runtime. This background explains why the setting appears to be supported but has no effect in both ASP.NET Core Module and HttpPlatformHandler v2. This confirmed that the two modules share a common ancestry and that the behavior was inherited, not coincidental.

For those who relied on this feature, the only workaround was to downgrade to v1.x, which still supported `recycleOnFileChange`.

### A Migrating Codebase

It's also worth noting that the source code for the ASP.NET Core Module (ANCM) has migrated across three locations over its history:
1. It started as an internal fork of the original (closed-source) HttpPlatformHandler.
2. It was then open-sourced in the [aspnet/AspNetCoreModule](https://github.com/aspnet/AspNetCoreModule) repository.
3. Later, the code was moved to the [IISIntegration](https://github.com/aspnet/IISIntegration) project, and finally integrated into the [dotnet/aspnetcore](https://github.com/dotnet/aspnetcore) monorepo.

This migration history is important for anyone researching or maintaining IIS modules, as relevant code and documentation may be found in any of these locations depending on the timeframe.

## Why recycleOnFileChange Matters for HttpPlatformHandler Apps

For web applications hosted via HttpPlatformHandler—such as Node.js, Python, Java, or Go apps running behind IIS—`recycleOnFileChange` is a practical tool for automating process restarts when important files change. Unlike ASP.NET Core apps, which have built-in file watchers and hot reload mechanisms, these non-.NET apps rely on IIS only for process management and proxying. IIS does not monitor source code or configuration changes by default.

In real-world scenarios, `recycleOnFileChange` is useful for:
- Automatically restarting the backend process when deploying new application code (e.g., updating `app.js`, `server.py`, or a JAR file)
- Restarting when configuration files change (e.g., `config.json`, `.env`, or `web.config`)
- Ensuring updates to static assets or templates that require a process restart are picked up

**Examples:**
- Deploying a new version of a Node.js app: If `app.js` or `package.json` is updated, the process restarts automatically, loading the new code.
- Updating a Python app's `requirements.txt` or settings file: The backend restarts, ensuring new dependencies or settings are active.
- Replacing a Java app's main JAR or properties file: The process is recycled, so the new version runs without manual intervention.

In contrast, ASP.NET Core apps benefit from their own file watching and hot reload features, making this IIS-level feature less critical for them.

## Experimental Support Added

Based on this feedback, I have added experimental support for `recycleOnFileChange` in the latest release ([v9.0.5-rc.1](https://github.com/lextudio/httpplatformhandlerv2/releases/tag/httpplatformhandler_v9.0.5-rc.1)). Implementing this feature in C++ was made much more efficient with the help of GitHub Copilot, which provided code suggestions for file monitoring and process recycling logic, accelerating the development process. Now, when you update a file specified in `<recycleOnFileChange>`, the process should recycle as expected.

If you encounter any issues or have suggestions for improvement, please open a new issue on the [GitHub repository](https://github.com/lextudio/httpplatformhandlerv2/issues).

---

To explore more on this topic, check out all posts tagged [HttpPlatformHandler]({{ site.baseurl }}//tags/httpplatformhandler/).

*This post documents the journey from user report to feature implementation, and highlights the importance of community feedback in open source projects.*
