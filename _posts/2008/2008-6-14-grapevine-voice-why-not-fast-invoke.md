---
layout: post
title: "GrapeVine Voice: Why Not Fast Invoke?"
description: "This post talks about why FastInvoke is not used in GrapeVine."
tags: Code-Beautifier-Collection Delphi
permalink: /grapevine-voice-why-not-fast-invoke-e0af02d2d68a
excerpt_separator: <!--more-->
---
(Originally posted to CSDN on Feb 21, 2006)
<!--more-->

You may find the following words in Readme.pdf, and wonder why some piece is missing,

> GrapeVine will bring in the following changes:
> * **FastInvoke method will be used to load pluses, which has been revealed to be much faster.**
> * Generics methods will be added to reduce duplicate code.
> * Many .NET 2.0 BCL new classes will be used such as Stopwatch and WebBrowser to replace a few custom classes.
> * BDS OTA version 5 support will be added in order to load with BDS 2007/Highlander (BDS 5.0).

Now I think it is time to talk about the missing piece, FastInvoke.

Back in 2006, when I saw this CodeProject article, I decided to play with it. However, at that moment, HardQuery was still developed on .NET 1.1, so there was no way to do FastInvoke there.

Now, when GrapeVine goes .NET 2.0, a lot of changes have been introduced. And the most important one that prevents FastInvoke is a change in feature instance loading process.

The PropertyRegistry introduced in "2006–10–17 HardQuery Release 2 Milestone 5" did not only bring me a lot of fun, but also removed the restriction that every feature instance must be Singleton. This simplified that loading process, but from then on, features have been loaded with reflection by calling the constructors directly.

If you read the FastInvoke article carefully, you will notice this optimisation is for MethodInfo instances only. However, ConstructorInfo is not MethodInfo.

After all, I have fulfilled all other things listed for GrapeVine.
