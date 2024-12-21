---
layout: post
title: "GrapeVine Voice: Something needed to be done"
description: 本文描述了 CBC GrapeVine 的一些情况
tags: Code-Beautifier-Collection Delphi
permalink: /grapevine-report-something-needed-to-be-done-19fe776c41b
excerpt_separator: <!--more-->
---
(CSDN Sept 25, 2006)

Something about GrapeVine is already considered by me. If you have read the readme file included in HardQuery Final, the section named Change Log lists all words I made during this long development process. GrapeVine is already there.

Now I am not sure about the final version number for GrapeVine. Next version number of BDS should be 5.0, so if CBC GrapeVine final is 6.0.*.* some body will get confused. Maybe I will use 5.6 then. However, I will surely make great changes in the architecture again, so 5.6 seems not to be a great leap in number.

I starts to remove some Singletons inside of LeXDK. They are not needed in fact. After reading Refactoring to Patterns, I decide not to be a "Patterns Happy" any more. Patterns are useful only if they are suitable.

The changes I made now will be merged into HardQuery Update 1. I cannot make GrapeVine ready until there is a new IDE on .NET 2.0 to test it.

Stay tuned.
<!--more-->