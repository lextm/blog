---
layout: post
title: "Compiling Mono: Gtk# 2.99"
description: "This post talks about how to compile Gtk# 2.99."
tags: Mono
permalink: /compiling-mono-gtk-2-99-a6640cfc8cc
excerpt_separator: <!--more-->
---
I think GTK# 3.0 is coming soon, as Gtk# 2.99 is now in milestone 2. It does introduce some problems if

* You compile both Mono and Gtk# from master,
* You are now trying to compile Mono.Addins.
<!--more-->

The compilation failed at Mono.Addins.Gui project,

``` text
Building Mono.Addins.Gui.csproj
Mono.Addins.Gui/AddinManagerDialog.cs(187,24): error CS0506: `Mono.Addins.Gui.AddinManagerDialog.Dispose()': cannot override inherited member `GLib.Object.Dispose()' because it is not marked virtual, abstract or override
Mono.Addins.Gui/AddinTreeWidget.cs(52,25): error CS0012: The type `GLib.IIcon' is defined in an assembly that is not referenced. Consider adding a reference to assembly `gio-sharp, Version=3.0.0.0, Culture=neutral, PublicKeyToken=35e10195dab3c99f'
Mono.Addins.Gui/ManageSitesDialog.cs(67,24): error CS0506: `Mono.Addins.Gui.ManageSitesDialog.Dispose()': cannot override inherited member `GLib.Object.Dispose()' because it is not marked virtual, abstract or override
Mono.Addins.Gui/NewSiteDialog.cs(46,24): error CS0506: `Mono.Addins.Gui.NewSiteDialog.Dispose()': cannot override inherited member `GLib.Object.Dispose()' because it is not marked virtual, abstract or override
gtk-gui/generated.cs(65,52): error CS0234: The type or namespace name `SizeRequestedArgs' does not exist in the namespace `Gtk'. Are you missing an assembly reference?
Mono.Addins.Gui/HeaderBox.cs(98,27): error CS0115: `Mono.Addins.Gui.HeaderBox.OnSizeRequested(ref Gtk.Requisition)' is marked as an override but no suitable method found to override
Mono.Addins.Gui/HeaderBox.cs(125,27): error CS0115: `Mono.Addins.Gui.HeaderBox.OnExposeEvent(Gdk.EventExpose)' is marked as an override but no suitable method found to override
Mono.Addins.Gui/HoverImageButton.cs(83,44): warning CS0618: `Gtk.Style' is obsolete: `Replaced by StyleContext'
Mono.Addins.Gui/HoverImageButton.cs(150,33): error CS0115: `Mono.Addins.Gui.HoverImageButton.OnExposeEvent(Gdk.EventExpose)' is marked as an override but no suitable method found to override
make[1]: *** [csproj_build] Error 1
make[1]: Leaving directory `/home/lextm/src/mono-addins/Mono.Addins.Gui'
make: *** [all-recursive] Error 1
```

Mono.Addins works fine for latest stable Gtk# but not for the latest. I did not yet find out how to compile that stable Gtk# from source code yet. Will further investigate when I have time.
