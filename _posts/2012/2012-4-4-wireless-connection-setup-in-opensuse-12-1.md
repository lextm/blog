---
layout: post
title: "Wireless Connection Setup in openSUSE 12.1"
description: "This post is about the wireless connection setup in openSUSE 12.1."
tags: Linux
permalink: /wireless-connection-setup-in-opensuse-12-1-ccc288d10cbc
excerpt_separator: <!--more-->
---
> I am using openSUSE 12.1, but the tip should apply to other recent openSUSE releases.

I noticed an issue today during the installation of openSUSE 12.1 on my desktop machine. That is, using Live CD I can connect to Internet wirelessly (via NetGear WNA1100 wireless adapter), but once openSUSE is installed on the hard disk and boots up, I cannot find the wireless network connection initially.
<!--more-->

Other guys hit the same problem, too, http://forums.opensuse.org/english/get-technical-help-here/wireless/462402-wireless-works-live-cd-not-after-install-intel-3945-toshiba-satellite-a105.html. So here I provide a summary,

## Root Cause
The live CD uses "User Controlled with NetworkManager" mode, so you can easily set up wireless connection using the network icon in top panel.

Once installed on hard disk, openSUSE boots up with "Traditional Method with ifup" mode, in which the network icon disappears.

## Resolution
It is possible to switch modes like this,

1. Open Applications -> System Tools -> YaST.
1. Choose Network Settings from YaST items.
1. Go to the "Global Options" tab.

Now you can switch modes freely. I think a reboot is needed for this change to take effect. I stick to User Controlled with NetworkManager, which works pretty good (even better than Windows, as I have to manually install NetGear drivers on Windows).

Note that Gnome 3 does not work on my system, so in step 1 I am still using the old menu. For Gnome 3, the steps should be slightly different.
