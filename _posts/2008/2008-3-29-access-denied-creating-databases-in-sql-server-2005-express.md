---
layout: post
title: "Access Denied: Creating Databases in SQL Server 2005 Express"
description: This post talks about why you cannot create new databases in SQL Server 2005 Express.
tags: Microsoft
permalink: /access-denied-creating-databases-in-sql-server-2005-express-deae52d56b4b
excerpt_separator: <!--more-->
---
Most people wonder why they have deployed SQL Server 2005 Express but failed to create new databases with it. And the error message is most confusing,

> Error 5 & Access Denied

Even if you think you have enough rights to access the folder (yes, when you are the administrator).

Though Google is a nice place to find solutions, this time you will get lost in the seas of puzzles because nobody provides a complete explanation.

I met this issue last week and in my case to reinstall SQL Server 2005 Express is the only work around I found.

Remove the SQL Server 2005 Express installed. And then use the standalone installer from Microsoft to install it.

Remember this time, when I enter this page during installation, please uncheck Hide advanced configuration options.

Then in this page, select Local system instead of Network service.

In my case, no other default options are changed. OK. Everything works well now.

As a result, when I deploy SQL Server Express with my application, I no longer make it install silently but provide my clients a guide on how to use the GUI installer and install with advanced configuration options. Although this makes the installation experience interrupted and kind of complicated, the issue has gone.

Wish this post helps. And if you know how to configure the Local system setting without reinstallation, please leave a comment here to let me know.
<!--more-->
