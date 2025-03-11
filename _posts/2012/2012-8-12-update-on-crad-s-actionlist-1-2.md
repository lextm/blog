---
layout: post
title: "Update on Crad's ActionList 1.2"
description: "This post is about Crad's ActionList 1.2 release."
tags: .NET
permalink: /update-on-crads-actionlist-1-2-1300b9afbd18
excerpt_separator: <!--more-->
---

You probably know that except working on #SNMP and DockPanel Suite, I am also [maintaining Crad's ActionList]({% post_url 2012/2012-4-30-packaging-crad-s-actionlist-for-net-via-nuget %}).

Today, I am happy to announce the availability of its 1.2 release. [The NuGet package](https://nuget.org/packages/ActionListWinForms/1.2.0.0) can be found here along with its release notes.

<!--more-->

But importantly this time you get better Visual Studio support if you execute this installer.

This installer is mandate right now as the design time support is split out and is no longer part of the NuGet package. You have to use the installer to register design time support in Visual Studio.

Supported Visual Studio releases are 2008, 2010, and 2012.

If you have any question, please go to https://github.com/lextm/ActionListWinForms/issues

Cheers :)
