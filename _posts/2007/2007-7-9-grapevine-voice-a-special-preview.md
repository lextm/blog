 ---
layout: post
title: "GrapeVine Voice: A Special Preview"
description: "This post describes about a special preview build of GrapeVine release."
tags: Code-Beautifier-Collection Delphi
permalink: /grapevine-voice-a-special-preview-e51d4bbaf9bd
excerpt_separator: <!--more-->
---
I am planning to release a special GrapeVine Preview. Why? There are several reasons,
<!--more-->

1. Now I am using a Vista Home Basic machine to develop GrapeVine, and CTeX cannot generate PDF documents. So, there is no document available at this moment.
1. There is no Delphi for .NET compiler for me to build Lextm.AddMany.dll on .NET 2.0. I know I can do it in Delphi 2006, but now I do not have it installed. So, AddMany feature is not available.
1. Delphi 2007 IDE is much stronger than Delphi 2006, which means some features in CBC must be turned off. So, some features are missing.
1. I am planning to change the package naming schema to distinguish GrapeVine builds from older builds in order to prevents older versions from updating to GrapeVine. However, the InDate update would be provided after publishing the Preview. So, the Preview build cannot update to later Milestone builds automatically.

Don't get me wrong. As a matter of facts, the Preview can do a lot of work for you except for the missing parts.

I will publish it soon (Maybe tonight). Stay tuned.

BTW. Because this version cannot update itself, no version number is given. If there is one, it is meaningless. So, never report a bug of it to me.

Remember, GrapeVine is for Delphi 2007/C++Builder 2007 only.

(Updated: I did not take care of UAC at first, and now find that CBC is not UAC compatible. So the Preview build cannot function correctly if UAC is turned on. It should run well on other Windows.)

It is now available at GForge.
