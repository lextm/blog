---
layout: post
title: "Weird or Not: Undocumented Changes in OTA"
description: This post is about undocumented changes in Delphi IDE OTA.
tags: Code-Beautifier-Collection Delphi
permalink: /weird-or-not-undocumented-changes-in-ota-648b47d2db58
excerpt_separator: <!--more-->
---
(CSDN June 23, 2006)

Lately a bug in older N3 versions is reported and fixed.
<!--more-->

When you launch delphi personality, and create a new project, some null reference exceptions show. It is not hard to find the origin of the bug. In WiseEditor Plus AutoCompletion, a trigger is added to IOTAEditor's Modified event. However, when a project file .bdsproj or a Together model file is opened, this trigger should not be added and the trigger event should never be fired.

After fixing this, I turn to test on delphi 2006, and found the bug is gone. This fix is included in N3 Update 1 RC 5.

But today, when I begin to test CBC latest version on delphi 8, I found the old version of CBC N3 (internal version string is NixNewNer 1) ran well when a new project is created. It is weird or not?

A possible answer is that delphi OTA is changed from 7.1 to 9.0, so some internal changes make things different. I heard about this kind of internal changes before (as so many people complaint), and this was the first time I met it.

But after a few seconds I thought that it was normal. How many times I changed LeXDK without declaring the changes?

After all, now this bug is fixed. In all, I should first correct my mistakes and then complaint.
