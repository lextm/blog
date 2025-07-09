---
layout: post
title: "FileDirectoryPath 1.0: How to Compare Two Paths"
description: "This post shows how to compare two paths in C# with the library FileDirectoryPath."
tags: .NET
permalink: /filedirectorypath-1-0-how-to-compare-two-path-69926ba6e0e1
excerpt_separator: <!--more-->
---
(CSDN June 02, 2006)

需要完善SBT中自动完成功能的时候，我发现了加入触发事件的窍门。虽然只能绑定一个自定义事件到编辑器的Modified事件，而不是最为理想的OnKey*系列的事件，也可以实现不少很有用的小功能。
<!--more-->

I was wondering how to compare two paths these days. For example,

1. `@"C:/Dir1\\File.txt"`
1. `@"C:\DIR1\FILE.TXT"`

Yes, it is not easy to find something useful in MSDN.

Today, my problem is solved! FileDirectoryPath 1.0, which is original part of famous NDepend, is now available a separate open source (LGPL) library.

So what is the way to compare two paths?

``` csharp
filePathAbsolute1 = new FilePathAbsolute(@"C:/Dir1\\File.txt");
filePathAbsolute2 = new FilePathAbsolute(@"C:\DIR1\FILE.TXT");
Debug.Assert(filePathAbsolute1.Equals(filePathAbsolute2));
Debug.Assert(filePathAbsolute1 == filePathAbsolute2);
```

En, this is wonderful! Thanks a lot, Patrick Smacchia.
