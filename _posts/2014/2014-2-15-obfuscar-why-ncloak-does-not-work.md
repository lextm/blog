---
layout: post
title: "Obfuscar: Why NCloak Does Not Work"
description: "This post talks about why NCloak does not work."
tags: .NET
permalink: /obfuscar-why-ncloak-does-not-work-f4ed152f06dd
excerpt_separator: <!--more-->
---
Mono.Cecil is an important library which enables very easy MSIL/CIL manipulation. Upon it several projects are built, both commercial and open source. In obfuscator land, Obfuscar is such a typical example, but it is obviously not the only one.
<!--more-->

NCloak is another MIT licensed obfuscator based on Mono.Cecil and it introduces a few interesting features,

* Full obfuscation of all members (already in Obfuscar)
* String encryption (already in Obfuscar)
* Simplification and Optimization of code
* Anti-reflection and anti-ildasm methods
* Basic tamper proofing solution (resource based)

Is it possible to reuse some of the code in Obfuscar? I just finished a few experiments.

* Sadly its code simplification code cannot be used, as .NET CLR (at least 4.0) does not recognize the generated assembly.
* For the same reason, anti-reflection is also broken.
* Basic tamper proofing seems to be experimental, so I did not touch it.
* Anti-ildasm is almost useless.

Thus, the last useful bit is code optimization. As a result, a new option is now added, named `OptimizeMethods`.

There are other open source obfuscators, but their licenses are too restrictive, and I could not reuse their code at this moment.

