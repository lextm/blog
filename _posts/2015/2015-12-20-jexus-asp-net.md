---
layout: post
title: "Jexus 网站服务器和 ASP.NET 跨平台开发"
description: "这片文章分享了关于 Jexus 和 ASP.NET 跨平台开发的一些个人看法，供有兴趣的朋友们参考。"
tags: Jexus-Manager IIS .NET
permalink: /jexus-网站服务器和-asp-net-跨平台开发-e4cac4316352
excerpt_separator: <!--more-->
---
一周前受衣明志大哥邀请在烟台市他主办的首届胶东开发者大会上与大家分享了关于 Jexus 和 ASP.NET 跨平台开发的一些个人看法。本文内容基本和当日的演讲一致，局部可能补充了一些额外信息，供有兴趣的朋友们参考。
<!--more-->

## 微软的跨平台战略

微软在过去的一年多中时间中发生了令整个 IT 行业感到惊叹的变化。这一切始于 Ballmer 的退位和 Nadella 的决心，更始于早已在微软各个基层部门蠢蠢欲动的二次创业。

以开发工具团队来说，他们很早就开源了 ASP.NET MVC 开发框架，并从那以后连续开源了后续全部新的开发框架，例如 Web API 和 SignalR，例如 OWIN 组件 Katana，并且和开源社区如 Mono 保持着良好的互动。

而其他团队，例如 Hyper-V，则同样与 Linux 内核社区有积极互动。

因此当 Nadella 先生在2014年10月表态 Microsoft Loves Linux 时，长期的微软观察家应该并不会表现出太多惊讶，因为这真的只是个水到渠成的过程。

以 ASP.NET 为例，业界的公司早已或多或少的使用了 Linux 或者基于 Linux 平台的解决方案。因此如果微软提供 ASP.NET 跨平台开发和部署支持，那么此前完全采用 Linux 的公司可以直接在现有平台上部署网站，从而节约购买 Windows 授权的费用。混合使用 Linux 和 Windows 的公司则有机会重新调整平台间的相对规模，达成成本控制目标。

除去公司内部计算平台，在多种主流公有云平台上，采用 Linux 虚拟机为主的解决方案也非常普遍，成本低廉，同时适合各种级别的公司和个人来部署网站应用。

因此只要微软 ASP.NET 技术能够支持跨平台开发部署，那么就能立即进入一个全新的市场领域。

## .NET Core 5 和 ASP.NET 5

为了达成跨平台目标，微软开发工具部门在发布了 .NET 4.5 和 ASP.NET 4.5 之后花了相当长的时间来构架下一代网站开发技术。在这个超过两年的漫长过程中，以下几个目标逐渐清晰，

1. 采用新思路来重新设计框架基础。这方面向 node.js 学习不少。
1. 采用全新技术，主要是 Roslyn。
1. 脱离 .NET Framework 的束缚实现跨平台。

结果就是我们现在已经看到的 ASP.NET 5。

为了使得 ASP.NET 5 运行在新平台上，.NET 团队也借此机会开发了全新的运行环境，也就是 .NET Core 5。

.NET Core 5 完全开源，整个开发过程和全部代码都可以在 GitHub 上面找到。它的 API 参考资料可以在下面找到，

一个明显的变化是很多我们熟悉的 .NET Framework 类型被删除了，例如 System.Security.Cryptography 下面的一些类型，System.Net 下面的 UdpClient 类型和 Socket 类型的同步方法。

在 VS 2015 中新建一个 .NET Core 函数库工程的时候，也有很大变化。首先就是工程类型变成了 .xproj，依赖项管理方式改为通过 project.json 文件指定，而编译结果也换成了 NuGet 包。

ASP.NET 5 方面同样如此，完全开源之外也带来了很大的变化。System.Web 这个古老的部分和 WebForms 一并被删除。今后我们就不再通过 HttpContext 类型访问运行时的各种信息，也不再通过 web.config 文件中的 <system.web> 标签来管理配置项目了。MVC/Web API/SignalR 三个原本独立的框架得以统一为一个开发模型（例如Web API 中的 ApiController 类型现在就和 MVC 的 Controller 类型合二为一）。

在最终应用的部署上，假如 ASP.NET 应用部署在 IIS 和 Windows 上，那么需要额外安装 HttpPlatformHandler。在 Linux 平台上，则首推 nginx 和 Kestrel 搭配的部署方式。

由此我们可以看出微软提供的迁移方式有一个从 ASP.NET 4 到 ASP.NET 5 的迁移步骤。这一个看似简单的步骤其实并不简单。代码的迁移和修改暂时还需要很多手工步骤，部署方式的变化要求 Linux 和 nginx 知识的学习，而之前开发者学习多年的 Windows 和 IIS 知识似乎都过时了。

有没有更加简单的方式让 ASP.NET 应用登陆 Linux 平台呢？

## Mono 和 Jexus 网站服务器

Mono 这个开源项目其实一直伴随着 .NET Framework 成长。Miguel de Icaza 先生早年一直领导着 Gnome 这个开源桌面系统的开发。在2000年微软公布了 C# 语言和 .NET Framework 之后，他非常感兴趣并且希望能把这些新技术带到 Linux 平台，于是一手建立了 Mono 这个项目和社区。现在 Mono 的稳定版本是 4.2.1，得到了 Xamarin 和微软两家公司的共同支持。

和 .NET Core 5 另起炉灶相比，Mono 处处都保持着和 .NET Framework 的兼容性。在微软去年11月完全基于 MIT 协议开放 .NET Framework 参考代码后，Mono 立即开始集成微软的代码（迄今完成超过600多个类型），非常明显的改善了兼容性。不过 Mono 保持了自己独立开发的 CLR 实现和 C# 编译器，有自己的 AOT 运行环境和 C# Shell。在应用程序框架方面，Mono 提供 WinForms 和 WebForms 支持，也包含了微软早已开源的 MVC 5、Web API 2 和 SignalR 2。

在 Mono 这个稳固的基础之上，中国四川的一位微软 C# MVP 刘冰历时多年设计了一款免费的网站服务器，取名 Jexus，最新稳定版本是5.8.0。比较有意思的是，它基本是用 C# 开发，直接通过 Linux 内核的 epoll 机制来处理网站请求，而不是采用 libuv 之类的封装库，所以提供了高性能保证。作为一款跨平台软件，它支持各种主流 Linux 发布版本和 FreeBSD。

视频一：Ubuntu Server 上安装 Jexus

http://v.youku.com/v_show/id_XMTQyMTA1OTA1Ng==.html

从架构等技术特点来看，Jexus 也可以媲美 IIS 等商用服务器。比如它提供了多站点支持，拥有应用程序池来调度管理工作进程，具有良好的稳定性和容错能力。又比如它支持 HTTPS 和 WebSockets，支持 FastCGI 协议和 OWIN 标准。它不仅可以作为一款应用服务器，来托管各种 ASP.NET 4 应用（WebForms、MVC、Web API、SignalR），同样也可以作为一般服务器使用，包含 URL 重写、反向代理、压缩传输等基础功能和 SQL 注入预防等多项内置安全防护。

因为 Jexus 提供了如果便利的迁移方法，所以国内外一些网站已经采用它来作为服务器。在 Jexus 官方网站上有相关的案例可供参考。

视频二：Visual Studio 2013 导出 MVC 5 网站

http://v.youku.com/v_show/id_XMTQyMTA2MDUzMg==.html

视频三：Jexus 上架设 MVC 5 网站

http://v.youku.com/v_show/id_XMTQyMTA2MTUxMg==.html

## Jexus Manager

为了进一步简化 Jexus 的管理，方便熟悉 IIS 的开发者迁移，我在2014–2015这段时间开发了一个可视化的管理工具，名叫 Jexus Manager。

这是一个可以跨平台运行的程序，支持 Jexus，IIS 和 IIS Express 三种服务器的管理，操作方式完全和微软的 IIS Manager 一致。

从技术细节来看，它也和微软 IIS 高度相似，比如提供了 Microsoft.Web.Administration 和 Microsoft.Web.Management 两个 API 接口，实现配置文件的读写和用户界面的扩展。

## Jexus 的未来蓝图

在未来的版本中，Jexus 服务器可能会加入下面的功能：

* 完美支持 web.config 中的 `<system.webServer>`
* 提供 Microsoft.Web.Administration API 给本机其他程序
* 提供 appcmd 命令行管理工具以达到本机和远程管理
* 完整的 ASP.NET 5 支持！
* 提供更多配置选项
* 提供基于 REST 的远程管理 API
* 提供网页版的管理工具
* 可靠的商业技术支持服务

而 Jexus Manager 管理工具则会在2016年分阶段完全开源。

## 参考

* Jexus 官方网站 http://jexus.org
* Jexus 英文资料 https://server.jexusmanager.com
