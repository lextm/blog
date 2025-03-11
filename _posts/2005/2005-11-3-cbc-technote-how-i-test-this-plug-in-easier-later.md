---
layout: post
title: "CBC TechNote: How I Test This Plug-in Easier Later"
description: A post about why I chose C#Builder 1.0 as the debugging host for CBC.
tags: Code-Beautifier-Collection Delphi
permalink: /cbc-technote-how-i-test-this-plug-in-easier-later-96cd9dafd9da
excerpt_separator: <!--more-->
---
(Originally published to CSDN on Nov 03, 2005)

Thanks to BDN because it provided a good article on C#Builder's ToolsAPI. I read it a lot of times. Maybe it is the best article I have under this subject.

Also, thanks to GExperts' pages. On that common technique of plug-in debugging is provided.

Last, thanks to myself. I chose C#Builder 1.0 IDE as the host. I am right, it works. Maybe you can try this way if you want to debug your OTA .NET plug-ins faster.
<!--more-->

There are some reasons why I succeed:

1. You know that ToolsAPI 7.1 in BDS 1.0 is a subset of BDS 3.0's ToolsAPI 9.0. So things ok for 7.1 should be ok for 9.0.

1. What's more, it works much faster. You must be tired of Delphi 8/2005's launching speed, but C#Builder 1.0 launches very fast. Also, I don't use IDE debugging, but choose to log every function call by means of Debug/Trace.

1. C#Builder 1.0 is small. Without those MS SDK and runtime files and Examples, it is just totally 40-M large.

However, later ToolsAPI introduces more features, so if you need a special feature, you should use Delphi 8/2005 to test after all.
