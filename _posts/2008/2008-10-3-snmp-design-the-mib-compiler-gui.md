---
layout: post
title: "#SNMP Design: The MIB Compiler GUI"
description: This post is about how to design the MIB compiler GUI.
tags: SNMP
permalink: /snmp-design-the-mib-compiler-gui-219e6495f7a8
excerpt_separator: <!--more-->
---
If you played with commercial SNMP products for developers, you may notice how they were designed. For example, SilverCreek combines the compiler with the browser while MGSoft splits them into separate executables. Therefore, I think it is time to decide how to design #SNMP Browser and Compiler.
<!--more-->

## Plan A

In this plan, the browser has less features than it is now. The feature set is,

* Loads *.module files from the module inventory (Yes, instead of MIB inventory).
* Display a object tree.
* Support SNMP operations such as GET, SET, GETNEXT and so on.
* Support TRAP and INFORM.

Then these features will be added in the compiler,

* Compile new MIB documents to *.module files and add to inventory.
* Delete module files from the module inventory.

## Plan B

In this plan, the compiler will be part of the browser. So all features described in Plan A will be available in the browser.

However, this means there will be a few more panels and menu items added to the browser which may be an issue for collaboration. Do you know it is hard to merge Form and UserControl in WinForms applications?

## Current Approach

I was interested in Plan B at first, and that is why you can add and delete MIB documents from the current MIB browser.

But Plan A sounds better, because Steve is willing to maintain and improve the browser. I don't want him or myself to waste time on merging changes from both of us simply because of WinForms.

Therefore, now I am going to create a new project file in #SNMP Suite, named #SNMP MIB Compiler following Plan A. This GUI compiler will also use DockPanel Suite to host panels.

Although it starts as a separate project, I think it is possible to integrate the panels into the browser if necessary in the future. Yes, that makes Plan B always available as a back up.

At last, I want to state that I am always open to suggestions. At least, the compiler is going to be official released in CrossRoad, so there is plenty of time to adjust it.
