---
layout: post
title: "WinForms Tips: 两个很简单但是不容易想到的点子"
description: "这篇文章讲述了两个很简单但是不容易想到的 WinForms 技巧。"
tags: Code-Beautifier-Collection Delphi
permalink: /winforms-tips-两个很简单但是不容易想到的点子-889fdc0ac00
excerpt_separator: <!--more-->
---
(CSDN Oct 18, 2006)

1. 一个只读的 TextBox 怎么才不是灰色？

如果你改用 RichTextBox 就十分简单了。这个控件有相同的接口，但是在设为只读时是白色的。

2. 如何嵌入IE？

在 .NET 2.0 上，使用 WebBrowser 类就好了。不过在 1.x 需要导入一个 ActiveX 控件。
<!--more-->