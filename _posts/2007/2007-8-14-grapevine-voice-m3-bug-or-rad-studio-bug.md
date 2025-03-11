---
layout: post
title: "GrapeVine Voice: M3 Bug or RAD Studio Bug"
description: "This post talks about a bug in M3 installer, and also a bug related to BDS.exe."
tags: Code-Beautifier-Collection Delphi
permalink: /grapevine-voice-m3-bug-or-rad-studio-bug-53893c39d016
excerpt_separator: <!--more-->
---
Tomasz Wawrzyniak (Dear Tom) has been talking with me about M3 installation issues these days. Thanks for his reports, I corrected M3 installer, and also find an important issue in BDS.exe fire again.

You may have noticed while other Delphi experts, such as Castalia, GExperts, and CnPack Wizards, have different installers for different versions of Delphi, Code Beautifier Collection provides an installer for all Delphi versions. What is the reason? How can I make it?
<!--more-->

In fact, there are two rules existing for years,

## Rule I, Native

Most of Delphi experts are native experts. As a result, they must link to some IDE packages. Because of the incompatibilities of the packages across Delphi versions, there is no way to compile one version of experts for all Delphi versions. For example, you must compile CnPack Wizards against Delphi 7 packages in order to make an installer for Delphi 7.

If you need to compile against different versions, you have to make installers for different versions. That is the rule I.

## Rule II, .NET

The rule for .NET expert, such as Sharp Builder Tools and Code Beautifier Collection is different. If you compile against latest Borland.Studio.ToolsAPI.dll, the expert can work even in old versions of RAD Studio.

CBC 5.3.3 can be installed for all BDS versions 1–4. That can be a good proof.

## New Rules?

However, these rules are governed by Borland/CodeGear. So they can be changed without notice.

Now GrapeVine M3 cannot install correctly into Delphi 2007 because it is compiled against a newer version of Borland.Studio.ToolsAPI.dll.

I will contact CodeGear guys soon about this issue. Wish they could try their best to follow Rule II. If impossible, I will be forced to provide different installers, too.
