---
layout: post
title: "GrapeVine Voice: JCF Deeper Integration"
description: "This post talks about the improved integration of JCF into GrapeVine."
tags: Code-Beautifier-Collection Delphi
permalink: /grapevine-voice-jcf-deeper-adapting-83f7e56f48e4
excerpt_separator: <!--more-->
---
Code Beautifier Collection makes use of JEDI Code Format console program to format Object Pascal source files. What has been missing for a long time is an editor that enables users to modify default Borland style to suit their unique needs. I put this feature high in the list, but it is until now I have enough time and knowledge to make the editor ready.

In fact, JCF contains such an editor in its source code, but the editor is only available in GUI versions of JCF. So now I split the editor into a separate project named JCFStyle, and include this executable in GrapeVine's upcoming M8. I will also update the preferences dialog box so you can launch this executable easily from within the IDE. This small utility is also licensed under MPL as JCF.

Stay tuned.
<!--more-->
