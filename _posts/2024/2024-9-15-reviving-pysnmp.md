---
layout: post
title: "Reviving PySNMP: Modernizing SNMP for Python, 2022-2024"
description: "Discover the journey of reviving PySNMP, a crucial SNMP library, from its dormant state. This post reveals the technical challenges, strategic decisions, and collaborative efforts that brought PySNMP back to life, ensuring its compatibility with modern Python versions and enhancing its functionality for the community."
categories: [History, PySNMP]
tags: SNMP Python
excerpt_separator: <!--more-->
---

> I wrote about [PySNMP history here](https://www.pysnmp.com/history) before, but that article was more targeting the audience of PySNMP users. This time I want to share more interesting facts about how PySNMP was revived, bit by bit, and the technical decisions made by me and my team. Thus, it will be a long post, but I hope you will enjoy it.

SNMP (Simple Network Management Protocol) remains essential in the networking world, enabling network administrators to monitor and manage devices efficiently. One of the most popular Python libraries for SNMP, PySNMP, had fallen dormant. In this post, we detail our efforts to revive and modernize PySNMP, ensuring it remains a reliable tool for the Python community. Along the way, we'll explore technical challenges, lessons learned, and future goals.
<!--more-->

## The Road to PySNMP Revitalization

I evaluated quite a few SNMP libraries before creating my own \#SNMP in 2008. Therefore, I came across PySNMP and was impressed by its documented feature set. However, I wasn't a Python developer at that time, and I didn't find PySNMP code a good reference for that C# project, so I didn't pay much attention to it.

\#SNMP Pro edition was the first commercial product created by my own company, LeXtudio Inc. in 2013. And since then the team have been working with various clients to provide custom SNMP solutions. We noticed that such clients might use different SNMP libraries for different projects, so naturally sometimes they rely on Net-SNMP and PySNMP. So, we started to pay more attention to PySNMP, especially when we tried to add new features to \#SNMP Pro.

## Initial Challenges and Roadblocks

Some client turned to us for help because they were not able to get PySNMP to work as expected a few years ago. That was the time we noticed Ilya Etingof stopped his work on PySNMP, and the project was in a state of limbo. We weren't ready to help them out, so we turned down the request.

However, the situation didn't change much in the following years, and we received more support inquiries about PySNMP. Therefore, in 2022, we decided to take a closer look at PySNMP again and evaluate if we could help.

Of course, it took us no time to find existing forks from a few parties. It would be interesting if my team were able to work with them to bring PySNMP back to life. But it turned out that the forks were created for different purposes, and none of their maintainers were interested in reviving PySNMP as a whole.

So, we decided to fork PySNMP ourselves and started to work on it.

## Forging Ahead with PySNMP Development

In the last few weeks of 2022, our goal was just to ship our own packages based on existing patches. We didn't want to introduce any breaking changes, so we just cherry-picked some patches from existing forks and shipped our own PySNMP 5.0 releases.

I think it was a good start, especially after we launched [the new PySNMP.com homepage](https://pysnmp.com). Not only we were able to help a few clients to get their projects back on track, but we knew that the community were watching.

One year ago in Sep 2023, we were funded to improve PySNMP test coverage, so new test cases were added from time to time. Switching to the local test agent/manager in Feb 2024 was a big step forward, and we were able to catch a few bugs that were missed before.

## Tackling Dependencies: The PyASN.1 Story

Because PyASN.1 was handed over to a different team, my team had to make sure PySNMP and PyASN.1 were in sync. It was a bit challenging because PyASN.1 might simply break PySNMP.

The very first incident happened when PyASN.1 0.5.0 was out. The breaking change was in fact authored by Ilya himself, but his fix on PySNMP was on a different branch. While my team cherry-picked the fix, the new PyASN.1 maintainers also made some changes on their side for users of the legacy releases.

Recently PyASN.1 0.6.1 was released and broke PySNMP a second time, where they removed some compatibility shims. My team were able to immediately ship patched PySNMP releases.

Breaking changes might sound like a bad thing, but in fact they are good for PySNMP, because users of old releases have been forced to learn what are the new releases. For many of them, that's also the moment they know we are the new maintainers.

## Our Vision for the Future

The 6.0 releases were the first ones that we intentionally brought a lot of breaking changes. We wanted to prepare for the new Python 3.12 release, so deleting legacy bits like asyncore naturally would affect PySNMP users.

We quickly realized that most of the code was built around asyncore as the default I/O framework, while its asyncio related code was limited and drastically different. The documentation and examples were also outdated. After removing asyncore and making asyncio the default, we anticipated significant breaking changes. This required faster, more frequent releases to address the gaps.

This is exactly the moment that we were approached by the Home Assistant team and the OpenStack team for help. Things became stable around the 6.0.11 release.

## Tackling Dependencies: The PySMI Story

PySMI was another dependency that we had to take care of.

We didn't realize that PySMI had some breaking changes till we shipped PySMI 1.3.0 that broke PySNMP 6.0. But luckily we were able to ship PySNMP 6.1 to match the latest PySMI.

Around the same time period, my team were able to review almost every useful PySMI/PySNMP commits from the past and prepare a list for future integration if some of them were not yet cherry-picked.

## Our Vision for the Future, Continued

The last big change in 6.x phase was the removal of all sync wrappers in PySNMP 6.2. We knew that some users were still using sync wrappers, but we didn't want to carry on the unnecessary burden.

We were in a rush to work on 6.x releases, so we left quite a few things to 7.x releases,

* PEP 8 compliance
* SMI/MIB API change
* v1arch/v3arch API change

To surprise you a bit, those changes were actually done by Ilya a few years ago for his unfinished 5.0 release. Though it might look like simple tasks that we just cherry-picked them and shipped in PySNMP 7.0, in fact we had to be very careful to make sure they didn't break anything. Thanks to all test cases created along the way, we were confident during the development cycle.

One thing you might notice is that we didn't take al changes Ilya made on SMI/MIB API. That's because he chose a wrong path to implement asynchronous MIB API, which heavily depended on recursive calls. With our small but reliable unit test cases, we were able to quickly identify/analyze the issues and decided to take a different path.

We believed the above are enough changes in 7.0 releases, so a few other changes were introduced in 7.1 releases,

* DNS queries are now done asynchronously
* nextCmd/bulkCmd/walkCmd/bulkWalkCmd are redesigned

Noticeably, we couldn't fully understand the strange design of nextCmd/bulkCmd in the past, because they didn't much the simple GET NEXT or GET BULK packets, but more like WALK or BULK WALL operations. That's why we added walkCmd/bulkWalkCmd in release 6.0.7 to make the design more clear.

When we worked on recent 7.1 releases, we found more issues in Ilya's design that he wanted to support certain special cases well but in the meantime make the common cases more complicated. We rather simplified the design and left the special case handling to end users.

## Ending

We appreciate all the support we got from our generous clients funding the journey. Together we were able to bring PySNMP back to life, and we are proud of what we have achieved so far.

Thanks to all open source projects who migrated to our forks and helped us to test out the new releases. It was a great pleasure to work with them. It's their trust that made us confident to ship new releases and finally gain ownership of Ilya's PyPI packages via the PEP 541 process.

We are always seeking community input and contributions to PySNMP. Moving forward, we plan to continue refining the core code, adding support for modern Python versions, and improving documentation. If you're interested in contributing or testing, feel free to [join us on GitHub](https://github.com/lextudio/pysnmp) or reach out directly.

The road to reviving PySNMP has been long, but it's only the beginning. With continued community engagement and contributions, we're committed to keeping PySNMP at the forefront of SNMP solutions in the Python ecosystem. We look forward to tackling the challenges ahead and sharing more milestones with the community.
