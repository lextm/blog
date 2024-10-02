---
layout: post
title: "How I Got Start Menu Back in Windows 8 with Free Stuffs"
description: "This post is about how I got start menu back in Windows 8 with free stuffs."
tags: Windows
permalink: /how-i-got-start-menu-back-in-windows-8-with-free-stuffs-b1a6f0d84a53
excerpt_separator: <!--more-->
---
I played with Stardock's Start8 since its initial release, but since Stardock would like to make some fortune from this useful tool and I did not plan to pay, I have been searching for a free alternative for a while. Today I think I have found the last piece, so here comes a blog post that covers my findings.
<!--more-->

## Classic Shell

http://classicshell.sourceforge.net

First please download and install this utility (Only Classic Start Menu component is needed, but you might try out Classic Windows Explorer and others) which will add a start menu back. By right clicking on this new start button, you can open its Settings dialog. Here are the settings I recommend,

1. Click on All Settings radio button at bottom.
1. Go to Windows 8 tab.
1. Select Skip Metro screen.
1. Choose All for Disable active corners.
1. Go to Start Button tab.
1. Choose Aero Button under Button Look, or choose Custom Button (more in following section).
1. Click OK to close the dialog.

Now you can click on the start button and check out how the start menu looks like.

## Removing Metro Applications

Right click on the start button and choose Exit menu item. It's time to go back to Metro and remove applications that might pull you out of the desktop. Below is a list of apps I removed,

* Picture
* Messenger
* Mail
* Music
* Video
* and many others

Now let's go back to C:\Program Files\Classic Shell and double click ClassicStartMenu.exe. We are almost done.

## Find a Windows 7 Start Button Icon

The last bit that bores me is that Classic Shell does not have a good enough icon for the start button. Luckily today I found one.

1. Download Windows 7 Start Button Changer from here, http://www.thewindowsclub.com/windows-7-start-button-changer-released
1. Unzip the package and find Start Orb (1).bmp from 10 Sample Orbs folder.
1. Go to step 6 in first section and choose Custom Button.
1. Change Button Image so it points to this BMP file.
1. Set Button Size to 0, so the original BMP image size will be used.
1. Click OK.

After all these changes, now the Windows 8 at your hand looks almost the same as its brother Windows 7.
