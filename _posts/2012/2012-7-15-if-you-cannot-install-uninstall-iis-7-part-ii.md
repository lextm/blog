---
layout: post
title: "If You Cannot Install/Uninstall IIS 7, Part II"
description: "This post is about how to fix IIS 7 installation issues."
tags: Windows IIS
permalink: /if-you-cannot-install-uninstall-iis-7-part-ii-73a14fe3db0
excerpt_separator: <!--more-->
---

I blogged about this last year as [part I]({% post_url 2011/2011-2-26-if-you-cannot-install-uninstall-iis-7 %}).

In this part, I am going to tell you more about the corruption.

<!--more-->

Microsoft releases a tool for you to detect CBS (component based setup) issues, named System Update Readiness Tool,

http://windows.microsoft.com/en-US/windows7/What-is-the-System-Update-Readiness-Tool

You can download the one that matches your system and then execute it. Note that this tool was designed to fix some of Windows Update issues, so it does not only report CBS issue details, but also can resolve some CBS issues.

After executing this tool, it will generate a log file `%windir%\Logs\CBS\CheckSur.log`. By opening this file, you can see [what has been broken and attempt to fix that](https://learn.microsoft.com/troubleshoot/windows-client/installing-updates-features-roles/errors-in-checksur-log).

I suggest once found errors in this log file you open [a support case](https://support.microsoft.com) to request assistance. I attempted to resolve the errors on my box, but could not resolve them all manually.

Anyway, [an in-place Windows upgrade](https://learn.microsoft.com/troubleshoot/windows-server/setup-upgrade-and-drivers/repair-or-in-place-upgrade) usually resolves all issues, which is what I did last time.

Note that this is simpler than completely reinstalling Windows on the box.

(Updated: Microsoft finally published [a similar article here to summarize the steps](https://learn.microsoft.com/troubleshoot/developer/webapps/iis/www-administration-management/troubleshooting-iis-7x-installation-issues)).
