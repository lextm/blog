---
layout: post
title: "HardQuery Report: Milestone 10 and 11"
description: "This post describes the progress of HardQuery."
tags: Code-Beautifier-Collection Delphi
permalink: /hardquery-report-milestone-10-and-11-89695bd67dce
excerpt_separator: <!--more-->
---
(CSDN Sept 11, 2006)

You have to wait a few days more since I need to test HardQuery Final more than ever, and wish it will be a stable enough version. However, I still publish some milestone versions to keep you update and away from bugs.
<!--more-->

In M10, I ported Liz's Readme Viewer from delphi to C#, because I found there are some problems to build a delphi for .NET plus based on LeXDK (terrible). Now I guess something wrong with CLR Compatibility. Maybe I miss some settings. I will dig it later. This feature is included in WiseEditor Plus now. Whenever you open a project including a readme file (e.g. Readme.txt, Readme.rtf, and so on), the readme file will be opened automatically for you.

Also, I updated the Inno Setup script to add ArtCSB Plus Beta inside.

In M11, more bugs are removed and some important changes take place.

Why it is fast named as M11 just one day later? There is a big improvement on CodeBeautifiers Plus, the UNDO support. If you read along this log you will know I had done an AStyle plugin for SharpDevelop. Since its Beta 1 cannot handle reloading after astyle.exe processes the file correctly, when I announce it on the SharpDevelop User Community, I ask for help.

I never dreamed Daniel Grunwald would answer my question, who is a major developer of SD. He suggested me making a temporary file aside, formatting it and loading it directly to SD editor's buffer. As a result, this kind of formatting can enjoy SD's undo service.

Today, I successfully finished the Beta 2 of that SD plugin. What's more? After analysing WinMerge feature's code, I found David manipulated BDS editor's buffer there. I went deeper into OTAUtils unit and found FillBufferWithFile and CreateFileFromBuffer right in the place.

Although David did not leave a comment, you and I could understand the functions immediately. As a result, I redid something inside the CB Plus and everything was okay. However, the process was not quite easy.

David's FillBufferWithFile implementation had bugs. After reading some OTA materials I found a solution after a few trials (poor documented OTA!!!).

I was hurried to bring UNDO service in but I broke the old architecture inside CB Plus. Now, Project and Project Group menu items are disabled. I will make them work later. I do not know whether it will be in M11 or in a hotfix.

Stay tuned.
