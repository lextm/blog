---
layout: post
title: "BigDipper Light: Planned Release Details"
description: "This post is about the planned release details of #SNMP 7."
tags: SNMP
permalink: /bigdipper-light-planned-release-details-f5ad3c9e5f8b
excerpt_separator: <!--more-->
---
HoneyCell 6.0 is our last release that has some binaries targeting .NET 2.0 SP2. This is because .NET 2.0 SP2 support is not yet expired. As BigDipper is to be released in next May, all 7.0 binaries will be targeting .NET 3.5 SP1 (.NET 2.0 SP2 support expires next April).

Therefore, today I started to clean up .NET 2.0 stuffs in our master/default branch. Well, it is amazing! All duplicate code that live for a long time is removed completely, and new extension methods are created.

Have to confess that there are lots of changes today already, and luckily we have enough test cases to ensure that the changes do not break anything critical.

Stay tuned.
<!--more-->