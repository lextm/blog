---
layout: post
title: "Switched to AkelPad, a Powerful Notepad Replacement"
description: "This post is about my switch to AkelPad, a powerful Notepad replacement."
tags: Windows
permalink: /switched-to-akelpad-a-powerful-notepad-replacement-5ab9896f70
excerpt_separator: <!--more-->
---
I was using Notepad 2 along with Notepad++. Notepad++ is feature richer but it lacks of an x64 build, while Notepad 2 obviously lacks of lots of features.

A few days along, I came across AkelPad by Internet search, and now I am happy with it except the following facts,

* The developers are not Windows UAC aware. As this application is not designed for Windows Vista and above, you have to install it to a safe place, such as D:\AkelPad on my machine. In this way you will hit less issues.
* The installer sucks as it tries to replace Notepad.exe in the copy and replace manner. Please don't use the replace Notepad mode while installing it. Later I will share a tip on how to replace Notepad in a much better way.
* There is no shell extension to bind to Windows Explorer context menu like Notepad++. Cannot imagine why not.

So please follow the tips to resolve the cons if you feel the same,
<!--more-->

## Replace Notepad

A better way is to use a registry key hack (Process Explorer uses this approach too),

1. Expand `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options` node, and add a new key `notepad.exe`.
1. Add a string value to this new key, and pointed to the path of AkelPad.exe with `/Z`, such as `"D:\AkelPad\AkelPad.exe" /Z`.

## Add to Context Menu

1. Expand `HKEY_CLASSES_ROOT\*\shell` node, and add a new key named `Open with AkelPad`.
1. Under this new key, add `command` as a new key.
1. Change the `(Default)` value to the path of AkelPad.exe with `%1`, such as `"d:\AkelPad\AkelPad.exe" %1`.

## Enable Coder Plugins

By default, syntax highlighting is not enabled, so you need to click Options | Plug-ins menu item, and then enable them in Plugins window.

Hope you like AkelPad. If you have any comments, you may join [its forum](http://akelpad.sourceforge.net/forum/).
