---
layout: post
title: How I Ended Up with VSCode as Git Client
description: A post about how I ended up using VS Code as my default Git client on all platforms
tags: Visual-Studio-Code
excerpt_separator: <!--more-->
---

This is a short story on how I gave up all other Git clients and ended up with VSCode as my everyday companion.
<!--more-->

## Relying on Many Clients
I used to install many Git clients (like SmartGit, TortoiseGit) and enjoy their unique features such as interactive rebase wizard and/or diff/merge editor. As it is not easy to develop a good enough cross platform client software a few years ago, I had to evaluate and adapt to different clients on Windows/Linux. The popularity of Electron makes it possible to write cross platform software using web technology, and the last standalone Git client I used was GitKraken, a neat client powered by Electron.

## The Enterprise Trap
However, I often find it difficult to install a separate client software in a corporate network. There are far too many clients out there, but due to security policies each company is able to select just a few options and make them available to the employees to use. I was forced to use tools like SourceTree or Git Extensions or the Git client inside Visual Studio, which I really dislike. They do work in simple cases, but when I need to carefully reorganize the commits with operations such as rebase they lack clear insights into the entire commit history or interactive editor. Of course I had to abandon GitKraken because it's not free for commercial use.
Since then I started to look for good alternatives. Interestingly I didn't realize Visual Studio Code later became my final choice. VSCode is naturally based on Electron and is installed already on all my machines, so turning itself into a good Git client makes perfect sense.

## Switching to VSCode
Well, I dislike the default Git features built into VSCode, as they are not enough for a high demand user like me. By evaluating quite a few extensions, I decided to build my baseline upon Git Graph. Similar to GitKraken, Git Graph builds its features around a beautiful commit history view, so that all typical operations such as pull/push/checkout and branching can be done by just right clicking somewhere. Even cherry pick/rebase can be initialized from there. But this is the open source world, and the people behind Git Graph cannot implement everything in their spare time. Recently I added GitLens to the baseline as it adds blame related views as well as an interactive rebase editor.

> The company behind GitKraken acquired GitLens recently, which isn't a surprise. But look forward to seeing what happens next in that area.

Stay tuned as I am going to blog about how to do rebase in VSCode.
