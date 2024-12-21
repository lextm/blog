---
layout: post
title: "CatPaw Rumors: Repository Access, Good Mixture Or Bad?"
description: "This post is about repository access issues on MonoDevelop on openSUSE"
tags: SNMP
permalink: /catpaw-rumors-repository-access-good-mixture-or-bad-e2aaebc1d686
excerpt_separator: <!--more-->
---
In order to test out #SNMP on Mono/openSUSE, I start to use MonoDevelop on openSUSE and it works fine in many aspects. But well soon issues arise.
<!--more-->

I have used the following access methods to CodePlex repository and they work fine together,

1. Visual Studio 2010 (Team Explorer is included) on Windows.
1. SharpDevelop 3.2 (with TortoiseSVN) on Windows.

You may ignore how much effort SD team pay to make this smooth. When MonoDevelop on openSUSE is involved, incompatibilities reveal. MonoDevelop makes use of MSBuild script based csproj file differently,

1. AssemblyInfo Task settings are not honored. I don't know if this is a Mono issue or AssemblyInfo Task issue.
1. Once a project is modified in MonoDevelop and checked in, Visual Studio will try to upgrade it. This indicates that MD does not generate proper MSBuild script in the project file.

Therefore, I won't check in any project files again from Mono side, until MD team resolve such incompatibilities.

Well, it is really amazing to see that MonoDevelop on Windows is much poorer than its build on openSUSE. Why? :)
