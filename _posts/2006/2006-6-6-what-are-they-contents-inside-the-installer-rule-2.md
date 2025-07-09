---
layout: post
title: "What are they? Contents Inside The Installer (Rule 2)"
description: This post is about the contents inside the installer of CBC 2.0.
tags: Code-Beautifier-Collection Delphi
permalink: /what-are-they-contents-inside-the-installer-rule-2-2cbdc7a9159f
excerpt_separator: <!--more-->
---
(CSDN June 06, 2006)

The installer is made with Inno Setup. It is a good tool to make Windows installers. (However, it is not open source if you are careful.)
<!--more-->

I package all the source code there including those not prepared to be released. For example, the NFamily Plus in plan is now shipped only with source code and a SharpDevelop project. You could test it if you like. BDS projects are not included because they are out-of-date.

I compile the whole source against BDS 4 before shipping. So the installer works best for BDS 2006. However, lately I found it works for delphi 8. For C#Builder 1.0, AddMany Plus should be disabled. The only version fails is Delphi 2005. The assemblies built with release settings are shipped. If you need debug versions, you can compile by yourself from the source.

AStyle and JCF are bundled also. And actually AddMany.dll and csbgoodies.dll are directly taken from AddMany 4.1 and C#Builder Goodies 1.1, I have not modified them.

More things shipped in data folder such as live templates files in order to bring more features. A few more docs.

The fullsource project is used to model the whole project and refactor.

Tiny tools used are included in src folder, built before shipping, and some are used in the installation process or used by certain feature.

As a result, the installer is never slim again. The size is almost doubled from version 2.4, but the features implemented worth the while.
