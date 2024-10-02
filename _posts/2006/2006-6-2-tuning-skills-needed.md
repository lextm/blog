---
layout: post
title: "Tuning Skills Needed"
description: 这篇文章是介绍 CBC 2 项目的进度和遇到的性能问题。
tags: Code-Beautifier-Collection Delphi
permalink: /tuning-skills-needed-5e563c20b137
excerpt_separator: <!--more-->
---
(CSDN June 02, 2006)

需要完善SBT中自动完成功能的时候，我发现了加入触发事件的窍门。虽然只能绑定一个自定义事件到编辑器的Modified事件，而不是最为理想的OnKey*系列的事件，也可以实现不少很有用的小功能。
<!--more-->

已经实现的列表有：

1. 自动匹配()和[]。
1. 在///之后按下空格键则添加。
1. 自动完成, 等少数几个tag的匹配，带有参数的tag暂时不支持。
1. 在C#语言下，保留了SBT的几个自动完成项目，不过改为了空格键触发。这个和BDS 4的live templates部分冲突。
1. 在Delphi语言下，输入procedure, function, property之后，空格键触发相关的自动完成。
1. 每输入一个字符串的前三个字母则调用Code Insight实现自动提示。

一个明显的问题就是AutoCompletion和Input Helper的执行效率问题。这个曾经令CodeRush和CnWizards的开发人员烦恼的问题现在正在让我烦恼。优化整个过程，需要大量的实验。而我现在根本没有时间来做这样复杂的实验。特别是如何做出准确的测试来验证。

如果你恰好做过，请劳烦告知我。
