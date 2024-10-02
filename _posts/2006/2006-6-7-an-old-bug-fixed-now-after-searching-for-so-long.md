---
layout: post
title: "An old bug fixed now after searching for so long"
description: This post is about a bug in CBC 2, which is fixed now.
tags: Code-Beautifier-Collection Delphi
permalink: /an-old-bug-fixed-now-after-searching-for-so-long-b123d7e1c926
excerpt_separator: <!--more-->
---
(CSDN June 07, 2006)

I have been using serialization now and then. Lately when I make some public classes with [Serializable] to internal classes, annoying exception shows when I use a XmlSerializer. The constructor of it which takes a Type parameter fails.
<!--more-->

I find nothing in the MSDN and .NET SDK Docs but I know the only reason is my modifications. Maybe the serializer needs to know much about the Type so it can only be a public class. But why MS fails to make this point clearer.

This bug dates back to very old versions of CBC2. I am sorry you cannot save you preferences and an exception is popped. The only thing I feel lucky is that even without preferences files, CBC 2 can still run and do some staff for you.

You can either modify the source (change some internal Preferences classes to public), or wait for N3 RC 1.
