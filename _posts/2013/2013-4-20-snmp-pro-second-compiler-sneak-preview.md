---
layout: post
title: "#SNMP Pro: Second Compiler Sneak Preview"
description: "This post talks about the second sneak preview of #SNMP MIB Compiler Pro."
tags: SNMP
permalink: /snmp-pro-second-compiler-sneak-preview-dc62ff62f38
excerpt_separator: <!--more-->
---
In the first preview I demonstrated the basic building blocks of the Compiler Pro. In this post, we are going to review the new additions.
<!--more-->

## Object Tree Panel
After having the documents compiled, your first question must be "how can I see the objects?" and here comes the answer, the Object Tree panel is now added also in the compiler.

To make it even more convenient to use, double-clicking any node on the tree, you will be redirected to the document that defines this node and the exact line and column. I call this function "Jump to Definition".

The reverse jump needs some time to implement, so it will not ship in the initial release.

## Error List Panel
The problem of reading errors and warnings from the Output panel is obvious. There are far too many things written there, and it is very difficult to locate exactly what you want.

Well, now with the Errors List panel you can focus more, because you can select whether both errors and warnings should all appear, and by ordering the list by columns you can fully focus on a single file or a single category of errors.

## Consolidated Menu Items
You might notice that some menu items have been removed. Yes, they are removed because they are no longer useful.

* Compile and Compile All are now merged as a single Compile menu item, which means to compile all documents in the solution. The original design to use separate items was stupid, as there is almost no difference between the two.
* Reset is removed, because now if a loaded module is modified and compiled again, the compile can automatically unload the previous version and attempt to load the new version. This means the Module List and Object Tree panels will be taken care by the compiler, instead of the user who manually clicks Reset. Thus, this menu item is now obsolete.

## Various Improvements Under the Hood
The type resolution has been redesigned to extract type inheritance information out, and in this way we can perform type verification on receiving SNMP packets in the future or provide better format of those data received (such as displaying PhysAddress as HEX).

Table entities detection is now more accurate as we no longer rely on the authors to use standard naming convention, but use metadata extracted such as types of the entities to tell which is a table, which is an entry and which are the columns.

There are already tons of changes made to the ANTLR grammar file (to simplify a few rules), and more is coming.

Stay tuned.