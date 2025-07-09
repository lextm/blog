---
layout: post
title: "HardQuery Report: Source Navigator Highlight"
description: This post reports the progress of HardQuery and changes in Source Navigator feature.
tags: Code-Beautifier-Collection Delphi
permalink: /hardquery-report-source-navigator-highlight-53186ae0900e
excerpt_separator: <!--more-->
---
(CSDN Oct 10, 2006)

What features I create are added into CBC? Although most of features are directly ported from other open source projects, I did create some of my own. Latest one is named Source Navigator. I use this name because it is similar to ArtCSB's Source Navigator. However, the UI is completely different.
<!--more-->

I was a Visual Studio 6 user, so I like the navigation bar inside VC 6. It may be the most interesting feature I like. SharpDevelop has a similar bar, while Castalia adds such a bar to delphi IDE.

It is a not-to-hard-to-implement feature in fact if you use CodeDom technology. However, different people make different UI. ArtCSB creates a tree like form, while Sharp Builder Tools makes a tabbed list form. They do not use a bar.

When I decided to port in ArtCSB's Source Navigator, I thought it would be one of the best CodeDom examples I had. Yes, analysing the code was real fun. I saw how easy it turned when CodeDom was using. I wanted to make things a little bit different. So soon I decided to make a bar for myself.

At this moment, the bar is very simple. I make no use of the bookmarks, which is something I am willing to add.

What is wrong with the bar? I have to mention that MS who creates CodeDom also leaves bugs. For instance, in .NET 1.x, the constructors and destructors cannot be handled correctly. As a result, tool vendors have to make their own parsers. I am not going to implement my parsers because I do not have time. I will use SharpDevelop's parser for C#. But I do not know where to find a fast delphi source parser. A C++ parser is also a problem. I am not sure I have enough power to build them finally because I am still a poor programmer indeed.

Stay tuned. A second version may be better.
