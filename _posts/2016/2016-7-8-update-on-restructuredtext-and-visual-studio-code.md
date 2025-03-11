---
layout: post
title: "Update on reStructuredText and Visual Studio Code"
description: "This post is about the update on reStructuredText and Visual Studio Code."
tags: reStructuredText
permalink: /update-on-restructuredtext-and-visual-studio-code-1b23916c4c0f
excerpt_separator: <!--more-->
---
When I started the reStructuredText extension for Visual Studio Code in Nov 2015, I wasn't expect it to be a hot extension in the gallery. But even without an ambition, now it serves >1,700 users, so time to make it better.
<!--more-->

Interestingly that more people enter the arena with their reStructuredText extension, like [this one](https://github.com/tht13/RST-vscode) starting in Feb 2016, and [this one](https://github.com/searKing/preview-vscode) adding reStructuredText support in Jun 2016.

As all of them provides preview, below I make a comparison,

| Extension | vscode-restructuredtext | RST-vscode | preview-vscode |
| --------- |------------------------ | ---------- | -------------- |
| Technology | sphinx | docutils | rst2mdown |
| Effect | Most accurate | Somewhat useful | Hard to predict |

So why rst2mdown might give unpredictable result? reStructuredText has a far richer syntax than Markdown. Therefore, when you convert to Markdown, information lost happens, and the final preview result can be completely different.

Why cannot docutil achieve the best result? Because it only processes a single file, that included files and other features related to a complete sphinx project cannot be properly rendered.

As a result, only a true sphinx based solution like vscode-restructuredtext can offer the most accurate preview with full theme support.

To try out the best preview tool, you can download/upgrade to Visual Studio Code 1.3.0, and then [follow the guide](https://marketplace.visualstudio.com/items?itemName=lextudio.restructuredtext).
