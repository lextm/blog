---
layout: post
title: "Cross Platform Object Pascal (Part I)"
description: This post talks about that there are totally three major groups working on cross platform Object Pascal.
tags: Code-Beautifier-Collection Delphi
permalink: /cross-platform-object-pascal-part-i-e4d73af87646
excerpt_separator: <!--more-->
---
> This post was original named as RemObjects Updates because after reviewing what RemObjects has done in the past two years, I am sure this company is doing something good. But soon there was a thread on CodeGear newsgroup about Delphi and the .NET platform which I involved, I thought it is now the time to write about something different.

Object Pascal is not a new language. However, its cross platform support is required by many developers. Therefore, there are totally three major groups working on this issue.
<!--more-->

## Borland/CodeGear Delphi/Kylix

In the past, when we talked about Object Pascal, we must be referring to Borland Delphi. So when Kylix for Delphi was out there, we all knew that Delphi became cross platform (for Windows and Linux). Even though Kylix was not yet perfect, it was once the best way to do cross platform Object Pascal development. However, Borland stopped this product line and CodeGear now has not enough resources to revive it.

## FPC Community

The second trial in this field is Free Pascal Compiler. And have to say it is wonderful that FPC supports so many platforms (not only Windows and Linux). This reminds me of GCC, but it is sad that there are still lots of issues. First, it is not 100% Delphi compliant. Second, the IDE for it is not that perfect. Third, there are some copyright issues unresolved. Even though it is a very successful open source project but using it in commercial applications seems impossible.

## RemObjects Chrome

The latest and promising solution is provided by RemObjects. Yes, it is Chrome for .NET/Mono. Even though there is no more VCL in Chrome, the .NET BCL is still powerful enough. And as Microsoft continues to add new pieces into .NET, Chrome has lots of libraries and components. Novell tries its best to make Mono stronger each day, so now Chrome for Mono applications can run on Linux and Mac OS X.

## My Choice

So what is the best solution? I believe if CodeGear can revive Kylix or take over FPC, Delphi is still the best. Win32\64 + .NET/Mono + native cross platform is most complete solution that meets everyone's requirements. Chrome is the second because cross platform .NET/Mono can handle most problems. You can try FPC if either Delphi or Chrome fails you.