---
layout: post
title: "GrapeVine Voice: Installation Experience Changes (Part I)"
description: "This post talks about the installation experience changes in Code Beautifier Collection."
tags: Code-Beautifier-Collection Delphi
permalink: /grapevine-voice-installation-experience-changes-part-i-8928cd2e56a3
excerpt_separator: <!--more-->
---
I'd like to review some historical phases at first, (details can be found in docs/Readme.pdf)
<!--more-->

## Without An Installer

The first version of Code Beautifier Collection (named under JCFExpert) was released a long time ago. It was not included in an installer so manually installation is required.

It must be tough for users at that moment. They had to build the assemblies at first, then install it using SharpBuilderTools' Expert Manager.

So if you have chance to review that package, you will see JCFExpert bundles SharpBuilderTools 3.1. SBT, which is much larger than JCFExpert, is included only to install JCFExpert.

## Simple Installer

2005–10–30 when I "Announce CBC 2.2 RC 1", I wrote a very simple installer myself to install CBC, so SharpBuilderTools Expert Manager was no longer bundled.

In fact what I wrote was something similar to an Expert Manager which is far from an installer. However, I had successfully reduced the package size.

## Inno Setup Installers

On 2005–12–16 I started to write an installer with Inno Setup while I was learning it bit by bit. Yes, it is an amazing technology that changed CBC user experience a lot then. I could imagine why download counts increased after I shipped CBC as an installer.

And I added a few installation tasks version by version.

1. On 2006–4–24 when I "Announce CBC 2 WalkPace Update 1 (5.0.1.1018)", installer was updated to create more menu items in Start Menu. So Mix for .NET menu items were added.
1. Later I installed UnhandledExceptionManager into your GAC.
1. Added installation helper executables both before installation (install.exe) and after installation (installforallusers.exe and installforcurrentuser.exe) in GrapeVine M3.
1. Added pascal script to find and uninstall older installed versions automatically in GrapeVine M3.

And now the installer is much more powerful and feature complete.

In Part II, I will discuss about what big changes are made in GrapeVine M3 in order to make CBC install nearly perfectly on Windows Vista. Yes, it is a tough migration. Wish it helpful.
