---
layout: post
title: "HardQuery Report: Prepare, for Highlander"
description: "This post talks about my preparation for .NET Framework 2.0."
tags: Code-Beautifier-Collection Delphi
permalink: /hardquery-report-prepare-for-highlander-7b18d63fb452
excerpt_separator: <!--more-->
---
(CSDN July 13, 2006)

It is last year that MS released .NET 2.0. However, for Borlanders .NET 2.0 will come in early 2007.

Lately I have been prepared to learn something on ASP.NET 2.0 so I try to compile CBC against .NET 2.0. It is very simple if NAnt is used. Change the -t:net-1.1 to -t:net-2.0 and everything works fine. However, it is not what it looks like.
<!--more-->

Notice that CBC links to some other open source assemblies. All of them were compiled against .NET 1.1. So on a computer where only .NET 2.0 is available, I am not confident that CBC can run correctly.

What is lucky? All of them are open source, so I can compile the source against .NET 2.0. SMS.Windows.Forms, csbgoodies, and SharpZipLib are easier than AddMany (currently, I cannot find a easy way to compile delphi for .NET code although the compile is capable of doing so).

Since HighLander will come so late, I have plenty of time to finish this migration. Wish myself good luck.
