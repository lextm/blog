---
layout: post
title: "#SNMP Pro: Recent Releases"
description: "This post would show you the recent releases of #SNMP Pro."
tags: SNMP
permalink: /snmp-pro-recent-releases-5e72c7973ba0
excerpt_separator: <!--more-->
---
You should notice that #SNMP Library is now releasing more frequent with minor releases in just a few months, such as 9.0.0, 9.0.1, 9.0.2, and today 9.0.3. To match such a new strategy, the Pro edition is also releasing more changes in the past few weeks, such as 1.1.2 and 1.1.3. Such a change we make is to increase transparency and deliver urgent bug fixes in a quicker way.
<!--more-->

## More About 1.1.2 Release
[Two annoying issues](https://github.com/lextm/sharpsnmppro-sample/milestone/1?closed=1) were addressed in 1.1.2 release.

First, we chose to utilize assistant OID names during OID extraction process, as the previous extraction code was not smart enough to handle out of order OID definitions.

Assume that the child definition `ieee8021TcMib` occurs firstly, and the parent definition `ieee802dot1mibs` comes secondly, the extraction code would create an assistant item `ieee802dot1_1` which works as a temporary parent for `ieee8021TcMib`.

``` asn
ieee8021TcMib MODULE-IDENTITY
DESCRIPTION
"Initial version."
::= { org ieee(111) standards-association-numbers-series-standards(2)
lan-man-stds(802) ieee802dot1(1) 1 1 }
ieee802dot1mibs OBJECT IDENTIFIER
::= { org ieee(111) standards-association-numbers-series-standards(2)
lan-man-stds(802) ieee802dot1(1) 1 }
```

Such an approach works, but with a price that this OID would have two names `ieee8021TcMib` and `ieee802dot1_1`, while the latter does not come from the documents.

In 1.1.2 release, a new approach is used, so such assistant items have gone forever.

We also changed how duplicate modules are handled. In the past, we accepted duplicate modules to be analyzed and always used the last module definition, which leads to more trouble than we thought. So now whenever duplicate modules are detected, the library simply reports an error, so the users can define how they would like to handle that.

## More About 1.1.3 Release

While 1.1.2 introduces some improvements, it also adds [an annoying bug](https://github.com/lextm/sharpsnmppro-sample/milestone/3?closed=1), where some exceptions are not properly handled.

1.1.3 fixes this bug.

## How to Get The Latest Release

As registered users, you should have already received the instructions on how to get the binaries.

If you do not yet see the mail, please write to our support team at support@lextudio.com.

Stay tuned as we are working hard on the next release 1.2.0.
