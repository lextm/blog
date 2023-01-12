---
layout: post
title: "Touch Mouse Mate: Hardware Review and Touch-over-click Mase"
description: "This post is about the background information about Touch Mouse."
tags: Windows
permalink: /touch-mouse-mate-hardware-review-and-touch-over-click-mase-32f39db01a4c
excerpt_separator: <!--more-->
---

There are already tons of articles on the Internet talking about Microsoft Touch Mouse, its hardware specification, SDK, and so on. Then in this article I won't try to say something old, but reveal a few tips that I discovered.

<!--more-->

## Hardware: Touch Mouse vs. Magic Mouse

I do own a few Apple products, like iPod Video and iPad 2, but I don't have a Magic Mouse and a Mac. Therefore, all my previous understanding of Magic Mouse was based on its advertisement, till my current employer Morgan Stanley started to have developers using Mac. I played with the Magic Mouse for a few minutes, and then observed how one of my colleagues uses it for coding and navigation.

If you compare the two mouse models (Touch Mouse and Magic Mouse), you will find that they are almost the same in the following aspects,

- They do both have physical clicks. In this aspect, they are not different from normal mouse models.
- They have a touchable surface where your finger slides can be understood by the mouse driver and translated to gestures. That makes them special.

Obviously Apple does a better job, by integrating its OS and apps with its Magic Mouse, where you can enjoy a lot of gestures here and there (in OS X, or XCode, or any other apps that Magic Mouse aware). But for Microsoft, its OS and apps do not have that level of tight integration with Touch Mouse, and without middle-click support, it can make life even tougher (does Magic Mouse support middle click or OS X does not have middle click?).

## Touch-over-click

Before seeing and learning Magic Mouse, I though that I can use a few touch gestures instead of physically clicking. I felt the same before Touch Mouse arrived on my desk. But I was wrong, as by default, both Magic Mouse and Touch Mouse require its users to press the physical keys to perform clicks. The gestures on the surface are independent of clicks. Then why it ends up like this?

To answer this question, let's try to explore what is touch-over-click. J5 created this feature in his Touch Mouse Enhancer and [I tried to improve it by utilizing the new engine]({% post_url 2012/2012-3-6-touch-mouse-mate-1-5-milestone-2-one-step-further %}). However, it seems to be a dead end as I could hardly find a good way to distinguish a click, and a slide easily under the time constraints. For a click, a key down simulation must be generated as early as possible, so that TMM responds to drag and drop without sensible delay (we do have a small delay, which occurs between the state transition from "Left down pending" to "left down" and other similar cases). But within this short delay, the touch zone center of mass movements for clicks and slides are not distinguishably small. I tried several pairs of parameters (delay and movement), but none of them minimizes false triggers to an acceptable rate.

Therefore, in 1.5 Beta touch-over-click is disabled. And for me, it also answers why Apple and Microsoft engineers do not consider touch-over-click a "feature". I guess they have explored in this field already, and finally found out that physically clicks may be a better solution.

## The Maze

Now should we remove touch-over-click completely? I am puzzled. I don't personally use touch-over-click any more, but I guess there are still users who like this. So it will be kept in the coming releases, till we find out a better solution or implement other similar features.
