---
layout: post
title: "Strange Visual Studio 2017 RC Installation Error"
description: "This post is about a strange Visual Studio 2017 RC installation error."
tags: Visual-Studio
permalink: /strange-visual-studio-2017-rc-installation-error-acdce0000c34
excerpt_separator: <!--more-->
---

I met the issue below,
<!--more-->
``` text
The product failed to install the listed workloads and components due to one or more package failures.
Incomplete workloads
.NET desktop development (Microsoft.VisualStudio.Workload.ManagedDesktop,version=15.0.26127.0)
Visual Studio core editor (Microsoft.VisualStudio.Workload.CoreEditor,version=15.0.26004.1)
Incomplete components
.NET desktop development tools (Microsoft.VisualStudio.Component.ManagedDesktop.Prerequisites,version=15.0.26109.1)
.NET Framework 4.6.1 development tools (Microsoft.Net.ComponentGroup.DevelopmentPrerequisites,version=15.0.26004.1)
.NET Portable Library targeting pack (Microsoft.VisualStudio.Component.PortableLibrary,version=15.0.26109.1)
Blend for Visual Studio (Microsoft.ComponentGroup.Blend,version=15.0.26004.1)
C# and Visual Basic (Microsoft.VisualStudio.Component.Roslyn.LanguageServices,version=15.0.26109.1)
ClickOnce Publishing (Microsoft.Component.ClickOnce,version=15.0.26004.1)
Data sources and service references (Microsoft.VisualStudio.Component.VisualStudioData,version=15.0.26004.1)
Entity Framework 6 tools (Microsoft.VisualStudio.Component.EntityFramework,version=15.0.26004.1)
Managed Desktop Workload Core (Microsoft.VisualStudio.Component.ManagedDesktop.Core,version=15.0.26109.1)
Profiling tools (Microsoft.VisualStudio.Component.DiagnosticTools,version=15.0.26109.1)
Visual Studio core editor (Microsoft.VisualStudio.Component.CoreEditor,version=15.0.26004.1)
You can search for solutions using the information below, modify your selections for the above workloads and components and retry the installation, or remove the product from your machine.
Following is a collection of individual package failures that led to the incomplete workloads and components above. To search for existing reports of these specific problems, please copy and paste the URL from each package failure into a web browser. If the issue has already been reported, you can find solutions or workarounds there. If the issue has not been reported, you can create a new issue where other people will be able to find solutions or workarounds.
Package 'Microsoft.VisualStudio.TeamFoundation.TeamExplorer,version=15.112.26110.0' failed to install.
Search URL: https://aka.ms/VSSetupErrorReports?q=PackageId=Microsoft.VisualStudio.TeamFoundation.TeamExplorer;PackageAction=Install;ReturnCode=3001
Impacted workloads
.NET desktop development (Microsoft.VisualStudio.Workload.ManagedDesktop,version=15.0.26127.0)
Visual Studio core editor (Microsoft.VisualStudio.Workload.CoreEditor,version=15.0.26004.1)
Impacted components
.NET desktop development tools (Microsoft.VisualStudio.Component.ManagedDesktop.Prerequisites,version=15.0.26109.1)
.NET Framework 4.6.1 development tools (Microsoft.Net.ComponentGroup.DevelopmentPrerequisites,version=15.0.26004.1)
.NET Portable Library targeting pack (Microsoft.VisualStudio.Component.PortableLibrary,version=15.0.26109.1)
Blend for Visual Studio (Microsoft.ComponentGroup.Blend,version=15.0.26004.1)
C# and Visual Basic (Microsoft.VisualStudio.Component.Roslyn.LanguageServices,version=15.0.26109.1)
ClickOnce Publishing (Microsoft.Component.ClickOnce,version=15.0.26004.1)
Data sources and service references (Microsoft.VisualStudio.Component.VisualStudioData,version=15.0.26004.1)
Entity Framework 6 tools (Microsoft.VisualStudio.Component.EntityFramework,version=15.0.26004.1)
Managed Desktop Workload Core (Microsoft.VisualStudio.Component.ManagedDesktop.Core,version=15.0.26109.1)
Profiling tools (Microsoft.VisualStudio.Component.DiagnosticTools,version=15.0.26109.1)
Visual Studio core editor (Microsoft.VisualStudio.Component.CoreEditor,version=15.0.26004.1)
Log
C:\Users\lextm\AppData\Local\Temp\2\dd_setup_20170128095042_019_Microsoft.VisualStudio.TeamFoundation.TeamExplorer.log
Details
Command executed: "C:\Program Files (x86)\Microsoft Visual Studio\Installer\resources\app\ServiceHub\Services\Microsoft.VisualStudio.Setup.Service\vsixinstaller.exe" /q /s /admin /appidinstallpath:"C:\Program Files (x86)\Microsoft Visual Studio\2017\Community" /logFile:"C:\Users\lextm\AppData\Local\Temp\2\dd_setup_20170128095042_019_Microsoft.VisualStudio.TeamFoundation.TeamExplorer.log" /skuName:Enterprise /skuVersion:15.0.26113.0 /appidname:displayName "C:\ProgramData\Microsoft\VisualStudio\Packages\Microsoft.VisualStudio.TeamFoundation.TeamExplorer,version=15.112.26110.0\TeamExplorer.vsix"
Return code: 3001
Return code details: This VSIX extension failed.
```

Instead of asking Microsoft, I simply deleted all contents under C:\ProgramData\Microsoft\VisualStudio\Packages and reran the installer. Well, lucky day and it works.
