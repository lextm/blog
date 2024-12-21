---
layout: post
title: "How I Did xUnit.net 2 Addin for MonoDevelop/Xamarin Studio"
description: "This post is about how I extended xUnit.net 2 addin for MonoDevelop/Xamarin Studio."
tags: Mono .NET
permalink: /how-i-did-xunit-net-2-addin-for-monodevelop-xamarin-studio-c61029051407
excerpt_separator: <!--more-->
---

I started [my very first project](https://github.com/lextudio/codebeautifiercollection) to extend Borland Delphi/C#Builder. And then I created an AStyle addin for SharpDevelop, and then [an OpenCover addin]({% post_url 2012/2012-7-25-opencover-addin-for-sharpdevelop %}). And a few months ago, I launched [an extension for Visual Studio Code for reStructuredText users]({% post_url 2015/2015-11-28-dockpanel-suite-docs-site-restructuredtext-and-visual-studio-code %}). So I think except Eclipse/Visual Studio/IntelliJ IDEA, I have touched most of the IDE platforms. And today I finally enter the land of MonoDevelop/Xamarin Studio.

<!--more-->

MonoDevelop started as a fork of SharpDevelop, and there is already an addin for xUnit.net 1.x. What I wanted to do initially, was to send [a pull request](https://github.com/xunit/xamarinstudio.xunit/pull/10) to the original author, Sergey Khabibullin.

However, the process was not smooth. The rule of thumb for open source projects is to move on, so I move on to publish my improved version as [a new addin](https://github.com/lextm/xamarinstudio.xunit).

If you review the code changes, you can see what I have done,

1. Move completely to MonoDevelop's new addin project model and based on MonoDevelop.Addins NuGet package.
1. Fix the code to check both xUnit.net 1.x and 2.x references for unit testing projects.
1. Provide a developer guide, so that new beginners don't have to fight hard to learn how to contribute.

The most tricky parts are as below.

## MonoDevelop on Ubuntu

I might be wrong, but only when I run the project in MonoDevelop on Linux (Ubuntu), I can easily debug the addin by simply starting the debugger. That one click debugging experience does not work on Windows and OS X. I am not sure whether that's by design, but it really hurts beginners like me, although I do have Windows/OS X/Ubuntu. If a guy only has Windows or OS X and would like to contribute, he/she would be frustrated.

(Updated: It is now possible to run Xamarin Studio 6 on Windows to debug the addin, which is cool.)

## MonoDevelop.Addins Incompatibility

I am not sure why, but for this addin I have to stick with MonoDevelop.Addins 0.2.3. Once upgraded to the latest, the code simply won't compile any more due to .NET compatibility issue (the compiler asks for System.Runtime assembly).

(Updated: I found a way to hack the csproj file to target .NET 4.5 profile and then this error message is gone and I can use latest MonoDevelop.Addins package.)

## xUnit.net Dll Hell

To support multiple platforms, xUnit.net NuGet package "xunit.runner.utility" has far too many assemblies shipped, and they change in different beta and RC builds. And it is not surprising that when a specific version is used, some code in the addin would break. So I have to revise the integration code multiple times.

(Updated: I decided to stick to the net35 version.)

## MonoDevelop Community Repository Issues

Finally I got the addin working locally, and attempted to publish it to the MonoDevelop Community Repository there were further issues.

> Updated (Jan 12, 2023): VS for Mac extension gallery [moved](https://learn.microsoft.com/previous-versions/visualstudio/mac/migrate-extensions?view=vsmac-2019).

Initially I could not easily trigger a build of the addin, as the documentation is sparse. I might be wrong, but later selecting "Publish releases automatically at every change" under Edit Source page seems to solve that.

Then another issue came that the build server told me "xunit.runner.utility" NuGet package requires NuGet 2.8.5 and above, while the build server itself only had NuGet 2.8.3. I used [the Gitter channel](https://gitter.im/mono/monodevelop) to inform the MonoDevelop guys, but again the process is slow. Thus, I simply downgraded that NuGet package to a previous beta build, which only requires NuGet 2.8.3, and after that the build server was happy to serve me.

Now the addin is there and waiting for approval. Hope that wouldn't take too long.

## Overall Experience

I think the current local debugging experience on Linux and using a build server to process the addin repository are cool ideas, but if I can simply zip up the bits and publish a package for a group of testers without going through the approval process would make a quicker feedback loop.

With the merge of Xamarin and Microsoft, Xamarin Studio/MonoDevelop would be a more important product in the portfolio, and really hope there would soon be some improvements and documentation efforts to make the authoring and publishing experience quicker and smoother.

(Updated: Now the addin is approved and available for MonoDevelop and Xamarin Studio 5.x. However, the infrastructure changes in MonoDevelop and Xamarin Studio 6 requires lots of changes and [I am now working on that front](https://github.com/lextm/xamarinstudio.xunit/issues/1).

Join me if you want to help out.)

Stay tuned.
