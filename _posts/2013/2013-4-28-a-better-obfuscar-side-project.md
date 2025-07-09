---
layout: post
title: "A Better Obfuscar, Side Project"
description: "This post talks about a better Obfuscar as a side project."
tags: .NET
permalink: /snmp-pro-a-better-obfuscar-side-project-ec176ca6a7c3
excerpt_separator: <!--more-->
---
Open source developers of .NET platform should not care much about obfuscation of the assemblies, as they even have the source code publicly available. However, if an open source project begins the commercialization, an obfuscator is needed to encrypt the secrets of the code base. That's what this blog post is going to talk about.
<!--more-->

## What is Obfuscation?
Simply speaking, after obfuscation the assembly becomes harder to understand. It won't stop anyone from decompiling it via ILSpy or any similar decompilers. It just makes the decompiled result strange enough. What about an example?

Download JustDecompile from Telerik.com.
Decompile itself to a project with source files.
Now if you try to compile the project, you will see what I mean.

## What You Should Not Expect From Obfuscation
You should not expect obfuscation to hide everything, as the openness of MSIL makes it even possible to reverse part of obfuscation, via an open source project,

https://bitbucket.org/0xd4d/de4dot

As it says on the homepage,

> If you don't count "don't distribute it" as a solution, **the best obfuscator feature is symbol renaming**. It's impossible to restore the symbols unless they're part of the assembly. All of the other "protections" are 100% reversible.

I am fully aware of the limitation of obfuscation, but for #SNMP Pro editions I will have to obfuscate the code base. So all I need now is just an obfuscator that can perform symbol renaming for me. Well, that means Obfuscar,

https://code.google.com/p/obfuscar/

## What I Did On Obfuscar
As the original project was long dead (last commit was in 2010 Dec), I have to fork it. Luckily other guys already did this, including RemObjects who built a product called Oxfuscator,

http://www.remobjects.com/oxfuscator.aspx

Thus, I just need to fork from one of them, and merge all patches from the forks to my own fork. Because I have been in the open source world for so long, it all becomes nature and here is my fork on GitHub,

https://github.com/obfuscar/obfuscar

I might charge users for a fee, as now this tool is fully functional, but I rather keep it open source and focus on my SNMP compiler.

So, if you are also looking for a free and useful obfuscator, come and get Obfuscar from my fork. I believe with all the patches, many of the previous bug reports on Google Code have been resolved.

Let me know if there is any new bug, https://github.com/obfuscar/obfuscar/issues.