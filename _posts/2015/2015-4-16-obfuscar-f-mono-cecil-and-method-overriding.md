---
layout: post
title: "Obfuscar: F#, Mono.Cecil, and Method Overriding"
description: "This post is about how Obfuscar handles F# assemblies."
tags: .NET Mono
permalink: /obfuscar-f-mono-cecil-and-method-overriding-f91dca4d13ba
excerpt_separator: <!--more-->
---
Due to the announcement of Google that it is going to shut down Google Code, I finally decided to take the chance to migrate all Obfuscar issues at Google Code to GitHub. The migration was smooth and everything is now at https://github.com/lextm/obfuscar/issues.

One reported issue caught my attention, because it is related to F#, a functional programming language which I am not familiar with. Is this language so different that Obfuscar cannot process generated assemblies? Remember that tons of bugs have already been fixed in release 2.0 and 2.0.1. OK, I tested it out yesterday and was completely surprised at my findings.
<!--more-->

## F# Magic and Assembly Internal

I would not drill down too deep, but a glance on the F# compiler core library FSharp.Compiler.dll can give you some hints on the differences.

So to sum up,

* There are many internal classes generated (this assembly contains more than 10000 classes).
* There are a lot of generic usage in classes and methods (quite complex to analyze).
* Inheritance is quite heavily used.

## Mono.Cecil to Analyze Method Overriding

Several scenarios were analyzed in order to see why Obfuscar 2.0.1 could not obfuscate the code properly. And the reason was quite simple that when a method overrides a method with generic parameters (several variations though), the InheritMap class could hardly find all method groups, which led to the crash as some overriding methods were mistakenly renamed.

Mono.Cecil does not provide built-in support to find all such method groups. That's why Obfuscar uses InheritMap to do the tasks. But when InheritMap tries to compare two methods, it was too careless to only compare parameter types by converting types to strings. If such comparison is used, those generic parameters can never match anything else. Therefore, to resolve the issue completely, one solution is to find a better way to compare two methods.

I wrote one yesterday which was hacky and had to improve it a little this morning. Am I the only one who needs to perform such tasks? Luckily after reading a few Mono.Cecil threads I came across the Mono Linker code,

https://github.com/mono/mono/blob/master/mcs/tools/linker/Mono.Linker.Steps/TypeMapStep.cs

It clearly shows how to match methods when generic classes are in scope. After testing the code, Obfuscar can now perfectly obfuscate the F# compiler itself.

Well, I also boost the performance a little bit so that it can handle such assemblies with >10000 classes. To compare, it takes release 2.0.1 forever to work on the same assemblies.

Stay tuned.
