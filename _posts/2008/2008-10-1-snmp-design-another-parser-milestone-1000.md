---
layout: post
title: "#SNMP Design: Another Parser Milestone, 1000+"
description: This post is about the progress of the MIB parser.
tags: SNMP
permalink: /snmp-design-another-parser-milestone-1000-ff525619b835
excerpt_separator: <!--more-->
---
On September 11, I received a mail from Robert Arnold that he can provide a bunch of MIB documents. So I asked him to package them to me. All those documents are taken from this web site. Robert wrote some scripts to grab documents from the pages, so I don't need to navigate and copy contents.

http://support.ipmonitor.com/mibs_byname_A.aspx
<!--more-->

It was two weeks later that I finally had time to work on those documents. Therefore, a lot of bugs were found in the parser and fixes were located as well. When I checked in Change Set 16025 yesterday morning, the parser was significantly improved. But more bugs were found in the browser once so many documents were available.

So I spent almost one day on the browser. Several parts were refined,

## MIB Inventory
Steve added a lot of code inside ObjectRegistry and ObjectTree to handle user imported MIB documents. But I think it is better to handle them in an individual unit. So MibInventory class is now added.

## Compiler Units
The parser/compiler is now split into two logical units. The engine is now separated into a new unit called Compiler, which serves as the front-end (input: MIB documents, output: module entities). The back-end is still part of ObjectTree who assembles all module entities into an object tree (input: module entities, output: MIB object tree).

## Recursive Assembling
A critical bug is found in the back-end that many entities are not assembled because of their complex dependency on other entities. This requires a recursive algorithm inside so most of these ignored entities can be assembled round by round.

## Complex OID Definitions
In the past, it is rather hard to handle { iso 2 840 10036 }, { iso(1) org(3) dod(6) 1 }, and so on. But now both front-end and back-end can support those definitions correctly.

So now I am going to check in the latest updates. The following picture sets a new record, 1217 modules loaded in Module List panel, while 61 modules pending.