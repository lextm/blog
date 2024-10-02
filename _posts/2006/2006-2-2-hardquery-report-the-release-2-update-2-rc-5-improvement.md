---
layout: post
title: "HardQuery Report: the Release 2 Update 2 RC 5 improvement"
description: A post about HardQuery Release 2 Update 2 RC 5 improvement
tags: Code-Beautifier-Collection Delphi
permalink: /hardquery-report-the-release-2-update-2-rc-5-improvement-600f40f5e02b
excerpt_separator: <!--more-->
---
(CSDN Feb 02, 2006)
<!--more-->

When you edit a C# XML comments such as
``` csharp
///
/// Logging service class.
///
/// Debug related functions such as Debug,
/// EnterMethod, and
/// LeaveMethod are
/// available only in Debug Build mode.
```

and press Alt + Q in Delphi 2006 with CBC installed, you may see the Doc Preview dialog and see a few hyper links in it. However, when you click on one link, because the target page is not available, an annoying default error page of IE will be displayed. It is a bug, but I cannot fix it until the day before yesterday.

When I was asked to browse an article on the Code Project for a friend, I came across an x.doc plug in for VS which does similar task as CBC Doc Preview. In the article, its author shows how to prevent the above mentioned error page. In fact, the browsing action should be disabled when a user clicks the links. I found his idea and used it in CBC now. As a result, a long life bug is now fixed.
