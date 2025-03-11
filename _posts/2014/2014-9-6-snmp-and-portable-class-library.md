---
layout: post
title: "#SNMP and Portable Class Library"
description: "This post talks about the future of #SNMP and how it will support Portable Class Library."
tags: SNMP .NET
permalink: /snmp-and-portable-class-library-52ce3ff6d47
excerpt_separator: <!--more-->
---
Microsoft introduced Portable Class Library (PCL) a very long time ago, so as to support cross platform code sharing (Windows, Windows Phone, Windows RT, Silverlight initially). Xamarin started to support PCL a few months ago, and fully integrated into Visual Studio. Does that finally solve all code sharing issues? Well, far from perfect yet, especially for #SNMP.
<!--more-->

The top three platforms #SNMP now support are,

* .NET on Windows
* Xamarin.iOS
* Xamarin.Android

You can hardly believe that all dependencies we need are available on all of the platforms, but I could not build a PCL easily. Yes, I bet Microsoft is the one to blame, as they cut too much from the core profile in favor of dying platforms, such as Silverlight, Windows RT, and Windows Phone (yes, I never buy a Windows Phone).

Thus, soon I will publish the next major release of #SNMP, where only the core classes are available in a new assembly named SharpSnmpLib.Portable.dll. To consume all functionality platform specific assemblies are also required,

* SharpSnmpLib.Full.dll (for .NET on Windows and Mono, and that's why I don't call it .Windows.dll)
* SharpSnmpLib.iOS.dll
* SharpSnmpLib.Android.dll

It is going to be released by the end of 2014, as another major feature is still under development. More information is to be published. Stay tuned.
