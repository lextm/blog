---
layout: post
title: "SquareRoot Puzzle: NDepend Check on #SNMP 4.0"
description: "This post is about #SNMP 4.0 and NDepend."
tags: SNMP
excerpt_separator: <!--more-->
---

Recently I got a license for NDepend Pro. I am going to make good use of this amazing tool.

The first thing I did is a quick analysis on what we did from 3.1 to 4.0 (4 and a half months passed except Jan at which time I was not able to code). I followed [Patrick's post here](http://codebetter.com/blogs/patricksmacchia/archive/2009/05/21/a-quick-analyze-of-the-net-fx-v4-0-beta1.aspx).

<!--more-->

## A view of the work achieved

``` sql
SELECT METHODS WHERE CodeWasChanged OR WasAdded
```

We changed a lot of code, which shows the suite evolution is still fast. (The Library is stable now, but the Browser, Compiler and Agent are moving fast.)

## New Core Public Types

``` sql
SELECT TYPES FROM ASSEMBLIES "SharpSnmpLib", "SharpSnmpLib.Controls", "SharpSnmpLib.Mib"
WHERE IsPublic AND WasAdded
```

Only one new types is introduced in 4.0. That is the SearchResult class. You will use it more and more in the future, as [we recommend `IObjectTree.Search`]({% post_url 2010/2010-3-6-squareroot-puzzle-iobjecttree-find-or-search %}).

## New Assemblies

``` sql
SELECT ASSEMBLIES WHERE WasAdded
```

Only one assembly is added to our binary release package. That is snmpd.exe, our SNMP agent reference design.

## New Public Types

``` sql
SELECT TYPES WHERE WasAdded AND IsPublic
```

We have a few new types here except for SearchResult,

- WatchDog: This is a class that works as a hardware watch dog. The Browser utilizes it to monitor the module folder for changes. Without it, changes occurring in a short period of time cause a sequence of UI updates. It can be extended to provide more functionality. (Note that this class is released under MIT license and distributed in a standalone source file.)
- AccessFailureException: This is an exception type used snmpd for read-only or write-only SNMP objects.

## New Public Namespaces

``` sql
SELECT NAMESPACES WHERE WasAdded AND IsPublic
```

Two namespaces are added,

- Lextm.Common: This namespace currently only contains WatchDog class.
- Lextm.SharpSnmpLib.Agent: This namespace contains all agent side relevant classes, such as SnmpApplication, SnmpContext and so on.
  Rambling

Our biggest improvement here is the snmpd agent. :)

I will play more with NDepend and blog more about this wonderful tool.
