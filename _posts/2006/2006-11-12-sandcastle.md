---
layout: post
title: "Sandcastle：NDoc的继承人"
description: "这篇文章讲述了 Sandcastle 项目的一些信息。"
tags: .NET
permalink: /sandcastle-ndoc的继承人-fd544ecc3f17
excerpt_separator: <!--more-->
---
(CSDN Nov 12, 2006)

怎么说呢，即使是在没有MS参与的时候，我们还是有很多好的开源项目可用，例如NAnt，NDoc。但是或许就是因为开源的关系，我们从来不考虑赞助一点点资金――当然就我个人的情况，我不知道怎么用我的银行户头把钱汇过去。可是时间一长，这些项目就逐渐的淡出了我们的视线，仅仅停留在古老的版本上面的。也就这个时候，MS才记得要自己搞出一些东西平息程序员的怒火。在这类软件中，首先要说的当然是.NET 2.0自带的MSBuild。但是这里想重点谈的就是Sandcastle。
<!--more-->

## 什么是Sandcastle？

具体的信息在这里可以看到。

在发布VS2005之前，MS内部开发了一个用于生成帮助文档的工具。这就是Sandcastle的前身。但是当时编译一次文档就需要十多个钟头――好家伙，真是够长。当然，后来发布的Sandcastle由于做了很大的优化，就只要30分钟了。（看得出来MS内部的开发流程也是十分Agile的，现有成果，然后才作重构和优化的。）

当然，现在的Sandcastle经历了几个CTP版本的测试已经比较成熟了。

## Sandcastle同NDoc的比较

由于NDoc项目终结了，所以一直没有机会达到.NET 2.0完全支持的地步。另外，NDoc还是MSDN 2003的风格，同VS2005漂亮的样式稍有差距。但是下面这些特点是Sandcastle一直缺乏的。

1. JavaDoc，LaTeX的支持。这个也不知道会不会在后期加入。我特别喜欢的就是LaTeX的支持。NDoc生成的LaTeX文档十分的漂亮。
1. 官方的GUI工具。现在我使用的GUI工具还是Sandcastle Help File Builder（SHFB）。MS官方仅仅提供了全部的命令行工具。
1. 将来似乎会被加入到VSSDK里头，这样想仅仅安装Sandcastle似乎就麻烦了一点。

## 我的选择

今年11月之前我一直使用的是NDoc。很显然，CBC还处于.NET 1.1的平台上面，NDoc的工作就很好了。但是，面临着NDoc没有更新的情况，我迟早也会转入Sandcastle的上面。促使这一个过程加速的重要原因，就是SHFB了。由于这个界面同NDoc别无二致，隐藏了全部细节，十分方便NDoc的用户转到这一新的工具上面。另外，由于该工具还提供十分方便的命令行版本，可以集成到NAnt或者MSBuild脚本中，所以我还不犹豫的将CBC的文档全部放心的交给了它来处理。

现在唯一的希望就是MS可以继续发布独立于某个SDK的Sandcastle才好。免得我每次需要下载很多不需要的东西。
