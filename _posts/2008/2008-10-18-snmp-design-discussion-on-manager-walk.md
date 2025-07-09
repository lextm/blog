---
layout: post
title: "#SNMP Design: Discussion on Manager.Walk"
description: "This post is about a discussion on Manager.Walk design and implementation."
tags: SNMP
permalink: /snmp-design-discussion-on-manager-walk-e6c3c359ff9b
excerpt_separator: <!--more-->
---
OK, according to Producing Open Source Software, there should be no private conversation under the surface, so I am going to publish a few conversations between me and Steve so you can be updated.
<!--more-->

This time, let's start with a talk about Manager.Walk.

> Steve: Crowe's library had a ManagerSubTree. An older version of an app uses Crowe's library. I was tasked to switch that app to use our stuff, and I don't know how you want to deal with this. pretty much they used it in a way to see all of the print jobs in the table, and then goto the last one and return information on that index. I know we do have Walk, which returns a one dimensional list of answers, but I guess I need more help in understanding how that works and stuff.
>
> Lex: In fact, when I started to write table related code for #SNMP, I did not refer to Mr. Crowe's code any more, so I really don't know how ManagerSubTree works (I will investigate it later). Therefore, I cannot easily say if #SNMP can do the same or not.
>
> Lex: Hi now I think I can answer the question about `ManagerSubTree` class in Mr. Crowe's SNMP library. Yes, although it appears like a class, the function it supports is similar to Manager.Walk in #SNMP. Manager.Walk returns a list of objects (depends on WalkMode argument), and ManagerSubTree provides the same list from its indexer or GetEnumerator() method (and it only walks in the subtree).
>
> OK, now let's take a look at another key difference. In ManagerSubTree, there is a fix tool to fix something against a non-compliant agent. #SNMP library does not yet have similar code and I don't know if it is necessary.

Hope this also helps you understand the relationship between Mr. Crowe's SNMP library and #SNMP.

Stay tuned.
