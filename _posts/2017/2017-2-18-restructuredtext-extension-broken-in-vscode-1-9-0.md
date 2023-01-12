---
layout: post
title: "reStructuredText Extension: Broken in VS Code 1.9.0"
description: "This post is about why the reStructuredText extension was broken in VS Code 1.9.0."
tags: reStructuredText
permalink: /restructuredtext-extension-broken-in-vscode-1-9-0-3e01952ad155
excerpt_separator: <!--more-->
---

A user reported this issue a few days ago that the extension no longer works after VS Code 1.9.0 release, while I was packing up things before my departure from Shanghai to Montreal. I could not even debug VS Code at that time.
<!--more-->

So I was planning to take a look once I finally arrived but VS Code 1.9.1 release fix was released, and both the debugging issue and the extension empty display issue were fixed. Aha, what a mess. What exactly happened?

Luckily I had some reliable guy in the VS Code team itself, who kindly informed me the culprit is [a change they made in 1.9.0](https://github.com/Microsoft/vscode/issues/20229) (reverted in 1.9.1), where broken HTML pages won't be loaded into VS Code views.

Thus, can you imagine that Sphinx generates broken HTML pages? Of course not. Let's see one example below,

``` html
<!DOCTYPE html>
<!-- [if IE 8]><html class="no-js lt-ie9" lang="en" > <![endif] -->
<!-- [if gt IE 8]><! --> <html class="no-js" lang="en" > <!-- <![endif] -->
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>#SNMP Documentation &mdash; #SNMP Library 2.10 documentation</title>
```

See it? The `<html>` tag was placed in conditionals which were added to serve IE 8!!! Probably VS Code (aka Electron) no longer thinks that's valid HTML, while it was originally Microsoft who forced everyone to use such a hack. So ridiculous a case.

As IE 8's lifecycle has expired, I think it would be a responsibility of all web site generators (such as Sphinx) to stop using such conditionals. That should finally give us cleaner web pages.
