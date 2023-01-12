---
layout: post
title: "#SNMP Design: Update on TwinTower Release Candidate"
description: "This post talks about the update on TwinTower release candidate."
tags: SNMP
permalink: /snmp-design-update-on-twintower-release-candidate-f2f4a2b53714
excerpt_separator: <!--more-->
---

Steve and I have worked hard to prepare a TwinTower Release Candidate lately (and that's why Steve came across [the Zero Puzzle]({% post_url 2008/2008-9-6-snmp-design-the-puzzle-of-zero %}) and [I fixed it completely]({% post_url 2008/2008-9-8-snmp-design-solving-the-zero-puzzle %}) yesterday). However, there is more to do on the browser side than on the library side, so I am now considering such a plan to release two candidates before the final release,

<!--more-->

## Candidate One

This candidate contains all bug fixes and new features since last release on the library side. The changes includes,

1. most v2c support added.
1. all known bugs scheduled for TwinTower fixed.
1. FxCop, Gendarme, and StyleCop high priority items cleaned up.

- to be released this weekend

## Candidate Two

This candidate contains all changes in Candidate One and a basic MIB browser.

- to be released once Steve check in the last bit of the basic browser.

## Final Release

The final release should fix all bugs detected in Candidates.

- to be released after code review and refactoring.

Stay tuned.

(BTW, since CodeGear just released Delphi 2009, I am going to spend some time to upgrade GrapeVine for it, so TwinTower final release may be available in October).
