---
layout: post
title: "CatPaw Rumors: Now We Have Bindings And More"
description: "This post is about the new features in CatPaw SNMP Agent"
tags: SNMP
permalink: /catpaw-rumors-now-we-have-bindings-and-more-b54b4026575f
excerpt_separator: <!--more-->
---
#SNMP Agent starts to look good after I decide to follow IIS and ASP.NET patterns. Yes, the pipeline pattern makes it so easy to do authentication, handler mappings, and so on. Our release 4.0 is a nice indication that we are on the right track, and the upcoming release 5.0 is evolving fast. A few days ago, I announce that we implemented most SNMP v3 support in snmpd. Today, we go ahead and borrow one more idea from IIS. That is, the bindings.
<!--more-->

For IIS HTTP web sites, we can configure bindings easily. So a site can monitor both (http) `127.0.0.1:80`, (http) `[::1]:80`, and (https) `*:443`. That's a very convenient way to say how many incoming requests I care of. But what about our current SnmpDemon in release 4.0? Well, it must be terrible. Even in our Browser, we had to use two Listener instances to monitor incoming requests in all unassigned scenario.

Like I explained before, this is sort of a System.Net limitation. So now, how to make life easier? We can hide all details by encapsulating multiple Listener objects in a single class,

1. Rename Listener to ListenerBinding.
1. Add a new class named Listener.
1. Start to tune Listener and ListenerBinding implementation according to how Listener is used in the whole code base.

Still ListenerBinding class is the one who performs the heavy tasks, while Listener class hides all details from consumers. You only need to make use of ClearBindings, AddBinding, Start and Stop to enjoy the ease.

There are nice additions checked into our repository recently, and why not take a look yourself? Once I finish the implementation of SecureAgentProfile, a 5.0 beta will be available.

Stay tuned.
