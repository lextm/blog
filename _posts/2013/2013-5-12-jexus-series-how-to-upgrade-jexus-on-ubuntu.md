---
layout: post
title: "Jexus Series: How to Upgrade Jexus on Ubuntu"
description: "This post talks about how to upgrade Jexus on Ubuntu."
tags: Jexus-Manager Linux
permalink: /jexus-series-how-to-upgrade-jexus-on-ubuntu-167ae3a1b6ef
excerpt_separator: <!--more-->
---
> In last post we discussed how to install Jexus on a clean Ubuntu 13.04 machine. Here we discuss how to upgrade from Jexus 5.2 to 5.3.1.

## What is Jexus?

Jexus Web Server is a free web server for Linux (it is free, but not open source). It is powered by Mono and aims to provide best support for ASP.NET applications (while it also provides excellent PHP support out of the box).

Its homepage is at http://www.linuxdot.net/ (in Simplified Chinese).
<!--more-->

## Upgrade Steps
1. Download and unpack Jexus

   ``` bash
   wget http://www.linuxdot.net/down/jexus-5.3.1.tar.gz
   tar -zxvf jexus-5.3.1.tar.gz
   ```

   Jexus binary package is downloaded from its official site, and extracted to a folder named `jexus-5.3.1` after this step.

1. Stop current Jexus 5.2 server,

   ``` bash
   cd /usr/jexus
   sudo ./jws.stop
   ```

   Assume the previous release was installed at /usr/jexus, we stop the service.

1. Copy new files to Jexus folder

   ``` bash
   cd ~/jexus-5.3.1
   sudo ./upgrade
   ```

   Now let's go back to the extracted folder and upgrade necessary files to /usr/jexus.

1. Fix startup commands

   ``` bash
   sudo vi /etc/rc.local
   ```

   Press i on keyboard to enter edit mode.

   Replace previous start command `/usr/jexus/jws.start` with `/usr/jexus/jws start`.

   Remove `/usr/jexus/state.start` if it presents.

   Press Esc on keyboard to exit edit mode.

   Type :wq and press Enter on keyboard to exit vi.

   Here we remove the old entries, and use a new entry to start Jexus at startup.

1. Start Jexus HTTP service

   ``` bash
   cd /usr/jexus
   sudo ./jws start
   ```
