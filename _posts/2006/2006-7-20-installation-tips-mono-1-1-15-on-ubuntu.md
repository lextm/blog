---
layout: post
title: "Installation Tips: Mono 1.1.15 on Ubuntu"
description: "This article describes how to install Mono 1.1.15 on Ubuntu."
tags: Mono Linux
permalink: /installation-tips-mono-1-1-15-on-ubuntu-53bd76750e6
excerpt_separator: <!--more-->
---
(CSDN July 20, 2006)

Mono 1.1.15 is not new but it was just yesterday that I made it run on my Ubuntu Dapper Drake.

I am not using the apt-get way. That way gives me Mono 1.1.13 at this moment. The Mono homepage provides a .bin installer for all Linux distributions (RH and SuSE are all Novell is thinking about).

For Ubuntu users like me, it is not hard to use this installer of 1.1.15, too.
<!--more-->

First, install mozilla-browser. You can use apt-get for this.

Second, make the .bin file runnable. It is not hard, isn't it?

Third, sudo ./**.bin.

You should then find a link on the desktop, and you will find what to do next.

Even if this auto-created link fails, the executable monodevelop in MONOFOLDER/bin folder should be okay. Launch it to use MD.

Have a nice day with Mono and Ubuntu.

(Added on 07/21)

You must pay attention to the third step. It is very important to sudo this. When you are correct, Mono installer should choose /opt/mono-1.1.15 as the default folder and install Mono well. Otherwise, monodevelop launches with exceptions.

Also, it seems that Mono installer .bin conflicts with SCIM and cannot finish under Chinese Ubuntu. I do not know how to disable SCIM easier, but change the default language of Ubuntu to EN (U.S.). Maybe you should do the same, if you use Chinese language support.

At this moment, I have not made mono 1.1.16.1 running. I will check that issue later.
