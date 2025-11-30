---
layout: post
title: "Recover a Missing .NET MSI on Windows with WiX Toolset"
description: "When Windows prompts for a missing .NET MSI package, this post tells how to extract the MSI from the EXE bootstrapper using WiX Toolset."
image:
  path: /images/desktop-runtime.png
  alt: Microsoft .NET installation error.
tags: .net windows
categories: [Tools and Platforms]
excerpt_separator: <!--more-->
---

You might often try to install latest .NET bits like SDKs and runtimes on your Windows machine to keep things up-to-date. But when suddenly a dialog tells you about the missing `dotnet-host-8.0.3-win-x64.msi`, you might immediately feel surprised, and realize the cached MSI package is gone. Next, you go to .NET download page, but you can only find EXE installers, no hint on the MSI package Windows is asking for. What exactly is going on?

<!--more-->

> Here .NET 8.0.3 is just an example. You might see other versions like .NET 8.x, .NET 9.x, and .NET 10.x. The missing component could be `dotnet-host`, `dotnet-hostfxr`, `dotnet-runtime`, or `aspnetcore-runtime`, depending on what you are installing or uninstalling.

## Why Windows suddenly wants an MSI

Every .NET runtime, hosting bundle, or desktop runtime for Windows is ultimately installing tons of MSI packages. The EXE you download from Microsoft is a Burn bootstrapper that chains several MSIs (host, hostfxr, runtime, and sometimes ASP.NET Core module). During installation, Windows Installer copies each MSI into the default cache such as `C:\ProgramData\Package Cache\{ProductCode}\`. If that cache entry is deleted (by cleanup tools, manual disk scrubs, or drive restores), any later repair, update, or uninstall will prompt for the original MSI.

The design of Windows Installer troubles many users, and now you cannot install the new version, or uninstall the old one, without the original MSI package. So how to get it back?

## Extract with WiX Toolset

Since Microsoft used WiX Toolset 3.x before .NET 10 to build the installers, you can use the same tool to pull the embedded container apart.

1. Install WiX Toolset 3.14 (`winget install WiXToolset.WixToolset`) and verify that it has been properly installed (default: `C:\Program Files (x86)\WiX Toolset v3.14\bin`).
2. Extract the contents from the bootstrapper:

   ```cmd
   "C:\Program Files (x86)\WiX Toolset v3.14\bin\dark.exe" dotnet-hosting-8.0.3-win.exe -x .\cached
   ```

Now open up the `.\cached` folder, and you should see all the MSI packages that were originally bundled inside the EXE, and `dotnet-host-8.0.3-win-x64.msi` is among them.

When Windows prompts you for the missing MSI, just point to this extracted file. Voilà! Problem solved.

## What about .NET 10 or later?

Starting from .NET 10, the installation packages are built with WiX Toolset 5.x, and the above approach with WiX Toolset 3.14 won't work. So, if we try to extract the contents of `dotnet-hosting-10.0.0-win.exe` with `dark.exe` from WiX Toolset 3.14, we won't get the expected MSIs.

Instead, let's install WiX Toolset 5.x.

```cmd
dotnet tool install --global wix --version 5.0.2
wix burn extract -oba .\cached2 dotnet-hosting-10.0.0-win.exe -o .\cached
```

You can find the extracted MSIs in the `.\cached` folder now. Note that [you cannot ignore the `-oba` switch, or the extraction will miss file names](https://github.com/wixtoolset/issues/issues/8142).

## Side Note

Now you know how to extract MSIs from .NET installers, you might still wonder why the cached MSIs are missing in the first place. The reason is that third party disk cleanup tools consider those cached MSIs as temporary files, and delete them to free up disk space. And if you are not sure whether a cleanup tool will delete those cached MSIs, you'd better avoid it completely, or back them up to another location before running the cleanup.
