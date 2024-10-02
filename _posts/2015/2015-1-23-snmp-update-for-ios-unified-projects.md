---
layout: post
title: "#SNMP Update for iOS Unified Projects"
description: "This post is about how I updated #SNMP Library for iOS Unified Projects."
tags: SNMP Mono
permalink: /snmp-update-for-ios-unified-projects-35272fa4bba0
excerpt_separator: <!--more-->
---
Xamarin has sent me several mails regarding how to update component submissions to latest iOS platform. Thus, I made a few changes recently, which you can find at GitHub.
<!--more-->

## Project File Changes

I have created several testing projects, and found that finally the MonoTouch name is abandoned. The new projects all target Xamarin.iOS platform, and also add Xamarin.iOS.dll as reference. You can go into C:\Program Files (x86)\Reference Assemblies\Microsoft\Framework\Xamarin.iOS\v1.0 to check the details.

Meanwhile, for executable projects, now 64 bit must be enabled.

There are also namespace changes, such as removing the MonoTouch prefix.

[The following change set](https://github.com/lextudio/sharpsnmplib/commit/d3caee6984061e2db17dc048cef5449a29dc2a05) shows all the changes I made.

## Packaging Issue

I have been using Windows 10 for a while, as well, as Visual Studio 2015. Thus, when I ran xamarin-component.exe to pack up things, I got this exception,

``` text
Running mdoc "update" " --debug" "-LC:\Program Files (x86)\Reference Assemblies\Microsoft\Framework\MonoAndroid\v5.0" "-L
C:\Program Files (x86)\Reference Assemblies\Microsoft\Framework\MonoTouch\v1.0" "-LC:\Program Files (x86)\Reference Asse
mblies\Microsoft\Framework\Xamarin.iOS\v1.0" " --import=E:\Projects\sharpmibsuite\sharpsnmplib\xamarin_support\SharpSnmpL
ib.Portable.xml" "-o" "C:\Users\lextm\AppData\Local\Temp\sharpsnmplib-8.5.2–1494637963\en" "E:\Projects\sharpmibsuite\sh
arpsnmplib\xamarin_support\SharpSnmpLib.Portable.dll"…

Unhandled Exception: System.ComponentModel.Win32Exception: The system cannot find the file specified
at System.Diagnostics.Process.StartWithCreateProcess(ProcessStartInfo startInfo)
at System.Diagnostics.Process.Start()
at System.Diagnostics.Process.Start(ProcessStartInfo startInfo)
at Xamarin.Components.Packaging.Utility.Exe(String command, Boolean verbose, String[] args)
at Xamarin.Components.Packaging.Creation.PackageCreator.WriteMonodocsUsingXmldocs(ZipOutputStream zipStream, PackageS
pec spec)
at Xamarin.Components.Packaging.Creation.PackageCreator.CreatePackage(PackageSpec spec)
at Xamarin.Components.CreateManuallyCommandHandler.Invoke(String[] args)
at Xamarin.Components.MainClass.Main(String[] args)
```

Not surprising at all, as I can easily confirm with Process Monitor that mdoc executable could not be found.

Luckily Mono 3.12 for Windows installer has been available, so I simply extracted the needed binaries and [copied them locally](https://github.com/lextudio/sharpsnmplib/commit/8b364a3ac76f2c66124aa214a78da30e52811b8a). Then everything works.

Hope you find this post useful upgrading your Xamarin Component Store submissions.
