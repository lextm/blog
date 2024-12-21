---
layout: post
title: "TritonMate Words: Syntax Highlighting for SMI/MIB"
description: "This post is about syntax highlighting for SMI/MIB."
tags: Code-Beautifier-Collection Delphi
permalink: /tritonmate-words-syntax-highlighting-for-smi-mib-efe99ad93af2
excerpt_separator: <!--more-->
---
Finally syntax highlighting is added. Currently we use SharpDevelop's text editor control, and its syntax highlighting engine (line number as well).

Since SharpDevelop does not have an SMI/MIB syntax file, I followed the standard approach to port smi-mib.xml from jEdit. Yes, without doing this you never know #D guys learned from jEdit :)

Here I share the syntax highlighting file, http://code.google.com/p/sharpsnmplib/source/browse/Compiler/smi.xshd so that you may reuse it in your applications.
<!--more-->