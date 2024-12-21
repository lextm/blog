---
layout: post
title: "SharpDevelop的AStyle插件"
description: "这篇文章介绍了 SharpDevelop 的 AStyle 插件。"
tags: .NET SharpDevelop
permalink: /sharpdevelop的astyle插件-6f3b56044526
excerpt_separator: <!--more-->
---
(CSDN Sept 15, 2006)

原本还是偶而用一下SharpDevelop，这东西生成C#代码注释绝对是一流，BDS根本没有这样好的支持。另外，BDS解析工程间依赖的能力太弱，真的需要Build all的时候，慢的出奇，SD却没有这个问题。

当SharpDevelop2.0还在Beta时，我一时狠心，就把CBC的BDS工程全部导出，改用SD来维护CBC了（当然，SD也不是完美无缺，做.NET1.1开发时，似乎不能很好的处理窗体的资源文件，这越来越成为一个大麻烦，但是.NET2.0项目则没有这个问题）。

SD有一个自动美化代码缩进的功能，类似于AStyle，但是绝对还没有达到AStyle的水平。我也一直打算写一个相关的插件，只是缺少资料罢了。当我终于在CodeProject上面看到了一篇介绍SD AddIn开发的文章之后，似乎就再也按捺不住了。
<!--more-->

开发过程十分简单，有点出乎意料。Beta 1版本依然使用的是CBC5.1里面呼叫AStyle的方法，让AStyle后台美化代码，然后重载入IDE。这样做的问题是无法很好的重载，SD总是提示用户需要手工在重载一次。

这时我就把Beta1贴到了SD的论坛上面。很快，Daniel Grunwald提醒我，应该把IDE里面的缓存Buffer存为临时文件，然后美化，再将这个文件读回缓存。这样还可以利用IDE现有的Undo服务。这自然使我十分需要的（关注CBC的人应该都知道我很早就想把Undo实现）。所以，当天我就完成了Beta2。

Beta2完成的时候，我顺便升级了CBC，让CBC的用户也可以享受到一样的Undo支持。可是，CBC的Undo确实可用了，但SD的Undo支持还有问题。想当然的，我认为是SD的bug，也就做了报告。

Matt Ward的回复才最终解决了这个问题。可以说，SD的架构还是有点小瑕疵。虽然Daniel的方案可以很好的载入美化后的代码，但是无法修改IDE的Undo Stack。Matt给出了另外一种方案。很快，Beta3出来了。

令人意外的是，自从Beta2出来之后，这个还在Beta阶段的工具的下载量就开始大大增加（一周就超过了90），远远超出了我的预计。自然，我会继续开发下去，让它和CBC分享不少代码。毕竟，这是一个比较有用的东西呢。
