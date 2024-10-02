---
layout: post
title: "The Success of Running MonoDevelop 7 on Linux"
description: "This post is about how to run MonoDevelop 7 on Linux."
tags: Mono Linux
permalink: /the-success-of-running-monodevelop-7-on-linux-a55f1469b1d1
excerpt_separator: <!--more-->
---
I still remembered the pain of running MonoDevelop 7 on FlatPak on Linux, but today finally decided to give the alternative way a go, and indeed it worked. So here is the story.
<!--more-->

## Installing Debian
So this time I switched to Debian 8.

## Installing Mono 5
Luckily the steps for Mono 5 installation on Debian worked flawlessly.

## Using Third Party MonoDevelop Installer
So this guy amazingly maintains [an alternative installer](https://github.com/cra0zy/monodevelop-run-installer) for MonoDevelop 7. I downloaded its latest release, and followed the readme steps to install.

## Launching MonoDevelop 7
OK, this time you should see a MonoDevelop Stable launcher in GNOME to launch the IDE. Or if you prefer command line, run `monodevelop-stable`.

## Fighting The First Issue

You probably would like to run a hello world project to test it out like I did. Then you probably would hit this famous error ("Could not connect to the debugger". Well, guess what, it is quite simple to fix it.

Open the project options (you should know how to do so). It is very likely that "Run on external console" is checked (as it is the default setting), under Run -> Configurations -> Default.

You have to uncheck this option. Then MonoDevelop would use its integrated terminal to run the console project.

## The xUnit.net Extension

If you happen to want to run xUnit.net test cases (when the project is not .NET Core based), you need to manually install [the extension I maintain from here](https://github.com/xunit/xamarinstudio.xunit).

Enjoy it.
