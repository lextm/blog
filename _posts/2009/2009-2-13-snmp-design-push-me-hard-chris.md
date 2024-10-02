---
layout: post
title: "#SNMP Design: Push Me Hard, Chris"
description: "This post is dedicated to Chris, who pushed me really hard this week to implement a few new features."
tags: SNMP
permalink: /snmp-design-push-me-hard-chris-bddd86e2dc4
excerpt_separator: <!--more-->
---
> This post is dedicated to Chris, who pushed me really hard this week.

Well, it is our luck to have Chris on board. He started to send me his ideas about #SNMP earlier this week via emails and kind of flooded my mail box. :) Therefore, I decided to publish some key points with you now so that you can begin your imagination.
<!--more-->

## Socket Sharing
If you still have old versions of #SNMP at hand, you will notice that ISnmpMessage derived classes are also IDisposable. Why? Socket objects were shared at object level, so if you sent such a message several times, no new socket objects were created.

I removed such sharing later when I decided to get rid of IDisposable. But what I did not realize is that this removal of shared sockets hurts performance significantly.

Now Chris points out that and tests on a prototyped implementation. His test results reveal that if we can share a socket object during a normal WALK operation (which consists of several GET NEXT operation under the hood), we improve the performance a lot.

We shall work on this topic immediately in order to work out a convenient implementation in the library. But I really want to make this as transparent as possible. It would be perfect if we can avoid API changes.

## Obsolete Items
Sure that we have a lot of obsolete items at hand. Chris suggests that we remove some of them at a certain time. Now my plan is to remove most obsolete items after TwinTower Refresh.

However, there are still items that hard to remove, such as ToBytes in low levels and some obsolete constructors only used in unit tests. We should leave them along for a longer term.

## Late Initialization and Deferred Calculation

There are a few methods in #SNMP generating the same bytes for every calls. There are also a few constructors that store raw bytes from incoming packets where this bytes were never used again in the following process.

Such overheads hurt performance a lot because they consume extra resources but offer nothing worth that while.

We are going to improve in this area, as Chris already has his local versions running well.

## Release Build or Debug Build

I believe that most of you feel puzzled that when I release this library, a pdb file is aside. So is this a Debug build?

Chris provides some evidence lately, so I will do a research on that later. I know that I use Release build in the project settings but ask to generate a pdb file aside, but how it turn out to have some debugging specific attributes is surely a question.

## ObjectIdentifier Related

Well, we need to add a lot of helpers for this class.

## Others

* Asynchronous methods.
* Exceptions.
* A new Listener implementation.
* Regionerate.http://www.rauchy.net/regionerate/

I tried my best to answer Chris' questions, but I believe our discussion scheduled today should be very interesting. Looking forward to that.

After writing the first few paragraphs, I had a chance to chat with Patrick, another new team mate, for a few minutes. The next post will provide you more information. Stay tuned.
