---
layout: post
title: "Jexus Manager: Release Candidate Phase"
description: "This post is about the recent changes of Jexus Manager."
tags: Jexus-Manager IIS
permalink: /jexus-manager-release-candidate-phase-46206e4a0b9a
excerpt_separator: <!--more-->
---
It is not easy to develop a product such as Jexus Manager, as it contains a large amount of code and targets too many pieces of IIS/IIS Express.
<!--more-->

## Rollbar and Crash Reports

I used to receive some feedbacks from CodePlex and GitHub, so that I might know something was broken. So overall the bug reports were just a few, and should I assume that everything was OK? I often wondered that how many issues I had missed, but until recently I hooked to Rollbar service I started to really see the facts from another angle.

So what is [Rollbar](https://rollbar.com/)? Like Azure Application Insights, it is a service that collects app crashes and user sessions, so that later as the vendor you can analyze the data collected to gain better understanding of the quality of your products.

Their official client library for .NET is unfortunately suffering multiple issues,

* The NuGet package contains an unsigned assembly, which is unacceptable if your project requires a signed version. I have to compile my own signed version in the end.
* They only target .NET Framework at this moment, while the code base should definitely work for a version of .NET Standard. I am not sure if anyone ported it to .NET Standard already, but this should be the primary task of Rollbar if they do plan to serve .NET developers well.

Anyway, once you fight the fight to put the client in place, it would be rather easy to post crashes to the server side, and later crash information can be displayed in a nice dashboard.

So the story goes, and soon I woke up in the morning and saw these many of reports.

Got it? There are far too many unhandled exceptions occurred on different users' machines, due to different environments, different IIS configuration, different sites, and of course some of my mistakes. I suddenly realized that most users were "silent", and they simply tried the tool and dropped it when it did not work out.

## Auto Update

Many of the issues can be easily fixed, but then the challenge becomes how to quickly push new versions to users. Luckily I recently enhance Jexus Manager to automatically detect new versions based on GitHub API. So if you click Help | Check Update, Jexus Manager will tell if you are using the latest build. In a recent build, I even let Jexus Manager to automatically check update at startup, so as to ensure end users are more likely to use the latest build.

## More Features

While busy fixing the remaining issues, I also went ahead to add more features. For example, Jexus Manager HTTP API page is enhanced, so that now you can add/remove reserved URLs.

ASP.NET Core support is also being tested and enhanced.

This tool would be better if you do send more feedbacks (either via GitHub issues, or silently via crash reports). So thank you in advance.
