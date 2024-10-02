---
layout: post
title: "Product Review: First Look At PowerShell"
description: This post is about PowerShell.
tags: Windows
permalink: /product-review-first-look-at-powershell-db413733099a
excerpt_separator: <!--more-->
---
Last Friday I needed to write a batch file that executes a command several times. I failed because I never fell in love with the syntax. As a guy who started to use PC in Windows 95 and to program in Delphi 7, I always find command lines hard to use and memorize.

But today, after trying PowerShell, I found it much easier to learn than cmd.exe. And writing a for loop is similar to C# language.

``` powershell
for ($i = 0; $ -lt 5; $i++)
{
    ping 127.0.0.1
}
```

But I still wonder why not create something like C# script?

(Updated: It is wonderful that I can do the old Command Prompt stuffs inside PowerShell 1.0. Thus I give up Command Prompt from now on.

Because there is a Command Prompt feature in CBC, I think I can enhance it on systems with PowerShell installed.)
<!--more-->