---
layout: post
title: "Force SQL Server Express to Local System"
description: This post talks about the  SQL Server issue that troubles me a lot in the past.
tags: Code-Beautifier-Collection Delphi
permalink: /force-sql-server-express-to-local-system-3e52f628b23c
excerpt_separator: <!--more-->
---

[In this post]({% post_url 2008/2008-3-29-access-denied-creating-databases-in-sql-server-2005-express %}) I talked about the issue that troubles me a lot in the past. And no MSDN material is so obvious that I can resort to.

<!--more-->

But today, I finally find where to set the local system option even if you does not install the instance with local system option checked. Unbelievably it is here in the Services panel.

Simply change the Log on as: option to Local System account, everything goes fine suddenly.

Hope this help when you come across the same issue.
