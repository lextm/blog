---
layout: post
title: "GrapeVine: License Issues and Lextm Common Library"
description: "This post talks about GrapeVine license issues."
tags: Code-Beautifier-Collection Delphi
permalink: /grapevine-license-issues-and-lextm-common-library-8b9a5e62f01e
excerpt_separator: <!--more-->
---
I decide to make a small change in CBC license. That is, LeXDK Core library should be under LGPL instead of GPL.

In this way, people can write closed-source Pluses for CBC from CBC 6.0 on. If you have done a new Plus, contact me so I can package it into next release of CBC. If you meet any problem using LeXDK, contact me so I can lend a hand.

Pluses I wrote are still under GPL including the Framework.

Why I make a change now? Yes, someone contacted me earlier this week and wanted to improve CBC, especially CodeBeautifiers Plus. I do not know what he/she may do in the future. Will there be another Plus or a new version of CodeBeautifiers Plus. The change of license can ensure if a new Plus is created, it can be under any license (GPL is one of the choices). It can be commercial, too.

I have reviewed Overseer and TraceTool. Yes, it is hard to decide which to use (because I still dream of a CodeSite copy). And what I can do now is to enhance Lextm.Diagnostics.LoggingService unit.

http://www.codeproject.com/csharp/TraceTool.asp?df=100&forumid=28124&exp=0&select=1095646

I want to imitate .NET Debug and Trace units, using Listener support. So I can implement a log4net listener, an overseer listener, and a TraceTool listener. And one day when I switch to CodeSite, I can implement a CodeSite listener then without heavily modification of existing code.

Why I do not prefer Microsoft Enterprise Library? You know I cannot use it because CBC is not an executable. I do not know how to configure bds.exe.config in order to make Enterprise Library working correctly.
<!--more-->