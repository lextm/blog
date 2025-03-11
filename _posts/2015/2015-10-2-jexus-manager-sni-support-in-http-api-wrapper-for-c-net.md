---
layout: post
title: "Jexus Manager: SNI Support in HTTP API Wrapper for C#/.NET"
description: "This post is about how to access SNI information in C# code."
tags: Jexus-Manager IIS .NET
permalink: /jexus-manager-sni-support-in-http-api-wrapper-for-c-net-3c56d620b2b2
excerpt_separator: <!--more-->
---
You probably know already that [IIS 8 and above start to support SNI](https://www.iis.net/learn/get-started/whats-new-in-iis-8/iis-80-server-name-indication-sni-ssl-scalability), and also know that such information is stored in HTTP API (http.sys related).
<!--more-->

But how to access such information in C# code? If you did a search on the Internet about such info, probably you hit nothing as the materials were out of date and only focus on IP based certificate mapping.

Today, I have just finished the initial revision of Jexus Manager with SNI support, so such a wrapper is available that supports both IP based certificate mappings, and SNI based ones,

{% gist fd410eafd82321c6bfd6 %}

SNI based mappings can be queried via `NativeMethods.QuerySslSniInfo()`.

The source code is released under MIT license. You might report any issue back to this post.
