---
layout: post
title: "Open Source Licenses Puzzle"
description: This post is about open source licenses puzzle.
tags: Code-Beautifier-Collection Delphi
permalink: /open-source-licenses-puzzle-d40590fbe2ad
excerpt_separator: <!--more-->
---
I am not a law school student, so I cannot understand those words. So today when I suddenly came across this link, I found that Code Beautifier Collection may break some rules somewhere.
<!--more-->

> "That is, a module covered by the GPL and a module covered by the MPL cannot legally be linked together."

This line may indicate that CBC cannot make use of jcf.exe and jcfstyle.exe which are MPL covered. However, if we consider that CBC in fact is shell executing them and does not link to them, this may not be an issue.

Should I find a lawyer to help clear the clouds and dusts? Who can solve this puzzle? Certainly I would remove incompatible parts in future releases.

If you want to start an open source project under GPL, I recommend you take a look at [this link](http://www.gnu.org/philosophy/license-list.html) at first and know what kind of code can go into your project.