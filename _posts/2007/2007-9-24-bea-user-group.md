---
description: 这篇文章是我参加 BEA User Group 之后的一点想法。
excerpt_separator: <!--more-->
layout: post
permalink: /动态语言-bea-user-group之后的一点想法-2ce5eefdde7c
tags: java
categories: [Programming Languages]
title: 动态语言，BEA User Group之后的一点想法
---
(CSDN Sept 24, 2007)

听说 BEA 是在阅读《Borland 传奇》的时候，而了解它则是在找工作的间隙。很遗憾自己一直没有选择做 Java，因此也就不可能应聘 BEA 的技术职位。但是很庆幸的这不妨碍我抽出一个下午的时间参与到 BEA User Group 里面。应该说到了上海之后自己也参加过了一次 EDA Tech Forum，但其氛围和 User Group 还是两样。
<!--more-->

首先过来讲座的专家都不是以卖产品为目的的，除了开场由 BEA 的人士围绕的产品是 BEA 的 WebLogic 平台。用 Jython 来做脚本还是很不错的想法，但是其实假如选择的是其他动态语言例如 Groovy，效果应该也是一样。毕竟真正使得配置可以成功的是一套 WLS 接口。Microsoft 同样也将动态语言 JScript 作为操控配置 Windows 的一个解决方案，效果也是十分类似，大大简化了配置服务器之类的工作强度。

我特别喜欢第二位介绍 Groovy 和 Grails的讲座。应该说我对于 Java 平台的一些技术还是有稍微的了解，因此听起这个讲座难度还不是很大。况且钱霄先生侃侃而谈，又有大量的举例，可以让你听一点皮毛也受益匪浅。契约编程看来已经是大势所趋了。从 Grails 的各种特性来看，其实 CodeGear 手中的 ECO 几乎全都具备――模型，持久化，各种 Action 和 Service 支持，可惜 ECO 一直没有像 Rails 和 Grails 之类这么流行――价格或许是一个因素。

至于 XRuby，大概是由于主讲的些许紧张，效果并不是那么明显，起码我还没有兴趣去试试看。

简单谈谈自己听完之后的对于动态语言发展的一些看法。

首先，动态语言在开发中的重要性已经在提高了。在我自己的项目中，像 MSBuild 脚本之类的东西实在是方便极了。Rails之类的开发高效率相信很多人都希望尝试一把。这也引发了现有的主要软件厂商对这一领域的兴趣。BEA 利用 Jython 来实现 WebLogic 平台的快速配置，Microsoft 借由 Dynamic Language Runtime 将 IronRuby 和 IronPython 在 .NET 平台上面实现……相比较而言，Microsoft 的脚步要快上许多。DLR 基本上已经很成熟，便于各种动态语言迁移过来，而 JVM 上面还没有一个通用的动态语言基础可以使用。这也导致 JRuby 之类的项目都必须自己来开发 JVM Dynamic Language Support。这一点同时也表现出了现有 Java 厂商目光的短浅，对于动态语言的支持十分有限。虽然 JRuby，Jython，Groovy 之类的开源项目也取得了一定成果，但是没有主力厂商的推动，发展还是很有局限的。

其次，动态语言应用于开发的优势还远远没有被发挥出来。一个很明显的例子就是动态语言 IDE 的匮乏。这也使得 CodeGear 有机会进入一个用户群巨大但是竞争相对较小的市场。例如 Ruby，虽然 Eclipse 和 NetBeans 都有 Ruby 的支持，而且已经做了多年，但是问题多多。CodeGear 3rdRails 一面世似乎就已经在很多方面远远领先。可见应用开源 IDE 虽然可以有效降低使用者的初始投入，但是产出依然十分有限，并且 IDE 的不稳定常常带来新的麻烦。商业 IDE 的介入对于迅速提高生产力、加速动态语言的普及都是很有好处的。

最后，就是动态语言的普及问题。当越来越多的程序员意识到动态语言的重要型，同时有了很好的 IDE 的支持，那么是不是动态语言普及的时候就到了呢？应该说在这个阶段，依然需要众多商业公司的参与。例如提供各种方面的控件、类库、DE 插件。最重要的还有培训和技术支持。唯有如此，才可能让动态语言真正进入主流的开发中，达到全盛。

当然，User Group 的抽奖活动也蛮有意思的――当然，我这么说是因为自己很幸运的被抽到了：-）
