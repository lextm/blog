---
layout: post
title: "#SNMP Design: Unity in Compiler Finally"
description: "This post is about the refactoring of the Compiler."
tags: SNMP
permalink: /snmp-design-unity-in-compiler-finally-4aa520053566
excerpt_separator: <!--more-->
---
If you have time to review our latest Browser source code, you will notice what I have done in order to fit Unity in. I moved nearly all global variables into the IoC container who helps construct every objects based on my configuration file.
<!--more-->

However, because I spent less time on the Compiler so its design is worse. So a lot of refactoring was performed. And the output is beyond my imagination. By creating a CompilerCore class, I successfully extract a lot of code out of MainForm. I cannot believe everything works out in this way unless here it is. So is it possible to develop a command line compiler based on this new class? Yup, I would probably do that soon.

It is really nice to learn about Unity, as I have a nice ride to redesign both the Compiler and Browser step by step. Now it is time to move on, as we still have a few key items for CrossRoad release. Stay tuned.

