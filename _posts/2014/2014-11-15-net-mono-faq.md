---
description: 关于 .NET 开源和 Mono 项目的常见问题解答，包括两者的关系、微软开源策略的演变、以及 Xamarin 与 Mono 的区别等关键问题的详细解析。
excerpt_separator: <!--more-->
layout: post
permalink: /net-开放源代码和mono相关的常见问题-持续更新中-2e74e039945d
tags: .net mono xamarin open-source
categories: [Frameworks and Libraries]
title: .NET 开放源代码和Mono相关的常见问题（持续更新中）
---
## Q1: Mono 已死

我：Mono 历经十余年发展，已经成长为一个庞大的生态系统。.NET Framework 和 Mono 的交集仅限于 CLR/编译器/BCL 底层以及 Web 栈。.NET Framework 的上层为 Windows 和 Azure 设计。Mono 上层针对 Linux, OS X 等多平台设计，其中不可替代的东西很多(虽然很多被 Xamarin 拿去做了商业化产品，如Xamarin.Mac)。

在开放.NET Framework 核心源代码之后，微软当然可以把 Mono 里面它需要的部分合并进去，不违反 Mono 的开源协议。但从它现阶段承诺跨平台技术支持的范围（server/web）来说，像 GTK# 这种桌面栈以及其他类似的 Mono 组件明显不在它的兴趣之内。这些栈未来的发展（例如 GTK4 的支持）未来依然需要在 Mono 社区的基础上来做。

至于将来微软如何和 Mono 社区(包括 Xamarin)互动，我们可以参考历史。在微软还不那么开放的情况下双方都能合作推出 Moonlight 那样的产品，现在只可能更加方便。

即使将来你在 Linux 和 OS X 上面可以安装微软官方的 .NET Framework，Mono 也会是一个替代选项。这个类似甲骨文的 JRE/JDK 和 OpenJDK 的关系。

## Q2: 微软应该公开WPF/WCF/WinForms/XX的全部源代码

我：对于一个企业开放自己项目的源代码，有些困难是一般开发人员难以想象的，

代码中包含不适合公开的机密信息（例如底层操作系统的私有接口等等）
代码中包含不能公开的其他公司信息（例如第三方代码或者函数库）
公司内部开发流程的修改
与外部贡献者的法律关系和合作开发模式
对于 WPF/WCF/WinForms 这样的 UI 和通信框架，微软使用了大量的原生API和极其复杂的内部设计。在现在这个阶段公开，似乎时机并不成熟，而且也似乎并不会像开发其他部分一样立马带来跨平台部署的优势。

WPF 和 WinForms 在其他平台上有 GTK# 或者MonoMac 这样更好的原生替代品，而 WCF 应用可以考虑迁移到早已开源的 ASP.NET Web API。

## Q3: 微软07年就已经开放了源代码啊

我：OSI 作为全球开放源代码运动的核心组织定义了一套详细并且符合知识产权保护法律的协议规定体系。只有采用经过 OSI 认证的开放源代码协议发布的源代码，才是真正“开放”的源代码。对于法律、知识产权了解不多的朋友可以自行登录opensource.org学习。

如大事记所列，2007年微软仅仅是基于自己的“参考协议”公开了部分源代码，既不能编译成完整的函数库使用，也实际上不允许类似的代码使用。对于 Mono 项目的代码贡献者来说，这反而是个负担。为了避免出现可能的版权纠纷，仔细阅读和研究过微软代码的人是不能够给 Mono 捐献核心代码的（所以笔者还真就没有研究过，日后也终于给 Mono 捐了点代码）。

2014年十一月微软的公告，则是彻底的基于 OSI 认证的 MIT 协议公开了 .NET Framework 的核心代码，并且提供了免费的专利授权。这使得 Mono 可以拿来就用，更好的繁荣 .NET/Mono 这两个庞大的生态系统。

## Q4: Xamarin 和 Mono 是一回事

我：这是一个明显的错误。

我们从大事记中可以看到的是 Xamarin 在努力的保持界线，例如将 MonoTouch 等产品重命名为 Xamarin.XX。最终的结果是，所有使用 Xamarin 字样的产品，都是收费的产品，不公开源代码，可以明显区别于开源的 Mono。

的确很多 Xamarin 公司员工同时是 Mono 项目的主要代码捐献者，但同时我们可以看到 Mono 项目的实际捐赠者非常多（包括基于 Mono 开发上层应用的个人和公司），他们并不都来自于 Xamarin，甚至很多都不是 Xamarin 产品的用户。

这个非常类似 IBM 运营 Eclipse 基金会的方式，Eclipse 开源，但是 IBM 当时基于 Eclipse 的产品例如 Rational XDE 之类可是地道的收费软件。
<!--more-->