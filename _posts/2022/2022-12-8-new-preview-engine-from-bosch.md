---
layout: post
title: "The New Preview Engine from Bosch"
description: A post about the new preview engine for sphinx from Bosch
tags: Visual-Studio-Code reStructuredText
excerpt_separator: <!--more-->
---

If you have been a long time user of reStructuredText extension for VS Code, you might have noticed that this project is under significant changes for a while,

- No more frequent release.
- The version numbers change in a different manner.
- Many preview builds were shipped without source code.

This post aims to shed some light on what's the story behind.

<!--more-->

## How Old Preview Engine Works

The old preview engine was ported from VS Code Markdown extension.

First, the HTML page generation was done by either docutils or sphinx command as showed in [this piece of code](https://github.com/vscode-restructuredtext/vscode-restructuredtext/blob/189.3.0/src/preview/rstEngine.ts#L22).

Once the raw HTML page was available, the contents were read into the memory and [further processed as below](https://github.com/vscode-restructuredtext/vscode-restructuredtext/blob/189.3.0/src/preview/previewContentProvider.ts#L47),

1. Replace the header section to insert preview settings, CSP settings and required scripts.
1. The tags in body section are analyzed and inserted with line numbers that were estimated based on the total line number of the source file, and the index of this HTML tag in the whole HTML page.
1. All normal URLs are converted to VS Code specific links.
1. Finally the enriched HTML contents are loaded into the preview panel.

Note that the injected elements were critical because they contain the extension settings (such as whether scrolling is in sync), current editor status (such as active line and total line numbers) and hooks to various preview panel events (such as click/double click, scrolling and so on).

Script files like [scroll-sync.ts](https://github.com/vscode-restructuredtext/vscode-restructuredtext/blob/189.3.0/preview-src/scroll-sync.ts) are very important to let the preview panel scroll to the right location or request the editor to scroll to the right line.

However, this engine itself lacks of a good way to generate accurate line numbers for HTML tags, and the scrolling experience can be terrible in many cases.

The initial C# based language server or snooty server didn't help much on previewing pages.

## The Introduction of Esbonio

I [wrote about this language server project]({% post_url 2022/2022-2-27-new-language-server-and-case-study %}) created by Alex Carney this February, and since then it has been used as the default for this extension. Esbonio is actually more than just a language server, as Alex tried to also tune the generated pages for previewing.

There were several rounds of conversation between Alex and me, so that we can sync up on his innovation. In order to avoid any breaking changes to users of this extension, we decided to keep the Esbonio VS Code extension alive,

1. It provides Alex a playground to try out new ideas.
1. I can cherry pick new things on a different pace (slower but more stable).
1. Alex can also explore integration with other text editors, such as a new way to host preview pages inside the language server so that editors load them as remote web pages from a web server, not HTML pages on disk.

While this collaboration set a good example and was going slowly but steadily, one day Bosch knocked on the door.

## The New Preview Engine Offered by Bosch

Bosch guys were so kind to set up calls with Alex and me and demonstrated their own live preview engine and other important changes they made in this field. I won't cover too much detail, but some are already known to you,

1. A new line counting mechanism was developed so that we can insert very accurate line number information into Sphinx generated HTML pages.

   > This has been first integrated in 190.1.x releases, and just back ported to 189.3.0.

   > We also need to thank the guys on Sphinx project for their guidance.

1. They found a simpler way to host preview HTML pages in VS Code.

   > I am reviewing their changes right now and shipped 190.1.x releases from a private repo.

1. They found a better way to communicate with Sphinx core engine to trigger live preview updates.

   > This has been sent to esbonio as a pull request and accepted just a few days ago.

1. They investigated many other performance issues and patches will be made available for individual projects in the coming weeks.

In short, the Bosch guys have made a huge contribution not only to this VS Code extension project, but almost the entire reStructured/Sphinx ecosystem.

Due to the scale, I expect a stable release of this extension with all Bosch proposed changes to be shipped in early 2023.
