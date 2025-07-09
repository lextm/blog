---
layout: post
title: "Configure AVG Free for Linux"
description: This post describes how to configure AVG Free for Linux on Ubuntu.
tags: Linux
permalink: /configure-avg-free-for-linux-ac164e5234c6
excerpt_separator: <!--more-->
---
I love AVG Free, but because viruses and Trojans are serious in China I use a commercial product named KAV7 on Windows Vista.
<!--more-->

However, for Ubuntu Linux, I am sure that AVG Free is a nice choice. The installation is simpler than the official manual. Simply right click the avg75fld-*.deb package, and choose Open with "GDebi Package Installer".

After installing, you will find AVG Free activated except the Update feature. Why it says "Update process failed. Reason: Sorry, you do not have permission to execute avgupdate."?

According to a thread or two on the AVG Free Forum, the normal user account such as lextm is not a member of a so called avg group.

Now all you have to do is simply launch a Terminal and type in

``` bash
sudo usermod -a -G avg lextm
```

Then please log out or reboot in order to apply the change.

Now you can go on to configure other options of AVG Free for Linux on your Ubuntu at home.
