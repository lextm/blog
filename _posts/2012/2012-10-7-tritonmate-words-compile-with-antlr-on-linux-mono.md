---
layout: post
title: "TritonMate Words: Compile with ANTLR on Linux/Mono"
description: "This post is about compiling #SNMP 7.5 on Linux/Mono."
tags: SNMP Mono Linux
permalink: /tritonmate-words-compile-with-antlr-on-linux-mono-4cca2cf7ed27
excerpt_separator: <!--more-->
---
It is fairly easy to compile #SNMP 7.5 on Windows, as the ANTLR C# runtime contains a MSBuild targets file which provides good enough integration. However, due to [a Mono bug](https://bugzilla.xamarin.com/show_bug.cgi?id=3055), this targets file cannot be loaded by xbuild. Thus, if you download #SNMP 7.5 source code and want to compile it on Linux, you find that it is impossible.
<!--more-->

So how to fix this if I could not resolve the Mono bug? Well, we need to find another way to compile the grammar file,

1. Remove .
1. Add to exec Antlr3.exe on Mono. This compiles Smi.g to SmiLexer.cs and SmiParser.cs.
1. Include the generated files in the project.

To achieve better cross platform compatibility, we don't need to really perform the above steps on SharpSnmpLib.AST.csproj, but use a few Condition test, as demonstrated in this change set,

https://github.com/lextudio/sharpsnmplib/commit/e10d42dbd84e16141d345b83470ee3cb6faff022

In this way, we can still use ANTLR targets on Windows, while switching to ANTLR3 compilation on Linux/Mono. I don't plan to do anything further here, as mainly the development is on Windows.

Unfortunately, this only fixes the ANTLR compilation issue, while NuGet is another silly piece that fails to work on Mono, and when I tried to fix it a bug occurred.

Let's see if those Microsoft guys can fix it sooner.

This NuGet bug prevents NuGet packages from being restored, so if you want to compile latest #SNMP code base on Linux, you can grab the packages folder from

https://github.com/downloads/lextudio/sharpsnmplib/packages.tar.gz

Decompress it, and then put the packages folder in the correct place. After that, the remaining steps are documented in KB600006 and KB600007.

I am going to receive my new laptop tomorrow. The development of TritonMate will be reactivated in a couple of hours.

Stay tuned.
