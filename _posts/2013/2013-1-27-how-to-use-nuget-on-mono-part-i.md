---
layout: post
title: "How to Use NuGet on Mono, Part I"
description: This post shows how to use NuGet on Mono.
tags: .NET Mono
permalink: /how-to-use-nuget-on-mono-part-i-8d2cd63bd1e0
excerpt_separator: <!--more-->
---
[Update: Microsoft starts to officially support Mono, so please simply use latest NuGet executable such as 3.5]

> There have been articles on how to use NuGet command line tool on Mono, but none of them contains all information you need to learn. Therefore, I am now writing down what I learned so far, and hope it is helpful.

Microsoft created NuGet instead of supporting OpenWrap. This should be recorded as another mistake after the one of Sandcastle/NDoc. Anyway, NuGet is more popular as far as I notice, so I have to adapt to it and fight against Microsoft's attitude such as "We've accepted patches from the mono team in the past. But we haven't gone out of our way to add Mono to our test suites." (from here) Is it that hard to build a Linux box, install Mono, and run at least some basic tests? As far as I know, not all Microsoft machines are running Windows.
<!--more-->

Mono MVC has an excellent article on what are the common issues you might meet, and how to resolve them. However, it is not simple enough, and miss a few things (especially when you are running openSUSE). So below are the steps I used on openSUSE 12.2,

1. Install mono-complete. NuGet.exe has a few dependencies (WindowsBase for example, as it requires System.IO.Packaging) that does not present in mono basic installation.

   ``` bash
   sudo zypper install mono-complete
   ```

1. Download the command line utility of NuGet from CodePlex.

1. Import necessary certificates so that NuGet can perform HTTPS requests,

   ``` bash
   mozroots --import --sync
   ```

1. Install Mono on Windows, and copy out Microsoft.Build.dll. If you don't have Windows aside, I share it here on DropBox. Someone might tell you to copy from Microsoft's Windows installation or reference assemblies cache. I don't think that meets Microsoft's EULA. The one copied from Mono is open source, so we should use that till Mono bundles it directly on Linux.
1. Finally put NuGet.exe and Microsoft.Build.dll in the same folder, and execute
`mono --runtime=v4.0.30319 NuGet.exe`

NuGet will try to update itself, and after that you get the latest executable (2.2 right now) running on Linux. Now you can follow Mono MVC's post to see how to create a shell script.

In part II, I talked about how to let package restore work on Linux/Mono.

## More Information on Microsoft.Build.dll
xbuild and related files are packaged in mono-devel. However, this rpm package for Mono 2.10.* does not contain Microsoft.Build.dll. That's why you have to perform step 4 above. Luckily Mono 3.0 does fix this issue.
