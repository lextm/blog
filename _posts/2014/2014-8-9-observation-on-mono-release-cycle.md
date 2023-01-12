---
layout: post
title: "Observation on Mono Release Cycle"
description: "This post is about the recent release cycles of Mono."
tags: Mono
permalink: /observation-on-mono-release-cycle-ad4ef995cd19
excerpt_separator: <!--more-->
---
In recently months (I personally think starting from the Xamarin phase), it has been a misery to know which Mono release is stable. This project goes a little in the way of Android, that

* *table releases are announced with no blog posts on Monologue or Xamarin blog (I don't know where they announced those releases).
* Downloads from http://mono-project.com can be broken or missing (OS X releases should be acceptable, while Windows releases sometimes broken, and openSUSE releases only target 11.4, and all other platforms are gone).
* Branches on GitHub are bit of messy.
<!--more-->

Miguel has kindly replied on the dev mailing list about the current status, and it matches all previous statements in this area that new releases are indeed tested.

> ``` text
> Message: 4
> Date: Tue, 29 Jul 2014 17:59:01 -0400
> From: Miguel de Icaza <miguel@xamarin.com>
> To: Bob Summerwill <bob@summerwill.net>
> Cc: Mono Development <mono-devel-list@lists.ximian.com>
> Subject: Re: [Mono-dev] Mono 3.6 release?
> Message-ID:
> <CANqeOFohatfSzZ6bWr_9u_FSsC0–0Qe6KRDi-fDJhuwZKn-Ebw@mail.gmail.com>
> Content-Type: text/plain; charset="utf-8"
> Yes, we do make a branch, and then we put it through QA.
> The we fix all the bugs that QA finds, and when we are ready we release.
> What is important is to not regress, so things will take as long as > they
> need to, because we are not going to ship a version that breaks someone's
> system, just because someone is in a rush.
> If you are in a rush, use a git checkout.
> Miguel
> ```

So now if you do want to play with Mono (most often in Linux case) you should utilize Git to clone the repository, and then check out the stable branches. Tags are not reliable, as after tagging a stable release I do observe changes coming to that branch still. My personal rule of thumb is that

1. Go to GitHub and land on the branches page with a simple query, https://github.com/mono/mono/branches/all?query=3.
1. See which branch was not updated for months (at least 1 month), and then that branch might be stable enough to try out.

So up-to-now, I can see Mono 3.2.8 is pretty stable (updated 6 months ago), while Mono 3.4.0 is kind of stable (updated 1 month ago, latest changes were in June), and Mono 3.6.0 and 3.8.0 are quite unstable. Yes, Mono 3.6.0 was also updated a month ago (most changes were made in July), but I don't think the Mono guys will create two stable branches (3.4.0 and 3.6.0) the same time, and there should be new change sets going to 3.6.0.

Note that Xamarin Studio on Mac OS X is now showing Mono 3.6.0 in stable channel. That's both weird and understandable for me. As an open source project, release often is a key to deliver new features (check out Xamarin Studio's recent cool stuffs) to developers. But if you are going to deploy production web sites on Linux machines, I bet Mono 3.2.8 or 3.4.0 are better options.

Like the dev mailing list reveals, the release cycle of Mono is not quite convenient at this period of time (so are the Mono based products, Unity, Xamarin.iOS/Android and so on). Hope we see some improvements in the next few months.
