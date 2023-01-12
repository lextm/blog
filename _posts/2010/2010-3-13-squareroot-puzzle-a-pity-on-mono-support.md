---
layout: post
title: "SquareRoot Puzzle: A Pity on Mono Support"
description: "This post is about why I could not work on Mono support"
tags: SNMP Mono
permalink: /squareroot-puzzle-a-pity-on-mono-support-36a947c50037
excerpt_separator: <!--more-->
---
A review with MoMA on the suite release shows that the Browser, Compiler and Agent all fails to support Mono due to their dependencies on Windows only libraries.
<!--more-->

I cannot make the Browser and Compiler without DockPanel Suite, so I think such a dependency is at least reasonable. In the next few releases, I have no plan to get rid of DockPanel Suite.

But about Unity, I have to say I have so little to change. IoC containers such as Unity (1.* and 2.0), StructureMap (latest), and Spring.NET (latest) all fail to pass MoMA tests, as they hit similar MonoTODO items. Therefore, I have no framework to switch to :(

Hope that Mono 2.8 can improve itself in this area, and then #SNMP Agent can run on it automatically. I don't believe that developers that target Mono do not use any IoC containers.
