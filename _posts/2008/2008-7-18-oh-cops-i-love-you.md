---
layout: post
title: "Oh Cops, I Love You"
description: "This post talks about the static code analysis tools that help me to write better code."
tags: .NET
permalink: /oh-cops-i-love-you-3d72b598ceac
excerpt_separator: <!--more-->
---
It is really hard to master coding, because you are not just simply implementing a feature of your project. Writing solid code, secure code, and beautiful code is not a day dream.

At this moment, I feel like upgrading my coding style, so I find myself resort to Effective C# a lot. But, it is not always easy to find bad code just by my eyes. Then I feel luckily as a C# developer, because there is a lot of cops around me to help.
<!--more-->

## Microsoft Code Analysis (FxCop)

This was a popular GotDotNet project, and from the old days I have forced myself to fix most violations it report. Generally speaking, FxCop points out best practices you should follow when using and designing elements. I love the name checker a lot, and also the localization helper.

Because Microsoft decides to merge FxCop functions into Visual Studio (for above-Pro editions only), I am afraid that one day I may not be able to get help from FxCop.

The latest version from Microsoft is 1.36

## Microsoft Source Analysis (StyleCop)

StyleCop focuses on source files. It helps you to develop a common coding style with others easily.

The latest version from Microsoft is 4.2. By default it only supports non-Express VS, but there is also an addin for SharpDevelop 3 here.

## Novell Mono Gendarme

Gendarme implements certain amount of FxCop features while providing new rules. Because it is open source, you can feel free to extend it whenever suitable.

At this moment, 0.2 is released for Windows. You can find it in Google Group for Gendarme.

## NDepend

NDepend provides a powerful query language named Code Query Language for you to query information from MSIL. It is a perfect way to dig deeper under the surface. However, I always find it hard to master because there are so many important features and tricks. Hope some day I can spare a whole week playing with it to investigate all its abilities.

## Conclusion

You'd better start new projects with these cops so they can help you from day one. And if you use them to analyze a legacy project, there might be thousands of violations.
