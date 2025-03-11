---
layout: post
title: "#SNMP Design: More Objects into Unity Container"
description: "This post is about the changes in CrossRoad to use more of IoC containers."
tags: SNMP
permalink: /snmp-design-more-objects-into-unity-container-aa6fc2425e35
excerpt_separator: <!--more-->
---
I have to confess in the past we don't pay much attention to Browser structure as much as necessary. Though began as a larger demo for the Library, it now turns out to be a useful utility itself after Steve's active development. However, I have to dive in sometimes to clean up my not-so-good legacy and close work items assigned to me. Well, that was very painful before we shipped TwinTower final because then I realized we need to lay a solid ground floor at first.
<!--more-->

Therefore, in order to make CrossRoad a real crossroad, we are going to start as early as possible. The latest changes with Unity is significant in the following aspects,

1. The global resources like Manager instance, profile registry and object registry are now in the container as singleton.
1. The docking panels are now managed by the container, too.
1. Unity helps inject necessary resources into the panels automatically.

I am happy to see they are now loosely coupled, so we can move on easily.

There are still issues. For example, if you close a panel, there is no way to get it back at this moment. We know most of them and hope to fix them one by one in this sprint.

Right now I will move on to our Compiler and integrate Unity with it, too. Stay tuned.

During the composition of this post, I had a nice discussion with Steve on Google Talk. I think both of us agree on a few big tasks for CrossRoad already, so the next post I will let you know more details. But we are always open to suggestions, so please don't hesitate to let us know your ideas.
