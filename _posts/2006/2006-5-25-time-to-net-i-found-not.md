---
layout: post
title: "Time to .NET? I found it not"
description: This post is about the problems of .NET Framework.
tags: Code-Beautifier-Collection Delphi
permalink: /time-to-net-i-found-it-not-98043f7486d8
excerpt_separator: <!--more-->
---
(CSDN May 25, 2006)

When developing the Tip of the Day feature, I decided to make it a separate executable. The advantage is that I can make a complete different version later without the Plus recompiling. However, some disadvantages can not be ignored. For example, there is no chance to add a "show tips on start" checkbox.
<!--more-->

I knew this advantage, and I accepted it. But there is another problem I have to see to.

It is the .NET framework which enables a .NET executable to run. But it is too big to install the runtime. For Delphi for .NET, the problem is even bigger.

If you compile the TipOfTheDay project in src folder, you will get an executable of about 1M. It is not a big project, but the embedded Borland.Delphi and Borland.Vcl namespaces make it fat.

Maybe I should redo this project in native code.

In the beginning I love .NET. But after some consideration, I think there are problems. Maybe when Vista is shipped and the framework is preinstalled, everything would be alright. But I think the Delphi for .NET part of the size problem can not be solved completely because the runtime is not provided by Microsoft.
