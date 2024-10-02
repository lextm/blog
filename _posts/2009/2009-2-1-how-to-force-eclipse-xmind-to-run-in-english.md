---
layout: post
title: "How to Force Eclipse/XMind to Run in English"
description: "This post is about how to force Eclipse based products to run in English."
tags: Java
permalink: /how-to-force-eclipse-xmind-to-run-in-english-48dd5334de90
excerpt_separator: <!--more-->
---
It is quite convenient that more and more software vendors provide multi-lingual products. However, I don't think all of them hire good translators. Therefore, in order to understand how to use the tools smartly, I have to pick up English from some configuration dialog.

But you may notice Eclipse based products such as XMind do not provide such a dialog. So how to force it to display English? I did not realize this trick until I read this IBM article. Right, it is tricky to modify some INI file.

In my case, I opened up xmind.ini in XMind installation folder, and appended the following lines to its end,

``` text
-Duser.language=en
-Duser.country=US
```

Saved it and launched XMind again. Oh, it works as expected. Nice.
<!--more-->