---
layout: post
title: "Jexus Series: Application Pool Setting"
description: "This post talks about Jexus application pool setting."
tags: Jexus-Manager
permalink: /jexus-series-application-pool-setting-7e026fdff6f7
excerpt_separator: <!--more-->
---
Unlike IIS who has full application pool support, Jexus currently only supports a single application pool.

> For more information on Jexus/IIS comparison you can go to https://github.com/jexuswebserver/jexus-contrib/blob/master/comparison.en.md

To configure IIS application pool, you might follow [this article](http://www.iis.net/configreference/system.applicationhost/applicationpools).
<!--more-->

Microsoft exposes many options for you to configure an application pool, but Jexus only exposes a few,

| Option | Description |
| ------ | ----------- |
| httpd.processes | Equivalent to IIS's maxProcesses, which enables/disables Web garden.
| httpd.user | Equivalent to IIS's userName, which specifies worker process identity. Note that due to Linux mechanism, there is no need to specify password in Jexus.
| Runtime | Equivalent to managedRuntimeVersion. Note that Jexus supports the IIS style (major.minor), so it is valid to use Runtime=v4.0. |

Jexus supports application pool recycle in the following manner,

* It supports overlapping rotation. Equivalent to disallowOverlappingRotation=false.
* It automatically recycles the pool every 29 hours. Equivalent to IIS default application pool recycle setting.
* It does not generate a log entry when rotation starts.
* It does not support on demand recycle or any other recycle triggers yet.

The Jexus developer promises to expose more in future releases, and then this post might be updated.

For all information on Jexus configuration, please go to https://github.com/jexuswebserver/jexus-contrib/blob/master/readme.en.md
