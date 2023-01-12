---
layout: post
title: "插件架构"
description: "这篇文章讲述了设计实现插件架构的一些事情。"
tags: Code-Beautifier-Collection Delphi
permalink: /插件架构-a1ac28444cfe
excerpt_separator: <!--more-->
---
(CSDN Sept 12, 2006)

中午吃饭，博士和我讨论了程序中各部分相互依赖的问题。他问我是不是总是build all，那样似乎就可以掩盖一些缺陷。

我依然不太理解他的提问。不过，仅仅是步行去吃饭的那么一点时间，似乎没有办法讨论太高深的技术。不过，build all，我确实很久没有用过。
<!--more-->

从LeXDK的第一个版本5.0（包含在WalkPace中）开始，我的工程就从Project升格到了Project Group。我很高兴自己将复杂的SBT代码分散到多个工程之内，截断了相互依赖的源头。然后，就是分层设计。基础的类库还分为依赖于BDS和中性两类，有点为跨IDE支持做准备的意思。不过，由于Visual Studio，SharpDevelop和BDS的插件API差别太大，所以，这样的划分还没有 实际的意义。

分割之后，我就可以将bug隔离在某个dll里面，跟踪，除错，都简单了很多。同时，build all也就没有太大的用处，每次都只用编译一个工程，BDS就会自动分析依赖，开始编译的过程。

如果你依然在一个巨大的工程上工作，似乎也应该考虑重构啦。简单明了的结构，可以消除太多不必要的麻烦。
