---
layout: post
title: "DockPanel Suite: Some Update for 2016"
description: "This post is about some update for DockPanel Suite in 2016."
tags: DockPanel-Suite
permalink: /dockpanel-suite-some-update-for-2016-f04dd830106d
excerpt_separator: <!--more-->
---
It is August, and my last post on DockPanel Suite was in December. So I have to admit that too little has happened there, but if you do monitor this project, you should notice significant changes.
<!--more-->

## New Releases (2.10 RTM/2.11 Alpha)

On July 6 2016 we finally shipped [2.10 release](https://www.nuget.org/packages/DockPanelSuite/).

We expected to ship it as 3.0 release a few years ago, but later shifted to a 2.x release. Thus, although it ships far too many features, most of which are already well known.

Below is a list that highlights the most important ones,

1. Themes are now shipped as separated libraries and NuGet packages.
1. Visual Studio 2012 Light theme is added.
1. Visual Studio 2013 Blue theme is added.

We also resolved a few outstanding issues (memory, flickers for example). As a result, it is highly recommended that all users switch to this stable release.

Starting from July, two Alpha builds of 2.11 release have been published. They feature a new mechanism called "patch controller". We are now shipping a selection of unstable patches (enabled by default), and also providing users a few switches to disable them if needed. This allows more testing to be performed on those patches for us to collect feedback. If you like to stay on the bleeding edge, try them out and send us issue reports [at GitHub](https://github.com/dockpanelsuite/dockpanelsuite/issues).

## Documentation

[One new article](http://docs.dockpanelsuite.com/themes/basics.html) has been added recently to reveal the basic building blocks of themes.

I also tried to write more XML comments occasionally.

You are welcome to contribute to our documentation site, as it is also open source [at GitHub](https://github.com/dockpanelsuite/dockpanelsuite_docs).

Stay tuned.
