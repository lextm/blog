---
layout: post
title: Pascal for .NET――有趣的生物圈
description: 介绍了用 Pascal 语言开发 .NET 程序的一些工具和它们的有趣故事。
tags: Code-Beautifier-Collection Delphi
permalink: /pascal-for-net-有趣的生物圈-8b16b7bca899
excerpt_separator: <!--more-->
---
(Originally posted to CSDN on Nov 01, 2005)

## Anders的雄心――大鱼是Microsoft

1996年，Anders Hejlsberg从Borland出走到了Microsoft。从VJ++开始，Anders就努力打造一个全新的开发技术。VJ并不是Java，已经是大家都接受的事实了。到了2000年，Windows翻开了新的纪元，MS公开了酝酿已久的.NET平台。虽然那时.NET还在Beta阶段，众多业界人员已经可以感受到强烈的冲击。确实C#和.NET同Java是那样的相似，但是，我们必须承认，.NET做的比Java好一点点。

首先，MS第一次不限制你使用什么语言。虽然MS官方只发布C#和VB .NET编译器，它欢迎其他厂商提供其余语言的.NET编译器。.NET平台消除了很多语言之间的隔阂，大协作的可能大大增加。

其次，C#和Visual Studio .NET看起来就像我最喜欢的Delphi。Anders为Delphi做了一个很好的Update，从语言到开发工具，只不过成了MS的东西。MS的RAD水平也远远超过了VB6那个时代。

现在Java反而是最苦恼的，在前台开发领域本来就一直落后于Native的Delphi/C++Builder等等，以至于龟缩在后台做J2EE，而现在C#/.NET来了，连它的老家后台服务领域都被微软给盯上了，它的机会就更少了。其实Java语言真的很优秀，OO的一套很漂亮，但是很多人像我不会考虑用它来作用户界面的，即使有SWT和JBuilder。

## Danny的响应――小鱼是Borland

作为Anders好思想的继承者，Danny Thorpe在Borland决定加入.NET阵营的很短时间内就给出了一个Delphi for .NET Compiler Preview，确实让人高兴。不过，那仅仅是一个编译器，还没有IDE的配合，形不成很好的生产力。另外，你不可能指望用一个还叫Preview的东西开发出可靠的产品。所以，作为Delphi的忠实用户，我们其实一直在等待Delphi 8。

不过摆在Borland面前的工作实在是太艰巨。首先，MS在发布之前就已经花了很长时间来准备.NET平台，而且看起来VS .NET真的是远比VS6优秀。其次，Borland自己一度全神贯注于Linux平台上面Kylix IDE的开发，以至于耽误了很多宝贵时间，在.NET平台上面甚至一度落后于SharpDevelop或者Mono这样的开源项目。

Delphi 8在2003年底终于做出来了，Danny所写的Delphi for .NET编译器品质也很不错，可是，我还是跌破了眼镜。那个BDS 2.0 IDE几乎让人相信它不是Borland自己的产品，除了名字。启动速度奇慢就不说了，还经常跳出异常要我重启IDE。这样我就不得不放弃了本来的计划。用它学VCL for .NET，可是噩梦。不过用Delphi 8改学WinForms和WebForms就好多了了（ECO是个好东西，MS几年内恐怕都搞不出来，另外还有一点点Together绘制UML图的实用功能）。这个代号Octane的东西确实让我在火上煎熬了好长一阵子。

那个时候我就在想，如果Borland把Delphi for .NET编译器以及ECO这样的新技术嫁接到VS上面就好了。可是我告诉自己不可能，Borland还算是一间很大的公司呢，怎么可以做MS的寄生虫？因此，除了等待D8下一个补丁，我还在热切的期待Delphi 2005。我一度误解了它的代号DiamondBack的意思。我的理解是”钻石回来了”，就是说这个产品会让人想起Borland从前那些优秀的IDE来。虽然它实际上是指一种蛇的名字，但是Delphi 2005确实是我想象中的那块钻石。你可以照着Delphi 2005 Reviewer's Guide的指引去使用Delphi 2005的新功能，很贴心很好用的（除了loading还是很慢，而且需要你打很多补丁）。

马上发布的Delphi 2006又会是怎样的好东西呢，拭目以待。

## marc的抉择――虾米是RemObjects

如果Delphi社区人人都像我这样虔诚地等待着Delphi 2005来临，那么Borland的CEO肯定会十分高兴。不幸的是，肯定有些人需要别的解决方式来节约时间――”等待毕竟是一生最初的苍老”。

这类珍惜时间人的一个代表是marc rohloff。我很早就在BDN上面下载了这位仁兄设计的一个BDS插件叫做21834_code_converter_for_c_builder_and_delphi_for_.net。可以说相比起其他BDN上面发布的BDS OTA插件，有几个不能遗忘的独到之处。首先他的插件是一个EXE可执行文件（不是DLL），自带安装/卸载功能。同时，他尽可能的减少了代码对于BDS OTA架构本身的依赖，以消除BDS OTA那些恼人的bugs的影响。

假如Delphi 8不好用的话，这类人会有什么反应呢？Borland还做不到的，不如我们自己来做。我自然不是指marc取得了Borland的授权，然后将Delphi的编译器加到VS .NET里面。那好家伙做得更加彻底，带头写了一个全新的Pascal编译器。这个编译器几乎支持与Delphi语言一致的语法，品质也很不错。当然，这不是一个Delphi clone――像FreePascal。在这个叫做Chrome的编译器上，marc还添加了很多他以及RO的其他员工认为十分有用的新语法，来增强Pascal的力量，比如Class Contract等等。单纯从语言上来说，Chrome Pascal确实是Delphi之外一个不错的选择。它是Pascal，它也是Object Pascal，只不过，它不是Delphi，它完全是另一套东西。

Chrome的诞生完全是因为Marc确实需要一个优秀的Pascal for .NET产品来将RemObjects SDK移植到.NET平台。Delphi 8提供了很好的编译器，却整体上面还不是一个好的解决方案。Chrome + VS .NET就是RemObjects最后做出的选择。

marc成功了，因为他现在正在进行Chrome 1.5版本的发布准备了，生意不错呢（修改这篇文章的时候1.5版本已经发布了）。RemObjects的成功很正常，因为在很多Borland没有做的或者做得不好的地方，RemObjects都做得很好：

1. RemObjects提供免费的Chrome命令行编译器和SDK。如果你把这个和MS免费提供的.NET SDK一起用，你会发现没有VS .NET这样的IDE自己居然也可以干出很多大事情呢。最起码，这可以让你学习用Pascal来开发.NET项目。Delphi社区很早就有了这样的呼声――大概是Java出来的时候，可是Borland没有在意。
1. Borland没有及时的跟进新技术，去支持.NET 2.0 Beta。其实Delphi 2005发布的时候，.NET 2.0 Beta 1就已经出来了，但是，Delphi 2005还是只支持1.1。这使得Delphi用户还不能像Visual Studio用户一样及时了解.NET 2.0的新特性，像泛型，像ASP .NET 2.0，像Avalon。但是，如果你选择Chrome，你会发现现在它就是.NET 2.0上面除了C#、VB.NET等等MS语言之外最好的First Class语言了，对泛型等新特型的支持已经很不错（我个人以为Borland R&D肯定已经有了类似的东西，但是Borland没有发布出来罢了，连个Preview也没有――保守作风呀）。当然，RemObjects的灵活性，还在于它突破了MS的限制，将眼光放得更远。它官方宣称正式的支持Mono，让Linux下面开发.NET项目的用户也多了一个新的语言选择。Borland的路线图里面还没有看到Mono的影子呢，不过，单用Borland的Kylix就十分方便了。
1. "好风凭借力，送我上青天"。RemObjects的Chrome插件紧紧地把Chrome编译器绑到了VS .NET上面，使用户可以轻松获得MS苦心打造的IDE的良好服务。这个显然比Borland选择的自主开发IDE方案更快捷，也更省钱。但是用户除了Chrome插件之外还必须购买MS那昂贵的VS .NET。所以RemObjects自己并不能给Chrome定价很高，以赚取很多钱，否则谁会选择她。幸好她是一间足够小的公司，一点点市场就可以让她活得很好。

Chrome 1.5的发布肯定会引入许多更好的特性。可以期待。

## 写在最后

.NET时代，你的选择是什么呢？这里列出一些参考建议：

1. 如果你本来就是MS VS6的用户，推荐你继续用MS的VS .NET。VC的用户可以选择C#或者C++/CLI，VB的用户可以选择VB .NET。但是，你知道，你熟悉的MFC死去了。因为MS似乎是迟早要放弃Win32的。
1. Delphi的用户可以继续用VCL，只不过VCL for .NET做了一些小小的限制。应该感谢Borland，这些限制作为普通用户的你几乎感觉不到。当然，你也可以用Delphi for .NET开发纯粹的.NET程序。同时Delphi Win32开发仍然是Borland提供的IDE的一部分。
1. 作为新接触Pascal的用户，你比从前多了选择的权力――Delphi或者Chrome。选择Delphi可以做Win32/.NET的开发，而选择Chrome只能做.NET。在.NET平台方面，由于语言之间没有太多界限，两者之间是可以协作的。

## 修改之后

Chrome1.5基本上是一个简单的升级。这大概是因为Chrome的1.0就已经达到了相当的水平，做出了足够的突破。

Borland也改变了自己的保守作风。你可以查看BDN上面的文章，细细品味。真的，需要你细细品味。

总之Chrome的出现不意味着Borland就要出局了。反而是有了竞争，今后Borland和RO都会做得更好一些。
