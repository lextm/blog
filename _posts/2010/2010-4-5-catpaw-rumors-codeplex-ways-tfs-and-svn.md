---
layout: post
title: "CatPaw Rumors: CodePlex Ways, TFS and SVN"
description: "This post is about my experience on CodePlex and TFS/SVN"
tags: SNMP
permalink: /catpaw-rumors-codeplex-ways-tfs-and-svn-1b9aa6a4ab98
excerpt_separator: <!--more-->
---
I hate the A vs. B discussion, so I promise this post is not one of that kind.
<!--more-->

I think CodePlex is a nice place to host open source projects, whether yours targets Windows. Yes, I know CodePlex.com has a lot of bad things,

1. This is not a "open source" place, as many projects use a license that do not match OSI open source definition.
1. It starts with TFS repository, which makes it very hard to use from other platforms (Linux, Mac and so on).
1. It is sponsored by Microsoft.

Now things change, mate.

1. Even SF.net has fake "open source" projects.
1. CodePlex introduced SVN repository access based on the awesome SVNBridge project. And now it even supports Mercurial repository (sad it is not Git). Even the TFS repository can be accessed via Teamprise client.
1. Well, Microsoft is not the enemy of open source. On this point, I agree with Miguel of Novell/Mono.

I started to use Teamprise Explorer for my open source projects on CodePlex (Alex and #SNMP Suite). The open source license Teamprise team granted to me can still be used today with their latest version (not sure what may happen as they are now part of Microsoft). Well, after a few days I began to miss CVS. Yes, that's why I switched to the SVN way once CodePlex team announces SVNBridge.

It was then Steve joined me on #SNMP Suite and he told me sometimes his working copy became corrupt suddenly. I don't know if that's caused by my frequent check-ins, but that makes Steve's life a little harder as he had to periodically drop the working copy and started from scratch. Now I began to try out TFS and SVN at the same time, and I kind of experience issues similar.

I will try to use more TFS now, as it has better integration with other parts of CodePlex (the issue tracker part) and its client is now official part of Visual Studio 2010. But SVN will be used besides, as I still use SharpDevelop a lot :)
