---
layout: post
title: "AddMany 4.1 Porting Notes"
description: This post is about the porting of AddMany 4.1 to CBC 2.
tags: Code-Beautifier-Collection Delphi
permalink: /addmany-4-1-porting-notes-eace63c85cae
excerpt_separator: <!--more-->
---
(CSDN April 25, 2006)

1. Can only be built with AddMany copy local true. Cannot Link Units.

2. Purified Pascal implementation of OtaAddMany is "abstract". So can not be used by CBC.

3. When distributing, AddMany.dll (merged version) and Lextm.AddMany.dll (wrapper) should be put in the same folder of Lextm.CodeBeautifierCollection.AddMany.dll.

In delphi-produced AddMany, IDEPlugin class adds BDS menu items in its constructor. So I have to reimplement this constructor in order to add new items on CBC 2. The wrapper, Lextm.AddMany.dll in delphi for .Net, contains a modified version of IDEPlugin which does this function. Lextm.CodeBeautifierCollection.AddMany.dll is a plug in assembly which directly registers a feature to CBC 2 in C#.
<!--more-->