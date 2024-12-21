---
layout: post
title: "Delphi 的用户们，早点开始享受 MSBuild 吧"
description: 这篇文章介绍了 Delphi 2007 中 MSBuild 的引入对于 Delphi 程序员带来的好处。
tags: Delphi .NET
permalink: /delphi-的用户们-早点开始享受-msbuild-吧-c7ad9f01c446
excerpt_separator: <!--more-->
---
(CSDN Oct 10, 2007)

Delphi 2007 的发布进一步表明了 CodeGear 对于 .NET 的态度――一切为我所用。当然，做到现在的阶段，Delphi 团队也是一步步走来。

首先， Delphi for .NET 所使用的框架 VCL for .NET 重新封装了 CLI 的各个接口，使得 VCL Win32 的代码可以尽可能的迁移到 .NET 平台上。

其次，在 Delphi IDE 中，重构和 Together 都是用 .NET 技术做好然后加入的――当然，后来为了提高执行效率一部分重构用 Delphi 重写了。

现在，Delphi 和 C++Builder 的生成引擎（build engine）换成了 MSBuild，使得 Delphi 同 C# 一样得到了 Windows 平台上最好的生成引擎支持。

关于前面两个改变，相信多数新版 Delphi IDE 的用户已经比较熟悉了，这里就不多做介绍。这里重点要介绍一下 MSBuild 的引入对于 Delphi 程序员究竟带来了哪些好处。
<!--more-->

## 什么是生成引擎

对于长期仅仅使用 IDE 来做开发的初级程序员来说，生成引擎是一个陌生的概念。而对于使用 Console 命令来做开发的高级人员，和生成引擎几乎是天天打交道。从你是不是了解和熟悉生成引擎，大约也就可以看出你的编程境界到了什么阶段。

我所接触的最古老的生成引擎就是make和nmake了，类似的还有gnumake。这些都是为C和C++应用开发的引擎。程序员编写makefile脚本文件，然后make.exe就会自动去调用C编译器和连接器从源代码得到最终的程序。当然，还可以利用脚本让make干些其他工作，例如删除中间文件等等。

不要认为这个用批处理命令也可以实现，因为批处理对于操作系统的依赖性太强。不同的操作系统批处理命令还是差别很大的。makefile脚本作为一个操作系统上面的中间层，提供了通用的命令和语法，所以使得不少Unix到Linux的迁移变得不那么困难了。

## 现在可用的生成引擎

ANT 是 Java 平台的生成引擎标准。Borland 的重心一度集中在 JBuilder，所以 JB 对于各种 Java 规范的支持都很及时，但是这方面 Delphi 却没有一直没有跟上时代的步伐，IDE一直使用着一个封闭的生成引擎。虽然以 ANT 为借鉴，SF 上面开了 WANT 项目，开发出了一个适用于 Delphi 的基本的引擎出来，商业软件如 FinalBuilder 也给予了 Delphi 不错的支持，可是真正能够将这些工具用于生产的项目却是不多――CnPack 使用了 WANT，算是一个很不错的范例了。

比较而言，商业软件 FinalBuilder 做的更加完备，可以做的自定义和扩展都很丰富。而 WANT 的开发一直没有达到一个很成熟的程度，所以我在做早期的CBC时一直都是使用自定义的 NANT 脚本来做 Delphi 项目的生成。

## MSBuild 的诞生

Windows平台的生成引擎过去一直是Borland的make和微软的nmake的战斗。但是这两个都没有办法很好的支持Delphi和后来的.NET。NANT的出现，打破了这个古老的局面。

可是开源的 .NET 工具是一段悲壮的历史。在 .NET 1.x 的时代，多个开源项目曾经在微软的地盘占尽风头，像 NUnit，NDoc 和 NANT。但是在 .NET 2 发布之后，微软以将自己的技术做到了 SDK 中，从根本上取代了 NDoc 和 NANT，NUnit 也是一直得不到微软的支持。

MSBuild 出来的目的首先是为了让微软自己Windows平台上面的各种语言得到一个好的生成引擎。虽然 NANT 好用，可是不在微软自己手里，怕受制于人。NANT 实在是个好东西，对 Mono 的支持很好，长期下去对于微软是个威胁。可是自从 MSBuild 出现，Windows 平台上再使用 NANT 的开发者就不多了。

## Chrome 对于 MSBuild 的支持

Chrome 对于 MSBuild 的支持开始的很早。.NET 2 还在 Beta 阶段时 RemObjects 就很好的利用 MSBuild 引擎设计了 chrome 文件的格式，使得编译 Chrome 项目变得十分简单。可是那时 Delphi 2006 还是基于 .NET 1.1 所以还没有办法使用这个方便的引擎。既然 NANT 不能用了，MSBuild 也是 Delphi 唯一的选择。

## Delphi 使用 MSBuild

当你用 Delphi 2007 打开旧工程时，你会发现不管是 dpr 还是 bdsproj 都不在是真正的工程文件了。现在你需要好好研究的就是 dproj 文件了。这个 XML 文件同 C# 工程文件 csproj 采用了完全一致的格式，只是属性都是针对 dcc 编译器的。所以任何 MSBuild 的扩展，像 MSBuild Community Tasks，都可以用在 Delphi 工程的扩展上面。基于这个引擎，编译前后的动作都可以简单的用XML来定制，使得整个开发过程大大的简化。由于 MSBuild 可以看成是一个可以方便扩展的脚本引擎，所以用得好的话威力可是很大的。

学习 MSBuild 并不是那么困难，就是需要一些合适的指导。下面这个网址就指向一个不错的培训材料，

http://brennan.offwhite.net/blog/2006/11/30/7-steps-to-msbuild/

越早熟悉这个引擎就可以越早提高你的开发效率。因此，早点开始使用吧。
