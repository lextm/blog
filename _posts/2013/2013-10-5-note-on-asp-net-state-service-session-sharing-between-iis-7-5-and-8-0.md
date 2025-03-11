---
layout: post
title: "Note on ASP.NET State Service Session Sharing Between IIS 7.5 and 8.0"
description: "This post talks about how to configure ASP.NET state service session sharing between IIS 7.5 and 8.0."
tags: .NET IIS
permalink: /note-on-asp-net-state-service-session-sharing-between-iis-7-5-and-8-0-bfdd9d003395
excerpt_separator: <!--more-->
---
Microsoft has many articles to document how to configure ASP.NET state service session sharing, such as

http://msdn.microsoft.com/en-us/library/ms178586.aspx and http://support.microsoft.com/kb/313091
<!--more-->

However, you might need to perform actual steps. For example, if you get the following two front end servers in your web farm,

* a Windows Server 2008 R2 machine (fully patched) with a .NET 4 application pool
* a Windows Server 2012 machine (fully patched) with a .NET 4 application pool

you might find that sessions cannot be shared properly.

A fact IIS administrator might not notice is that Windows Server 2012 in fact ships with .NET Framework 4.5, so it is not 100% the same as .NET 4.0 shipped by Windows Server 2008 R2.

Thus, in order to get session sharing working, .NET 4.5 needs to be applied on the Windows Server 2008 R2 machine.

For more information, you can check [this thread](http://forums.iis.net/t/1202777.aspx?Sharing+ASP+NET+State+Service+sessions+between+IIS7+5+and+8+0+doesn+t+work).
