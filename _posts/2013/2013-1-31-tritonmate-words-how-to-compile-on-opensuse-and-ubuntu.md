---
description: 'Finally I learned how to run NuGet on Mono, so below is the updated
  steps to build #SNMP latest code base on Mono and openSUSE.'
excerpt_separator: <!--more-->
layout: post
permalink: /tritonmate-words-how-to-compile-on-opensuse-and-ubuntu-f4cf99c83309
tags: .net linux mono snmp
categories: [Programming Languages]
title: 'TritonMate Words: How to Compile on openSUSE and Ubuntu'
---
Finally I learned how to run NuGet on Mono, so below is the updated steps to build #SNMP latest code base on Mono and openSUSE.
<!--more-->

1. Install necessary packages

   ``` bash
   sudo zypper install mono-complete git
   ```

1. Clone #SNMP code base

   ``` bash
   git clone git://github.com/lextudio/sharpsnmplib.git
   ```

1. Prepare to build

   ``` bash
   ./prepare.sh
   ```

1. Import certificates

   ``` bash
   mozroots --import --sync
   ```

1. Download Microsoft.Build.dll from my DropBox folder, which comes from Mono 3.0 Windows installation, and copy it to .nuget folder in #SNMP source folder.
cp ~/Downloads/Microsoft.Build.dll ~/sharpsnmplib/.nuget

1. Start the build

   ``` bash
   ./release.sh
   ```

Note that the first step is slightly different on Ubuntu,

``` bash
sudo apt-get install mono-complete git mono-vbnc mono-devel mono-xbuild
```
