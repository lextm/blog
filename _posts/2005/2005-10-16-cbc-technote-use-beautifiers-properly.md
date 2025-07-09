---
layout: post
title: "CBC TechNote: Use Beautifiers Properly?"
description: A post about when to use code beautifiers and how to avoid the pitfalls.
tags: Code-Beautifier-Collection Delphi
permalink: /cbc-technote-use-beautifiers-properly-cd446deaf8e6
excerpt_separator: <!--more-->
---
(Written on 2005–10–16; originally published to CSDN on Nov 03, 2005; modified and republished.)

"There is no silver bullet". This is a universal truth you should keep in mind before reading afterward.
<!--more-->

## 1. Do your thing ahead!
Automatic tools can help you to save time, but primarily, when you're typing, you should add indentations and spaces yourself. Mainly, I use a beautifier when I copy others' code to my files. What's more? When you read Lippman's Essential C++ or C++ Primer or any other good written books in Delphi/C/C++/C# and other languages, you will find that code in them is formatted very good. If you need to copy code from these classics, it will take you no time to format the files.

## 2. Bugs and shortages remain in beautifiers
JCF and AStyle are still under development. So, there are bugs undetected. I found that JCF provides us basic protection from crashing files. Whenever it comes across a internal bug or parsing error, a dialog is triggered. You can use the backup to recover your file. However, AStyle is designed to be too simple to serve you like JCF. the sample file `assembly.cs` in the `samples` folder is a good example of AStyle's craziness. So, you may still need to do beautifying manually sometimes.

As a result, personally I don't suggest you, my dear users, use the `Project` and `Group` actions of CBC. In future version, I should either prompt the user about this or develop a backup mechanism in CBC's body.

Languages are developing themselves. Delphi has evolved a lot these years, and Delphi for .NET new syntax are introduced. In .NET 2.0, C# language also adds an important extension. But in a short period, I think, for Open Source Software developers, responses to these changes are not so fast as the users' expectation. In that troubling window, users will be bored waiting. (I experienced this case, too. It occurred when Delphi for .NET syntax was born, but luckily Anthony updated his JCF soon after I contacted him.)

## 3. Keep backing-up your source files
Although this should become a habit of advanced programmers, beginners know little about it.

For those new in this field, I suggest you use WinZip or WinRAR or any other plain tools to keep copies of your projects.

When you find that way complex, you may choose some basic SCM (software configuration management) tools, such as Microsoft Visual SourceSafe. They are GUI based and friendly. Although they are not professional enough in my view, common needs are met.

If you run a group in enterprises, you should buy business-level products such as Borland StarTeam, or well-designed and open-source CVS that proves to be excellent. The features they provide may be what you're thinking of.

(Update: it is so funny to see myself recommending Source Safe at that time, but Git or Mercurial was introduced too late :) )
