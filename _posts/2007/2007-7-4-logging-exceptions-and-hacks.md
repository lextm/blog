---
layout: post
title: "Logging, Exceptions, and Hacks"
description: "This post describes how to log exceptions."
tags: Others
permalink: /logging-exceptions-and-hacks-83bec1bf4075
excerpt_separator: <!--more-->
---

In the development of my project, I have to connect to a device through sockets. The problem is that this device driver has a bug that prevents a PC to create a second socket with it. This means I have to take care of the socket I create every time. If a socket is not closed, I will never be able to connect to the device again. I do not want to reboot the device. However, there seems to be necessary.

Since I am not the only one on this project, I ask for help. There is no positive reply. The one who is responsible to the socket part does not want to share the source with me. So what I can do is disassemble his part and modify it directly. Luckily I know how to use log4net, so I can insert some code to generate logs about socket creations and deletions. After reading the logs I can find out where is the leakage.

The conclusion is that most leakages are caused by exceptions. Because some exceptions are not correctly handled, some created sockets are not deleted at all.

The code quality is not quite good which causes a lot of trouble. But, I am not the one who designs the software, which means sometimes I have to fix some bugs in the background (such as hacking some DLLs). Maybe when Vault is installed and used here, I can publicly merge the fixes into the code tree.

Anyhow, it is funny to work in this project. Refactoring and patterns help me a lot.
<!--more-->