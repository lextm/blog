---
layout: post
title: OpenFileDialog Crashes With COMException 0x80040111
description: This post is about a strange issue I encountered when using OpenFileDialog.
tags: Visual-Studio Windows .NET
permalink: /openfiledialog-crashes-with-comexception-0x80040111-f51e18d1ab89
excerpt_separator: <!--more-->
---

I have been updating Jexus Manager quite frequently as more and more useful crash reports were sent to me by Rollbar. And today a strange issue caught my attention.
<!--more-->

## Exception Details
``` bash
Traceback (most recent call last):
at System.Windows.Forms.SaveFileDialog.CreateVistaDialog() in "System.Windows.Forms.SaveFileDialog" line 0
at System.Windows.Forms.FileDialog.RunDialogVista(System.IntPtr hWndOwner) in "System.Windows.Forms.FileDialog" line 0
at System.Windows.Forms.CommonDialog.ShowDialog(System.Windows.Forms.IWin32Window owner) in "System.Windows.Forms.CommonDialog" line 204
at JexusManager.Features.Certificates.ExportCertificateDialog.<.ctor>b__0_2(System.Reactive.EventPattern`1[System.EventArgs] evt) in "E:\JexusManager\JexusManager.Features.Certificates\ExportCertificateDialog.cs" line 51
at System.Reactive.AnonymousSafeObserver`1.OnNext(T value) in 
"System.Reactive.AnonymousSafeObserver`1" line 22
System.Runtime.InteropServices.COMException: Creating an instance of the COM component with CLSID {C0B4E2F3-BA21–4773–8DBA-335EC946EB8B} from the IClassFactory failed due to the following error: 80040111 ClassFactory cannot supply requested class (Exception from HRESULT: 0x80040111 (CLASS_E_CLASSNOTAVAILABLE)).
```

It is important to know that the relevant functions indicate that .NET Framework was trying to call a Windows Vista and above API to show the new OpenFileDialog UI, but failed, on operating systems such as Windows 7 and Windows Server 2012 R2. Can this happen?

Google does return many search results, but only a Stack Overflow thread provides [enough explanation](https://stackoverflow.com/questions/29929862/exception-from-hresult-0x80040111-class-e-classnotavailable) under the hood. It seems that if Visual Themes feature is turned off for whatever reason, Windows would hide the COM interface and lead to the crash. However, this answer does not provide any specific workaround.

> More reports show this issue is quite typical on Hyper-V Server 2016 (1607) with .NET Framework Version: 4.6.2. Though I never use this system.

So I personally found two workarounds, and used them both in Jexus Manager to handle different scenarios. The related commit is [here](https://github.com/jexuswebserver/JexusManager/commit/a6eb456bb495c207996341584d8895007b1e4cb2)

## Workaround 1: Set `FileDialog.AutoUpgradeEnabled` to `false`

Microsoft has [an ugly property defined](https://learn.microsoft.com/dotnet/api/system.windows.forms.filedialog.autoupgradeenabled), and I can only use this to let the ancient dialogs pop up. Anyway it should work (as many users reported success).

## Workaround 2: Fallback from `Ookii.Dialogs.VistaFolderBrowserDialog` to `FolderBrowserDialog`

I have been using `Ookii.Dialogs.VistaFolderBrowserDialog` to show the Vista style folder browse dialog. However, the developer of Ookii.Dialogs failed to handle the `COMException` either. Thus, I have to manually create a traditional `FolderBrowserDialog` if the exception occurs.
