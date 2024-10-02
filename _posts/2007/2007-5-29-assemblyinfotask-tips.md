---
layout: post
title: "AssemblyInfoTask Tips"
description: "This post describes some tips for AssemblyInfoTask."
tags: Code-Beautifier-Collection Delphi
permalink: /assemblyinfotask-tips-5db57caa1c66
excerpt_separator: <!--more-->
---
AssemblyInfoTask is a MSBuild custom task published on GotDotNet.com. In fact, it is written by a MSBuild team member.

If you want to have assembly version number generated in Visual Studio style (such as 2.1.010529.12), you will love AssemblyInfoTask.
<!--more-->

However, the version available from GotDotNet.com is out-of-date now and lacks of latest updates.

1. The version number mask should be changed according to [this post](https://learn.microsoft.com/en-us/archive/blogs/msbuild/fixing-invalid-version-number-problems-with-the-assemblyinfotask).
1. If you are using SVN to manage the source code, you'd better follow [this post](https://www.andrewconnell.com/blog/using-msbuild-to-generate-assembly-version-info-at-build-time-including-subversion-fix/). The "Subversion Fix" section is very useful.
1. You should copy `%ProgramFiles%\MSBuild\Microsoft\AssemblyInfoTask\Microsoft.VersionNumber.Targets` to a local folder and make the above changes. Then set AssemblyMajorVersion and other properties in the *.targets file. I love this "one targets file one project" way.
1. Do not change your projects like others tell you. Simply create a batch file named `versioningbuild.bat` and write

``` batch
%windir%\Microsoft.NET\Framework\v2.0.50727\msbuild.exe (your.proj) /p:CustomAfterMicrosoftCommonTargets="(localfolder)\Microsoft.VersionNumber.Targets"
@IF %ERRORLEVEL% NEQ 0 pause
```

Note: replace `(your.proj)` and `localfolder` with proper contents.

In this way, if you do not build using this batch file, AssemblyInfoTask will not execute. That's why the version of my project only changes when I release it with `versioningbuild.bat`.

(Updated: Now AssemblyInfo Task is available from [MSDN Code Gallery](http://code.msdn.microsoft.com/AssemblyInfoTaskvers). Tip 2 is also useful if you use CodePlex TFS Command Line Client.)
