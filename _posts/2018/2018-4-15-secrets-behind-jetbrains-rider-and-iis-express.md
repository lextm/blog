---
description: Exploring JetBrains Rider's integration with IIS Express, including configuration management, hidden applicationHost.config files, and standard output capturing for debugging.
excerpt_separator: <!--more-->
image:
  alt: Copyright © Lex Li. Autumn time at Columbia University.
  path: /images/columbia-university.jpg
layout: post
permalink: /secrets-behind-jetbrains-rider-and-iis-express-d2ad006301e1
tags: .net iis
categories: [Programming Languages]
title: Secrets Behind JetBrains Rider and IIS Express
---
I did not realize JetBrains was working on IIS/IIS Express integration, as I uninstalled Rider from my Windows machine, and only use it on Mac. However, it was [a Stack Overflow thread](https://stackoverflow.com/questions/45560884/jetbrain-rider-access-denied-when-using-iis-express-with-windows-authenticatio) that drew my attention a few days ago.
<!--more-->

So it was surprising to see that JetBrains decided to,

* Follow Microsoft's approach to use a hidden `applicationHost.config`, but in its `.idea` folder.
* Design the relevant UI elements for configuration.

![img-description](/images/rider-iis-express.png)
_Figure 1: Rider dialog on IIS Express settings._

You can also see from the bottom left corner that IIS Express standard output is also captured and displayed in Rider so that troubleshooting issues should be easier (than VS).

> Note that the relevant UI elements might only appear in EAP/nightly builds.

I might come back to post more about the integration once it is available in a Rider stable release. Stay tuned.

Update: Jexus Manager now supports both VS and Rider's private config files,

![img-description](/images/jexus-manager-rider.png)
_Figure 2: Jexus Manager with Rider support._
