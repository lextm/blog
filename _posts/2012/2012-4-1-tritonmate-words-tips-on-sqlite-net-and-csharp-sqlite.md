---
layout: post
title: "TritonMate Words: Tips on sqlite-net and csharp-sqlite"
description: "This post is about tips on sqlite-net and csharp-sqlite."
tags: SNMP .NET
permalink: /tritonmate-words-tips-on-sqlite-net-and-csharp-sqlite-36ae8b1a3c89
excerpt_separator: <!--more-->
---
If you followed the recently changes in #SNMP, you know we have a new MIB compiler implementation based on ANTLR in the bottom layers, which exposes various new opportunities to explore.

To make full usage of this powerful compiler, we need to make big changes in the top layers such as updating the compiled module file format (*.module). You can imagine, using a database is an obvious option to replace the original text file format.
<!--more-->

## Challenges on normal SQLite approaches

I have evaluated several open source databases, and it seems that SQLite is the best for our needs (open source, small, though feature rich). So I started to try several SQLite libraries, and wished to find a light-weighted one to help me learn SQLite bits. However, most of the well known libraries

have too many features (which may not be useful for #SNMP)
have dependency on the native SQLite driver (sqlite3.dll), which I hate a lot.
#SNMP MIB Compiler is good at portable deployment. Currently, this compiler application can be zipped up and deployed because it is purely .NET. I don't want to lose this nice feature due to migration to SQLite.

## New Hope

Because of Xamarin, I started to pay more attention to all information demonstrated in its seminars,

http://xamarin.com/seminars

And I just watched this one called "Third Party Libraries with MonoTouch and Mono for Android", and came across [sqlite-net](http://code.google.com/p/sqlite-net/) for the first time.

I was happy that sqlite-net is one step closer to my goal, as it is a simple wrapper over sqlite3.dll, which provides very easy to learn ORM API.

To evaluate it, in one of the projects I created at office (a Launchy clone called Lex Pad), I made use of sqlite-net to migrate from a local text file to SQLite. I was able to finish all tasks in a only few minutes (less than 30 minutes). That experience was wonderful, except that it does not resolve the deployment problem yet.

Well, it was only a few hours ago when I tried to make sqlite-net to work with csharp-sqlite I found that sqlite-net already has some support for it and I just needed to update it to support the latest csharp-sqlite build,

http://code.google.com/p/csharp-sqlite/

https://github.com/praeclarum/sqlite-net/pull/29

Now the deployment problem is resolved :), since csharp-sqlite is a C# port of SQLite (rewritten from native to C#).

Though I have been busy with Touch Mouse Mate in the past few weeks, mates, please don't worry. I was still watching out for #SNMP, and will focus on it more in the coming weeks.

Stay tuned.
