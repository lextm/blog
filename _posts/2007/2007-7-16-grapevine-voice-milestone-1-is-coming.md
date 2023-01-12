---
layout: post
title: "GrapeVine Voice: Milestone 1 is Coming"
description: "This post describes about the changes in GrapeVine M1."
tags: Code-Beautifier-Collection Delphi
permalink: /grapevine-voice-milestone-1-is-coming-14b901b93fe9
excerpt_separator: <!--more-->
---

Most Vista changes are not hard to overcome. After some digging, there are only two issues left. One is that Expert Manager cannot delete a registry because of UAC or some other security feature of Vista. And the other is a new naming schema for CBC GrapeVine packages.

For the latter, I have just made up my mind. Every package will have a prefix `gv` which stands for GrapeVine. In this way, they can be distinguished from older versions.

I would solve the first problem at first then update InDate code to conform to the new naming rules.

I have uploaded another Preview version to GForge here. It is still a Preview, but much better than last one.

Stay tuned.

(Updated: UAC compliant will be achieved easily if a manifest file is used. Inno Setup creates Vista-compatible installers in this way, too. You can use Kenny Kerr's Manifest View 1.0 to see inside them.)
<!--more-->