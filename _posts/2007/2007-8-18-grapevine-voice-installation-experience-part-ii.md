---
layout: post
title: "GrapeVine Voice: Installation Experience (Part II)"
description: "This post talks about the installation experience of GrapeVine build."
tags: Code-Beautifier-Collection Delphi
permalink: /grapevine-voice-installation-experience-part-ii-b2899f34a18d
excerpt_separator: <!--more-->
---
For MSI installers, it seems easier to install for all users. I do not have time to study MSI, so I try to make something similar with Inno Setup.
<!--more-->

Registry manipulation is an important issue here. At startup Delphi 2007 finds experts in registry under LocalMachine and CurrentUser branches. So if CBC is installed for all users, the expert registry entry must be placed under LocalMachine while for one user under CurrentUser.

However, Inno Setup does not support install for all users natively, which means the installer cannot copy preferences files into every users folders. Because Program Files and other common folders are now critical folders on Windows Vista, I make use of Delphi IDE so as to complete the installation which turns out to be an easy way out there.

And luckily I find out that I can divide the whole installation into two separable phases,

1. Installer installs all files into Program Files, installs GAC assemblies, and creates a registry entry for CBC.
1. When Delphi starts up and CBC is loaded into Delphi, CBC copies preferences files from Program Files to user's local folder.

In this way, I can finally make install for all users possible.

Actually that's why I add two installer helpers.

## Phase 1

When you double click installer, in fact the installer only extract all files into Program Files folder. Then installforallusers.exe, a helper, is launched. You can then decide whether to install CBC for all users. If for all users, a registry entry is added to LocalMachine. Otherwise, the entry is added to CurrentUser.

## Phase 2

When Delphi is fired, CBC should be loaded if a registry entry is there. If CBC is already installed, nothing would happen. If not, CBC copies preferences files into user' local folder by calling another helper, installforcurrentuser.exe.

In order to prevent double copy, a new registry entry is added under CurrentUser. The entry value is CBC version number. If a newer version of CBC is installed, preferences files will be updated because the registry entry value is lower than the just installed CBC.

Because it is hard to remove preferences files from local folders, I decide to leave them there.

## Conclusion

I have to say I made a lot of changes in the installer of M3. Thanks for Tom's reports I fixed most bugs. If you meet bugs during installation, please contact me immediately.

How do you make installer? Use old-fashioned InstallShield or newly-available InstallAware or use other techniques? I'd like to know.
