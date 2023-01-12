---
layout: post
title: "How to Install Custom Controls to Visual Studio, Part I"
description: "This post is about how to install custom controls to Visual Studio."
tags: .NET Visual-Studio
permalink: /how-to-install-custom-controls-to-visual-studio-part-i-39fa7733bb3
excerpt_separator: <!--more-->
---
I thought this is an easy task as so many components vendors have their fancy installers doing this, but only when I attempted to create one for Crad's ActionList (http://github.com/lextm/actionlistwinforms) I found out how difficult it is to locate all information you need. Therefore, this will be a long post with all information you might need.
<!--more-->

Note that I just finish Visual Studio 2008 support, which will be covered in part I. Visual Studio 2005 is tool old to attract me, and Visual Studio 2010 and 2012 poses new challenges of supporting both .NET 2 and .NET 4.

Another notice is that I will focus on Windows Forms controls in this post, as I am not an author of WPF or Silverlight controls.

## Basic Integration (Mandate)

By creating a new registry key

> HKLM\SOFTWARE\Microsoft\.NETFramework\v2.0.50727\AssemblyFoldersEx\ActionListWinForms

I tell Visual Studio to understand that a new control library named ActionListWinForms is added.

I set (Default) value to C:\Program Files\ActionList for Windows Forms\net20\ so that VS knows where to search for the assemblies.

> The same should be done for .NET 4 I guess, but I do not yet test it.

After doing this and restart VS, I can now create a new tab named "ActionList for WinForms" in Toolbox panel, right click and activate "Choose Item…" menu item.

You can see that magically Crad.Windows.Forms.Actions.dll is listed there just like any other registered .NET assemblies. That is what AssemblyFoldersEx registry keys brings.

This provides us the basic integration, that we can manually create a tab and add new items.

## Advanced Integration (Optional)

Now to achieve better experience, we need to automate Visual Studio to simulate our manual steps above (create a new tab and add items).

This requires familiarity on Visual Studio COM interfaces and Visual Studio SDK. However, you should not be panic, as we are kindly served by open source community with a project named Visual Studio Toolbox Manager.

By calling this utility the whole automation process will be carried out automatically.

Please note that this project is no longer active (since 2010), so you might meet various problems using it against Visual Studio 2008. I collected all patches that are available for this project and plan to create a new release in the next few days. You can wait and check out my fork if you plan to also create your own control installer.

## Sidenote 1

Some articles indicate that it is safer to install the assemblies to GAC. So I also use `gacutil` to install them to GAC.

## Sidenote 2

If you have split your control library to non-designer and designer assemblies, make sure you put them in the same installation folder. In this way, VS can locate the designer assembly by reading AssemblyFoldersEx. I also install the design assembly to GAC though I am not sure whether I should.

Once the end user drags the control to a form/user control, only the non-designer assembly will be added as a reference. The designer assembly is only important for Visual Studio. In this way, client profiles (.NET 3.5/4) can be perfectly supported.

## Full Sample

OK, so if you want to find a sample which covers all details, you can refer to ActionList for WinForms project, where I share [an Inno Setup script](https://github.com/lextm/ActionListWinForms/tree/cc4a57b20148c19c3fdaef120e9e0aa6d87d288b) and the customized Visual Studio Toolbox Manager build.

Let me know if you have any question simply by leaving a comment.

Cheers.
