---
layout: post
title: "OTA/.NET Compatibility Tests"
description: This post is about the compatibility tests of OTA for .NET.
tags: Code-Beautifier-Collection Delphi
permalink: /ota-net-compatibilty-tests-6bf780a81a54
excerpt_separator: <!--more-->
---
(CSDN June 08, 2006)

Using OTA for .NET, David made SBT for different BDS versions easily.

There is fewer `#if`s because almost all interfaces in Borland.Studio.ToolsAPI.dll (4 versions now) are the same.

However, there are some important differences CBC meets.
<!--more-->

First, IOTAModuleServices does not have a ActiveProject property in BDS 1.0. So I have to modify Lextm.AddMany project, and replace calls for the property (there is a workaround so I can make it).

Second, `IOTAGalleryCategoryManager`'s `FindCategory` is not overloaded in BDS 1.0. So

``` csharp
IOTAGalleryCategory _Cat = _GalleryCategoryManager.FindCategory(OTAGalleryCategories.sCategoryRoot);
```

inside FileWizards raises exception under BDS 1.0. I change it to

``` csharp
IOTAGalleryCategory _Cat = _GalleryCategoryManager.FindCategory("Borland.Root");
```

and hope it will be okay.
