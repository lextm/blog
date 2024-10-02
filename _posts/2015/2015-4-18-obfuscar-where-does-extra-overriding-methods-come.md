---
layout: post
title: "Obfuscar: Where Does Extra Overriding Methods Come"
description: "This post is about why Obfuscar warns of extra overriding methods and how to resolve that."
tags: .NET
excerpt_separator: <!--more-->
---
An issue has been reported to me one year ago, but I could not easily fix it as the code base was not quite clear where the bug comes from exactly.

Don't get me wrong. It is pretty easy to reproduce it, and then analyze the IL instruction with ILSpy. But even if the cause is identified, the difficulty is how to properly fix it. So let's review the technical details and see why this issue occurs first.
<!--more-->

## The Wrong Obfuscation Process

When Obfuscar processes the assembly, it first identifies two method groups to be renamed,

1. IA.get_PropA and ClassA.get_PropA.
1. IB.get_PropB and ClassB.get_PropB.

Due to the proper type ordering introduced in 2.0 release, the first group is renamed to A ahead of the second group.

Then when the second group is going to be renamed, Obfuscar checks the methods of IB and ClassB to see if name A is already used somewhere. Well, it could not see any conflict (as Mono.Cecil tells). So it goes ahead and rename get_PropB to A.

In this way, overriding relationship is added to the code, which makes ClassB.get_PropB an overriding method of ClassA.get_PropA, as both of them are virtual and now both named as A. Note that such relationship is valid at MSIL level (as the IL instructions are valid), but since the relationship does not exist in original source code, it is still harmful as it can lead to unpredictable execution result.

## The Puzzles

1. Could Mono.Cecil avoid the issue? No. Cecil is a MSIL parser, so it does not take good care of method relationship that seriously. The flexibility it provides can lead to any kind of evil if you make mistakes.

1. Could .NET Framework avoid the issue? No. C# compiler emits MSIL instructions and then CLR executes them. If post processing of MSIL generates extra overriding relationship, CLR simply accepts that.

## The Fix

You can see from CodePlex that Jirka7a proposed his patch on how to fix the bug. It might work (I did not test), but it does not look good. The naming algorithm should not be heavily modified, as that will affect all kinds of scenarios.

We only need to focus on virtual method renaming, and give the algorithm enough context on how to pick up a proper name. That approach finally shows a better way. For example, when Obfuscar tries to rename get_PropB, it checks IB and ClassB, as well as IA and ClassA. That makes sure the naming algorithm finds out A is already used, and automatically switches to a (the next unique name).

You might wonder what might happen if indeed we need to rename both method groups to the same name. That can only happen if they are the same method group with overriding relationship in original source code.

Stay tune.
