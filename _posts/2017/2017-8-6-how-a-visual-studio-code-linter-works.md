---
description: An in-depth exploration of how Visual Studio Code linters work, using the ruby-linter extension as an example to understand the core components and event-based architecture required for implementing language linting features.
excerpt_separator: <!--more-->
layout: post
permalink: /how-a-visual-studio-code-linter-works-681c8388b0ea
tags: visual-studio-code open-source
categories: [Tools and Platforms]
title: How A Visual Studio Code Linter Works
---
I blogged about [what a basic Visual Studio Code language extension should contain]({% post_url 2017/2017-5-27-receipt-of-visual-studio-code-extension %}) a few months ago, and today we focus on linter.

<!--more-->

## Linter Basic

The essential responsibility of a linter is to scan your source file and report back warnings and errors. Many programming languages do have good command line linters, so the remaining task of an extension is quite simple,

- Pass the file information to linter.
- Collect linter output and display.

## Study By Example

Now let's analyze [the ruby-linter extension](https://github.com/hoovercj/vscode-ruby-linter/blob/master/package.json#L21) to better understand how it works.

First, this extension must be triggered by a special event "onLanguage",`"activationEvents": [ "onLanguage:ruby" ]`. That means when a Ruby file is opened, the extension would be triggered.

Second, [the extension](https://github.com/hoovercj/vscode-ruby-linter/blob/master/src/extension.ts#L8) initializes a linting provider to wrap the actual command line linter. [The linting provider](https://github.com/hoovercj/vscode-ruby-linter/blob/master/src/features/rubyLinter.ts#L20) in turn calls `ruby -wc` to executing the task.

Finally, the command line output of the linter should be [parsed](https://github.com/hoovercj/vscode-ruby-linter/blob/master/src/features/rubyLinter.ts#L28).

Visual Studio Code defines the Diagnostic type to store warnings and errors, so that we can easily use regular expressions to extract information from command line output and pass it to the editor.

As the infrastructure is quite simple, you can make use of the code to implement a similar linter for another programming language in a just a few hours (I did this for reStructuredText).
