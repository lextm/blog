---
layout: post
title: "CBC TechNote: How to solve the coupling effect with SBT?"
description: A post about how I kept my code isolated from David's Sharp Builder Tools.
tags: Code-Beautifier-Collection Delphi
permalink: /cbc-technote-how-to-solve-the-coupling-effect-with-sbt-6fde78543560
excerpt_separator: <!--more-->
---

(Written on 2005–10–6, originally posted to CSDN on Nov 03, 2005, republished here with some modifications)

The architecture of CBC (JCF Expert) was SBT v0.9. I chose it because it was included in Delphi 2005 (and C#Builder 1.0) and it was simple enough for me to modify. So in the beginning, I put new code inside David's files. The result is a bad/ugly piece of software.

I decided to change my approach in CBC v2.0, but at this very moment, I have not enough time to sacrifice. Later I would do it. What I could do is still evolving in SBT v0.9's architecture, but isolating my code out of David's and putting them somewhere else.

I tried to make use of SharpBuilderTools.dll at first, in order to skip a lot of porting work. But SBT wizards have a tight tie to the plug-in's uncustomizable Configuration class preventing me from adding my configurations (that should be a refactoring chance, since it disobeys the Open Closure principle).

So now, I have to drop this simple idea, and implement more classes. I chose not to crack SBT files, since I'd better to do more by myself, if I want to learn the architecture better. Finally I decided to keep as many files untouched as I can, but crack a few file, such as `Configuration.cs`.

Unbelievable that I finally made it. CBC v2.1 is the result. SBT files are put into SBT directories. Also, some of my classes are inheriting from SBT's classes. I extends its architecture in this way.
