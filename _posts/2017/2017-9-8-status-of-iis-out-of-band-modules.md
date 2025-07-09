---
layout: post
title: Status of IIS Out-Of-Band Modules
description: This post is about the status of IIS out-of-band modules, such as ARR, URL Rewrite, HttpPlatformHandler, IIS CORS, and ASP.NET Core.
tags: IIS
permalink: /status-of-iis-out-of-band-modules-80a3af57c489
excerpt_separator: <!--more-->
---
When Microsoft designed and shipped IIS 7, they decided to provide a few more extensions to IIS users for free. And those were called out-of-band modules.
<!--more-->

The last important post from Microsoft on them is [this one](https://blogs.iis.net/iisoobs/updates-released-for-arr-url-rewrite-and-httpplatformhandler-including-windows-10-support), so you notice a few facts,

## OOB Modules for IIS 10 on Windows 10/Windows Server 2016 (And Above)

Only a selected set has been upgraded,

* ARR 3.0
* URL Rewrite module 2.0
* HttpPlatformHandler 1.0 (you can learn more from about it from [this post]({% post_url 2023/2023-4-7-the-rough-history-of-iis-httpplatformhandler %}))
* IIS CORS module 1.0
* ASP.NET Core module (1.x/2.x, part of .NET Core/.NET)

## Other Modules

So you might wonder what happens to other modules. Simply speaking, they are deprecated for IIS 10 and above, and you cannot use them. However, they remain fully supported on IIS 7.x and 8.x.

> Note that they have been removed from Microsoft Download Center, so you can no longer get them from Microsoft. Be careful if you try to download from a third party.
>
> Forget about all other posts that tell you via registry hack how to install them.

The common issues are,

* Installer failure. (Again, don't attempt to fool the installers, as you are in fact fooling yourself.)
* Runtime crashes of IIS worker process (w3wp.exe) due to such modules.
* Other functionality related issues.

Then how to address the need of such modules if you really cannot get rid of them right now?

1. Find a Windows Server 2012 R2 machine, and use such modules on IIS 8.5. Its lifecycle would end on October 10, 2023, so you still have a few years left.
1. Find alternative modules/tools from third party vendors. As most modules are simple, alternatives are not that hard to find.
1. Develop your own if no other vendor can be found. The extensibility of IIS means you can help yourself as last resort.

## Alternatives for Some Modules

* IIS Media Services and Transform Manager users should check out Azure Media Services. The cloud services are huge upgrade of what IIS offers, and should be considered a great opportunity to host your media files and enable a variety of other features.
* FTP 7.5 has become the built-in FTP services for IIS since IIS 7.5.
* Advanced Logging has some features (custom logging) ported back as part of IIS default logging. However, its other features are no longer available. If you need those missing ones, it is very likely that you have to develop your own IIS extension. IIS 8.5 and above has [Enhanced Logging](https://docs.microsoft.com/iis/get-started/whats-new-in-iis-85/enhanced-logging-for-iis85) which covers most if not all features of Advanced Logging.
* Search Engine Optimization Toolkit users should fall back to manual management of related assets/files, while using other SEO services (like Google/Bing's online tools) for analysis and reports.
* Database Manager users should switch back to general tools, such as SQL Server Management Studio, or the new cross platform SQL Server Operations Studio.
* Web Farm Framework users should consider Azure Stack for private cloud usage. If you insist on running a classic web farm for IIS 10, there isn't anything similar offered by Microsoft right now.

## Extra Note on Windows ARM64

| Module | Comments            |
|--------|---------------------|
| ARR | You can only use it with x86/x64 application pools. ARM64 application pools will crash. |
| CORS module | You can only use it with x86/x64 application pools. ARM64 application pools will crash. |
| URL Rewrite module | * Microsoft installer: You can only use it with x86/x64 application pools. ARM64 application pools will crash. <br>* Possible to resolve this by extracting the right bits from IIS Express ARM64 but no one did that. |
| HttpPlatformHandler | * Microsoft installer: You can only use it with x86/x64 application pools. ARM64 application pools will crash. <br>* Open source HttpPlatformHandler v2: Refer to [this post]({% post_url 2024/2024-4-8-httpplatformhandler-v2 %}) to install the this. |
| ASP.NET Core module | * Microsoft installer: You can only use it with ARM64 application pools. x86/x64 application pools will crash. <br>* LeXtudio patch: Refer to [this post]({% post_url 2023/2023-3-31-successful-and-failed-attempt-my-first-pull-request-for-asp-net-core %}) to patch ASP.NET Core module on Windows ARM64. |

More would be added here if I find out. You can also leave a comment with your questions or suggestions.
