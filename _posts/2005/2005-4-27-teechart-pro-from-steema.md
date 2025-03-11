---
layout: post
title: 寻找被忽视和低估的TeeChart Pro (from Steema)
description: "本文详细介绍了在 .NET Framework 下使用图表控件 TeeChart Pro 的方法。文章从安装和基本使用开始，深入探讨了其高级功能和实用技巧，包括3D图形、Guntt图的拖拽、坐标显示、公式绘图等。同时，作者分享了他在使用过程中的发现和感受，以及如何在 Delphi 环境下重现这些功能。这是一篇对于希望深入了解和使用 TeeChart Pro 的开发者非常有价值的指南。"
tags: .NET Visual-Studio macOS xUnit
permalink: /寻找被忽视和低估的teechart-pro-from-steema-1b4d255ba814
excerpt_separator: <!--more-->
---
(Originally posted to CSDN on April 28, 2005)

TeeChart Pro用惯了，最近又从网上下了一个有原代码的压缩包，解压以后Recompile.exe一运行就安装完成了。唯一的遗憾是这样的免费东东，一没有附Demos，二没有带帮助，所以一两年来只会画一些简单的图。感觉这个Pro除了比Delphi6/7/2005自带的TChart（那是Steema授权Borland加进去的）多了一个强大的向导之外，没有什么特别之处。

也是最近用Delphi 2005开发WinForms程序,发现那个Component One的东西非常不好用.这一方面是因为习惯了TChart那一套,另一方面Component One用VB.NET开发的这一套控件，着实保持了MS开发一贯的”不好用”原则。接连三天的郁闷之后，一气之下上了Steema的官方站点(steema.com)。很意外的是里面提到了全新的Steema TeeChart Pro for .NET，让人眼前一亮。马上下载了Lite版和Evaluation版。
<!--more-->

让人欣喜的是，虽然这是一套完全用C#写成的控件，使用上面却和原来的VCL版本几乎一样。对于那些热爱TeeCharting的同事而言，这大概是非常好的消息。

不过，这还只是我重新发现TeeChart的开始。

闲来无事，打开开始菜单，看了一下TeeChart for .NET的Feature Demo。所见到的一切让人立即被吸引和征服。

1. 3D的图形非常漂亮，可以任意随鼠标移动而旋转
1. Guntt图可以拖拽
1. 单击图形可以显示出坐标，自动判断点击的位置在不在曲线上面
1. 支持公式绘图，画正弦曲线等等异常方便
1. 有一幅图最好玩，你的鼠标移动中，会看到鼠标和图形中几个点之间的距离被一直跟踪着，程序自动地将鼠标与距离它最近的点连接起来。
1. ……

总之，这是查帮助都看不到的东西！而且每一个演示的所有代码都是已经提供的，而且非常简洁。虽然是C#语言的，但是我很快就用Delphi在Win32，和VCL.NET上面重现了其中的几个。这是自己之前想都不敢想的强大功能。

CSDN的Delphi区最近有很多人提问这样的绘图问题，同时也有一些人对TeeChart抱有疑问，真希望他们可以看看这个Demo，了解TeeChart，使用TeeChart。难得的WinForms，WebForms，CF全能选手。

Added：

2.0 for .NET的版本又多了一个极好的Demo，电子全球地图。呵呵，Steema的那些家伙呀，真是厉害。

Happy TeeCharting！