---
description: Troubleshooting guide for IIS Express issues after upgrading to Visual Studio 2015, including configuration file changes and common 500.19 errors with MIME types.
excerpt_separator: <!--more-->
layout: post
permalink: /iis-express-failures-after-upgrading-to-visual-studio-2015-6dd3d7eabc7a
tags: iis visual-studio
categories: [Tools and Platforms]
title: IIS Express Failures After Upgrading to Visual Studio 2015
---
The following changes in VS 2015 will affect your development if you upgrade from VS 2012/2013,

* IIS 7/8 Express is uninstalled, and IIS 10 Express is installed.
* VS2015 uses `<solution folder>\.vs\config\applicationHost.config` as IIS Express configuration file. This new configuration is based on IIS 10 Express, so not fully compatible with previous IIS Express releases.

The changes break the following scenarios.
<!--more-->

## Settings Overridden in Web.Config Leads to 500.19 Errors

Many settings such as MIME types are significantly changed in IIS 10 Express (`.vs\config\applicationHost.config`). So if you added your own MIME types in `web.config` in the past, and now you might hit 500.19 reporting that duplicate elements are detected.

[A workaround](https://stackoverflow.com/questions/33660627/iis-registered-mime-types/) that works for all IIS Express releases is to always remove such elements from `web.config` and then add them.

This does not only apply to MIME types, but also other IIS settings if they vary from IIS 7/8 Express to IIS 10 Express.

## Changes to Global Configuration File Does Not Take Effect

Of course, you will have to modify `.vs\config\applicationHost.config` from now on, unless you do want to enable the global configuration file via project file hack.
