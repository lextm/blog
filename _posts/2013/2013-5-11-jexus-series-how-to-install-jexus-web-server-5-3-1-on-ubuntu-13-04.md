---
layout: post
title: "Jexus Series: How to Install Jexus Web Server 5.3.1 on Ubuntu 13.04"
description: "This post talks about how to install Jexus Web Server 5.3.1 on Ubuntu 13.04."
tags: Jexus-Manager Linux
permalink: /jexus-series-how-to-install-jexus-web-server-5-3-1-on-ubuntu-13-04-fb344997faa0
excerpt_separator: <!--more-->
---
This is a series of posts regarding the free Linux web server called Jexus.

## What is Jexus?

Jexus Web Server is a free web server for Linux (it is free, but not open source). It is powered by Mono and aims to provide best support for ASP.NET applications (while it also provides excellent PHP support out of the box).

Its homepage is at http://www.linuxdot.net/ (in Simplified Chinese).
<!--more-->

## Install Steps

1. Install Mono runtime

   ``` bash
   sudo apt-get install mono-complete
   ```

   As Jexus requires Mono runtime, in this step we install latest stable Mono runtime (2.10.\*) via apt-get. Mono 3.0.\* is recommended if you know how to get it compiled and installed.

1. Download and unpack Jexus

   ``` bash
   wget http://www.linuxdot.net/down/jexus-5.3.1.tar.gz
   tar -zxvf jexus-5.3.1.tar.gz
   ```

   Jexus binary package is downloaded from its official site, and extracted to a folder named "jexus-5.3.1" after this step.

1. Create default web site

   ``` bash
   sudo gedit /var/www/default/index.html
   ```

   When gedit is opened, type in some text, such as "Hello World from Jexus". Save and close the file.

   /var/www/default is the default web site path for Jexus. In this step we create a test page using gedit. You might use any other Linux text editor to create this test page.

1. Install and launch Jexus

   ``` bash
   cd jexus-5.3.1
   sudo ./install
   cd /usr/jexus
   sudo ./jws start
   ```

   Here we put Jexus binary to /usr/jexus folder, grant the jws shell script file execution permission, and then use it to register Jexus modules in Mono GAC and launch the HTTP service. If you want to install Jexus to another location, please change the commands accordingly.

Now if we open Firefox and navigate to http://localhost, the test page we created is displayed correctly,

In the next post in this series, we will see how to upgrade from an older Jexus release to a new release. Stay tuned.

If you are interested in Jexus, but do not understand Chinese well, you can post your questions to https://github.com/jexuswebserver/jexus-contrib/issues.

## Updated:
Below is the alternative way in step 3 to create the test page using vi,)

1. `sudo vi /var/www/default/index.html`
1. Press i on keyboard to enter edit mode.
1. Type "Hello World from Jexus" and press Esc on keyboard to exit edit mode.
1. Type :wq and press Enter on keyboard to exit vi.