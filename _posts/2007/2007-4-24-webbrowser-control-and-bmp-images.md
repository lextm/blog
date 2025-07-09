---
description: This post describes why to open BMP images in a WebBrowser control can
  be troublesome.
excerpt_separator: <!--more-->
layout: post
permalink: /webbrowser-control-and-bmp-images-855a5bb4f23f
tags: .net windows
categories: [Programming Languages]
title: WebBrowser Control and BMP Images
---
It is convenient to develop a WinForms application with a WebBrowser component because Word documents and other files can be opened in it. The only problem I found last week was that BMP files cannot be opened inside.

I guess the reason for that difference is that BMP is not a compressed format, which is not suitable for Internet usage. If it is the reason, then why Firefox supports BMP very well?

After all, when you want to Navigate() to a BMP file, stop. You should convert the image to GIF/JPEG/PNG format instead.
<!--more-->
