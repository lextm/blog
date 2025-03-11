---
layout: post
title: "HoneyCell Drops: Why We Need PortInUseException Now"
description: This post is about the new PortInUseException.
tags: SNMP
permalink: /honeycell-drops-why-we-need-portinuseexception-now-88fb45fb7962
excerpt_separator: <!--more-->
---
> It is not easy to review the code base as I don't have much time recently and the weather in Shanghai is too hot.

Yesterday I checked in new changes, where a new exception named PortInUseException is introduced. Why it is added now?
<!--more-->

The story started with an error in snmpd.exe (also in Browser.exe) when we try to start the listener but the desired binding (0.0.0.0:161) is already taken by another application, such as Windows SNMP agent.

Even if #SNMP 5.2, you will see a simple message box popped up and saying the port is already in use. However, the UI is not in correct state, as it seems the listener is working correctly. This is because Listener.Start method does not throw an exception. Instead, the exception comes from an event. I was expecting such a design can unify exception handling experience as you can subscribe to one event and handle all possible exception raised from this class. I was wrong, because even snmpd.exe cannot query the correct state from Listener and change its UI correctly.

The new exception resolves such an issue, as it makes Listener.Start possible to report a binding failure. But we have to stop all started bindings in any binding fails, as it is the easiest way to keep state management simple (so called "all or nothing"). Only after that snmpd.exe can track Listener.Active correctly and provide correct UI state.

If you are using Listener like we do in snmpd.exe, please review our latest changes in the repository and hope you find it useful.

Stay tuned.
