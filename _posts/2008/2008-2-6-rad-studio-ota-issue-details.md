---
layout: post
title: "RAD Studio OTA Issue Details"
description: This post describes how I find a bug in RAD Studio OTA.
tags: Code-Beautifier-Collection Delphi
permalink: /rad-studio-ota-issue-details-6e111b51c005
excerpt_separator: <!--more-->
---
Now I'd like to introduce how I find this bug.
<!--more-->

## The Background and Steps

I'd like to modify AddMany (CodeCentral entry #25077) project without breaking the original source code. Thus I did the following,

1. copy the project file AddMany.dproj to Lextm.AddMany.dproj.
1. open the new project in Delphi for .NET.

Then the issue came that IDE thought the output should be Lextm.AddMany.dll while the correct one is AddMany.dll because the real project file is still AddMany.dpr.

Also when I tried CBC's Delete Project Target, CBC said that target does not exist. Then I debugged inside and saw that IOTAProject.ProjectOptions.TargetName is wrong. The returned string is `***\Lextm.AddMany.dll` while the expected is `***\AddMany.dll`.

Luckily [the workaround is described here]({% post_url 2008/2008-2-6-rad-studio-ota-issue-details %}) so if you also meet this issue you can try my code.

## Update:

This bug is logged as QC#57890. And it applies to both Delphi for Win32 and .NET DLL/BPL projects. Strangely it does not affect EXE projects.
