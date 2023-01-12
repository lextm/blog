---
layout: post
title: "Jexus Manager: Recent Changes"
description: "This post would show you the most important changes in Jexus Manager."
tags: Jexus-Manager IIS
permalink: /jexus-manager-recent-changes-to-save-the-world-ada896d098aa
excerpt_separator: <!--more-->
---

You probably noticed that I have been back to work on Jexus Manager due to the adventure on Docker/ASP.NET Core. So finally I can spend some time on the things I planned a while ago. Thus, this post would show you the most important changes.

<!--more-->

## Better Self Signed Certificates

Well, I covered this in [a earlier post]({% post_url 2017/2017-6-14-why-chrome-says-iis-express-https-is-not-secure-and-how-to-resolve-that %}), so in short Jexus Manager is now capable of generating certificates with proper SAN extensions. And as always, it is never easier to configure HTTPS sites in this tool visually. Every detail is at your fingers.

## Goodbye to "Unable to launch the IIS Express Web server"

[I blogged about]({% post_url 2015/2015-11-5-jexus-manager-secrets-behind-visual-studio-iis-express-integration %}) how horrible things can happen if your IIS Express configuration is out of sync with the web project file.

At that time sorry that you still have to manually open those files in a text editor and struggle to find a fix.

Though still a work in progress, now I am offering a better approach, aka "Project Diagnostics".

So if you meet the classic error of a site, you can

1. Close Visual Studio
1. Open Jexus Manager
1. Add the solution file as a new IIS Express server. (in VS2015 and above), or work on the default IIS Express server node.
1. Navigate to the site under this server.
1. Locate "Visual Studio Project Diagnostics" under Actions panel.

This simple menu item would trigger the diagnostics helper, who uses the site bindings to update your VS web project file, and make it working again.

It would generate a report on the project file analysis, and then you can apply the corresponding steps to resolve the issue.

Let me know if it works for you. Any issue can be reported at GitHub.

Stay tuned.
