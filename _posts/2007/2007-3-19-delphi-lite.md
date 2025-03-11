---
layout: post
title: "Bug Report Reply: Delphi的Lite版本"
description: "这篇文章讲述了所谓的 Delphi 的 Lite 版本。"
tags: Code-Beautifier-Collection Delphi
permalink: /bug-report-reply-delphi的lite版本-58497f576876
excerpt_separator: <!--more-->
---
(CSDN March 19, 2007)

这也是我第二次听说有Delphi Lite版的用户尝试使用CBC。
<!--more-->

> 我使用delphi 10 lite v3便携版，并已经打好对应的update2补丁。安装好CBC以后不能运行，告诉我
>
> "应用程序正常初始化（0x0000135）失败"，不能使用。
>
> 不过，我使用cnPack就没有问题。
>
> 还有，我已经安装好了jcf，astyle没有安装，是不是因为这个问题？

自然，这个问题我不可能遇到，因为我没有使用过Lite版本，一个非官方的裁剪版本。但是可以猜到为什么CnPack可以而CBC不行――CBC是C#做的。

Lite版本应该是删去了.NET部分的Delphi，没有Together也没有其它的部件，甚至没有Borland.Studio.ToolsAPI.dll这个关键的文件。这样bds.exe在启动的过程中不能正确地初始化.NET环境，也就不能加载CBC的框架。.NET是CBC存在的必要条件。

同样的问题我想Delphi 5/6/7的用户在尝试使用CBC时也会遇到。因此，我认为这不能算是CBC的一个bug，毕竟设计CBC的时候，我就将Galileo IDE也就是BDS 1.0–4.0（Delphi 2007应该是5.0）考虑在内。

我能给出的建议就是请使用Borland CodeGear官方发布的Delphi IDE，Delphi 8–2006都可以使用CBC。不过对Delphi 2007的支持需要在等待一段时间。
