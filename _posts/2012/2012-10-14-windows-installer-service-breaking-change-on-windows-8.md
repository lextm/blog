---
layout: post
title: "Windows Installer Service Breaking Change on Windows 8"
description: "This post is about Windows Installer Service Breaking Change on Windows 8."
tags: Windows
permalink: /windows-installer-service-breaking-change-on-windows-8-93547462fa3a
excerpt_separator: <!--more-->
---
Windows Installer team published [a nice blog post](https://learn.microsoft.com/archive/blogs/windows_installer_team/windows-installer-troubleshooting-tips-from-halloween) about how to detect whether Windows Installer is busy with an MSI package.

And the recommendation was

> For Windows Installer 3.0 or greater, we recommend switching from the mutex to attempting to stop the msi service. If you are unable to stop the service, the service is busy installing another product.

Hi guys, why do you change this on Windows 8?
<!--more-->

I just found that on my Windows 8 Enterprise box I could not install Expression Studio 4 or Windows Phone SDK 7.1, as the setup.exe thinks Windows Installer is busy. So I launched Visual Studio 2012 and wrote the following code,

{% gist 3888301 %}

Well, the output of this console application is horrible,

``` bash
busy
idle
Press any key to continue . . .
```

So, now only the mutex check is reliable, while the service check completely fails.

If you happen to meet the same problem, please execute the MSI packages directly to install the product. That's a workaround I found to install Expression Studio and Windows Phone SDK.
