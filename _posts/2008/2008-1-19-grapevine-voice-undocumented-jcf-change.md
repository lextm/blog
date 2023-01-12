---
layout: post
title: "GrapeVine Voice: Undocumented JCF Change"
description: This post talks about an undocumented JCF change.
tags: Code-Beautifier-Collection Delphi
permalink: /grapevine-voice-undocumented-jcf-change-54804104e7d
excerpt_separator: <!--more-->
---
According to Anthony's notes, 2.34 of JCF introduces the following changes,

* Compiled in Delphi 2007 using the latest version of JCL and JVCL
* Generics are now supported: imported and passed all of TridenT's test cases for new syntax for generics.
* The settings tree is now built in code rather than in the .dfm. this was apparently causing problems building the programs in Delphi 6 and 7.

I am so familiar with JCF that I can add one more change here,

* -config switch cannot override registry key for the setting file.

How I found this? CBC relies on this switch to format Delphi source files by calling jcf.exe like this,

So when I got this error,

I knew my overridden trick failed.

> Notice that the registry value for JCF setting file is out of date so should not be used by jcf.exe if I override by -config.

-config is not a documented command line parameter in the JCF Help file so I know one day Anthony might change the trick but I don't know it comes this soon.

I do send a message to Anthony. I will update GrapeVine when I get his reply.

Stay tuned.

(Update on Feb. 7th.:

this issue is resolved in SVN source code right now and the next release of JCF should contain this patch.)
<!--more-->