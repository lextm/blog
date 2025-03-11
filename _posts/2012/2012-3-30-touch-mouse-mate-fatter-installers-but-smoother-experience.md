---
layout: post
title: "Touch Mouse Mate: Fatter Installers But Smoother Experience"
description: "This post is about the latest news of Touch Mouse Mate."
tags: Windows
permalink: /touch-mouse-mate-fatter-installers-but-smoother-experience-62030cdf0c90
excerpt_separator: <!--more-->
---
If you subscribed to Touch Mouse Mate CodePlex homepage for every changes, you will notice that recently though the binary version number remains, the installers have been updated several times. That's because I was tuning the installation experience step by step.
<!--more-->

The following changes have been made,

* .NET Framework 4.0 and Visual C++ 2010 runtime have been bundled in TMM installers. This increases the size of both installers significantly, but end users needn't to find such dependencies themselves (especially when they are not IT experts).
* If TMM is still running, the installers provide an option to help kill it before installing/uninstalling.
* The 64 bit installer will refuse to run on 32 bit Windows.
* Windows XP SP3 is now the oldest Windows version supported.
* We use a home cooked utility to detect running TMM instead of psvince.dll. Initially was written in C#, but later rewritten in Turbo Delphi 2006. This rewritten is a must for generic usage, as not every Inno Setup based installer bundles .NET Framework like TMM.

So hope you are not surprised to see the fatter installers, and enjoy the smoother installation experience.

Stay tuned.
