---
layout: post
title: "Trident Sign: Listener Adapters"
description: "This post is about listener adapters implementation."
tags: SNMP
permalink: /trident-sign-listener-adapters-5ae14aef23c5
excerpt_separator: <!--more-->
---
It is a really interesting question why Gendarme think Listener.HandleMessage is a large function. But now I have the answer and today I finally refactored on this function, and designed a few new classes.
<!--more-->

## Listener Adapters
For an SNMP v1 manager, actually only TRAP v1 message is useful. So why it needs to be bothered by other versions of messages? Now you can use a simple listener adapter for v1 manager and hook it to the Listener object.

Yes, it sounds like filters for incoming messages. That's it.

I have also created a default adapter for backward compatibility, too. You can check how to use it in the samples.

## Breaking Change Notice

Now all events for Listener component are obsolete except that one for exceptions. So you must follow the samples to update your code as so to adapt the changes.

Stay tuned.
