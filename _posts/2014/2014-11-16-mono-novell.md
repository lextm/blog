---
layout: post
title: "Mono历史片段：Novell的崩溃和Xamarin的浴火重生"
description: "本文介绍了 Mono 历史中的一个片段，Novell 公司的崩溃和 Xamarin 公司的诞生。"
tags: Mono
permalink: /mono历史片段-novell的崩溃和xamarin的浴火重生-bf1dd7b8621b
excerpt_separator: <!--more-->
---

Novell 是一家神奇的技术公司[1]，它自行开发和收购了很多不错的软件和标准，包括但不限于 NetWare，IPX，WordPerfect，Quattro Pro，Unix，SUSE和Mono。和它曾有心挑战微软的霸权，虽然最后以失败收场，但是在整个开源运动的过程中，它所扮演的角色无可取代，

1. 于1993年收购Unix System Laboratories并获得UNIX版权，最终在SCO诉Linux一案中Novell保卫了Linux[2]。
1. 收购Ximian和SUSE，使得Mono这个开源项目得到了一个相对宽松的发展环境并进入了企业市场。（这部分前话今后会另外撰文）
1. 与微软达成了交叉专利合作协议以增进产品互操作性，也促成了Moonlight项目开发过程中Mono和.NET团队的合作。

但是由于运营状况不佳，2010年11月Novell被Attachmate集团收购，并且大约半年后开始大规模裁员。在各个产品中Mono团队受到的影响最大，全部失去了职位。当时正值MonoTouch和Mono for Android产品发布的初期，这两个极有价值的项目突然面临不确定的未来，原有用户的产品激活服务也遇到困难。这使得好不容易积累的用户群体突然感到恐惧。

不得不承认Miguel de Icaza是个做事很有腔调的人[3]。他重新找到了Nat Friedman，并且创建了新的公司来继续Mono产品的开发，名叫Xamarin。由于Attachmate当时仍然掌握着MonoTouch等收费产品的版权，所以Xamarin只能基于Mono开源项目的源代码重新开发类似MonoTouch和Mono for Android的全新产品，并准备在最短的时间内将它们推向市场。很多老用户和潜在新用户都在焦急的等待中等待着Xamarin新产品的发布。

当然谁也没有想到到了七月事情峰回路转，Attachmate旗下刚刚建立的SUSE部门主动找上门来。Xamarin和SUSE达成了一揽子协议，让MonoTouch和Mono for Android的版权回到了Xamarin手中[4]，

1. Mono，MonoTouch等产品的全部知识产权由SUSE授予Xamarin。
1. Xamarin则继续为SUSE的客户提供相关产品的技术支持服务。
1. Mono开源项目的主导权也由SUSE转交到Xamarin手中。

经过这样的公平交换，Xamarin终于卸下专利包袱可以全力投入到开发之中。有趣的是，MonoTouch和Mono for Android其实由两拨人开发完成。在Xamarin初期为了避免专利问题，这两拨人交换了角色，来开发对方曾经做过的部分，据说其中诞生了很多全新的想法和实现。在拿回MonoTouch等产品版权后，这些新东西也逐步注入到产品之中，总算没有白费气力。（后面会开始介绍Xamarin公司的兴起）

但是值得注意的是自从Xamarin创建后，很多留下Novell时代印记的技术就失去了原来的地位，它们包括

* libgdiplus和Mono的Windows Forms实现
* Mono for Visual Studio，一个在Visual Studio开发和远程部署调试Mono程序的插件
* Moonlight，开源的Silverlight实现

同时也有部分Mono核心团队的成员因为个人的原因加入其它公司或者创建了自己的公司。事实证明这些同学其实从来没离开过这个业已庞大和有生命力的生态系统，他们又在新的岗位上推动了Mono的发展（后面会详细介绍两位）。

最后不得不提一下2014年九月的一段新闻。MicroFocus公司宣布收购Attachmate集团，并由此获得了Novell这个厂牌。有趣的是MicroFocus同样收购了Borland厂牌。这两个古老而著名的品牌最后以这种方式到了一起。

## 参考

[1] http://en.wikipedia.org/wiki/Novell

[2] http://en.wikipedia.org/wiki/SCO-Linux_controversies

[3] http://tirania.org/blog/archive/2011/May-16.html

[4] http://tirania.org/blog/archive/2011/Jul-18.html
<!--more-->