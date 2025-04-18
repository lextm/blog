---
description: 这封公开信详细分析了CnPack开源项目的发展历程及未来方向，提出采用更开放的组件架构来推动项目进一步发展的建议，参考Eclipse和CodeRush的成功模式，探讨如何实现从功能集合到平台型架构的转型，以吸引更多开发者参与并创造可持续的生态系统。
excerpt_separator: <!--more-->
layout: post
permalink: /至cnpack项目组的公开信-草稿-40064c875807
tags: code-beautifier-collection delphi open-source
categories: [Tools and Platforms]
title: 至CnPack项目组的公开信――草稿
---
(Originally posted to CSDN on Nov 30, 2005)

至CnPack开发组和用户社区的一封公开信

――对于CnWizards未来发展的一些看法

撰文lextm

11/6/2005
<!--more-->

## 写在前面

最近几天又抽空认真的看过了一遍CnPack几年来的记录文档，感触良多。从一份计划书到现在这个比较成熟的开源项目，可以说CnPack特别是CnWizards已经有了极大的影响力。最近的一段时间，我注意到官方论坛上面对于CnWizards的未来目标已经有了一些提及。不知道你有没有注意到论坛上面CnPack IDE专家包版面置顶的一个帖子――”调查：请大家选一下喜欢的工具，以便改进！”，向用户们征询常用的专家。可以说，由于CnWizards已经有了1.6兆的大小，代码量的积累更是0.1版本的数倍甚至数十倍，从最初很小的专家集合演变成为了甚至可以取代一部分Delphi老牌/商业OTA插件的”大项目”了。量变自然应该伴随质变。下一步开发组除了继续修补bugs，应一些用户的要求开发新功能之外，是不是可以有新的突破呢？CnWizards的未来是什么样子呢？CnPack开发组是不是可以顺利的达到创建之初的宏伟目标呢？这样的一些问题不知道正确答案是什么。所以我试着给出一些自己稍微成熟的看法――至少比我之前发布在论坛上面那个路线图会成熟多了，我以为，嘿嘿。

## 第一波的转变――从无到有

CnPack项目的诞生对于中国Delphi程序员社区来说是意义重大的一件事情，历史功绩也应该是无可限量的吧。起码，它的出现证明中国程序员也可以通过社区合作的方式开发出成功的开源项目。

### 发源自中国的Delphi社区，壮大于我们之中

Borland公司的Delphi开发工具历经十年，在世界范围内已经建立了一个巨大的用户群。中国国内的Delphi用户是一个很大的族群（CSDN网站发布的用户开发语言调查结果据说Delphi比重一度接近50%），近年来涌现出的优秀Delphi程序员代表也是数不胜数。但是这一两年以来，随着Delphi热潮的褪去，大富翁论坛等等Delphi社区组织明显失去了鼎盛时期的光景。

我个人对此的见解是，简单的答疑为主的论坛形式决定了这种方式下的社区形式很难满足所有参与者的长期需要，很难凝聚起智慧和力量。对比之下，国外的Delphi社区组织所以比较有生命力，甚至作出以FastCode和FastMM为代表的开源项目来反哺Borland Delphi，一个重要的方面与多年以来JCL/JVCL为代表的一些成功的开源项目提供的巨大的积累和支撑密不可分的（另外一个方面是他们还比较重视社区成员间的交流，经常在Borland官方组织的活动之外自行举行一些区域性的交流探讨活动）。CnPack项目，我以为是中国Delphi程序员在合作开发方面的一个新尝试。而CnPack项目组至今几次比较成功的聚会，也可以看作是社区交流探讨活动的成功代表。

不可否认，周劲羽同志在大富翁论坛上发布的那个开创性帖子以及项目开发方案的形成（2001.12）就是CnPack项目正式诞生的日子。从最初的0.1.0Demo版本开始，弱小的CnWizards最先走上了一条坎坷但是注定光明的道路。正是在这样的路上，小不点长成大人物。前前后后众多Delphi程序员热心的参与，使得CnWizards发展得很快。

### 第一波转变的深刻影响

初步的分析了CnWizards历史更新记录之后，我觉得CnWizards的第一波转变主要发生在0.6.6这个版本以后。这样的断代结论是基于0.6.6版本的两个显著特点的。一是之前CnWizards的功能是比较简单，不支持多语言，界面也显得初级，而从0.6.7版本起，有了最为独特的多语言支持（目前很多国外的商业项目甚至都不具备），一个比较成熟的项目架构初见端倪。另一个则是新版本发布时间变长了，项目相对进入了稳定发展期。0.6.6版本之前，有时候仅隔几天官方就会发布新版本，后期一般是在一个月左右的时间。但是从0.6.7版本开始，新的稳定版本的发布时间间隔有了明显的变化（虽然这一方面是因为CnPack官方开始时时在主页发布重要的Nightly Build版本）。这也是一个项目开始成熟的标志吧。

那么这样第一波的转变到底有了哪些显著的影响呢？我想大概可以划分成下面几个方面：

* 团结了中国一部分有激情的Delphi程序员，从单打独斗变成了集团作战。

尽管一开始CnPack开发组人员很少，CnWizards也是功能很有限。随着开发人员的不断加入和项目代码量的积累，现在的CnWizards功能可以说是很丰富了，可用性/易用性甚至不输给Castalia之类商业产品。

特别是一些牛人的参与，更是有机会欣赏到优秀的代码。我最为欣赏的几位包括Riceball，很早就从JEDI项目中见到了他的大名（Jedi Program Editor的负责人）；张伟，他领导的ISee项目我还在念高一的时候就听说了；陈省以及周爱民都是因为看了他们所写的书而被我看作Superstars。这样的一些组员很多之前都开发了自己独立的OTA插件，最典型的像ShadowStar的CodeFast（CF用户也有很多）。他们的加入大大增强了开发组的实力，也带来了CnPack每个小阶段的新变化。

正是最初成员们的努力， CnWizards的专家数量由少到多，功能由弱到强。在这里，我想向他们的坚持和付出表示致敬。

* 中坚力量初步形成，培养了领导人物

周劲羽和Passion，还有许多以他们为代表的早期参与者，已经在不断的实践中经历了常人难以想象的快乐和忧伤。他们为每一个新成员的加入而兴奋，为每一个新特性的完成而庆祝，也为每一个恼人的bug而辗转难眠，为CnPack的明天而时常发呆（有点个人的想象成份）。虽然在项目开始的时候他们还不是很老辣的顶尖高手，但是我想，至少现在说他们可以是国内Delphi OTA开发方面极为出色的”大人物”也是名副其实吧。

另外，整个项目的管理和发展，也肯定使他们二人的领导能力得到了很大的提高。所以你可以发现在官方论坛等地方看到很多对于IDE OTA bugs和解决方法的探讨，看到各个子项目负责人的新计划和新想法。最近给人印象最深的就是CnImage/CnGraphics小组的一次讨论调查――是一个图像类就包含所有的滤镜功能还是分化出一个滤镜类。这样一类探讨相比较一般论坛上面泛泛的讨论更加深入，对于拓展初学者的视野和交流高手见解都是十分有益的。

* 对于Delphi IDE插件领域的影响深远

从一些用户的反馈来看，CnPack所提供的正式他们日常所需要的插件功能。甚至有一些用户使用了CnWizards之后开始逐渐减少其它插件的使用――我也是其中之一。可以说这样的一些细节都体现了CnPack正在逐渐的实现最初项目计划书中那些曾经高高在上的目标，对于Delphi IDE插件领域产生了不小的影响。”锲而不舍，金石可镂”。

但是，不可不察的是，由于一些历史因素，CnPack的发展过程使得它不可避免的存在一些小问题。我的观点是：

* 由于项目由小到大，最初建立的一套体系时而显得比较狭隘，时而又比较宽泛。

狭隘二字表现在代码的改动，也就是专家所有功能的设计权，都集中在少数几个人的手中――核心开发组。这大多是因为早期人手本来就少，而发布新功能的作者一般也以合适的身份加入了CnPack核心开发组的缘故。

但是这样的体制到了现阶段就会引起一些不必要的问题。

一个比较明显的表现在于一旦有热心人开发了新的功能，同时希望该功能进一步结合到CnWizards里面，他面临的主要选择有：1. 加入CnPack，取得开发权限，持续的改进该功能，直至被接纳到CnWizards中。2. 加入CnPack，但是没有开发权限，该功能CnWizards不接纳或者另选人开发。3. 不加入CnPack，这一功能也就不会快速加入CnWizards了。

由于特殊的原因，并不是每个人都做出第一种选择。而后面两种可能都是是很不理想的――可能挫伤部分程序员的参与热情，也影响了CnPack对于新想法的接纳。所以，我们需要一个更加开放的组织形式。

宽泛的一面则表现在与国外很多开源项目相比，申请成为CnPack的组员是相对比较容易的。通过审核加入CnPack不想想象中的那么困难。不过，好在核心开发组是很难进的，从一方面保证了最终代码的质量。可是这样明显导致了很大一部分组员其实很难有一展身手的机会。而且由于现在一个方面的特性一般是由一个或者很少几个主要成员完成，有点缺少合理的竞争。CnWizards特性也是只进不出，越来越多。其实真的不是每一个特性的作用都那么实用。而且有时由于一个重要人员的暂时停顿，一个特性的开发也就变得很慢。

* 项目初创阶段的架构选择和后期发展的矛盾

这个主要体现在几次架构变化和后遗症上面。

一是最初采用GExperts的架构。毕竟在项目启动时，当时最成熟的开源OTA插件架构就是GExperts，历史最悠久（不过如果那时候CodeRush开放其架构的话，或许用那个更好）。在我的印象中，GExperts架构最主要的问题是过于臃肿，单元文件都十分的庞大，一个Unit有太多的内容――完全可以划分成几个相对独立的小单元。这个也是Delphi自身最大的问题之一，VCL的源代码都有这个问题。这个架构也是初学者比较难学习的。

第二次对架构比较大的动作是后来开发支持多语言特性的0.6.7版本的之后，很多类的实现细节都有了改变。

但是，这样的两次改变后的架构还不时很灵活，还没有接近CodeRush的那种Rush API类型，各个小功能还不可以作为模块（BPL包或者DLL文件）动态加载（通过设置修改只不过禁止了这些功能）。所以添加一个新的专家就必须加到CnWizards代码内部，重新编译。

另一次不太明显的架构改变是为了支持Delphi 8/2005中OTA的一些新的元素而对架构做了一点点微调。问题是这样调整之后CnWizards对于Delphi新的OTA还是支持的不太漂亮。

## 第二波的转变

CnPack已经三岁多了。可以说正是它生长发育的一个关键阶段。在这样时刻我们讨论它的发展路线图是十分必要的一环，关系到这个项目，项目组，以及众多的热心参与者和用户群。本人曾经十分草率的在官方论坛上发表了一篇路线图帖子，初步的表达了我对于CnPack项目下一步发展的一些个人观点，很不成熟的。在这里，我希望进一步阐述一些自己后来的深入思索。

### 用更加开放的体系接纳新的创意

的确OTA技术在国内的关注程度从前是比较少的。这也是由于国内技术氛围比较关注于实际应用所致，另一方面是OTA的技术资料一般都是英文资料，也一方面限制了国人对其详细的了解。但是，怀有Extending the IDE想法的人应该是很多的，Delphi 5/6/7自身的代码编辑功能就不是很强。同样看一看CnPack官方论坛上用户们对于新特性的要求你也会发觉。但是，以核心开发组几个人的力量，我觉得从长久来看很难满足用户们的需求――以代码格式化特性为例，用户的呼声一直很高，但是很长时间了还没有看到可用的成品。还有很多我个人认为不错的想法仍然在CnPack”高层”的考虑之外――这也不是他们的错，一个开源项目要考虑的太多。那么，可不可以尝试用新的思路核心的体制来发展CnPack呢？――我以为用一个更加开放的体系会给CnPack项目带来新的生机。

为什么之前我多次提及Rush API？为什么CodeRush会在这样的十年中成为Delphi领域最成功的OTA插件系统？我觉得就是因为其设计者Mark Miller考虑到了将CodeRush做成一个很好的开发平台，而不是一个简单的功能集合。

使用过CodeRush，特别是自己开发过CodeRush组件的人都应该了解一点Rush API。它是Mark Miller在OTA架构上面自己做的一层不错的封装，Classes Library很简练。CodeRush同时提供了几个很简单的组件开发向导，使有需要的用户可以添加自己想要的新功能到CodeRush里面――新添加一个按钮，一个菜单，甚至一个浮动面板都十分简单，无需和庞大的OTA架构直接交流。这样的体验是你使用别的OTA插件是所没有过的。后期的CodeRush很多不错的功能都不是Mark Miller所写，而是直接采用了别人写的组件打包发布。可惜的是，现在Mark Miller逐步的将关注目光转到了Visual Studio插件上面。其他的Delphi插件像Castalia也是很不错，但是在架构上面，我觉得还没有可出CodeRush其右者。

在其他领域，也有相似的可供借鉴的案例。一举将Java开发王者JBuilder击败的Eclipse也是以一种极好的平台/组件架构得到了整个Eclipse社区的广泛支持，很多功能都是由随机参与的小公司或者个人完成的，像建模的插件就有开源的，Borland Together的好几种组件可以选择。

所以CnPack想要更进一步，登上下一个高峰，就应该尽早实现一个新的框架，也开发出平台/组件类型的架构。至少现在CnPack开发组之外的人员想要开发自己的新特性甚至自己的专家都不是问题，但是想要结合到CnPack里面就有些障碍。当新架构建立之后，很多有新想法，又有能力作开发的人，就可以在更加独立的情况下（比如不加入CnPack开发组的情况下），写出新的插件供CnPack用户下载使用。这样就可以借助到原来不能借助的力量来加强CnPack。

### 更详细的实施计划

在新架构都没有出来的时候就谈及这样的计划似乎为时过早，但是我希望现在就展现这样的图景可以吸引更多国内关注OTA开发者的目光。

参照Eclipse现有的发布方案，在新架构期CnWizards官方核心开发组的工作重点就转移到维护一个CnWizards平台上面，关注于平台的改善。这个平台应该主要包括功能组件的加载/管理，平台设置管理，用于开发新功能的必要向导等几个功能，有详细的功能组件定义规范。然后原来的各个功能以组件（BPL包或者DLL文件）的形式单独发布。每个组件应该实现的功能包括在CnWizards平台上注册/发布，实现主要功能的必需函数，自带组件必须的设置项管理功能。我个人的见解是采用BPL包来做功能组件，动态加载/调试都比较方便。

几个好处：

* 谁都可以发布自己的新组件给CnWizards的用户，也可以参与这个小组件的维护/更新，提高了CnPack项目参与范围和程度。实际上这一方面也减轻了核心开发组的工作压力。

* 一个功能领域可能会同时产生几个很好的组件设计，相互竞争，相互学习，共同成长。这个就很像Eclipse的情况，激发每个人的创造力。

* 通过官方的评选等形式的活动，将好的组件和平台一起打包发布。这样发布的版本可以很丰富，用户也可以有更大的自主权去选择喜欢的组件。

* 组件部分的授权协议可以考虑跳出CnPack选择的GPL等开源协议的限制，而是允许组件开发者采用共享/免费等其他更灵活的方式来做发布，充分的调动组件开发者的积极性。

当然这也给CnPack项目的负责人提出了很高的要求：从前台退到幕后，更多的担任领导组织工作。不过如果各位高手也参与组件开发的竞争，一定会更加精彩。

官方网站也需要一些变化。原来由一个开发组使用的开发/发布平台，将来可能需要部分给各个组件的开发者小组来使用，比如一个组件就肯定需要有一个自己的页面来做宣传。论坛也需要向着同样的方面转变。CnWizards的发布也就相应得复杂了。不再是发布一个单独的版本，而是用户可以自由定制。我觉得加入类似Eclipse的UpdateManager之类的功能来增强CnPack的升级功能，也是很有必要的，那样可以允许用户更方便的升级自己使用的平台和组件。

### 可以预见的将来

经过这样的一些改变，应该可以更大的调动参与者的热情，使得CnWizards从一个少数人的项目变成一个社区的集体活动。Eclipse可以成功，那么，CnPack至少可以从中受益。这对于开发组来说这一次转变，也将是一个巨大的挑战。首先，CodeRush证明了这样一个架构的可实现性，但是它不开放源代码，使得我们现阶段没有作为参照的标本，必须自力更生。然后，Java语言开发的Eclipse确实有很多架构性的东西很诱人，很值得学习，但是可以用Delphi语言来模仿吗？我不确定。所以，现在起似乎就需要群策群力，早做准备，以便在转变开始时就能站在一个比较高的起点上，后期少走弯路。

## 第三波的转变

方才已经谈完了最重要的想法，最后想谈一点不太相关的东西。

"为什么我们不能开一家CnPack有限公司呢？搞一个更为正式一点的组织？"

我提议开公司绝不是因为赚钱方面的考虑，而是挂了公司的牌子之后，日后可以以更加官方色彩一些的方式组织一些合适的活动，比如在大学中的CnPack宣讲活动，程序员聚会，技术论坛，以及与Borland公司互动――这些活动虽然以别的方式作也可以，但是难免会有一些不必要的麻烦。GExperts, Inc就是这方面一个不错的范例。

再说，开公司也不影响我们继续作开源的CnPack呀。个人感觉这样运作对于加强CnPack项目的宣传力度，保证项目长期良性发展都会有一些积极的作用。至于公司体制，则可以保留现有的简单松散的结构。由于不赚什么钱，一些复杂的企业制度方面的东西可以简化。开发组成员等也可以自由决定是不是加入这个公司。反正开公司的方针应该是更好的为开发CnPack项目服务。万一遇上什么版权等问题，公司体制也比个人体制在解决时更有优势。

## 写在最后

想法很多，也不知道自己说清楚没有，所以先发布一个草稿吧，希望得到大家的反馈。

希望CnPack茁壮成长。

## Updated on 2011:

CnPack项目依然是那么成功，而我自己已经与Delphi无缘了。年少轻狂时候认为自己是深思熟虑，而现在经历了多个开源项目之后慢慢发现确实很多东西不能过于理想化:)
