---
layout: post
title: DockPanel Suite 3.1.0 Release
description: A post about DockPanel Suite 3.1.0 release and my departure from this open source project
tags: Windows .NET Visual-Studio
excerpt_separator: <!--more-->
---

I just published DockPanel Suite 3.1.0 release on NuGet, almost three years after the 3.0.6 release.
<!--more-->

## Changes in This Release
First, this release does not introduce too many changes. Its initial goal was to put VS2005 theme in its own NuGet package, so that developers who choose to use a modern theme (like one of VS2015 themes) do not have to pay the price of bundling another theme. However, this isn't a simple change either, because the code base was tightly coupled to a default theme. So, as the final solution I had to develop a new theme with almost no visuals and make it the new default.

Second, to better support .NET Core based projects, this release started to use the SDK style project format and generate assemblies for .NET Framework 3.5/4.0 as well as .NET Core 3.1. This change introduced [the biggest issue](https://github.com/dockpanelsuite/dockpanelsuite/issues/616) so far on building/shipping DockPanel Suite, which took about a year to resolve.

Other changes are minor, but might have an impact on usage, so before upgrading to this new release you should test your apps thoroughly.

## My Retirement Plan
I started to work as a maintainer of DockPanel Suite because of my personal projects that rely on this component. However, now I have no active WinForms project that depends on DockPanel Suite, and my personal focus has moved to new stacks such as Angular/React/Blazor.

Therefore, here I announce my plan to retire from this maintainer role. If someone reading this would like to take it over, please feel free to follow [this GitHub issue](https://github.com/dockpanelsuite/dockpanelsuite/issues/663).

> If you are looking for alternative options, you will find [Krypton Docking](https://github.com/ComponentFactory/Krypton) has been open sourced. One of its derived works quite active and might help you out.
