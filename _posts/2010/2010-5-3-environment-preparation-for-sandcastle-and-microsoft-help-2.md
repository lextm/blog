---
layout: post
title: "Environment Preparation for Sandcastle and Microsoft Help 2"
description: This post is about how to prepare the environment for building Microsoft Help 2 in Sandcastle.
tags: .NET
permalink: /environment-preparation-for-sandcastle-and-microsoft-help-2-5dc393d6cd66
excerpt_separator: <!--more-->
---
I found it very hard to prepare the environment for building Microsoft Help 2 in Sandcastle, so below are the steps for your reference.
<!--more-->

1. Download and Install a Microsoft product that contains Microsoft Help 2 runtime, such as Visual C# 2008 Express.
1. Download and install VS2005 SDK following to this article,
http://helpware.net/mshelp2/h2faq.htm#novsnet2. I choose to install FEB 2007 v4 RTM.

If you experience this issue,

``` text
Error HXC4001: File file://…/Help2x.hxc, Line 2, Char 77: XML syntax error: No data is available for the requested resource.
Error processing resource 'MS-Help://Hx/Resources/HelpCollection.dtd'.
Fatal Error HXC2056: Parse of the .HxC file failed.
BUILD FAILED: Unexpected error in last build step. See output above for details.
```
please follow suggestion of this article.

On my computer, Resources.HxC is here, C:\Program Files (x86)\Visual Studio 2005 SDK\2007.02\VisualStudioIntegration\Archive\HelpIntegration\Resources.HxS

If you use Sandcastle Help File Builder then it may report Sandcastle is too old. That's because VS2005 SDK ships a very old version of Sandcastle. Please download the suggested version and then manually configure SHFB to use the new version.
