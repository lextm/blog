---
layout: post
title: "Overseer: Use It For .NET"
description: "This post talks about Overseer, a logging tool for .NET."
tags: .NET
permalink: /overseer-use-it-for-net-efff10eed378
excerpt_separator: <!--more-->
---
I loved CodeSite. During the short trial, I found it easy to log most information I needed in a friendly way. But then I turned to C# and .NET and thought that I could not use CodeSite anymore. I was totally wrong, because soon CodeSite added support to .NET.
<!--more-->

However, as an open source developer, I had to resort to open source solutions most of the time. So I searched Code Project and found some alternatives. log4net entered Code Beautifier Collection at last. I'd like to say that it serves CBC very well.

When I started my career, I found I was in bad need of CodeSite. The problem was that nobody knew it here and it was not listed in purchase plan. Luckily I found Overseer for .NET at that moment (although it was not used immediately).

http://www.sharpplus.com/freewares

Today I finally have some time to try Overseer for .NET. The only disadvantage is that no document is available to tell me how to set it up. So after compiling I find that I cannot see the logging.

What's wrong then? Yes, there are something missing. You have to download the original Overseer! Original Overseer is the watcher, while you should use Overseer for .NET in your .NET project to send messages.

http://www.torry.ru/authorsmore.php?id=1768

BTW, you should always manually run overseer.exe before any debugging. Why? overseer.exe adds a registry flag so your project can find it later.

In all, when you cannot afford CodeSite, Overseer is a good alternative.
