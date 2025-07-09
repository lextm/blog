---
description: This post talks about a limitation of InstallAware MSIcode.
excerpt_separator: <!--more-->
layout: post
permalink: /installaware-msicode-limitation-e2e6c6aedeb
tags: windows
categories: [Operating Systems]
title: InstallAware MSIcode Limitation
---
You cannot write a loop in MSIcode, which sometimes makes things a bit bitter. For example, my uninstaller should wait to start uninstallation until the application exits. Generally speaking, it requires a loop to implement this wait behaviour.
<!--more-->

Is it caused by a MSI limitation? I do not know. So for this moment, my uninstaller will simply aborts with a warning. At least, this provides enough information to my users.

So sometimes I do miss Inno Setup, which is both localization friendly and Pascal script based.

BTW, IA is still a great product, because it handles complex installation for me (and a lot of others, such as CodeGear Delphi).
