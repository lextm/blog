---
layout: post
title: "New Inno Setup Installer Script Samples (Version Compare, Running Processes)"
description: "This post is about two new Inno Setup installer script samples."
tags: Inno-Setup
permalink: /new-inno-setup-installer-script-samples-version-compare-running-processes-112b407de77e
excerpt_separator: <!--more-->
---

A long time ago, I used Inno Setup extensively on open source projects, such as Code Beautifier Collection (https://github.com/lextudio/codebeautifiercollection). At that time I was able to share a few tips,

- [Initial post]({% post_url 2007/2007-8-28-inno-setup-script-sample-for-version-comparison %})
- [Better version]({% post_url 2007/2007-9-7-inno-setup-script-sample-for-version-comparison-advanced-version %})

Recently during the development of Touch Mouse Mate, I wrote two new installer scripts which may be interesting for Inno Setup beginners.

https://github.com/lextm/touchmousemate/blob/master/setup/x64/setup.iss

https://github.com/lextm/touchmousemate/blob/master/setup/x86/setup.iss

<!--more-->

## 32 Bit/64 Bit Installers

There are two approaches if your product is going to be installed on both 32 bit and 64 bit Windows. You can write a single installer to support both, or write two installers (one for 32 bit and the other for 64 bit).

I don't like to put all stuffs in one installer as that can make the installer too big (for example, you need to pack both Visual C++ runtime x86 and x64). Therefore, I choose the two installers approach for Touch Mouse Mate.

The following rules are set (avoid possible confusion),

- 32 bit installer refuses to run on 64 bit Windows. 64 bit installer refuses to run on 32 bit Windows.
- Dependencies (such as Visual C++ runtime and .NET Framework) are packed.
- Platform dependent library files are put in different folders (x64 or x86).

## Version Comparison

The version comparison code has been updated slightly in the two installer scripts.

## `psvince.dll` 64 Bit

I am not a Visual C++ expert, and I don't want to waste my time compiling 64 bit `psvince.dll` from source code. Therefore, I wrote a `processviewer.exe` command line utility in Delphi (Turbo Delphi 2006) to provide the same functionality.

However, as this becomes an executable, we have to pack the command line utility and release it to temp folder on demand, which has been demonstrated too in both installer scripts.

Hope you like them.
