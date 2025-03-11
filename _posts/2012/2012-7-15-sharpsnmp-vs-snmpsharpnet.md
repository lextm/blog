---
layout: post
title: "SharpSnmp vs. SnmpSharpNet"
description: "This post is about the similarity and difference between #SNMP and SnmpSharpNet."
tags: SNMP
permalink: /sharpsnmp-vs-snmpsharpnet-5fdce55232e7
excerpt_separator: <!--more-->
---

This post was based on my original answer to this Stack Overflow question,

http://stackoverflow.com/questions/10841613/sharpsnmp-vs-snmpsharpnet/10845234#10845234

I try to provide a few updates and also provide more details.

#SNMP homepage is at https://sharpsnmp.com.

SNMP#NET homepage is at http://snmpsharpnet.com.

<!--more-->

## The Beginning

[I started to work on #SNMP]({% post_url 2008/2008-4-27-announce-sharp-snmp-library-for-net %}) in April 2008, before leaving Cisco in September.

SNMP#NET was also started in 2008, as its very first release [on SF.net](http://sourceforge.net/projects/snmpsharpnet/files/snmpsharpnet/) was in Nov 2008.

milans and I decided to write the libraries in the same year, under the same LGPL license terms, which can be an interesting coincidence. Neither of us knew each other at that time, until [I found out his project in May 2009]({% post_url 2009/2009-5-1-trident-sign-another-open-source-snmp-library-via-c %}). After that I wrote to Milan and learnt [how to use snmp4j agent]({% post_url 2009/2009-9-13-trident-sign-how-to-set-up-snmp4j-agent-part-i %}).

Besides, #SNMP's SNMP v3 support was ported from SNMP#NET, where I avoided reinventing the wheels.

At that point I already noticed the huge differences between the two projects, so I did not expect any further integration and continued my efforts on #SNMP.

## The Differences on Design Principles

#SNMP was derived from Malcolm Crowe's research project, and I did some refactoring and enhancements so as to provide an easy-to-use API.

Since [I conducted a review]({% post_url 2007/2007-12-25-product-review-snmp-libraries-for-net-evaluation-report %}) on existing SNMP libraries a few months ago before my work on #SNMP, I already had a few ideas on what kind of API is "easy to use".

The final API design was inspired by Dart's PowerSNMP for .NET, but of course I used whatever I found convenient and did not plan to clone Dart's.

Therefore, if you have a chance to review all releases of #SNMP, you will see that it always tries to maintain simplicity on API side. Even if you plan to perform SNMP v3 operations or write an SNMP agent, you can just use a few lines of code once you understand how #SNMP works.

SNMP#NET seems to be heavily influenced by snmp4j,

http://snmpsharpnet.com/node/1

Personally I dislike that, though it may help a few Java developers to migrate their projects to C#/.NET, it does not make very good use of C# language and .NET platform. As I am kind of familiar with SNMP#NET's weakness, [I wrote some tip]({% post_url 2011/2011-2-2-a-tip-for-snmpsharpnet-users %}) about how to properly use it.

## The Differences on Project Management

milans and I have different backgrounds, so we chose different approaches to manage our projects, which is quite obvious if you watch both.

#SNMP started at CodePlex.com, and follows Test Driven Development from its day one. I tried to develop a large test suite along the way, and also checked in changes very frequently.

I also tried to put down my ideas on the development on my blog. The long term benefits I get from that is joyful. Every now and then I find it fun to refactor the code, to add new features, and perform reviews on the change sets, because of the good records I have kept. If you can track the evolution of your project, you will find the same.

However, SNMP#NET is on another extreme. From SNMP#NET I could not see any unit test suite. I don't know how it was tested. It just magically works, and is stable. And this project only releases source code snapshots with binaries. There is no public repository for it. Milan used to blog here,

http://www.snmpsharpnet.com/blog/3

But he haven't written a new post in the past two years.

## The Differences on API Richness

#SNMP started as a SNMP manager library initially, as that was what I knew about SNMP in early 2008. But [agent support]({% post_url 2008/2008-10-18-snmp-design-incomplete-agent-demo %}) appeared in late 2008. And this has been enhanced in 2010 with the [introduction of SNMP processing pipeline]({% post_url 2010/2010-11-14-honeycell-drops-snmp-pipeline-and-our-agent-demo %}).

Except that I wrote command line utilities (like the one provided by Net-SNMP), a MIB compiler and a MIB browser (similar to the one provided by MgSoft). The final piece is the SNMP agent (snmpd, similar to snmp4j test agent). All such sample projects demonstrate how to properly use #SNMP API. They evolve with the API over releases.

Noticeably, #SNMP has MIB document support (compiling MIB documents). It was developed manually in 2008, and this year I rewrote the whole MIB support using ANTLR engine.

SNMP#NET, though it has good small samples, does not have large scaled samples (no compiler, no browser and no agent). It also lacks of MIB support. It is still good for SNMP users if you only use basic SNMP operations. But once you require something beyond that, you will have to do it on your own.

## The Differences on Platform Support

#SNMP has been [tested on Mono and Linux]({% post_url 2010/2010-5-2-dockpanel-suite-tip-5-we-can-go-mono %}) for a few years now,

During these two years, many Mono bugs have been identified, reported, and resolved. I even resolved bugs in some of the dependencies (Crad's ActionList, and DockPanel Suite). My attempt of porting DPS to Mono finally inspires me to be a maintainer of it this year. The experience is fantastic, as I never imagined I could go this far.

There is no report on whether SNMP#NET can work on Mono. Personally I think it should work, as it is relatively simple, and fully managed.

## End

Fine. As I am the developer of #SNMP, this post must be biased, although I am trying hard to be objective. Therefore, I suggest you perform your own evaluation.

And hope you find [this post]({% post_url 2007/2007-12-25-product-review-snmp-libraries-for-net-evaluation-report %}) useful.
