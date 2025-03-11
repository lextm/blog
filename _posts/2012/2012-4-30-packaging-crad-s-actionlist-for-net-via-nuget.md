---
layout: post
title: "Packaging Crad's ActionList for .NET via NuGet"
description: "This post is about packaging Crad's ActionList for .NET via NuGet."
tags: .NET
permalink: /packaging-crads-actionlist-for-net-via-nuget-5c72e77ece94
excerpt_separator: <!--more-->
---

In case you don't know Crad's ActionList for .NET, you can refer to [this article](http://www.codeproject.com/Articles/13879/ActionList-for-NET-2-0).

<!--more-->

As usual, Microsoft re-invented the wheel and announced NuGet a long time ago. Whether you like it or not, you will have to accept the fact that one day you need to support it. One problem I met is that many old but useful free stuffs are not packed for NuGet, such as Crad's ActionList for .NET. So I stepped out and forked it on GitHub,

https://github.com/lextm/ActionListWinForms

and then created NuGet packages for it,

https://nuget.org/packages/ActionListWinForms

This serves myself well, as [many of my existing open source projects use this control]({% post_url 2008/2008-2-16-dockpanel-suite-tip-2-conflicts-with-crad-actionlist %}), which dated back to 2007 and 2008.

I hope that I can put more fixes to this library and maintain it for a while.

If you have any patch that would like to share (under CPL 1.0), let me know.
