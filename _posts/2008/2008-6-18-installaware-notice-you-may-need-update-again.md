---
layout: post
title: "InstallAware Notice: You May Need Update Again"
description: This post talks about the new update for InstallAware 7.
tags: Windows
permalink: /installaware-notice-you-may-need-update-again-7c791c38190d
excerpt_separator: <!--more-->
---
I didn't notice that Microsoft has released MSI 4.5 engine until I received a notice mail from InstallAware. It was happy to get an InstallAware 7 Update for MSI 4.5.

However, when I used the update to build an new installer with MSi 4.5, several testers found that it didn't function right. On a VPC image, this new runtime even prevents our application from installing.

Last night before I left the office, I fired a bug report to IA. Oh, this morning I got a reply that a new update for MSI 4.5 was published. So my report worked!?

As I didn't see any announcement on IA blog, so I'd like to post here. If you meet the same issue like me with the MSI 4.5 update you downloaded, you may go to that link again to download the latest version whose MD5 hash is 816487e376ec5b68bd19a32c5b5d6c64.
<!--more-->