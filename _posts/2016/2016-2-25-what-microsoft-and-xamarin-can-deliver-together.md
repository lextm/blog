---
layout: post
title: "What Microsoft and Xamarin Can Deliver Together"
description: "This post is about what new technologies Microsoft and Xamarin can deliver together."
tags: .NET Mono
permalink: /what-microsoft-and-xamarin-can-deliver-together-221f668884a7
excerpt_separator: <!--more-->
---
I am more than happy to see Microsoft acquired Xamarin a few hours ago, as I have been observed both for a very long time and currently working on a presentation on March 12 to talk about the history behind .NET and Mono in the past 16 years. This merge gives the talk more fun.

However, both companies have been focusing more on the promising future, and kindly avoided further information on what would be their next move. Of course, consider the facts that Microsoft BUILD and Xamarin Evolve conferences are coming pretty soon, then the guys probably want to keep the surprises for a few more weeks.

If we are brave enough to make a few guesses, hope that imagination can take us to the far far away land :) Below are the things I personally would like to see in the next few months.
<!--more-->

## Xamarin.Forms for Desktop, Blend for Xamarin.Forms, and WPF for Cross Platform

Microsoft has been quiet on WPF and Blend till Visual Studio 2015 ships. The new WPF goodies in Visual Studio 2015 look promising but do not bring much fundamental changes. If that means the team have been cooking WPF for cross platform, then I would be pleased.

On the other hand, at this moment writing Xamarin.Forms applications is painful in one spot. Without a designer as convenient as the Blend, developers cannot take full advantages of the XAML magics.

Of course, if Xamarin.Forms can be extended to support OS X, Linux, and Windows desktops, it would be much cooler to learn it.

## .NET Native + Mono AOT

So far Mono and Xamarin platforms still use Mono AOT tool chain. It works, but does not deliver the best performance compared to .NET Native powered by Microsoft's years of experience on application performance tuning. If .NET Native can penetrate into those platforms, then apps built on Xamarin platforms should see a significant boost.

## Visual Studio for OS X/Linux

JetBrains revealed its cross platform IntelliJ IDEA based C# IDE "Project Rider" a few weeks ago. If Microsoft wants to compete, its current option should only be Visual Studio Code, a promising platform, but young and simple.

Though MonoDevelop/Xamarin Studio is not as powerful and feature rich as Visual Studio on Windows, it already provides core feature set with an extension framework that works good. Many VS functionalities should be able to arrive on Xamarin Studio to support daily tasks that majority of developers need.

## The Unification of .NET Framework, Mono, and .NET Core

It is clear now that .NET Core is the future design. But .NET Framework must remain for legacy applications.

Mono should gradually merge with .NET Core, by removing its core modules and replacing with .NET Core bits. Application frameworks such as GTK# are still valuable to the ecosystem to enable native integration with all platforms.

## Cross Platform Visual Basic and Java

Visual Basic has been a missing piece on Mono/Xamarin platforms. Now Microsoft can fill the gap again by bringing VB developers to the new platforms.

Xamarin bought RoboVM last year, and now holds a product line with the Java programming language. Thus, after the attempt of J++/J#, Microsoft again has a chance to hit Java market.

## Final Thoughts

When Miguel de Icaza and the other Xamarin visionaries join Microsoft, I think that a lot of things they could not do initially at Xamarin due to the limited resources can be fulfilled under proper management.

Novell ruined Ximian and its assets a few years ago and almost destroyed MonoTouch when it laid off all Mono developers. I think that should teach Microsoft enough on how it should appropriately handle the merge this time. By giving enough resources and freedom to the teams (both Visual Studio and Xamarin), and by uniting the engineers and the developer community, this time Microsoft can play a handful of good cards on the cross platform development market and drive the innovation much further.

Stay tuned.