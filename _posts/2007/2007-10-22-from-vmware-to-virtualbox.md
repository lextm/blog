---
layout: post
title: "From VMware to VirtualBox"
description: This post talks about my migration from VMware to VirtualBox.
tags: Windows
permalink: /from-vmware-to-virtualbox-eda6ec764f49
excerpt_separator: <!--more-->
---
VMware (VMW) is cute but I could not afford the Workstation at home, so I turned to its Server. After it crashed on Windows Vista, I moved to its Player and found that I could not create an image in it. That is VMware personal product line, neither suits my requirements of cheap, stable, and not quite feature limited.

Then I met VirtualBox last weekend. Have to confess it looks ugly (reminds me of Windows 95). But its feature set is rich and it is free (according to the license FAQ I can even install it at office).
<!--more-->

Today I tried to migrate a VMware Server created Ubuntu image to VirtualBox. I failed not because of VirtualBox issues, but thanks to VMware Tools. I am not familiar with Linux command line interface (CLI) so I cannot uninstall VMware and install VirtualBox addition instead.

Therefore now I am downloading the latest Ubuntu release 7.10. I will try it this afternoon.

(Updated: VirtualBox does have a weakness that newer versions do not support VM created by older versions well. Hope this issue can be fixed in the near future.)
