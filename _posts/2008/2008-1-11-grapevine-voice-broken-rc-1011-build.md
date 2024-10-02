---
layout: post
title: "GrapeVine Voice: Broken RC 1011 Build"
description: This post talks about the broken RC 1011 build.
tags: Code-Beautifier-Collection Delphi
permalink: /grapevine-voice-broken-rc-1011-build-314829bbea70
excerpt_separator: <!--more-->
---
The installer of RC 1011 build is broken. A critical library called PSTaskDialog.dll is missing simply because I forgot to update Inno Setup script again. It is sad that I cannot find out how to ensure all required .NET libraries are there in the installer until the users get a runtime exception. This is a .NET limitation blamed by nearly every .NET developers (not a bug of Inno Setup).

I am going to release another RC this weekend, build 1012. The default start menu group name for GrapeVine would be changed to "Code Beautifier Collection 6" so as to work side by side with HardQuery installed on your machine. Stay tuned.
<!--more-->