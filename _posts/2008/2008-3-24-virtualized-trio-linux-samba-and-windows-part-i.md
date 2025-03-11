---
layout: post
title: "Virtualized Trio: Linux, Samba, and Windows, Part I"
description: This series focus on virtualized development environment.
tags: Windows
permalink: /virtualized-trio-linux-samba-and-windows-part-i-65565fa237b4
excerpt_separator: <!--more-->
---
> This series focus on virtualized development environment.

Although latest virtualization software such as VMware, VirtualBox, and Virtual PC supports file sharing between host and guest, you may find it not optimal especially when Linux is the guest. For example, if VMware is used, you can see files listed under hgfs folder in the Linux guest have restricted access control which can bring in problems.

It was last week I knew what Samba is and why it is useful in this very case. Therefore, I started to investigate how to set up a proper environment at office and at home.

In this part, I am going to tell how to do it at home with the following components,

* Host: Windows Vista Home Basic RTM
* VM: VirtualBox
* Guest: Ubuntu 7.10
<!--more-->

## VM Setup

Modify Ubuntu VM network adapter settings. Change the adapter from NAT to Host Interface. Please notice that "VirtualBox Host Interface 1" should be used.

If there is no name listed under Interface Name, please create a new interface in Host Interface group.

## Host Setup

Normally I use NAT networking option on the VM. However, in VirtualBox case, it is impossible to ping the guest from host. Thus, another approach must be used.

Luckily I found this post, so I know the existence of VirtNet driver,

http://forums.virtualbox.org/viewtopic.php?t=4580&highlight=samba+ubuntu

* install VirtNet driver. http://www.ntkernel.com/w&p.php?id=32
* create a bridge using these two NICs (VirtNet and VirtualBox Host Interface 1).
* assign an IP to the bridge (such as 192.168.1.30).

> Notice, because it is very easy to configure on Windows, I do not provide screen shots here.

## Guest Setup

Now let's move to Ubuntu. Open Administration | Network and there should be one Wired connection there.

Change the settings like this,

Please restart Ubuntu in order to activate the settings.

Then, open Administration | Shared to configure Samba. It is weird that Ubuntu guys use the title "Shared Folders" here, while Fedora guys directly use Samba title.

In Fedora it is quite easy to configure one more setting, the users. However, Ubuntu does not provide a dialogue. Thus, according to this help, command line is unavoidable,

https://help.ubuntu.com/community/SettingUpSamba

``` bash
sudo smbpasswd -a username

New SMB password:
Retype new SMB password:
Added user username.
```

I use user name `lextm` and `123456`.

## Test

Now let's launch a command prompt on host and type in,

``` bash
ping 192.168.1.31
```

Then you can map a network drive `\\192.168.1.31\lextm`.

When Windows asks for user name and password, use `MSHOME\lextm` and `123456`.

OK. Wish you could configure everything right now. If you meet any issue, please leave a comment.
