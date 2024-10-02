---
layout: post
title: "#SNMP Design: 3 MIB Files More"
description: This post talks about how I parse more MIB files.
tags: SNMP
permalink: /snmp-design-3-mib-files-more-c69206fb3006
excerpt_separator: <!--more-->
---
After reading Wikipedia, I kind of understand what is a yylexer. However, I am still going on my own lexer. I am sure if I keep refactoring down the road, I may achieve something similar to a standard yylexer.

It is quite funny to develop a lexer because it requires so many algorithms that I must pay attention to. Luckily again I have TDD besides, so every time I change an algorithm somewhere I know immediately what parts are broken, and what are OK.

Have to say there is so much that I need to learn bit by bit, but I can announce that three more MIB files are parsed correctly by my lexer. They are SNMPv2-TC, SNMPv2-CONF, SNMPv2-MIB. So now I have a lot more nodes in the tree right now.

Wish I can stabilize the code soon and publish a new version on CodePlex.com. Stay tuned.
<!--more-->
