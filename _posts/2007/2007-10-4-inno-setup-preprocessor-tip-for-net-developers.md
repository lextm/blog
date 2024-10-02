---
layout: post
title: "Inno Setup Preprocessor Tip for .NET Developers"
description: "This post talks about how to use ISPP for .NET developers."
tags: Inno-Setup .NET
permalink: /inno-setup-preprocessor-tip-for-net-developers-a4bece8d7349
excerpt_separator: <!--more-->
---
I love ISPP because it really makes things easier. But .NET sometimes brings differences. For example,

``` ini
#define MyAppVersion GetFileVersion("..\bin\release\Lextm.CodeBeautifierCollection.Framework.dll")
```

Because my assembly is .NET and I forget to set AssemblyFileVersion attribute in code, MyAppVersion is empty! How dangerous! That's why GrapeVine M4 and M5 installers does not save version information into registry.

Generally speaking, for .NET assemblies, AssemblyVersion is more common. You just need to specify AssemblyFileVersion so as to make them similar to Win32 DLLs.

I'd like to make AssemblyVersion equal to AssemblyFileVersion. However, if you take a look at CodeGear RAD Studio assemblies, you may find something different.
<!--more-->