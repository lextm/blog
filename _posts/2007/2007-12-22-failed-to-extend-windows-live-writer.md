---
layout: post
title: "Failed to Extend Windows Live Writer"
description: This post is about extending Windows Live Writer.
tags: .NET
permalink: /failed-to-extend-windows-live-writer-501d5f0e91fa
excerpt_separator: <!--more-->
---
There is an SDK for extending Windows Live Writer. However, I do not know where to start.
<!--more-->

I want to create a plugin that archives existing posts so you can easily backup your precious words. Also I think it can be further improved to help you migrate posts from one provider to another.

But even though WLW SDK provides three categories of API, I cannot find what I want.

Provider Customization API is for blog service providers like Windows Live Spaces, WordPress, and TypePad.

Application API is for launching WLW from an external application.

And I am not going to write one of Content Source Plugins which are common.

BTW, It is sad to see that a plugin installer should be MSI based. That prevents me from creating an installer with Inno Setup.

Why not release this project as an open source project so everyone can play with the code in order to meet all requirements out there? Should I wait until certain APIs are posed in later WLW? Sorry I won't wait. I would try other ways.
