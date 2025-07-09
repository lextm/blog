---
description: This post is about the new rules for CBC installer.
excerpt_separator: <!--more-->
layout: post
permalink: /what-are-they-new-rules-for-installer-distributions-rule-1-df7b0ac42df9
tags: delphi sharpdevelop .net code-beautifier-collection
categories: [Tools and Platforms]
title: What are they? New Rules for installer distributions (Rule 1)
---
(CSDN May 25, 2006)

Rule 1: Which projects you should use to rebuild from source?
<!--more-->

For Release Candidates, the source code contained may not be compiled easily. For most cases, SharpDevelop projects are used by me, so they are up-to-date. NAnt files and BDS projects may be out of date.

For Final and Updates, all projects should be okay.

The reasons:

I love SharpDevelop a lot, although it is not yet perfect. So I use it to maintain the projects.

NAnt scripts are easiest to use but hardest to write. So I do this work at last.

BDS projects are kept for some users who do not want to try SharpDevelop. Yes, BDS itself is quite excellent, but its future is not clear.
