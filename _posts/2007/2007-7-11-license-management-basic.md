---
layout: post
title: "License Management Basic"
description: "This post describes how to develop a license management system for shareware."
tags: Code-Beautifier-Collection Delphi
permalink: /license-management-basic-e126ab09cb81
excerpt_separator: <!--more-->
---

For shareware developers, it is reasonable to develop sort of license management system, aka a license generator for internal use and a license verification module inside your software.

It seems to be a lot of work but the logic is simple,

1. Get some kind of ID from your user. Network adapter MAC address was once the best choice. And now HDD serial number is preferred. As a matter of facts, you can combine them to generate a foot print for one computer.
1. Encrypt the ID to a license file.
1. Distribute the license.
1. Add a module in your software to verify the license.

Although all kinds of protection can be cracked, you can still gain some money from loyal users.

For Code Beautifier Collection users, there would never be license management system issues. Why? It is open source.

Isn't it wonder?
<!--more-->