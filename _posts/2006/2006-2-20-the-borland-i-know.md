---
layout: post
title: "The Borland I Know"
description: 介绍了自己对 Borland 的很多看法
tags: Code-Beautifier-Collection Delphi
permalink: /the-borland-i-know-141062ba985a
excerpt_separator: <!--more-->
---
(Originally posted to CSDN on Feb 20, 2006)

## 前言

知道Borland是因为使用Turbo C 3开始了我的编程学习，了解Borland则是因为李维的《Borland传奇》。痛恨Borland则是在这样的几天，在我深爱了它两年以后。
<!--more-->

## 开篇

这一次Borland打算出卖IDE小组，其实可以看作是R&D的人员终于打算和一个变了味道的Borland说再见了。Delphi确实成了Borland的继子，虽然是Borland的两位创建者一手开始了这个辉煌的项目。难怪网路上面那么多人希望那二位买下IDE小组，重整旗鼓。可惜日子已经过了这么久，Philippe Kahn说Borland已经长大了，他不想接手，Anders Hejlsberg和Chuck Jazdzewski最近的表态我还没有来得及看，估计有了C# 3.0和Avalon的忙活，他们回归IDE小组的机会也不大了（除非MS买下这些IDE）。Inprise危机真的又要出现了。好在这一次IDE小组要离开Borland了，如果可以幸运的找到一个好的下家，说不定我们这些人还有的盼。不过，死牵着Borland旗号却要做ALM的那个Borland恐怕是维系不了多久，说不定会让Borland这个宝贵的名字暗淡无光了。

David I的计划

David I没有跳船而逃，John Kaster和IDE小组的人员都还在继续围绕路线图开发BDS。这些都给我极大的安慰。与紧盯着企业市场的BOD不同，他们眼中还是开发者最重要。如果可以顺利的得到投资，可以顺利的继续Delphi的开发，我想在这样一个社区的支撑下，Delphi至少可以像RemObjects的Chrome那样生存下去。如果从买Delphi赚到的钱今后可以全部（或者绝大部分）回到Delphi的开发上面，我想，这个时代还是没有几个开发工具可以与Delphi抗衡的。这样的分家至少可以保证我不需要继续深入学习ALM那些阳春白雪的东西了。

## ALM的前景

我本来就是一个悲观主义的人。在ALM的市场上，一时半会我还看不出Borland有多大的”未来”。原本我对于ALM一窍不通，但是最近的使用让我觉得，Borland的工具在这个市场上不能算是十分的出色。例如StarTeam，抛去各式各样的高级功能，我仅仅发现和Visual SourceSafe有的那部分功能是我可以天天使用的。这样的话，我使用CVS会便宜太多，况且现在中国的很多企业也开始使用CVS了。不知道StarTeam的辉煌何日能够到来，虽然它也是十分的优秀。现在我没有马上转入CVS的阵营，一方面是因为没有找到合适的机会，另一个就是BDS的IDE还不直接支持CVS，反而是内置的StarTeam连接还不错。可是分家之后呢？如果Delphi可以增加CVS的支持，恐怕我就会毫不犹豫地使用CVS了。毕竟我可以看到CVS的源码，放心。

CaliberRM其实和StarTeam差不多。感觉和Word差不了太多，除了对于编程/软件方面有很大的侧重。但是连生成文档都需要呼叫Word，真是令人失望至极。我不知道谁会购买这样的软件。起码，程序员不会。至于项目经理们，我觉得他们恐怕也不一定会选择CaliberRM吧，因为选择的余地看起来是很大的。

至于Optimizeit，Blake Stone看好它也是很正常的，感觉还是很不错的。但是同样，在这个领域中有太多的竞争者，Borland却没有明显的领先多少。

Together产品线不知道最后划入哪边，因为它实际上已经并入了IDE里面。如果跟着ALM，我觉得就会让十分不错的Together技术沦为Visio那样的绘图软件了。虽然网上不少评论对于UML还是有微词的，但是在做CBC架构重构的时候，Together for C#让我感到了极大的解放。我可以在Model级别完成重构，可以通过Audits和Metircs评价自己的编码质量。虽然一时还没有机会使用Together for Delphi，我对它是充满了信心（我不再使用ModelMaker，是因为它毕竟是一家比Borland小的公司，况且他们在MM for C#和MM for Chrome上面花了太多的精力）。

## 谁会来接单

这个是我，以及整个Delphi社群，如今最关心的话题了。

MS接单的话，JBuilder大概就完了（好在还有Eclipse）。InterBase也完了（好在还有FireBird）。C#Builder完了（好在我已经在用#D了）。Together肯定会被保留，因为MS独缺这个好东西。如果Delphi团队可以重回Anders领导下，说不定也可以浴火重生。至于Kylix和BCB的命运，则是难以判定。ATL的命运多舛就可以看出MS对于这两个产品的态度。

SUN接单恐怕已经不可能了。原本的JBuilder时代还可以有这样的奢望，如今却是完全的不可能。况且SUN全力支持Java都没有做稳Java的王座，Delphi这些Windows的东西想要在SUN手上生存也是不太现实的。

IBM全线转入了Java，Together和JBuilder这样的天造之和居然不是IBM急需的东西（它已经有了Eclipse和Rational）。况且IBM在《Borland传奇》中的名声实在太差。想想OS/2的命运，我觉得Delphi死在哪里都好，不要死在IBM手上。不过今天的IBM是不是依然是书上那个样子？如果还是那样的话，为什么败者组的Eclipse最终击败了连战连捷的JB呢？

BEA和Borland的合作不知道现在是个什么样子，而且估计BEA仅仅会对Java产品线在意，所以，双B在这个背景下合并的可能性是十分有限。

Google的创新性以及和MS的不可调和性，使得网路上面大部分人对它寄予了希望。再者Danny Thorpe是Google的人了。如果Delphi可以回到他的船上，说不定可以延续下一个十年。然而，IDE是一个十分古老的行业了，和Google三天两头搞出来的令人眼睛一亮的技术相比，这个市场是十分残酷和收成不好的。那两位Google富豪会怎么选择呢？我只怕Google不敢接单，免得股票大跌，折了本钱。看起来Google收购IDE只会让Tod Nielson和BOD兴奋异常――持有Google的股票看起来还是一桩不错的买卖。可怜的总是用户。

Oracle的收购是很多人反对的。我个人对于Oracle的印象也是牛皮吹破的一团糟。所以我宁可使用FireBird也没有去摸Oracle。好在Oracle也是今不如昔，大概不会不顾这么多反对跳出来接招。

Apple接单的可能性也是今天才发现。既然CBX可以跑在Mac上面，这两家还是有点缘分的。况且Apple新近投入了Intel的怀抱。然而，Apple如今在我的心目中甚至都不是PC厂家了，而是一间像华旗资讯那样的卖MP3的公司了。Steve Jobs下一步不管做什么，我想都不会和Delphi的路线图有什么重叠吧。由于Cingular并没有掀起如同iPod一样的狂潮，所以我个人估计Apple最近的生意也不好做，难得腾出闲钱来买IDE。

其实网友们发挥了太多的想象力，为IDE小组寻找合适的婆家。不过我必须承认很多人是病急乱投医，完全没有分析最根本的事实。

1. 第一个错误就是认为小公司们可以买下Delphi。除非是我搞错了，RemObjects的Chrome可是没有独立IDE的，大约只有VS的用户才会买他们的产品（这一部分用户还必须曾经用过Pascal/Delphi才好）。即使是Novell那样曾经不错的公司也不太可能――看看他们的Mono，连帮助文档都是在线的，还没有合适的IDE（没有用过MonoDevelop，因为Kylix肯定会好用的多）。Corel如今大概面临着极大的威胁吧，那个让我知道它的CorelDraw如今面临着Adobe+MacroMedia联军的冲击，怕是情况比Delphi还要危险。假如我是Corel的老总，今天我也会拼尽全力去迎战最棘手的对手，而不是买下不相干的Delphi。

Borland是一家不大的公司，然而，相比软件业大多数的公司，Borland的规模还是算得上”庞大”的。最终IDE部门如果被业内公司买下，那么大概就是我最先分析的几家大户吧（为什么没有CA，是因为我对它一无所知）。

2. 第二个错误就是思路太狭隘。很高兴有人提议Borland的一些技术伙伴合资收购IDE小组。这无疑是最有力于Delphi等等IDE发展的一个选择，但是因为1中的分析，可能性不大。开源也是一样。由于所谓的Software Assurance协议的约束，Borland开源Delphi也必须负起相应的法律责任，所以，不到没人买单的情况下，开源不是Borland当前最佳的选择。

我和Allen Bauer的观点差不多，还是风险投资最合适。业内的公司收购IDE，必然会根据那家公司的需要修改Delphi路线图等等。这些似乎丝毫无助于Delphi等等IDE的继续发展。而风险投资则不会有这样一些麻烦。我想只要有钱赚，总会有人愿意掏钱。

其实要不是Lenovo刚刚收购了IBM PC业务不久，还处在消化不良阶段的话，我想这是中国企业收购国外核心技术的绝好机会。国内还没有什么编译器技术达到了Delphi的高度，IDE也是没有见到惊艳之作。如果有幸得到IDE小组这个宝藏，无疑可以在短时间内得到极大的提高。有了自己的CPU，有了自己的PC产业，有了自己的软件产业，还缺什么？金山都在用Delphi开发UI，而国内使用MS和Borland的IDE的单位更是数不胜数。为什么不买下人家优秀的东西呢？可惜金山太穷，怕是看到了机会也只能放弃。

## 结束

既然Borland R&D还没有灰心，我想，这一段传奇就还没有结束。十年多前在整个业界都在看Borland还能撑得了几天的时候，Anders和R&D的团队用他们的努力创造了一个不朽的神话――Delphi。今天，似乎是昔日重现。我期待会有一个好的结局。

## 后言

本来打算这段时间好好充充电，把Delphi网络部分好好学习一下的。可惜发生了这样的变故，几乎是逼着我投入.Net的怀抱。我也许会就此离开Delphi的领域，但是，一定会时时回望。因为Borland和Delphi的名字，似乎已经成为了挥之不去的印记。夏天到来的时候，我会穿起那件印着Borland名字的T-shirt，因为在我心里，那种精神是Never Gone的，而且到了那个时候，一切应该会有一个说法。
