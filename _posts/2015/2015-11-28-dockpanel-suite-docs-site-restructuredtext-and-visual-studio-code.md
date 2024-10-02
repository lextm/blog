---
layout: post
title: "DockPanel Suite: Docs Site, reStructuredText, and Visual Studio Code"
description: "This post is about the new docs site for DockPanel Suite, which is built with reStructuredText and Visual Studio Code."
tags: reStructuredText DockPanel-Suite Visual-Studio-Code
permalink: /dockpanel-suite-docs-site-restructuredtext-and-visual-studio-code-d9d5a6b37a0d
excerpt_separator: <!--more-->
---
> Well, such a long title should match a long post. You've been warned!

You probably know that Microsoft ASP.NET team did migrate of their documentation several times. Currently, they use Read the Docs to host it at https://docs.asp.net. Such a shift away from MSDN is really brave, but the user experience is pretty cool. I really love the "Edit on GitHub" buttons, which if I find something incorrect can immediately utilize to solve it for the whole community.

Of course, ASP.NET guys are not the first to do so, as Mono guys have used a similar approach when they build the new Mono Project home site. There are also other pioneers in this area, who see great community generated contents.

Thus, a few weeks ago when I was in a conference room in Microsoft Campus, Redmond, I thought I should try out such an approach for some projects. Yes, DockPanel Suite is a perfect option to experiment.
<!--more-->

## The GitHub Repo for Docs

It all starts from [a new Git repo](https://github.com/dockpanelsuite/dockpanelsuite_docs) at GitHub. If you check out the files, it looks just similar to Microsoft ASP.NET docs repo. Learning from Microsoft guys saves me tons of hours trying out the technologies.

Primarily speaking, the paragraphs come from our original Wiki articles at GitHub, but well formatted in a syntax called reStructuredText (reST). This syntax is more powerful than Markdown, and has already been tested out by many other projects.

## The Read the Docs Integration

It is pretty easy to sign up at Read the Docs, and configure a new doc project to point to the GitHub repo. Then every time a new commit arrives at GitHub, the pages are regenerated automatically and take effect in just a few minutes. So now DPS docs site is at https://dockpanelsuite.readthedocs.org/

Once Ryan is back from his vacation in South East Asia, we will try to change the URL to http://docs.dockpanelsuite.com/

I would not include all details and steps, but generally speaking [Read the Docs' own documentation](https://read-the-docs.readthedocs.org/en/latest/getting_started.html) can answer almost all questions I have.

## reStructuredText in Visual Studio Code

I am using Windows less and less, so when I worked on DPS docs, most of the time I was on OS X on my Macbook Pro. Visual Studio Code is really a light weighted editor with easy-to-use Git integration. It feels great except that it does not support reStructuredText natively (though Markdown works perfectly).

I suffered a few days, unless some day I went to GitHub and found [somebody else complaining](https://github.com/microsoft/vscode/issues/117).

Yes, it was 5 days ago, and I saw Benjamin Pasero commented that reST should be a good idea for a new extension. Probably I went crazy at that special moment, and started to write such an extension.

Information collection went smoothly and I could navigate Visual Studio Code to see how Markdown was supported. But soon I hit a problem that Markdown support is far too complicated to follow as it has many more features than syntax highlighting. Microsoft was lucky to find a good open source parser for Markdown in JavaScript, so that integrating it with Visual Studio Code was kind of a breeze. But existing reStructuredText parsers are either in Python or Java.

Fortunately syntax highlighting can be done in another way, by importing TextMate's syntax file. Microsoft created a small tool called "yo code", which can carry out the automatic conversion, with who I created a little extension 4 days ago. I tested it out and immediately published it to Visual Studio Marketplace. That's the 0.0.1 version of reST for VS Code.

Then 2 days ago I went back, added code snippets and other supporting files, and published the 0.0.2 version. This marks the birth of a new product from LeXtudio, and Erich Gamma himself clapped! It was such an honor!

I do have a few features on the list for this extension. Bigger ones include,

1. Porting the Java reST parser to C# and .NET Core, so that I can ship it with this extension on every platform without JVM. This should be done by using Sharpen following NGit's practice.
1. Writing a language server for reST.
1. Integrating with sphinx.

Of course, this means I finally have a chance to play with some technologies I have been monitoring for a very long time, Sharpen, .NET Core, and TypeScript.

Well, at last I'd like to welcome every DPS users to help out. Improving the documentation is now easier than ever! Stay tuned.
