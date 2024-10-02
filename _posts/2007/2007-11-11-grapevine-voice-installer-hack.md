---
layout: post
title: "GrapeVine Voice: Installer Hack"
description: This post talks about a GrapeVine hack during installation.
tags: Code-Beautifier-Collection Delphi
permalink: /grapevine-voice-installer-hack-840558857a23
excerpt_separator: <!--more-->
---
Install CBC for all users is not easy. I decide to hack bds.exe so as to make it easy. If every time bds.exe is launched, CBC registry key is checked, I can ensure CBC installed for all users (in fact if CodeGear does this for me and other developers it would be appreciated).
<!--more-->

I do not want to modify bds.exe because I am not aware of how to. Therefore, I prefer an easier way. I create a bds.exe myself, and then rename the original one to bds.real.exe. My bds.exe will check registry keys at first and launch bds.real.exe at last.

This hacking introduces several problems. First, bds.exe.config may not be loaded correctly. Second, you may not be able to install later Updates from CodeGear with CBC M9 installed. Third, RAD Studio official binaries are touched.

In upcoming releases, I may try to write a design time package to do similar tasks which should be a safer way.

However, you know I am not totally sure a design time package can do this all. So stay tuned.
