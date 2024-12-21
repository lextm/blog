---
layout: post
title: "Launch Firefox in C#"
description: This post talks about how to launch Firefox in C#.
tags: .NET
permalink: /launch-firefox-in-c-b74d7264d2a4
excerpt_separator: <!--more-->
---

I talked about this topic in [this post]({% post_url 2008/2008-2-5-grapevine-voice-firefox-s-flaw-or-windows %}), but today's content is brand new. Yes, finally I find out how to launch Firefox without an exception. Then HOW?

The old code to launch Firefox was,

``` csharp
Process.Start("https://docs.lextudio.com/blog");
```

And the new code is,

``` csharp
Help.ShowHelp(null, "https://docs.lextudio.com/blog");
```

I don't understand why Microsoft implements them differently and I don't want to waste my time to dig .NET Framework source code under that MS-RL. Maybe the guys want to promote Internet Explorer, isn't it?

<!--more-->
