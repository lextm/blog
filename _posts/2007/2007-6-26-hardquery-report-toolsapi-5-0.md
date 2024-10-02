---
layout: post
title: "HardQuery Report: ToolsAPI 5.0"
description: This post describes about Borland.Studio.ToolsAPI.dll 5.0.
tags: Code-Beautifier-Collection Delphi
permalink: /hardquery-report-toolsapi-5-0-fe0127a56797
excerpt_separator: <!--more-->
---

Borland.Studio.ToolsAPI.dll is an important reference assembly used by Code Beautifier Collection and other experts. Version 1–4 of it was built against .NET 1.1. And now, version 5 included in Delphi 2007 and C++Builder 2007 is against .NET 2.0.

In order to consume the interfaces defined in ToolsAPI 5.0, CBC should be compiled against .NET 2, too. However, I guess the source code can still be ported back to .NET 1.1 with modifications. Now I am evaluating the possibility.

Remember, even if the back port is possible, I insist Delphi 2007 and C++Builder 2007 be used. Support to older versions of BDS is stopped once 5.3.3 is released.

BTW, an experimental build of GExperts with DelForEx has been uploaded to CodeCentral now.
<!--more-->