---
layout: post
title: "Parallel Mono Environments, Some Update"
description: "This post talks about how to set up parallel Mono environments with latest updates."
tags: Mono
permalink: /parallel-mono-environments-some-update-3916d327ec97
excerpt_separator: <!--more-->
---
The Mono guys have [a good guide](http://www.mono-project.com/Parallel_Mono_Environments) on how to set up parallel Mono environment. However, it was pretty old (for Mono 1.* phase). I tried to build up my own paralle Mono environment for the first time a few days ago, so here I documented what are the changes you should pay significant attention to while preparing the same environment for Mono 3.2.8.
<!--more-->

## Migrating to Git

Mono source code is now fully hosted on GitHub, so you don't need source tarballs any more, and can directly go to https://github.com/mono to grab the Git clones.

## Autogen.sh and bootstrap-*

Make sure you execute `./autogen.sh --prefix=/opt/mono` if you cannot see `configure`. For gtk-sharp, you need to run `./bootstrap-* --prefix=/opt/mono`.

## Choose the Correct Branch

Don't build everything from master branch, as sometimes you cannot get it compiled.

For mono, you should use mono-3.2.8-branch to get 3.2.8. Mono master is currently broken.

For gtk-sharp, you should use gtk-sharp-2–12-branch. Gtk master is currently hosting 3.0 early builds.

For other stuffs (libgdiplus, mono-addins, mono-tools, mono-basic) you can try out master, as they are relatively slow growing, and the master branch should be kind of stable.

## Dependencies

How to get correct dependencies on your Linux distro is really the most challenging part of the whole build process. As it heavily varies on distros, I will only cover Ubuntu.

The scripts autogen.sh or bootstrap-* will tell you what is missing, and what are the assemblies that cannot be built (pay attention to this, as if the assembly is showed as no, you cannot get the desired assembly later). Grab the names of the missing components, and go to Ubuntu packages portal to search for them, http://packages.ubuntu.com/, most of the times you can find what you are looking for.

Below is a list of dependencies (might be incomplete) I installed along the road,

``` bash
sudo apt-get install git mono-complete monodevelop autoconf libtool automake libcairo2-dev libpng-dev glib-2.0 libtiff-dev libgif-dev libjpeg-dev libpango1.0-dev libatk1.0-dev libgtk2.0-dev libglade2-dev libgnome2-dev libgnomecanvas2-dev libgnomeui-dev
```

## MonoDevelop

If you plan to run previous MonoDevelop binaries (not compile it from the code) on the newly built mono, don't forget to clone gnome-sharp and get it installed. Otherwise, you lose Gnome integration.
