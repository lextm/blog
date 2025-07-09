---
layout: post
title: "Clear Visual Studio 2005 Vault Error State"
description: This post talks about how to clear Visual Studio 2005 Vault error state.
tags: Visual-Studio
permalink: /clear-visual-studio-2005-vault-error-state-63a024005060
excerpt_separator: <!--more-->
---
I was just checking in a lot of files to Vault. I thought it was dead so I killed Visual Studio 2005 in Task Manager. OK, from then on it complains that some files are exclusively checked out by a user so I cannot check them in until he checks in. And the serious problem comes, that user is me. Oh, who will save me???
<!--more-->

I believe it is a Vault bug but because I am still using the 3.5 old version, so I cannot hope this bug fixed today or in the future (SourceGear is selling 4.1 right now). Therefor I am forced to find out how to resolve it myself.

In fact, today is my lucky day that when I launch the Vault Client, a workaround is so obvious. I UNDO all checkouts but LEAVE my working files there. Then I launch Visual Studio 2005 again, and suddenly see everything is fine. Why not buy some lottery tickets tonight?

I have to confess that I never knew checking in hundreds of files would take such a long time. But I am sure next time I won't kill Visual Studio.
