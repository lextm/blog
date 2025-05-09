---
description: Major improvements in reStructuredText for VS Code (version 67.0.0+) including Workspace support, automatic conf.py detection, and simplified preview configuration.
excerpt_separator: <!--more-->
layout: post
permalink: /important-update-on-restructuredtext-for-vscode-efa0d412422f
tags: restructuredtext visual-studio-code open-source
categories: [Programming Languages]
title: Important Update on reStructuredText for VS Code
---
![img-description](/images/rst-vscode.png)
_Figure 1: reStructuredText for VS Code._

An image should save me a thousand words, but I rather write a blog post to reveal the biggest changes introduced in the latest releases (67.0.0 and above), so that you, the dearest users, have a chance to know the stories behind.
<!--more-->

## Long Time Pains

You can see from the left side of the image above that I was using the Workspace feature of Visual Studio Code. Workspace was added in VS Code 1.14, and allows users to group multiple folders in a workspace. The design of this extension always assumes you work on a single folder, so [Workspace was not supported](https://github.com/vscode-restructuredtext/vscode-restructuredtext/issues/52).

Even for a single folder, you might have multiple `conf.py` to work on, and switching the preview setting between them was painful. Manual editing `.vscode/settings.json` was not fun, and as one of the users I felt the same. However, to make a systematic change on the code base was not an easy task.

## Contribution From Tormod

Tormod Landet approached me in June with [a simple pull request](https://github.com/vscode-restructuredtext/vscode-restructuredtext/issues/91).

It contained some code interesting that made it later possible to innovate upon, where he attempted to scan the folder structure for potential `conf.py` candidates. I left a hint on the C# extension, and hoped that we could revisit this idea later this year when I had some more time.

But Tormod was more energetic than I thought, and he was able to work alone and deliver [a second pull request](https://github.com/vscode-restructuredtext/vscode-restructuredtext/pull/92).

This time he added a pop-up list and status bar element, so active `conf.py` file can be easily observed.

Unfortunately I was delayed by other things and just recently reviewed his changes (made in early July). There were a few minor user experience issues, which I went a head and fixed.

## New User Experience Explained

So if you are using this extension for the first time (or assume you just upgrade from an old version), the usage is simpler than ever.

Simply open a folder or workspace, and navigate to a reStructuredText source file `.rst`. Trigger a preview via shortcuts or clicking the preview button. Then this extension would prompt you to choose an active `conf.py` file to generate preview pages,

![img-description](/images/rst-popup.png)
_Figure 2: Selection of active conf.py file._

> Note that you can also choose `rst2html.py` as an alternative preview rendering engine.

After that, all preview pages would be rendered according to this active setting, showed in status bar,

![img-description](/images/rst-status.png)
_Figure 3: Status bar element for active conf.py file._

If you want to work on another `conf.py` file (or switch to `rst2html.py` engine), simply click the active file in status bar, and the extension would prompt you again with the options.

Thus, you no longer need to remember the extension settings and manually configure them (though in edge cases they might still be helpful).

* Release 67.0.0 contains the initial changes.
* Release 68.0.0 allows the active selected setting to persist.
* Release 69.0.0 fixed the remaining issues.

Hope you enjoy the new releases. Stay tuned.
