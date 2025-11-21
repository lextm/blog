---
description: This post shows how to tell whether a .NET assembly is compiled against
  .NET 4 or .NET 4.5.
excerpt_separator: <!--more-->
layout: post
permalink: /how-to-tell-net-4-5-only-assemblies-f5e9041533bb
tags: .net
categories: [Programming Languages]
title: How to Tell .NET 4.5 Only Assemblies
---
.NET 4.5 is a very special release of .NET Framework, as it is an in-place upgrade of .NET 4, as [detailed by Scott Hanselman here](http://www.hanselman.com/blog/NETVersioningAndMultiTargetingNET45IsAnInplaceUpgradeToNET40.aspx).
<!--more-->

However, one piece of information is missing from that article. Given a .NET assembly, something.dll, how can I tell it is compiled against .NET 4 or .NET 4.5?

"Why does it matter"? you might ask, but if you happen to run a .NET 4.5 assembly on .NET 4 you will get a miserable exception. This also applies to Mono stable releases (2.10.\*), as .NET 4.5 support comes from 3.0.\*.

If you happen to use a decompiler such as JustDecompile from Telerik, it is easy to open the assembly and see whether it is marked as .NET 4.5.

However, if you are using ILSpy, the assembly is still listed as .NET 4.

I think this is an issue of ILSpy, so I created [a pull request](https://github.com/icsharpcode/ILSpy/pull/383) and hope it will be accepted.

It is interesting that the assembly itself contains the meta data of target framework, which you can find from [here](https://github.com/icsharpcode/ILSpy/issues/382).
