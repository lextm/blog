---
layout: post
title: "SUN技术日的见闻-06.12.06"
description: "这篇文章讲述了我参加 SUN 技术日的见闻。"
tags: Java
permalink: /sun技术日的见闻-06-12-06-e6815979f036
excerpt_separator: <!--more-->
---
(CSDN Dec 06, 2006)

SUN是一间让人敬仰的公司，因此得知其将在武汉作两站技术日的活动。因此今天特意前往湖滨花园酒店，参与了第一天的活动。我匆匆赶到时，其实活动已经开始了。我的号牌十分有意思，全部是2。
<!--more-->

没有坐到前排是一大失算，因为后来发了很多礼品都是前排的同志们得了。

第一场讲座就算是一个大大的SUN广告了，着重讲的是多年以来SUN主导的创新。Solaris和Java自然是首当其冲。不过由于是提问环节，又有奖品，所以我们自然是搜肠刮肚。不过，很奇怪的是几个回答的人居然都没有说到OpenOffice和StarOffice。呵呵，看得出武汉这边用MS Office的实在是主流。可是大家没有注意，整个活动所有的讲稿都不是用的PowerPoint，呵呵，全是StarOffice哟。我个人十分感兴趣的是其中介绍的关于SPARC CPU架构的一点内容，RFID，以及Smart-Dust技术。

接下来是关于Solaris 10的内容。我个人自然不是十分感冒。我已经很习惯于使用Ubuntu之后，就逐渐失去了对其他OS的好感。毕竟我们一般的开发人员很少去考虑OS级别的东西。不过呢，看得出来，SUN一直嘲笑MS不会做OS还是有些道理。比如DTrace之类的调试技术真的很好看和实用，同时不用付钱就可以安装，又有很好的虚拟技术支持，像Xen 3。我现在还感到疑惑的就是ZFS这个东西了，粗听起来倒和WinFS有点类似。

上午最令我印象深刻的自然是Java Persistence APIs的一讲。本来我一直在看Martin Fowler的Patterns of Enterprise Application Architecture一书，很多持久化的东西看起来很麻烦。如果Martin现在写这本书，似乎使用了Annotation之后会好懂很多。O/R Mapping本来技术林立，现在有了SUN主导的JPA上阵，终于一统天下。感觉JPA很多内容都是十分类似于Borland的ECO，不过更加简化和自然――这自然是为了写代码方便，可是做ECO几乎不需要写代码，RAD的风格一如既往，所以自动生成的代码显得麻烦似乎也不是问题。利用已有的ECO经验，我发现理解起来JPA十分容易。比如Persistence Context，几乎就和EcoSpace是一个含义。

吃午饭十分混乱，当然，今天的人也太多。

赶回大堂的时候已经一点，所以就接着听JDK 5/6新特性的一讲。JDK 5是同.NET 2.0决战的一场，所以我之前的了解已经不少。Java的Generics距离C++/C#还有不小的距离，所以这里列出来似乎只能糊弄没有细心学过C++/C#的部分人。而Annotation看起来就是C#从1.0就支持的属性这个特性。反正JDK 5除去JPA之外很多改进都来自于.NET的压力。至于JDK 6的一些新特性我个人认为不是那么大众化，所以我也不知很想一一列举――我也不是很懂。

最后的一讲是NetBeans。我一直使用Eclipse，所以对于NetBeans只是知道而已。看起来也是一个不错的IDE了，比之SUN最初贡献的几个超级搞笑的IDE还是强劲了不少。关于这些特性我自然不想一一列举，但是我必须指出的是做讲演的那位SUN雇员似乎对于Eclipse和JBuilder的最新动态了解太少。

首先，NetBeans以Ant脚本作为Project文件自然是不错，可是Eclipse那样采用Metadata的做法也不是错误。再者JBuilder 2007现在是基于Eclipse的，那么两者之间肯定是使用的同样的Project结构。在这个问题上面，显示出他并不了解JBuilder 2007。

其次，NetBeans在代码编辑器上面确实有不错的特性，不过即时显示JavaDoc也不是什么很了不起的东西，赶MS的VS即时显示帮助标题的技术还差得远啦。智能提示错误和改进方案也很不错，但是我还有很多疑问，关于很多情况下的提示质量如何还有待考察，仅是现场演示的几个还不能令我信服。再一个不足是很多设置，像Code Template，都需要打开额外的对话框，而不是像Delphi 2006那样直接在IDE面板上面做，显得麻烦。

再者，Swing窗体设计器上面用于控件定位的提示看得出来同.NET 2.0做出的效果几乎一样，也算是大家扯平。”VB和Delphi没有这样的特性”，这句实在有错。VB 6自然没有这个，可是VB.NET现在肯定有，而Delphi自从Delphi 2006开始就完全支持这一特性，并且是在VCL for Win32以及VCL for .NET 1.1上面都作了出来。

最后是移动开发的向导和设计器。这个确实是SUN强过其他IDE的一个重要特性。我还没有在JBuilder中看见。

不过，JBuilder 2007页有很多东西是NetBeans一时无法做出的――TeamInsight肯定不会比NetBeans的Collaboration差，而EJB 3/SOA的RAD工具似乎NetBeans里面没有对应的东西。还有就是由开源项目Continuum，Maven，Subversion，XPlanner和Bugzilla做成的全新ALM线为基础做成的ProjectAssist不论对于个体软件过程还是团队协作都肯定是一流的支持。现在不是就有很多Delphi用户强烈要求Delphi 2007支持SVN和Bugzilla？呵呵，希望能有呀。

得到了印有Duke的漂亮T恤，还得到了两张光盘，呵呵，很满足了。至于Duke玩具和iPod Shuffle就不是我个人的运气可以帮我拿到了。等待下一次的运气吧。

当然，如果你和我一样更加关注JBuilder，那么这里有关于JBuilder 2007的一点资料。
