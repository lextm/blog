---
layout: post
title: "Refactoring Tools: Dangerous"
description: "This post describes why manual refactoring is much safer than using refactoring tools."
tags: JetBrains
permalink: /refactoring-tools-dangerous-c4ce872a5425
excerpt_separator: <!--more-->
---

The book Refactoring (Martin Fowler) is my favorite. I read it for the first time about four years ago. Since then, I have been refactoring for a long time in different projects with different programming languages (C#, C++, and Delphi).

Yesterday I tried to refactor code with ReSharper 3 RC, but Visual Studio froze suddenly. Why? This might be caused by bugs in ReSharper or something else. In this very case (and most cases), manual refactoring is much safer because our minds is much smarter.

Many refactoring tools crashed code. I am so lucky that I never experience crashes inside Delphi or Visual Studio 2005 thanks to the internal code protection. However, dangers may occur anywhere.

So as to keep your code safe, remember to make backup whenever necessary.
<!--more-->