---
layout: post
title: "BigDipper Light: What Is Next"
description: "This post is about the next release of #SNMP."
tags: SNMP
permalink: /bigdipper-light-what-is-next-12a1945bccb1
excerpt_separator: <!--more-->
---
Recently I submitted several new change sets to the repository, http://code.google.com/p/sharpsnmplib/source/list, which improves #SNMP compatibility with more SNMP devices.

The changes do not make their way to our 7.0 release, simply because I was not fully confident that I could make such changes. The technical details are provided below if you are interested in,
<!--more-->

## Long Time Issue

Everybody knows that SNMP is old. Since it is so old that many devices out there in the network may run an SNMP application which is too old to comply to latest SNMP standards/best practice. For example, a strange issue was reported here.

And our troubleshooting shows the problem was caused by the device itself. When this device decides to encode SNMP information, it generates the length bytes in a correct, but not optimal way (it does not generated the fewest bytes).

This kind of encoding way breaks #SNMP, as it can properly decode the message body. But when it tries to reconstruct the message for hash verification, #SNMP always generates the fewest bytes, which leads to the mismatch.

## Temp Patch

Tom Rickards (aka trickdev) contributed a patch eight months ago. In that patch, he tried to use another hash verification way to reconstruct the message body. This patch was merged into the code base, in change set 8dde882e9c62.

The disadvantage of this approach is that the new hash verification code does not match the original interface.

## Permanent Fix

Recently I created a new branch from change set 7843d32bbfd5 (the one just before 8dde882e9c62), where I revised all classes derived from ISnmpData to hold the original length bytes if they are constructed from a byte stream. This makes the reconstruction result exactly the same as the one generated from Tom's approach.

Therefore, using this approach, Tom's patch is no longer necessary, and we fixed the issue in a cleaner way.

I worked hard to back port this new fix to our main branch, and now it is present in the repository for you to play with. It is not yet time to say at what time I will cut a new release (7.5?), but we know now even after 7.0, we still have a lot to do for #SNMP.

Stay tuned.
