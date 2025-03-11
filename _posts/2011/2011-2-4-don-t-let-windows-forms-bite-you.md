---
layout: post
title: "Don't Let Windows Forms Bite You"
description: "This post is about Windows Forms and how to avoid common pitfalls."
tags: .NET
permalink: /dont-let-windows-forms-bite-you-3561762b22b7
excerpt_separator: <!--more-->
---
I just recently understand how heavily Windows Forms depends on native Windows components and why switching to WPF is nice for developers in some scenarios. So the story goes.
<!--more-->

Do you know that if you use RichTextBox in your application .NET Framework automatically sets a dependency on riched20.dll? And for some reason such a dependency can be very harmful, and many people suffer.

When you append certain text into the box, riched20.dll may spend a surprisingly long time and one of your CPU cores to do its task and ignore your anger.

This may be acceptable on multi-core machines, but what if your machine has only one core?

:) So next time please use a simple TextBox instead (TextBox does not rely on riched20.dll), or switch to WPF/Silverlight.

Is there any other well-known Windows Forms issue like this one?
