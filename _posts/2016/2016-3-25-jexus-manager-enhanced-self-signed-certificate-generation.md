---
description: A comparison of self-signed certificate generation capabilities between IIS Manager and Jexus Manager, highlighting the enhanced customization options available in Jexus Manager for modern certificate requirements.
excerpt_separator: <!--more-->
layout: post
permalink: /jexus-manager-enhanced-self-signed-certificate-generation-9ff4940d6b07
tags: iis jexus-manager windows microsoft
categories: [Tools and Platforms]
title: 'Jexus Manager: Enhanced Self-Signed Certificate Generation'
---
IIS Manager has a shortcut in Server Certificates page to create self-signed certificates, aka "Create Self-Signed Certificate…" menu item under Actions. By clicking this menu item, a wizard pops up.

Once a friendly name is given and a store is chosen (Personal or Web Hosting), IIS will create a self-signed certificate with the following properties,

1. Valid for one year.
1. CN is set to the host name of the machine.
1. SHA1RSA signed.
1. 2048 bits.
<!--more-->

As we know, the above settings are quite limited these days, as SHA1 is obsolete and we often need to set CN to another value. Can there be a better tool?

Jexus Manager is such a clone of IIS Manager, that it also has a Server Certificates page. But its certificate wizard is much more powerful. You see, almost all options you want to tune are present.

Enjoy it.

How to install Jexus Manager? Please refer to [this guide](https://docs.jexusmanager.com/getting-started/install.html).
