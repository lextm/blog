---
layout: post
title: ".NET on Linux: Mono installation on Ubuntu, Revisited"
description: "This post describes how to install Mono on Ubuntu, and how to fix the problem when MonoDevelop cannot run."
tags: .NET Linux Mono
permalink: /net-on-linux-mono-installation-on-ubuntu-revisited-9143dba89b99
excerpt_separator: <!--more-->
---
(CSDN Oct 08, 2006)

Something I mentioned in this blog is not always successful even for myself this time. Yes, when I gave up VMware workstation and installed Ubuntu directly via CD-ROM, I cannot get MonoDevelop run. Luckily, I could read the error information in the Terminal and followed instruction page here to fix it (Remember there is always help around the universe).

In fact, the installer failed to add some environment parameters. By using a Terminal (bash), a few "export" commands could make everything okay. Yes, finally MonoDevelop ran well again.

Wish you enjoy Mono on Ubuntu. Some WinForms application could now run well on my Ubuntu, and it is fun. I am now waiting for Mono 1.2.
<!--more-->