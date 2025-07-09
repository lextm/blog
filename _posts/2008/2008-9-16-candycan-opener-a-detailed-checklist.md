---
layout: post
title: "CandyCan Opener: A Detailed Checklist"
description: This post talks about the next major release of Code Beautifier Collection.
tags: Code-Beautifier-Collection Delphi
permalink: /candycan-opener-a-detailed-checklist-9fe92aa18c59
excerpt_separator: <!--more-->
---
Now I am trying to record a full checklist of every change I made to support Delphi 2009 in CBC 7.0.
<!--more-->

The changes are,

1. Modify OtaUtils.cs to support IDE 6.0 and adapt to registry root name change. (done)
1. Test ExpertManager and it works. (done)
1. Change version number in Microsoft.VersionNumber.targets to 7.0. (done)
1. Open all *.csproj files and replace old ToolsAPI references to new ones. (done)
1. Search for all RAD Studio 2007 strings and replace with RAD Studio 2009. (done)
1. Search for all Code Beautifier Collection 6 strings and replace with 7. (done)
1. Search for all GrapeVine strings and replace with CandyCan. (done)
1. Open setup.iss, and replace the old GUID with a new one. Then update all information necessary. (done)
1. Update InDate so it searches for cc*.zip from the homepage instead of gv*.zip.
1. Update PropertyRegistry or Path so it looks for dependencies in version number based folders.
1. Update bundled JCF and JCFStyle executables.
1. Update all source code related to Unicode (done, but need to test).
