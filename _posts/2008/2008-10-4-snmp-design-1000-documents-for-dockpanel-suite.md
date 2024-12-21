---
layout: post
title: "#SNMP Design: 1000+ Documents for DockPanel Suite"
description: This post is about how to implement the MIB compiler GUI with DockPanel Suite.
tags: SNMP
permalink: /snmp-design-1000-documents-for-dockpanel-suite-c7399068d59d
excerpt_separator: <!--more-->
---
Now #SNMP is not the only one who suffers the performance issue. I have just found DockPanel Suite has a similar issue. For example, I created a simple DockContent derivative that simply contains a RichTextBox to host the MIB documents. Then I followed the usual way to design the main window and let it open 1000+ documents. Wow, it froze there for a long time.
<!--more-->

Luckily I had all the time in the world to wait till all documents were opened (about 195,000K memory is consumed). And now you can see how the compiler GUI prototype looks like.

Do you like it?

(Updated: OK, just found out that both Visual C# Express and SharpDevelop 3 Beta froze and died in the same case. Wow. Maybe opening 1000+ files at a time is a crime so nobody assumes that I would ever commit it.

I have just found a workaround. Why not force the users to open <100 files at time? Remember it is still a prototype? In this way even if they want to open 1000+ files, they can try to add all files in five rounds.)
