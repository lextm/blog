---
layout: post
title: "News: A Simple Updater is ready"
description: This post is about the new feature that can update CBC automatically.
tags: Code-Beautifier-Collection Delphi
permalink: /news-a-simple-updater-is-ready-567efd6d9ef0
excerpt_separator: <!--more-->
---
(CSDN June 12, 2006)

I thought it was hard to implement. However, after some careful thinking and drawing, the picture is now clear.

Since I do not have another solid place to store the link to latest release (on GForge, every new file takes a new location), in order to make CBC easy to find the link, I post a special blog entry here which contains the links.
<!--more-->

The updater in CBC first browses and saves this blog entry to HTML file, then reads the links, and downloads the zip archive. Finally after unzipping, it executes the update installer.

What is missing now is that version checking is not added. Once the updater can analyse the version of the package, this feature is complete.

Stay tuned…
