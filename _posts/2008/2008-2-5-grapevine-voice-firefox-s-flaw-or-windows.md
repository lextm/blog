---
description: This post talks about the issue that prevents me from setting Firefox
  as my default web browser.
excerpt_separator: <!--more-->
layout: post
permalink: /grapevine-voice-firefoxs-flaw-or-windows-e108ed376916
tags: code-beautifier-collection delphi
categories: [Tools and Platforms]
title: 'GrapeVine Voice: Firefox''s Flaw or Windows'''
---
I'd like to set Firefox as my default web browser. However, then strange things happens. I cannot open an HTML file by double clicking it in Windows Explorer without a warning.
<!--more-->

.NET has a similar issue. When you Process.Start() an HTML file, an exception is thrown. That's why in CBC I am forced to forward such calls to Internet Explorer directly.

But NetSpell library used in CBC does not work around this issue, so when you click the linked button in the following dialogue,

you must meet this exception dialogue,

Please remember to click Continue. Otherwise your IDE may be closed unexpectedly.

Stay tuned.
