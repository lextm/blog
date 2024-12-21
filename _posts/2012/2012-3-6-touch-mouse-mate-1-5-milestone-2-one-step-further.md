---
layout: post
title: "Touch Mouse Mate: 1.5 Milestone 2, One Step Further"
description: "This post is about the second milestone of Touch Mouse Mate 1.5."
tags: Windows
permalink: /touch-mouse-mate-1-5-milestone-2-one-step-further-aca10ce76be9
excerpt_separator: <!--more-->
---
Hi guys,

Today you can download TMM installers from its homepage finally. That's the most important news except that we hit the second milestone of 1.5 release.
<!--more-->

## Milestone 1

Revision fe36f62585 was our first milestone in 1.5 phase, https://github.com/lextm/touchmousemate/commit/fe36f62585758196956b1cbd43bf194b435c3884.

This build accomplished our brand new engine that handles touch down/up events separately, and it resolved most of the known issues of 1.4 release.

However, an obvious result is that this new engine leads to conflicts with Microsoft's gesture engine. For end users, they will find scroll/pan, two fingers and three fingers stop working as desired.

In the following revisions, I was trying to introduce movement detection to this new engine, and hope that can resolve the conflicts. However, it is really difficult to determine whether a finger is clicked at the same spot or it has moved. Within 50 time units (minClickTimeout), the observed total movement does not have an easy-to-tell relationship with simple clicks or scrolls. I tried to choose a threshold for total movement (moveThreshold), but no matter which value is chosen, TMM either wrongly recognizes simple clicks when I want to scroll, or vice versa.

## Milestone 2

Revision 636a81a82 is our second milestone in 1.5 phase, https://github.com/lextm/touchmousemate/commit/636a81a8255591042abbd90bc84f79648ce7d6e5

Today I also tried to change left/right click zones (by shrinking them to top-half of the surface). The latest zone area definition is like below,

![img-description](/images/touch-mouse-zones.png)
_Figure 1: Touch Zones._

In this way when I land your palm on the bottom-half surface, it won't trigger TMM incorrectly. But suddenly a nice fact is there! Now movement detection is no longer necessary, right?

* In the top-half surface, we can continue using the new engine in milestone 1, which properly handles left/right touches and translates them correctly to mouse down/up events.
* In the bottom-half surface, the new engine won't do anything, and we can enjoy what Microsoft's gesture engine offers.

Well, it is still not perfect, but up-to-now it is the best solution I come across.

While I am going to further investigate movement detection in the top-half, my dear users can start to enjoy a stable build.

Stay tuned.
