---
description: 作者分享了从高中时期学习Turbo C到大学深入C语言和Delphi的编程历程。文章探讨了良好编程风格和习惯的培养过程，以及K&R的编程风格对作者的深远影响，强调了代码美化和清晰结构对于程序开发的重要性。
excerpt_separator: <!--more-->
layout: post
permalink: /a-primrose-path-to-programming-4aeb1f289b2c
tags: delphi windows
categories: [Operating Systems]
title: A Primrose Path to Programming
---
(Originally published to CSDN on Dec 29, 2005)

一些自己学习编程的小故事
<!--more-->

## DOS/Turbo C给我的思考

很早就用Turbo C编写了一些物理过程的仿真。华工的很多学生对这个技术都不会陌生，后来在华工的本科生课程里面叫做CCBP。不过，我开始做这个的时候还在念高二，是因为这门课程的发起人跑到我们华师一来搞TC教学实验。

现在觉得可笑的是，我所有的程序代码都是一个单元，一个main函数到底。因为所谓的教学，根本就没有讲C语言是什么东西，也就连定义自己的函数都不会了。那时的代码都是用软盘装，现在我已经没有办法找到它们了。一方面是因为现在我的机器已经没有软驱，另一方面是那些随便乱丢的软盘也不知道坏了没有。

没有使用过TC之前的C编译器，只看到李维的描述，所以，我真的不觉得TC那东西有什么革命性的进步。我对TC确实有不少反感。主要来源于

1. 鼠标不能用。后来知道Borland C++支持鼠标，可是那时候我已经学会了使用VC 6，并且开始在Delphi的海洋里面遨游了。
1. 快捷键都是三个键连按，我仅仅在课程快结束的时候记住了一些剪切粘贴之类。和Word定义的两键快捷键相比，真是一大麻烦的东西。
1. 还有就是必须设置好多路径，否则没法编译。后来学了C语言，自然是知道这是为什么，可是当时就是天真的觉得麻烦。

或许就是这样的一些原因，我个人一直对C/C++耿耿于怀，直到学习本科里面的C语言课程。

## The C Programming Language

那个可爱的老师叫做于治病（同音不同字），确实是华工计算机系青年才俊之中的牛人。我很感激他选择的是The C Programming Language做教材（当然我所在的AC班级的全英教学计划也不会给他选择谭浩强那本书的机会）。不过还是有不少同学坚持看谭浩强的书。这样的对比很快就催生了几个很不错的结论，可是我这里就只想提及最重要的两点：

1. 谭的书真是差劲，排版就糟糕透顶。谭的所有范例代码，都是乱糟糟的。跑起来自然是没有问题，可是和人家的书一比，跟盗版差不多。K―R的代码风格几乎让人难以忘怀，后人多作为典范。如果你使用AStyle美化C系列的代码，你会发现默认的风格里面就有这个。这也是我最欣赏的代码风格了。
1. 谭的书真是考试至上，但凡软考可能遇到的题目，都可以在练习里面找到接近的。可是K-R的书只会让你了解C语言，只会告诉你用C做系统（看看最后一章，如果你比较崇拜Unix的话），很多的例子我猜就是来自于UNIX的与源代码。难怪我觉得我的C语言学了之后不打算去考软考，不是因为我学的不好（我也算是班级考试的前几名呢），而是鄙视这种考试所考的内容。

反正我的代码现在空格很多，换行很多。不一定每个人喜欢这样的东西，可是我可以保证多数人喜欢看到漂亮的代码。

## Win/Delphi时代的轻松

开始使用Delphi的时候，总是参考别人的代码，结果缩进不一致，总是手工去调整，为了让代码美观我的键盘受到了巨大的折磨（当然不可以和NFS造成的伤害相提并论）。直到Delphi Formatter Expert出现，才开始简单了很多。后面的故事在别的文章里面也提过了，就是CBC的缘起。

我现在仍然把大量的代码美化，就是为了让自己某天修改的时候一眼可看出当时的逻辑来。

## 应该不会磨灭的痕迹

K-R为什么可以写出UNIX？我无法想象，但是这样良好的习惯，肯定不可能写出很糟糕的东西。

我们为什么需要读外文书，我觉得并不是因为全部的外文书都是宝贝，或者中国人就写不出，一个原因恐怕就是因为我们在许多细节上面太过潦草。
