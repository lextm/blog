---
layout: post
title: "New Project: MSBuild Launch Pad (mPad)"
description: This post is about my new project MSBuild Launch Pad.
tags: .NET
permalink: /new-project-msbuild-launch-pad-mpad-e1ce8c5acb15
excerpt_separator: <!--more-->
---
I used MSBuildShellExtension years ago. It was a nice helper when there was only .NET 2.0. But once .NET 3.5 came, it did not adapt to it as I wished.
<!--more-->

It was a few days ago I joined a StackOverflow thread, http://stackoverflow.com/questions/2833327/build-item-in-windows-explorers-context-menu-of-a-vs-solution-file/2834092#2834092 and suggested MSBuildShellExtension again. However, when myself checked out its homepage I noticed the project has been idle for a very long time.

It still has the following disadvantages,

1. It does not choose MSBuild version smartly by stepping into the script files. Manually selecting MSBuild version is not easy for beginners.
1. It does not parse the script files to see what targets are supported. If the files can be at least analyzed, end users can select which target to be called easily.
1. .NET 4 is now released, and MSBuildShellExtension does not yet support it.
1. Windows Vista and Windows 7 introduce UAC. But the Configurator does not work well with UAC.

I was planning to join this project and bring in some update, but why not start from a new perspective and write something new from scratch?

Here comes MSBuild Launch Pad, https://github.com/lextm/msbuildlaunchpad, my fourth CodePlex project (my fifth open source project).

Itself contains a launch pad application who parses sln/csproj/vbproj/vcxproj files to determine which MSBuild version should be used.

It will support proj files and other famous MSBuild based solutions (Delphi Prism, Sandcastle Help File Builder, WiX) in the future releases.

Still MSBuildShellExtension is being used to display MSBuild logs.

If you are interested in the new project, please drop me your comments.
