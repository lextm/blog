---
layout: post
title: "M8主题修改的对决？"
description: "这篇文章是关于 Meizu M8的几个美化工具"
tags: Meizu
permalink: /m8主题修改的对决-50ec3afcddf4
excerpt_separator: <!--more-->
---
终于在发布到2.0版本的时候，Theme Editor的作者majiyunsea回复了我在魅族论坛的帖子。

http://bbs.meizu.com/thread-1216752-2-1.html

当然了，肯定不是砸场子了，哈哈。应该说排除一些”牢骚”，可以看出majiyunsea对于魅族产品缺陷的体会比我要深许多。

我也立即测试了一下深度美化的一些东西，例如替换资源dll的方法，果然ThemeManager在提示重启之后显示界面出现了严重的bug，完全就是显示错误。可以通过在MTH主题包里面嵌入那些资源dll是一个没法完成的任务。这也解释了为什么其他深入美化的帖子要么推荐手工替换，要么采用CAB安装包。看来都是为了绕过这个严重的bug。

因此假如在后面的版本中我计划添加深入美化的支持，看来直接生成CAB文件是个必然的选择。我会仔细研究一下CAB的格式，看看是不是那里也有bug在等待着我。

关于M8新UI，乃至于Android版本的固件，我其实抱着一个很悲观的态度。毕竟后面的版本很可能会使得M8 Theme Builder需要重新设计，但是使用C#和.NET平台的好处就是我开发起来几乎不费什么力气，所以想要发布一个新版本并不是特别困难的事情。

希望M8 Theme Builder和M8 Theme Editor的竞争可以友好的继续下去。
<!--more-->