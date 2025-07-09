---
layout: post
title: "CatPaw Rumors: Post Release Summary Part III"
description: This post is about the CF assembly.
tags: SNMP
permalink: /catpaw-rumors-post-release-summary-part-iii-d38b80d60ab1
excerpt_separator: <!--more-->
---
It is unexpected that CatPaw needs two refresh releases (5.1 and 5.2). But it shows a few bugs need to be addressed as soon as possible.

A few bugs only occur in our command line tools. So they are minor and do not harm the whole package.
<!--more-->

The biggest problem comes from our CF assembly. It is hard to make sure everything works for CF, as I am not using .NET CF anymore. Therefore, when 5.0 was shipped we can see the CF assembly is in fact broken. I was planning to fix that all in 5.1. Fixing the csproj file and adding Mono code files are relatively easy. However, something from .NET CF itself leads to side effect.

As Microsoft cut off too many things, even though Mono classes filled in some gaps, an issue happened when I tried to work around a missing String.Split method. This breaks 5.1 release, so we have to release 5.2 this weekend.

Hope you are not bothered much by these issues. If you are, please grab our latest release which contains the fixes.
