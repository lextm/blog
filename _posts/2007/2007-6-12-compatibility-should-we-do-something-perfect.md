---
layout: post
title: "Compatibility: Should We Do Something Perfect?"
description: "This post describes the compatibility problem and how to resolve it."
tags: Code-Beautifier-Collection
permalink: /compatibility-should-we-do-something-perfect-ac9f9965582b
excerpt_separator: <!--more-->
---

During the evolution of Code Beautifier Collection, the settings file format has been changed for several times as well as the Plus registration file format.

I never thought about the compatibility problems that might occur because the risk is not too big. If the settings file format is changed, the users only need to set the parameters again. The core library will never try to load from the old format any more or save to old format. For simplicity, every time a change takes place, the file extension is changed accordingly.

However, for software interface such as OTA, or protocol such as TCP, any changes can impact on a lot of related software. The price of incompatibility will be too high.

We should keep the compatibility in our mind whenever a new version of protocol, file format, or interface is maintained or created. If it is impossible, at least a migration path should be provided. For example, I wrote a plus2plus2 utility to convert .plus file format to .plus2 when I dropped .plus format and turned to .plus2 format(If you are interested, it can be found in the source code package).

My project at work consumes a file format from a third party provider. However, the provider's latest changes bring up incompatibility issues that we have to adapt to. The changes are unreasonable in certain aspects. I believe a discussion will be set soon. Wish the provider changes its mind at last. If it does not surrender, I would have a lot of work to do.
<!--more-->