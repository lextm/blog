---
layout: post
title: "Jexus Manager: UAC Shield Icon and WinForms Buttons"
description: "This post is about how Jexus Manager shows UAC shield icon with WinForms buttons."
tags: Jexus-Manager
permalink: /jexus-manager-uac-shield-icon-and-winforms-buttons-db702ed73e13
excerpt_separator: <!--more-->
---
You might notice that in recent builds of Jexus Manager that the UAC shield icon starts to appear sometimes. This is because some operations require administrator permissions, and such permissions should be required on demand, instead of forcing you to run Jexus Manager entirely as administrator.
<!--more-->

But if you do not manipulate the items (here site bindings) that require elevation, the shield icons are gone. So what is the magic? You might find the methods in this Gist,

{% gist e966ca6bbf44403d906b %}

Microsoft carefully documents [the API on MSDN](https://learn.microsoft.com/windows/win32/controls/bcm-setshield). However, they fail to remember that we are all C# people.
