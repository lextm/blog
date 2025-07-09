---
description: Announcing Jexus Manager 2.0 Alpha 5 with new capabilities to persist configuration changes to disk, including authentication settings, site/application management, and binding configurations.
excerpt_separator: <!--more-->
layout: post
permalink: /jexus-manager-initial-persist-to-disk-support-in-2-0-alpha-5-a022b5935f64
tags: iis jexus-manager windows visual-studio
categories: [Tools and Platforms]
title: 'Jexus Manager: Initial Persist-to-Disk Support in 2.0 Alpha 5'
---
Visual Studio does provide some basic IIS Express integration, such as opening sites from IIS Express, and exposes a limited set of settings for you to configure,

* Anonymous Authentication
* SSL Enabled
* SSL URL
* URL (not modifiable)
* Windows Authentication

That's never enough if we are used to full IIS, and IIS Manager.
<!--more-->

Does Jexus Manager for IIS Express offer something better? Yes, the following are coming in 2.0 Alpha 5,

* Changes to authentication settings are persist to disk (read-only in the past).
* Changes to sites/applications (add/removal) are persisted to disk (read-only in the past).
* Changes to site bindings are persisted to disk (read-only in the past).
* Experimental server certificate support (requires to be run as administrator).
With such new additions, it is OK now to manage quite a few important features of IIS Express.

Jexus Manager for IIS Express Alpha 5 is available.

Stay tuned.
