---
layout: post
title: "如何迁移#SNMP到.NET Core平台的一些体会"
description: "本文介绍了如何迁移#SNMP到.NET Core平台的一些体会"
tags: SNMP .NET
permalink: /如何迁移-snmp到-net-core平台的一些体会-b5e8b56f69da
excerpt_separator: <!--more-->
---
> .NET Core 依然在飞速进化中，所以如果不是非常喜欢折腾的性格，建议各位还是暂时忍耐。

## 准备阶段

首先，Visual Studio 2015是必要的开发工具。虽然它已经包含了.NET Core的原始测试版，这里还是推荐[下载 RC1 安装包](http://get.asp.net/).
<!--more-->

请下载 ASP.NET 5 RC 那个版本。下面都是假设在 Windows 系统上。

执行安装程序，它会进一步下载更多的部件。等到安装完成，就可以进行 .NET Core RC1程序的开发。

下面让我们进一步升级到 RC1 Update 1这个升级版本：

1. 打开 Visual Studio Command Prompt。
1. 执行`dnvm upgrade`命令。
1. 再执行`dnvm list`命令。

如果一切正常，那么这时候输出应该是这样的，
``` batch
$ C:\Program Files (x86)\Microsoft Visual Studio 14.0>dnvm list
Active Version Runtime Architecture Location Alias
1.0.0-rc1-final clr x86 C:\Users\lextm\.dnx\runtimes
1.0.0-rc1-update1 clr x64 C:\Users\lextm\.dnx\runtimes
* 1.0.0-rc1-update1 clr x86 C:\Users\lextm\.dnx\runtimes default
1.0.0-rc1-update1 coreclr x64 C:\Users\lextm\.dnx\runtimes
1.0.0-rc1-update1 coreclr x86 C:\Users\lextm\.dnx\runtimes
```

## 开始迁移

下面可以开启 Visual Studio 2015，并且创建一个类型是 Class Library (Package) 的新工程。这种工程的文件后缀是.xproj。这种工程的编译结果会是一个 NuGet 包。

在往里面加入新东西之前，我们先来研究一下 project.json 文件。
需要注意的是 project.json 是全新的管理依赖项的方式，它既代替了原来管理 NuGet 包的 packages.config，也替代了原来 .csproj 工程文件中管理引用的部分。

[一个范例](https://github.com/lextudio/sharpsnmplib/blob/netcore5/SharpSnmpLib/project.json) 是 #SNMP Library 现在使用的 project.json 文件。

从中我们可以看到，既有用来描述 NuGet 包的各种元数据信息，也包含依赖项。

其中比较主要的部分是它指明了两个平台别名（moniker），一个是 .NET Framework 4.5.1（net451），另一个是 .NET Platform Standard 5.4（dotnet5.4）。

前者有一个基本的引用列表，所以不太需要指明具体库的应用，但是比较特殊的是 System.Runtime.Serialization，所以它是唯一需要写明的一个引用。

而后者怎是一个新的别名，用来标识一个包含完整 API 清单的 .NET 平台。凡是支持这个平台标准5.4版本的 CLR 实现（不限 .NET Framework，Mono 或者 Xamarin)，都可以使用我们编译之后的 NuGet 包。关于平台标准的细节可以阅读[下面的文档](https://github.com/dotnet/corefx/blob/master/Documentation/architecture/net-platform-standard.md)。

不过它已经更新 RC2 的版本，所以版本号已经改为从1.0计算了。

面向平台标准开发的一大困扰就是所有的引用都需要手工指明。而这些引用也最后来自于对应的 NuGet 包。那么怎么寻找这些包和它们的对应版本呢？

简单来说，步骤就是将要迁移的项目代码手工拷贝到新工程里，然后编译。凡是找不到的类型，我们使用微软临时发布的[一个查询网站](http://packagesearch.azurewebsites.net/)来查询包含它的 NuGet 包和版本。这是一个有点费时间的过程，因为

* 有些类型是 RC1不存在的，而且可能也不会出现在 RC2等后续版本。于是需要换变通的方式。
* 有些类型在后续版本中会有，那么需要等待。
* 有些类型仅仅出现在桌面版本的 .NET Framework 中于是需要条件编译。

因为仅仅作为一个测试，所以我在迁移 #SNMP Library 过程中就删去了很多代码。另外由于 Socket 类型的同步方法都被移除，我也不得不将很多 #SNMP Library 的代码改写为 async/await 方式。等微软正式发布 RC2，我会考虑再迁移一部分代码过去。
到此，只要编译通过，那么初步的迁移工作也就结束了。

## 写在最后
还有其他值得注意之处：

* 和 project.json 对应，Visual Studio 会维护一个 project.lock.json 文件。这个文件详细记录了依赖项展开的情况，了解它的结构有利于调试一些依赖项问题。但是不要将它签入到版本控制。
* .xproj 工程不像 .csproj 那样需要明确指示工程包含的源文件，而是默认将同一文件夹下面所有源文件引入。因此有可能迁移过程中需要调整下工程文件的组织。
* 暂时没有特别方便的单元测试集成。后面应该会有。
* dotnet5.x 是个临时的别名，后面都会改成 netstandard1.x。

上面仅仅谈到了迁移过程中最为重要的步骤。一些工具，如 dnvm 由于 RC2 起会被 dotnet 工具取代，所以都没有详细介绍。现在这个阶段，还是浅尝辄止比较经济实惠。

敬请关注后续文章。
