---
description: "This post is about syntax highlighting for SMI/MIB."
excerpt_separator: <!--more-->
layout: post
permalink: /tritonmate-words-syntax-highlighting-for-smi-mib-efe99ad93af2
tags: snmp sharpdevelop .net
categories: [Technologies and Concepts]
title: 'TritonMate Words: Syntax Highlighting for SMI/MIB'
---
Finally syntax highlighting is added. Currently we use SharpDevelop's text editor control, and its syntax highlighting engine (line number as well).

Since SharpDevelop does not have an SMI/MIB syntax file, I followed the standard approach to port smi-mib.xml from jEdit. Yes, without doing this you never know #D guys learned from jEdit :)

Here I share [the syntax highlighting file](http://code.google.com/p/sharpsnmplib/source/browse/Compiler/smi.xshd) so that you may reuse it in your applications.
<!--more-->