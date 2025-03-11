---
layout: post
title: "Microsoft SQL Server Instances"
description: This post talks about why there are several SQL Server services running on my workstation.
tags: Microsoft
permalink: /microsoft-sql-server-instances-14d9f80ef5e9
excerpt_separator: <!--more-->
---
I was curious about why there are several SQL Server services running on my workstation. Because there was no problem with the system, I did not spend time on this question but I knew one day I would find the answer. And today, the day comes.
<!--more-->

When I tried to execute an SQL script with isql.exe, I could not connect to SQL Server (DB-Library and Net-Library errors). Soon I found that isql cannot connect to named instances of SQL Server 2000 and 2005. Yes, that is the point. isql seems to be an old utility for SQL Server 6 and 7 so it never knows named instance feature introduced in SQL Server 2000 and 2005.

Do you know what is named instance feature? That feature enables you install multiple SQL Server on one Windows. That's exactly why I have many SQL Server services.

I am still digging how to execute SQL script for named instances. It is funny to see some legacy utilities still exist in SQL Server 2000 and 2005 installation without any modifications to suit new features at all. Wonder why Microsoft gets no complaints about that (Yes, I am complaining now).
