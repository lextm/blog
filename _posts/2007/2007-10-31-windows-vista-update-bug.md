---
layout: post
title: "Windows Vista Update Bug"
description: This post talks about a bug of Windows Vista Update.
tags: Windows
permalink: /windows-vista-update-bug-cad93850ea19
excerpt_separator: <!--more-->
---
Microsoft added an update of Mobile Intel 965 Express Chipset Family driver to Windows Vista Update on October 3rd. But if you installed this update on Windows Vista Ultimate, I guess you would see blue screen again. However, [the installer from Intel](http://downloadcenter.intel.com/Detail_Desc.aspx?agr=N&ProductID=2880&DwnldID=14580&strOSs=153&OSFullName=Windows%20Vista*%20Home%20Premium,%2032-bit%20version&lang=eng&iid=homepage+dc_gmad_vis) does not have any problem. Yes, I have just helped a teammate to fix this issue.
<!--more-->

Don't panic if you see the blue screen. It apparently tells you that some driver is bad (ig****.sys). Then you cannot log in to Windows Vista Ultimate correctly except you enter the save mode. Under safe mode, navigate to Device Manager, and uninstall the display adapters (check the box in order to uninstall driver as well).

Then, reboot. This time you should be able to log in while the screen resolution is quite bad. You can download the Intel official installer and install this correct driver (if Windows Update finds a driver for you please ignore it). After installing, the wizard will tell you to reboot.

Reboot again, and you can see now you can change your resolution back to normal (and you may try a bigger resolution, too)!

Luckily, the bad driver is an optional update in Windows Vista Update, so if you are not interested in optional updates, you are safe.
