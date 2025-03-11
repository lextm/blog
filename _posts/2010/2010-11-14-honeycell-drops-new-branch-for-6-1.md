---
layout: post
title: "HoneyCell Drops: New Branch for 6.1"
description: "This post is about the new 6.1 branch for #SNMP."
tags: SNMP
permalink: /honeycell-drops-new-branch-for-6-1-88e3742c0a3d
excerpt_separator: <!--more-->
---
We have a new release in plan, 6.1. It should be available some day in Dec or Jan I think (not yet determined).
<!--more-->

In order to make sure this is "purely" a bug fix release compared to previous ones, I started to use branching. A new branch named 6.1 was created, and it already has two change sets at this moment.

A bug was found when I worked on the default branch for 7.0. So the first change set was checked in last night. Today I also merged the changes on snmptrapd from default branch to 6.1 branch. Note that this is another nice and small sample to show how to construct SnmpEngine.

With SVN, managing branches can be slow and tough, but now everything is so easy now in Mercurial.
