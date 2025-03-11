---
layout: post
title: "Summary of BAML Reader/Writer Implementations"
description: "This post summarizes the implementations of BAML reader/writer in Microsoft and open source projects."
tags: .NET
permalink: /summary-of-baml-reader-writer-implementations-62950ac47481
excerpt_separator: <!--more-->
---
Both XAML and BAML play important roles in WPF. As Microsoft and Xamarin decides to extend XAML to Windows Store apps, Windows Phone, Xamarin.Forms, we won't see such interesting things disappear soon like Silverlight/Moonlight.
<!--more-->

XAML files can be easily manipulated by using XamlReader and XamlWriter classes (in PresentationFramework.dll) from Microsoft. In System.Xaml.dll there are also other classes (such as XamlReader and XamlWriter).

However, if you need to manipulate BAML files directly, you will find it bit of tough to get things done without some investigation. This aims to save you some time if you happen to do that like I am doing right now.

## Microsoft Implementations

If Microsoft can open source or at least make the following classes public, we should be able to save a lot of time, System.Windows.Markup.BamlReader and System.Windows.Markup.BamlWriter in PresentationFramework.dll.

> Note that you can see their reference source code, but that's not the "open source" approach compliant to OSI definition. (The target assemblies must be loaded via reflection.)
> 
> Also note that Microsoft is open sourcing WinForms and WPF source code as part of .NET Core 3.0. Then such classes might become available for other open source projects to use.

There is another class System.Windows.Baml2006.Baml2006Reader, which can be used to parse BAML files. ILSpy once used it to decompile BAML, but of course later gave it up. (The target assemblies must be loaded via reflection).

There is a very special class System.Windows.Markup.Localizer.BamlLocalizer. It gives you a way to load/write BAML but with a lot of limitations. It was designed to assist localization, so it does not expose all possibilities of BAML to us. The LocBaml sample from Microsoft utilizes this class.

## Open Source Implementations

Of course, there are other implementations that analyze BAML, such as the open source XmlBamlReader from Cristian Ricciolo Civera under Ms-PL (which later becomes part of ILSpy). It does not require target assemblies to be loaded via reflection.

The open source obfuscator Confuser has another implementation available under GPLv2,

(Update: Confuser developers now re-license the code under MIT, https://yck1509.github.io/ConfuserEx/. IL Repack developers reuse its code to implement WPF support.)

Popular decompilers and obfuscators are typical tools that depend on such implementations, so they either use the above or have their own. An interesting fact is that Telerik JustDecompile seems to use XmlBamlReader, and experiences the same bug of ILSpy #365 (not reported by me, but I contributed a patch).
