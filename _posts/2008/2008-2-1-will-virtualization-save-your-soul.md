---
layout: post
title: "Will Virtualization Save Your Soul?"
description: This post talks about how virtualization can help improve productivity.
tags: Windows
permalink: /will-virtualization-save-your-soul-e1041d55a0c0
excerpt_separator: <!--more-->
---
Viruses can damage enterprise network. Even if they are not that harmful, one or two workstations may be damaged. Unluckily, my workstation broke down last week. Both Internet Explorer and Registry Editor are broken so I have to ask the IT guys for help. How I wish they could install a Windows Vista for me because UAC can filter out a lot of viruses and Trojans, but according to the corporate rules, Windows XP is a still the only choice.
<!--more-->

Actually, there were another three guys whose workstations were down so IT guys helped all of us reinstall Windows. And I am the only one who restores development environment in a flash. How I achieve that? I just download Virtual PC 2007 installer again, install it, and then launch my old VM from within it. Now my Visual Studio 2005 is back with all other tools. Virtualization really saves me from reinstalling those beasts again.

BTW, because I did not install MSDN Library for Visual Studio 2005 in VM, now I can install MSDN Library for Visual Studio 2008 instead. I continue to install it outside VM in order to limit VM size as well as make updating it easier.

Virtual PC 2007 is enough if you only build Windows VMs. If you need to build Linux VMs, VirtualBox or VMware Server 1.x is required because Virtual PC does not support Linux well. If you can afford commercial tools, VMware Workstation 6 is fabulous.

Even though Windows Server 2008 will be virtualization enabled, I wonder if it can avoid harmful viruses in the future.
