---
layout: post
title: "#SNMP Design: Why Unity Appears in Browser and Related Changes"
description: "This post is about why the IoC framework Unity appears in Browser and related changes."
tags: SNMP
permalink: /snmp-design-why-unity-appears-in-browser-and-related-changes-6b9a4422bbc1
excerpt_separator: <!--more-->
---
You may doubt why I introduced Unity Application Block in latest builds. Well, the reason is simple, "we need it".
<!--more-->

Although IoC or DI has been a hot topic for some time, I solely understand the concepts and the basics, but never have a chance to practise with a real IoC container. So now it is good to know Unity and its power. Bet you know that it is bad to place global variables but using a IoC container, it is easy to access variables stored in this global container.

Aha, this is only the very basic usage of IoC container. Surely I will investigate concepts like AOP in the future when I need them badly. At this moment, I just make use of its XML syntax to inject objects into bigger ones in App.Config. In this way I can easily find out where to start a new refactoring.

One piece of the exciting news is that we finally get rid of Inventory class as we find a way to combine its functions with ObjectRegistry seamlessly. The direct result is that you can create a new ObjectRegistry other than ObjectRegistry.Default easier than ever. Simply pass a `folder` string to the constructor, this new instance will automatically load all MIB documents in that folder.

Finally we can get rid of embedded MIB documents and start to load whatever we want. Now the final problem is how to remove modules from the list. That will happen soon after we enhance the Compiler. Stay tuned.

You may ask why Unity. I know that I must be biased now because of my current job. :) But I really want to say that Unity is well documented and easy to use. I did try other containers in the past but when they failed me I could hardly hang myself there. Don't worry Unity will affect our open source spirit, as it is also fully "open source" under MS-PL as that license is approved by OSI.
