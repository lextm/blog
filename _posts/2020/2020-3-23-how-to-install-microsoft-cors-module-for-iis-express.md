---
description: Solution for installing and configuring Microsoft's CORS module for IIS Express, with automated PowerShell scripts to simplify the setup process for developers.
excerpt_separator: <!--more-->
image:
  alt: Copyright © Lex Li. Iced canal in Montreal.
  path: /images/iced-canal.jpg
layout: post
permalink: /how-to-install-microsoft-cors-module-for-iis-express-7ac24e4c3bc4
tags: iis microsoft powershell windows
categories: [Tools and Platforms]
title: How to Install Microsoft CORS Module for IIS Express
---
Microsoft released an IIS extension called [CORS module](https://blogs.iis.net/iisteam/introducing-iis-cors-1-0) a while ago, as to better help its customers.

Of course, this is their traditional way to shop out-of-band feature for IIS 7 and above. However, they didn't release the same bits to IIS Express users, and those developers have to resort to various hacks to resolve CORS issues there or switch to full IIS to enjoy the ease of this IIS CORS module.

Is there a way to install this module to IIS Express? The answer is YES. But the steps are bit of complicated if you don't master IIS configuration system.
<!--more-->

Therefore, I just started [a new GitHub repo](https://github.com/lextm/iisexpress-cors) with two PowerShell scripts to help you out in this situation.

With them you can easily install CORS module for IIS Express, as the install script copies the bits from IIS folders and configure IIS Express for you automatically.

If you hit any problem with the scripts, simply open an issue on GitHub so that I can take a look.

Stay tuned.
