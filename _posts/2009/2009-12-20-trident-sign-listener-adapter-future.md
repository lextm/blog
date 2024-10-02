---
layout: post
title: "Trident Sign: Listener Adapter Future"
description: "This post is about the future of Listener Adapter"
tags: SNMP
permalink: /trident-sign-listener-adapter-future-e61bee9d07c1
excerpt_separator: <!--more-->
---
In the past, I have a lot of plans for the agent. Listener component is one of the most important pieces. So I must pay special attention to it.

The very first revision exposes all events on Listener. It was the easiest way to test out the component. We can subscribe to different events in order to know what happens. I was satisfied with that revision.
<!--more-->

Soon a new requirement comes that we need to make it easy to develop an SNMP v1 aware agent. It was then I think why not create version specific Listener component? After a while I wrote the adapters and it made me happy to start my research on SNMP agent. That's our second revision on Listener.

Well, time goes by so fast. Once I used the pipeline model to code the agent design, I saw the limitation of both our first and second revision. We must have a unified way to handle all incoming SNMP messages just like IIS does to HTTP messages, then it is useless to expose so many events or create so many adapters. Therefore, our current implementation makes agent side listener adapters obsolete.

But if we look back, we will see that manager side adapters are still necessary. As a result, we will keep them.

OK, that's all for this post. Later I will post about our SNMP pipeline. Stay tuned.
