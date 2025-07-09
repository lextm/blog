---
layout: post
title: "VirtualBox上面虚拟Ubuntu不能上网的解决方法"
description: 这篇文章讲述了在 VirtualBox 上面的 Ubuntu 虚拟机不能上网的解决方法。
tags: Linux
permalink: /virtualbox上面虚拟ubuntu不能上网的解决方法-b600372b21e1
excerpt_separator: <!--more-->
---
(CSDN Oct 26, 2007)

受够了VMware Server的低下效率，转向了使用VirtualBox。 不过马上也遇到了Ubuntu虚拟机不能上网的问题。当然，在VirtualBox官方论坛上面找到了配置方法。下面就是本人对原文的一点粗浅翻译，仅供参考。
<!--more-->

1. 在host上面查看DNS服务器配置。在Windows host上面，打开开始菜单|附件|命令提示符，然后输入ipconfig /all。回车开始执行。用笔记录DNS服务器的信息以备后面使用。
1. 将VirtualBox的网络设置设为NAT类型。启动Ubuntu Linux guest。打开System|Administration|Network菜单，选择Wired Connection，单击Properties按钮，将其中配置改为DHCP，保存。重启Ubuntu。
1. 在重启后的Ubuntu中打开System|Administration|Network Tools菜单。将对话框中间部位的下拉列表选到Ethernet Interface，然后可以看到对话框下面显示出VirtualBox给Ubuntu分配的IP，记录IP和子网掩码。
1. 在同一个对话框内，选择Netstat标签，然后点击绿箭头获取Routing Table Information。注意表格中有一列为Gateway，请记录其中不是全零的那一个IP地址。
1. 回到2中间打开的Network对话框，打开属性，将类型从DHCP改为Static IP。输入刚才3中记录的IP地址和子网掩码。再输入4步骤中记录的Gateway的IP地址。
1. 保存，退出Properties，但不要关闭Network对话框。切换到DNS标签，删除这里自动设置的DNS服务器信息。然后添加1中间记录的DNS服务器。重启Ubuntu。

做完上面几步，你的Ubuntu应该又可以连上网络了。

[原文地址](http://forums.virtualbox.org/viewtopic.php?t=2430)
