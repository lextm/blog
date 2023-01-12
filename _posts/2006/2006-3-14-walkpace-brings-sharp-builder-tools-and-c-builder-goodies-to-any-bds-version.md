---
layout: post
title: "WalkPace brings Sharp Builder Tools and C#Builder Goodies to any BDS version!"
description: A post about how to bring Sharp Builder Tools and C#Builder Goodies to any BDS version as part of CBC
tags: Code-Beautifier-Collection Delphi
permalink: /walkpace-brings-sharp-builder-tools-and-c-builder-goodies-to-any-bds-version-935f0c0f21a4
excerpt_separator: <!--more-->
---
(Originally posted to CSDN on March 14, 2006)

When I finished writing an SDK for BDS OTA for .NET based on SBT's code, I found that I could bring Sharp Builder Tools and C#Builder Goodies to any BDS version using my SDK.

The first milestone you saw is the BF Update 1 or WalkPace Beta I. It contained a version of modified C#Builder Goodies.

The second milestone will be WalkPace Final (I think I will possibly provide some more update for BF users before WP Final).
<!--more-->

## FOR C#BUILDER GOODIES

From now on, I will release a Plus Pack for CBC 2 Basic (the terms will be explained in later articles). C#Builder Goodies functions will be included. After install CBC 2 Basic and Plus Pack, you can enjoy that tool again on any BDS version.

## FOR SHARP BUILDER TOOLS

However, SBT is a huge project to port in. Before my success at last, now I provide you a method to make a SBT for BDS 3/4.

1. Get SBT source.
1. Get LeXDK. Assemblies named Lextm.LeXDK.Core.dll, Lextm.Common and BeWise.Common.

   > You may need to correct the Borland.Studio.ToolsAPI reference.

1. Remove the reference of SharpBuilderTools.Common.dll in SharpBuilderTools.bdsproj.
1. Remove HelpConsts.cs from the project.
1. Add three assembly references in step 2. They should all be copied locally. Compile and see all the errors.
1. Rename all calls (about five places) for GetCsIndentationFromOptions in this project to GetCSIndentationFromOptions. Compile.
1. Build and install.

Then SharpBuilderTools.dll should be able to run on any BDS version (not in BDS 3 currently).
