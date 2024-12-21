---
layout: post
title: "Delphi Prism, My Take"
description: "This post is about my personal ideas about the changes on Delphi for .NET side."
tags: Delphi .NET
permalink: /delphi-prism-my-take-3bcb11339c73
excerpt_separator: <!--more-->
---
Finally Delphi Prism is officially launched (the announcement was made during PDC 2008). So everyone can read about it here and there . Therefore, I don't need to cut and copy the words here. This post will only express my personal ideas about the changes on Delphi for .NET side.
<!--more-->

## VCL for .NET
It is sad to see this library finally fades out. But luckily no big applications were built upon it. However, I find this line in FAQ funny.

"Developers using VCL.NET can either use Delphi 2007 to continue those products or can migrate their VCL.NET applications to VCL for Win32."

Well, didn't those VCL for .NET applications come from VCL for Win32? :)

## Delphi for .NET Compiler
This compiler is gone. Now Delphi Prism uses RemObjects' Chrome/Oxygen compiler. Hope that in the future features like Class Helper can be implemented by the RO guys (it is promised that both CG Delphi compiler and RO Oxygen compiler will share a certain amount of features, so nice idea). Maybe later we can see an Object Pascal language specification published by the two entities. Of course there may be some "Win32/64 extensions" and ".NET/Mono extensions".

## Linux and Mac OS X
People have been asking for Kylix revival for years, and now I guess it comes back in a managed way. Right, you can use Delphi Prism to target Mono platform from Novell. In such a way your applications can run on Linux and Mac OS X finally. Though not perfect, it is a way.

## Visual Studio Shell
The biggest change for most Delphi developers must be the IDE. Delphi Prism can be viewed as a bunch of utilities (compiler, wizards, and frameworks) plugged into Visual Studio Shell, which is a free RCP tool provided by Microsoft. Therefore, the code editor and form designer are totally the same for Delphi Prism and Microsoft C# developers.

So there would be no GExperts or CnWizards , or Castalia , but at last CodeRush is there.

## Conclusion
Have been waiting for this day for a long time, so I just cannot wait to touch Prism. Luckily it will be released soon.
