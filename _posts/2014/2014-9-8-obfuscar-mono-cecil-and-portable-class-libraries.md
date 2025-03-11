---
layout: post
title: "Obfuscar: Mono.Cecil and Portable Class Libraries"
description: This post describes how Mono.Cecil and Portable Class Libraries are related.
tags: .NET
permalink: /obfuscar-mono-cecil-and-portable-class-libraries-40ac70755d50
excerpt_separator: <!--more-->
---
It must be a pain to see that Mono.Cecil includes PCL support, but you still find PCL breaks Mono.Cecil based utilities, such as Obfuscar. Forgive us, as Microsoft designs it in a horrible way. There is still too much to be changed so as to catch up. Let's see two examples below.
<!--more-->

## SuppressIldasm Attribute in Obfuscar

Microsoft kindly provides an attribute in BCL, and once attaches to an assembly ILdasm utility refuses to decompile it. Well, unfortunately no other decompiler honors this attribute. I updated Obfuscar to insert such attribute to assemblies, only to match other obfuscators.

Now the issue comes, that if you happen to obfuscate a PCL assembly you notice that .NET 4's mscorlib becomes a dependency!

Alright, simply debugging into Mono.Cecil I can see that since the portable version of mscorlib is retargetable, Cecil falls back to the .NET 4 copy so as to locate SuppressILdasm attribute. Then when this attribute is inserted to the assembly, so does that mscorlib. Should we blame Cecil then? Of course not.

## IL-Repack Exceptions on PCL

Another example comes from IL-Repack, a clone of ILMerge, but Mono.Cecil based. When several assemblies are being merged, the PCL ones will trigger [exceptions](https://github.com/gluck/il-repack/issues/58).

So both issues can be [tracked down to Cecil](https://github.com/jbevain/cecil/issues/152).

And the fix IMHO cannot be easily done at Cecil level, as it might not be aware of the reference assemblies.

## Possible Fix

I fixed Obfuscar to add reference assemblies paths to resolver's search paths, and it seems to fix #17. Now I am reviewing IL-Repack to see if the same approach can be used.

Note that such ideas come a long way from my original pull request to ILSpy, https://github.com/icsharpcode/ILSpy/pull/383/files

It is so happy to find that piece of code becomes useful again.

## Update on Oct 12

The pull request is not yet accepted, but I did update it again yesterday to include some revised code. The PCL profile paths added to search path cannot be permanent, or a new issue happens which lets PCL's mscorlib overwrites .NET 4's mscorlib in cache. The latest revision thus adds the PCL paths on demand and then removes them. It is bit of ugly, but avoids changes to Mono.Cecil.
