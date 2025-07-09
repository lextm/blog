---
layout: post
title: "News: NixNewNer Update 1 RC 3 is available"
description: This post is about NixNewNer Update 1 RC 3.
tags: Code-Beautifier-Collection Delphi
permalink: /news-nixnewner-update-1-rc-3-is-available-e843d2da79fb
excerpt_separator: <!--more-->
---
(CSDN June 13, 2006)

Updater is ready so I ship it now. InDate is the final name for this feature and it is put in Utilities Plus.
<!--more-->

There are some tiny problems.

1. Since I don't want most users to test RC versions, so on the blog entry page, version number is set to 5.1.0.1117, the same as NixNewNer Final. As a result, when you update, you will get "no update is available" tip. When Update 1 is shipped, this number will be changed to 5.1.1.1117, then you can use the updater to download the update.

   If you want to test RC, later version of InDate will add some options.

1. Since I am not good at threading, this InDate Dialog should be running without interrupts. For example, you should wait until it prompts you. When it is working, BDS IDE is locked.

Certainly this is not what I like, so I will fix it later.

It is still in development.
