---
layout: post
title: "GrapeVine Voice: Prepared for First Preview"
description: "This post describes about GrapeVine release."
tags: Code-Beautifier-Collection Delphi
permalink: /grapevine-voice-prepared-for-first-preview-f7d5334d6d7a
excerpt_separator: <!--more-->
---

Delphi for .NET will only support VCL for .NET designer in Highlander, which means WinForms with Delphi for .NET becomes obsolete. So now I am not sure that some assemblies used in CBC can be still used.

Today I test and see that Mauro Venturini's Invisibles library and Visibles library are not compatible to .NET 2.0 (they refer to Borland.Delphi 10 which no longer exists). The solution for TBackgroundWorker component is to use BackgroundWorker directly. For Visibles library I have to disassemble it to C#. Reflector accomplishes this well.

At last, WebBrowser ActiveX is removed. WinForms WebBrowser component is used instead.

Compile, and everything is alright.

Because I have to setup the whole build environment, it takes time to release a preview.

Stay tuned.
<!--more-->