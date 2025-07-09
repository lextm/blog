---
layout: post
title: "More Threading and InDate is Almost Done"
description: "This post is about threading in .NET and the new feature InDate."
tags: Code-Beautifier-Collection Delphi
permalink: /more-threading-and-indate-is-almost-done-d4b9e87bd5bf
excerpt_separator: <!--more-->
---
(CSDN June 14, 2006)

.NET threading is not quite hard, if you only use a few threads. For example, two or three threads are used in InDate (in Integrated mode three threads, standalone mode two).
<!--more-->

In order to make the textbox unlocked when updating, I saw to SDK document and found a DirectorySearcher sample.

It is amazing that this sample tells just what I need. And I know a little about Control class by the way. After reading and modifying the source, I turn my Updater.cs into a user control and slightly edit FormInDate. Then it goes just fine.

I think only two threads are needed when integrated mode is set. I will see to that soon.
