---
layout: post
title: "GrapeVine Voice: Break The Path"
description: "This post talks about how to break down the PathTree class into smaller classes."
tags: Code-Beautifier-Collection Delphi
permalink: /grapevine-voice-break-the-path-da7842731d27
excerpt_separator: <!--more-->
---
A PathTree class was used in HardQuery builds to organize all files deployed with CBC assemblies. However, because some of the files are going to be modified in order to store user settings, they cannot be placed in Program Files any more on Windows Vista.
<!--more-->

What I am working at is to break the original tree structure into small pieces and install them into different folders, such as local application data folder and common application data.

It is very very complicated to decide which file goes to where. But it is also a chance that I can fully understand how to install an application for all users and for a single user.

In all, if you install CBC GrapeVine builds, remember that you install it only for yourself. There is no option to install it for all users.

I will try to make an install-for-all installer in later versions.
