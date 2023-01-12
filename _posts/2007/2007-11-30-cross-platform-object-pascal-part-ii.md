---
layout: post
title: "Cross Platform Object Pascal (Part II)"
description: This post compares Delphi and Chrome.
tags: Delphi
permalink: /cross-platform-object-pascal-part-ii-6d3ac47874e7
excerpt_separator: <!--more-->
---
In this part, I am going to do comparison between Delphi and Chrome. I try to illustrate why Delphi goes this way and Chrome approaches another. Correct me if anything is wrong.
<!--more-->

## The IDE

Chrome package consists of a runtime plus a Visual Studio plug in. The runtime ensures you can build and run Chrome applications without any IDE which is also named the command line version of Chrome.

In the past, Chrome VS plug in enables you to develop Chrome WinForms and WebForms applications in VS. And now, the plug in also enables you to develop Cocoa# applications for Mac OS X in Visual Studio.

Because Visual Studio 2008 introduces something named Shell, I guess one day RemObjects can build a standard alone Chrome IDE within it.

RO preferred Visual Studio because,

1. RO does not have an IDE.
1. Visual Studio is stable.
1. no need to maintain this IDE.

Borland used its own IDE because,

1. you can do anything in the IDE. That is why we have Together and Live Templates now.
1. no need to sell Visual Studio with Delphi.
1. there was no Shell at that moment and Eclipse was not perfect.

After about 3 years, everything changes. Now, Eclipse based IDE is so popular (CodeGear uses it for JBuilder and 3rdRails) and Microsoft releases Visual Studio Shell. Look like that RO made a better choice.

RO announces that it will add support to MonoDevelop. Let's wait and see what will happen.

## The Language

I do not want to start a language war.

Chrome is purely .NET and no VCL is there. Therefore, learning Chrome is like learning C#.

Delphi has VCL, so you need to learn it as well.

Both languages are evolving. RO and Borland/CodeGear did add a few interesting extensions to Pascal, an old language, but most of them are not well known.

Chrome does not support Win32, and Delphi does not support .NET 2.0, 3.0, and 3.5 completely (e.g., no visual editor support for Windows Forms and WPF).

## The Conclusion

You must make a choice if you want to learn Object Pascal today, but if you already use either of them, stick to it and keep an eye on the other.
