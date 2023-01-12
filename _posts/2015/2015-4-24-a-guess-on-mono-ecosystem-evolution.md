---
layout: post
title: "A Guess on Mono Ecosystem Evolution"
description: "This post is about how I guess Mono ecosystem will evolve in the future."
tags: Mono
permalink: /a-guess-on-mono-ecosystem-evolution-b096ccad6600
excerpt_separator: <!--more-->
---
Mono has been there for years and grown from its first component (Mono C# Compiler)[1] to a large platform (with multiple components). Each components were written at a certain phase due to the demands then, but primarily speaking they all come to make Mono useful for non-Windows operating systems.
<!--more-->

## The Foundation

The foundation components are the CLR, BCL, compilers, AOT and other basic utilities (such as xbuild) not listed. Without them, no application can run at all.

## The Application Frameworks and Libraries

To integrate with Linux and other operating systems' native API, and expose their functionalities, many other components are developed along the way, such as

* GTK# to expose GTK+ API.
* MonoMac to expose Cocoa API.
* Mono WinForms to simulate Microsoft's WinForms API.
* XSP to enable web application hosting.
* Mono.POSIX to expose POSIX API.
* Novell.Directory to expose LDAP API.

Since there are tons of tiny libraries there to enrich Mono, many are not listed in the diagram. [2]

If we compare Mono to Microsoft's .NET, we might get a few interesting facts.

1. The two has significant different application frameworks and libraries at top.
1. Their foundation components are similar.

The similarity can be further analyzed, that

* Mono CLR/FX follows the same ECMA standards, and attempts to be compatible with Microsoft's implementation throughout the years. The evidence can be found from Mono bug trackers (I personally fired a few compatibility issues and saw them closed as fixed). [3]
* Mono C# Compiler has been quite impressively compatible with Microsoft's old csc.exe, and now Roslyn. Its performance is even better than Roslyn at this stage. [4]
* Mono AOT has been there for years, while Microsoft just started its .NET Native runtime to catch up.

## The Possible Approach to Merge

Since last year Microsoft opens source Roslyn and .NET Core, Mono project has been actively investigating a suitable approach to use Microsoft's code [5]. The rationales are,

* Better compatibility. You won't be surprised that many BCL classes are now exactly the same (in Mono 4.0).
* Shifting focus. With Microsoft's stepping in to maintain the cross platform CLR/BCL and compilers (as well as MSBuild, the build engine), duplicate efforts can be avoided. The community can move to work on other areas (such as writing new application frameworks and libraries).

So in Mono 4.0 and its later revisions, we might see the ecosystem changes.

## The Xamarin Storyline

The products under Xamarin umbrella have built up their own ecosystem.

What might happen for Xamarin's ecosystem? We will see.

## References

[1] Mono history can be found at [Wikipedia](http://en.wikipedia.org/wiki/Mono_(software)).

[2] Further info on Mono components can be found at [Mono Project Site](http://www.mono-project.com/).

[3] Mono bug tracker can be found [here](http://www.mono-project.com/community/bugs/).

[4] Mono's plan on adopting Roslyn can be found [here](http://tirania.org/blog/archive/2014/Apr-09.html).

[5] Mono's approach to integrate Microsoft source code is listed [here](http://www.mono-project.com/docs/about-mono/dotnet-integration/).
