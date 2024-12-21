---
layout: post
title: "Brief Guide to Windows ARM64 Developers"
description: "A brief guide to Windows ARM64 developers, covering key aspects and considerations. Possibility to stay with x86/x64, ARM64 native development, specific notes to consider for web apps are all covered."
tags: Windows IIS
excerpt_separator: <!--more-->
---

The introduction of ARM64 architecture to Windows has opened up new possibilities for developers. The new ARM64 based Copilot+ PCs on new chipset like Qualcomm Snapdragon X Elite are not only enabling AI related innovations but also providing a platform for traditional developers to explore new opportunities. This post provides a brief guide to Windows ARM64 developers, covering key aspects and considerations.
<!--more-->

## Possibility to Stay with x86/x64

No doubt you can find it tempting to switch to ARM64, but it's not mandatory. You can continue to develop for x86/x64 platforms as usual and the ARM64 architecture supports x86/x64 emulation, allowing your existing applications to run on ARM64 devices.

Even the installers might continue to work without any changes. However, due to the changes to system files and directories, you might need thorough testing to ensure everything works as expected and your applications are not breaking the system by mistake.

For example,

* If your application is writing to the `Program Files` directory, you might be aware that this folder now contains both x64 and ARM64 binaries. Yes, ARM64 binaries are in the `Program Files` directory, not in `Program Files (ARM64)`.
* `%windir%\system32` contains mostly [Arm64X binaries](https://learn.microsoft.com/windows/arm/arm64x-build).

## ARM64 Native Development

However, if you want to take full advantage of ARM64, you can consider recompiling your applications for ARM64 to achieve better performance and efficiency. Different tools and frameworks are available to help you with this transition, so you might refer to C++ or C# documentation for more information.

For example, you should use [ARM64 specific developer tools](https://learn.microsoft.com/windows/arm/overview#find-tools-for-arm-development) to build ARM64 applications, such as [Arm-native Visual Studio](https://learn.microsoft.com/visualstudio/install/visual-studio-on-arm-devices).

## Specific Notes to Consider for Web Apps

### IIS on ARM64

If you are developing web applications, you might be interested in running IIS or IIS Express on ARM64. Both of them can run in three modes on ARM64 devices, including x86, x64, and ARM64.

For IIS, the mode option is controlled by several application pool settings, in which `enableEmulationOnWinArm64` is exclusive to Windows ARM64.

| Mode | `enable32BitAppOnWin64` | `enableEmulationOnWinArm64` | Comments |
| --- | --- | --- | --- |
| x86 | True | True | |
| x64 | False | True | This is the default mode for new application pools. |
| ARM64 | False | False | |

### IIS Out-of-Band Modules

Since most of [IIS out-of-band modules from Microsoft]({% post_url 2017/2017-9-8-status-of-iis-out-of-band-modules %}) are x86/x64 only, if you want to use any of them on ARM64 devices, you must change IIS worker process to x86/x64 mode.

The only exceptions right now are,

* [HttpPlatformHandler v2 from LeXtudio Inc.]({% post_url 2024/2024-4-8-httpplatformhandler-v2 %})
* ASP.NET Core module.
* URL Rewrite module, which has been ported to ARM64 as part of IIS Express. But you need extra steps to extract the bits from IIS Express and apply to IIS.

### ASP.NET Core Module for IIS

ASP.NET Core module is available for ARM64 devices, so you can run ASP.NET Core applications. However, due to the bug in its installer, you can only run the application pool in ARM64 mode.

[You can apply my patch to the installer to unlock x86/x64 mode](https://github.com/lextm/ancm-arm64), and vote/leave a comment on [this GitHub issue](https://github.com/dotnet/aspnetcore/issues/47115) to push Microsoft to fix the bug.

### IIS Express

For IIS Express, you can launch the command line differently to enter each mode.

| Mode | Command Line |
| --- | --- |
| x86 | `"%systemdrive%\Program Files (x86)\IIS Express\iisexpress.exe" /?` |
| x64 | No obvious way |
| ARM64 | `"%systemdrive%\Program Files\IIS Express\iisexpress.exe" /?` |

> This explained why VS 2022 (like version 17.9.6) shows an error message "IIS EXPRESS on arm64 is only supported for ASP.NET Core applications targeting .NET 7.0 and newer", because it can only launch IIS Express in ARM64 and x86 modes.

### IIS Express Out-Of-Band Modules

* HttpPlatformHandler v2 is available for ARM64 devices, so you can use it with IIS Express.
* ASP.NET Core module ARM64 build is bundled, but x86/x64 builds are not.
* URL Rewrite module is bundled.

### ASP.NET Core Module for IIS Express

The installer has the same bug as the IIS version, so you can only run the application pool in ARM64 mode.

There is currently no patch available for IIS Express, so you might need to wait for Microsoft to fix the bug.

## Conclusion

Windows on ARM64 still has a long way to go, but it's already a good time to start exploring the possibilities.
