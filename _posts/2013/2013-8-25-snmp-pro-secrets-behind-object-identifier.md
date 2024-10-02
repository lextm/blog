---
layout: post
title: "#SNMP Pro: Secrets Behind OBJECT IDENTIFIER"
description: "This post talks about the secrets behind OBJECT IDENTIFIER."
tags: SNMP
permalink: /snmp-pro-secrets-behind-object-identifier-ff242fd4474e
excerpt_separator: <!--more-->
---

You might sometimes wonder why the shortest OID is 0.0 (aka ccitt.zero). [I blogged about that]({% post_url 2008/2008-9-8-snmp-design-solving-the-zero-puzzle %}) a few years ago, so today I won't revisit that.

It was one day that on StackOverflow.com I came across [this question](http://stackoverflow.com/questions/17270451/understanding-c-sharp-code/17362732#17362732), and started to recall where this piece of knowledge was gained by me. Luckily I was able to go back to the great bible of SNMP and located that page. And this time, I also drilled down and located [the original standard document](http://www.itu.int/ITU-T/studygroups/com17/languages/X.690-0207.pdf).

It is such a sweet thing to help out another guy and also help myself understanding something deeper.

WOW, in fact Macolm left a comment in his code to point to that document!

<!--more-->
