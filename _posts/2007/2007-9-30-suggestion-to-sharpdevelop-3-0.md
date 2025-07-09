---
layout: post
title: "Suggestion to SharpDevelop 3.0"
description: "This post talks about my suggestion to SharpDevelop 3.0."
tags: SharpDevelop .NET
permalink: /suggestion-to-sharpdevelop-3-0-a4b1ba8b2cc8
excerpt_separator: <!--more-->
---
It is really fun to read SD blogs as well as its source code. And [the latest post](http://laputa.sharpdevelop.net/ChoosingTheTargetFrameworkInSharpDevelop30.aspx) talks about multi-targeting and asks for users' opinions. I suggest SD 3 Alpha continues to use option 1 now. And once SD 3 enters its Beta stage, option 2 may be better.
<!--more-->

I loved the multi-targeting feature SD 2.* supported long before MS Visual Studio, but I found so many unexpected behaviors at last that I had to give it up at last. Sorry I did not post a bug report then because I really thought the SD guys should focus on other issues not this one. In order to cross compile for .NET 1.1 and .NET 2.0, I wrote my own MSBuild script to work with MSBee instead. You can check Code Beautifier Collection HardQuery source code to see how I made that happen.

SD 3 is still Alpha but I have used it for Code Beautifier Collection GrapeVine for months because I do not want to use Visual C# 2008 Express any longer (NUnit support is must for IDE IMHO). Currently only I maintain that project so I can upgrade to MSBuild 3.5 and C# 3.0 without a fear. Compared to MSBuild 2.0, MSBuild 3.5 is feature rich which makes writing high performance MSBuild script possible, so I think give up C# 2.0 and MSBuild 2.0 not a big problem.

Sometimes we should let old staff go when new staff comes. .NET is such a fast train so if you want to support every bit of it you get lots of problems. That is why MS gives up C# 2.0 and MSBuild 2.0 support in their own products. I do not think they do this for earning more money. They may do this to make things easy and say goodbye to nightmares. I cut off HardQuery and GrapeVine too so I can spare a lot of energy to write a few chapters of a small book on how CodeGear rebirths that old Borland legend.

Keep your excellent work, SD guys.
