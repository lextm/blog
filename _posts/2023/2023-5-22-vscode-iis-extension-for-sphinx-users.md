---
layout: post
title: "VS Code IIS Extension for Sphinx Users"
description: "A post about how to use VS Code IIS extension to host Sphinx sites."
tags: Visual-Studio-Code Python Windows IIS
excerpt_separator: <!--more-->
---

If you use VS Code to author Sphinx sites, you might find the reStructuredText extension a good companion to help highlight the syntax and preview the pages. One limitation of that extension is it cannot help you host the site locally, so you need to set up a web server separately. This post introduces a new VS Code extension that can help you host Sphinx sites on IIS easily.
<!--more-->

## Install the Extension

If you are using [the Extension Pack](https://marketplace.visualstudio.com/items?itemName=lextudio.restructuredtext-pack), then the IIS extension has been added in 1.0.2+. Otherwise, you can install it separately from [the marketplace](https://marketplace.visualstudio.com/items?itemName=lextudio.iis).

## Use the Extension

Now let's open a Sphinx site folder in VS Code, and you can see in the status bar that a default IIS Express configuration file in `.iis` folder is selected.

![IIS Extension installed](/images/vscode-iis-step1.png)

Since the default config file was generated to contain a test site pointing to the root folder, you can now open `applicationhost.config` in `.iis` and change the site folder to the actual Sphinx output folder (e.g. `_build\html` in this case).

![Change folder path](/images/vscode-iis-step2.png)

Now you can click the ▷ button in the status bar to start IIS Express via Jexus Manager and host the site.

## Side Notes
As a development server, IIS Express allows you to configure domain names, certificates and other settings to test your Sphinx site before deploying to a production environment. And as its management console, Jexus Manager exposes all necessary settings for you to configure your IIS Express sites.

## References

* [VS Code IIS Extension](https://docs.jexusmanager.com/getting-started/vscode.html)
* [Jexus Manager](https://docs.jexusmanager.com)
* [IIS Express](https://learn.microsoft.com/iis/extensions/introduction-to-iis-express/iis-express-overview)
