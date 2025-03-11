---
layout: post
title: "DockPanel Suite: Review on Release 2.7"
description: "This post is about DockPanel Suite 2.7 release."
tags: DockPanel-Suite
permalink: /dockpanel-suite-review-on-release-2-7-42bb0be582ae
excerpt_separator: <!--more-->
---
After three months of further hacking and effective collaboration with some of the contributors, Ryan and I are proud to announce the 2.7 release of DockPanel Suite.
<!--more-->

More information (such as release notes) can be found on the homepage at http://dockpanelsuite.com, and the following are the highlighted items,

1. Better Mono support. A major stackoverflow issue has been remedied. We provide Mono guys a bug report.
1. Better .NET Framework Client Profile support. Removed dependency on System.Design.
1. Better middle mouse click support. Middle clicking now works in more places.
1. Less rendering issues. Missing docking indicator issue should occur less frequently. Deep nested control rendering can be disabled to improve performance.

As usual, you can grab the binaries from

NuGet, http://nuget.org/packages/DockPanelSuite
GitHub, https://github.com/downloads/dockpanelsuite/dockpanelsuite/DockPanel_2_7_0.zip
The source code is also available on GitHub.