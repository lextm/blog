---
layout: post
title: "HardQuery Report: NFamily Plus, not-so-new features"
description: "This post talks about NFamily Plus, a few new features with it."
tags: Code-Beautifier-Collection Delphi
permalink: /hardquery-report-nfamily-plus-not-so-new-features-6bcf14061e86
excerpt_separator: <!--more-->
---
(CSDN July 13, 2006)

If you take care of the homepage, you will notice that since NixNewNer Update 1, source code are distributed separately. And if you even take a look at the code package, you will certainly find something strange named Lextm.NFamily.Plus.csproj.
<!--more-->

It is a SharpDevelop project, and is a new Plus. All features are taken directly from SharpBuilderTools, a project that has been dead since David stopped. I, as well as a lot of SBT users, still want those features to run with BDS 4, and much more than that. As a result, I add these features to CBC. Actually, because LeXDK is heavily based on SBT source code, the porting is not so hard (but I make a few changes in LeXDK which cause a lot of lines to be modified).

If you like, you can build this plus yourself, and the .plus2 file is already there (that is why NixNewNer says NFamily module is not available when BDS starts).

In HardQuery, I will make NFamily compatible with CBC totally. Also, I may update some features to meet my personal favor.
