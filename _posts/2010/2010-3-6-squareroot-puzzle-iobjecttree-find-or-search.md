---
layout: post
title: "SquareRoot Puzzle: IObjectTree, Find or Search?"
description: "This post is about the design of IObjectTree.Find method"
tags: SNMP
permalink: /squareroot-puzzle-iobjecttree-find-or-search-eed6e2060504
excerpt_separator: <!--more-->
---
It is not easy to design a library, especially if the author tries to provide easy to use API. Therefore, only after so many revisions I finally have a chance to revisit a few annoying interfaces recently.
<!--more-->

Did you use IObjectTree.Find(uint[]) method directly? It was not exposed initially, but can be accessed from IObjectRegistry.Tree.Find later due to the Browser/Compiler requirements. But it is hard to use because,

1. It throws ArgumentOutOfRangeException if the numerical form cannot be resolved by this tree.
1. It does not help much when you try to convert 1.3.6.1.1.1.0 to iso.org.dod.internet.mgmt.mib-2.system.sysDescr.0.

Why cannot we make this function better? But how?

Such questions are hard to answer till today I decided we add a new Search method. This new method still accepts uint[] but it no longer navigates through the tree nodes to locate exact matched one. Instead, we try to locate the branch first and if we cannot map all the numbers to nodes on the branch, we simply stop and return the last node located and remaining numbers in a new class, SearchResult.

Now getting textual forms (module name::object name, or parent node.[…].object name) becomes much easier and we finally achieve what net-snmp performs for a very long time.

From now on, Find is obsolete, and we should move to Search. Below is a summary,

* Changes on Find are breaking, so you need to retest your code who relies on this function.
* Search provides more features than Find (tolerate if the object is not in the tree).
* Find is obsolete and will be marked as internal in our next release.
* To get textual forms, we need to utilize SearchResult class.

Note that IDefinition.TextualForm is also obsolete. To get the same output, first construct a SearchResult using this IDefinition instance (second parameter should be `new uint[0]`). Then, `SearchResult.Text` is what you need, while you can also check out `SearchResult.AlternativeText`.
