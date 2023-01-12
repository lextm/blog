---
layout: post
title: "BigDipper Light: Authentication and Privacy Further"
description: "This post is about the authentication and privacy issues in #SNMP."
tags: SNMP
permalink: /bigdipper-light-authentication-and-privacy-further-86429d12a875
excerpt_separator: <!--more-->
---
Ivo reported a new issue recently, and it shows that #SNMP does not yet handle SNMP v3 REPORT message completely.

The technical details behind the issue can be found in RFC 3414.

https://www.rfc-editor.org/rfc/rfc3414
<!--more-->

In short, under some scenarios an SNMP agent sends back an AuthNoPriv mode REPORT message for an AuthPriv mode request. MessageFactory class in #SNMP could not handle such REPORT message correctly (both 6.0 and early 7.0 builds).

It is not hard to fix it, but it is not easy to find the most suitable fix. I tried at least two different ways, and the latest I think is the best, as it not only resolves the privacy side issue, but also enhances authentication side.

RFC 3414 has other items that I did not pay enough attention in the past, so there is still room to improve #SNMP RFC compliance.

Stay tuned.
