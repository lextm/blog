---
layout: post
title: "New Structure for WalkPace Final"
description: A post about new architecture for WalkPace Final
tags: Code-Beautifier-Collection Delphi
permalink: /new-structure-for-walkpace-final-4fcea361893f
excerpt_separator: <!--more-->
---
(CSDN March 16, 2006)

Old CBC contains a few assemblies, typically three.

However, in this recently release of WalkPace, more assemblies are coming.

It is the direct result caused by architectural changes.

Now I decide to release some kind of an SDK to develop OTA utilities. CBC itself is now built on this SDK.
<!--more-->

How important is the SDK or LeXDK?

Last Update of CBC BF is a bad experience in fact. I have to update all assemblies on your PC in order to bring you all new features.

But since the shipping of this LeXDK, I can make sure that the features can be added without frequent updates.

Reflection technology is used to dynamically load the Plus (some kind of extension of CBC, will be mentioned in later articles). So now you can extend CBC by adding Plus Pack or by programming on the LeXDK yourself.

Some old Delphi guys may say it is VBish. However, I find it an easy to encapsulate functions and types. Also it isolates the bugs so that I can fix them one by one.

Wish I could finish this stage before April.
