---
layout: post
title: "Rhino Mocks vs. NMock"
description: This post compares Rhino Mocks and NMock.
tags: .NET
permalink: /rhino-mocks-vs-nmock-cea2fb93f6e7
excerpt_separator: <!--more-->
---
According to so many posts I read, Rhino Mocks is another hot mock framework for .NET. So beside NMock, today I gave Rhino a try too and got some interesting result.
<!--more-->

In NMock I could create an IOTAProject mock object. However, Rhino failed to mock such an object for me, and because I was using SharpDevelop, I could not debugging inside Rhino Mocks to see what was the problem.

What's interesting there? If you take a look at this page, you can see that my case is not similar to any cases listed there,

* IOTAProject is surely not a sealed class.
* it does not look like a private interface.
* I am not intercept calls.

Therefore, I wonder what happens.

(Updated: Isn't it another limitation of Rhino Mocks on partial mock support?

I have tried MockRepository.PartialMock but it refuses to create a mock for IOTAProject as it is an interface. Thus, am I forced to mock all members of this interface?

Maybe I can draw a sad conclusion that if you want to partially mock an interface in order to save time, Rhino Mocks is surely not a smart choice even if it provides other advantages.)
