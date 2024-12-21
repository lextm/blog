---
layout: post
title: "CBC Code Templates"
description: "This post describes how to use CBC Code Templates."
tags: Code-Beautifier-Collection Delphi
permalink: /cbc-code-templates-760c67c006c8
excerpt_separator: <!--more-->
---
(CSDN Jan 31, 2007)

Pawel Glowacki, a CodeGear guy, blogged about his xdoc Code Template here.

The fact is that I have done a few xml-comments-related templates when designing CBC. After installing CBC, there is a menu item in the Start Menu named "Install extra templates". Click it and a few C# templates will be added.
<!--more-->

You can download CBC from http://cc.codegear.com/Item/24010.

The only problem is that these templates are manual, not auto.

In fact I am wondering why Delphi cannot generate basic xml comments for us. SharpDevelop has such a nice feature.

The usage of these templates are complex because the IDE does not work as I expect.

The templates do not have `///` in the beginning. I make it because after typing a line of xml comments and hitting the ENTER, BDS will lead you to the next line and append `///` automatically.

However, keywords after `///` will not be fired by SPACE or TAB, so you must use CTRL + J.

An example of using the templates is

1. type ///.
1. type sum or summ.
1. Hit CTRL + J, and the template "summary" is triggered.
1. After finishing this tag, hit ENTER.
1. The IDE adds /// for you.
1. Type re.
1. Hit CTRL + J, and choose remarks tag from the popped list.
1. Finish the remarks tag.
