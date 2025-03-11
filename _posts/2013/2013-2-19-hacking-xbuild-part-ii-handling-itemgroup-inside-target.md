---
layout: post
title: "Hacking xbuild: Part II, Handling ItemGroup Inside Target"
description: "This post is the second part of my hacking xbuild series. It describes how I handle ItemGroup inside Target."
tags: Mono
permalink: /hacking-xbuild-part-ii-handling-itemgroup-inside-target-ccbae2ef6abf
excerpt_separator: <!--more-->
---
> The source code lives here right now, and my changes are under MIT/X11 just like the original code, https://github.com/lextm/mono/tree/xbuild_lex

A lot of people experienced the same problem with xbuild like me, that ItemGroup tags inside Target are not evaluated correctly. Of course, there are other stuffs missing, but this one alone is annoying enough. Can we have this resolved?

https://bugzilla.xamarin.com/show_bug.cgi?id=1862
<!--more-->

I don't want to wait till Mono guys implement this, as I have been waiting for a long time. So recently (starting at Feb 8) I started to set up the necessary environment and hack on this issue.

My current approach is to get something working, and learn the code base bit by bit. Therefore, the following trick is used.

Assume that we have the following MSBuild script fragment,

then instead of adding new elements in xbuild to analyze the inner ItemGroup, the patch I created converts the fragment to its equivalent form which xbuild can already understand,

```
Include="@(fruit);raspberry">
TaskParameter="Include"
ItemName="fruit"/>
```

In this way, quickly I made the unit test passed.

I am going to work on other similar issues in the next few weeks, and my goal is to get ANTLR C# MSBuild targets working on Mono. As a result, stay tuned because I will post more on my progress.
