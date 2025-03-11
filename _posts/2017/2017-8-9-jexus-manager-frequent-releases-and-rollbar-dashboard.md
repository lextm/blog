---
layout: post
title: "Jexus Manager: Frequent Releases and Rollbar Dashboard"
description: "This post is about how I use Rollbar to track Jexus Manager issues."
tags: Jexus-Manager IIS
permalink: /jexus-manager-frequent-releases-and-rollbar-dashboard-79afefd6f4ea
excerpt_separator: <!--more-->
---
It is really astonishing that I released 29 builds of Jexus Manager in 24 days. Tons of bugs have been fixed and some new features have shipped.

For the very first time of the project lifecycle I gain deeper understanding of how this tool is being used by others and how each issues originated. Even some hard-to-catch bugs became obvious with clear call stacks for me to analyze.

Of course, some NullReferenceException issues were difficult to track down, which required me to add more assertions around to collect more information. The frequent release approach makes sure that such assertions land on user desktop just in a couple of hours or days, so I can quickly learn more about the crashes and locate the exact culprit.

So next time if I create a new project, I would definitely enable Rollbar on day one.
<!--more-->
