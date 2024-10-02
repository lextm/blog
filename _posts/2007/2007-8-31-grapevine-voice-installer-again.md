---
layout: post
title: "GrapeVine Voice: Installer Again"
description: "This post is to update M3 installer."
tags: Code-Beautifier-Collection Delphi
permalink: /grapevine-voice-installer-again-5e2dba96f20e
excerpt_separator: <!--more-->
---
When I published this post, I did not expect ISPP changed most of things easily.

## What is ISPP?

ISPP is Inno Setup Pre-Processor. From its name you can guess what it does. Yep, it preprocesses your script and then builds the installer. In this way, ISPP provides you so many macros and build-in functions which free you from writing error prone Pascal scripts.

## Changes

Now I use marcos to store version information and other strings. Thus, every time I need to create an installer, only a few changes are required. When I release 6.0 M5, you can check up the new Inno Setup script for details. Also you need to install Inno Setup QuickStart Pack instead of Inno Setup.

## Limitation

Although ISPP solves a lot of problems, it is hard to write my own functions in its language. It is not similar to Pascal but C/C++. Luckily right now I do not need to do some customization here.

I am still planning about M5 because a plan is not yet finished. Stay tuned.
<!--more-->