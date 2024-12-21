---
layout: post
title: "#SNMP Pro: Release 1.1 is Out"
description: "This post is to announce the release of #SNMP Pro 1.1."
tags: SNMP
permalink: /snmp-pro-release-1-1-is-out-11ddf223eaa7
excerpt_separator: <!--more-->
---
You probably noticed that #SNMP Library has just been updated to 8.5 and released finally at NuGet.org.

Of course, #SNMP Pro has an important update too, which I announce at this moment. Yes, it is the 1.1 release of both the MIB Compiler Pro and SharpSnmpPro.Mib assembly.

The changes (compared to the initial release on Feb 3rd, 2014) are as below,
<!--more-->

## SharpSnmpPro.Mib Assembly

* Description, Reference, Status are added to IEntity.
* DescriptionFormatted extension method is added to IEntity.
* IObjectTypeMacro interface is added.
* Added SmiVersion enumeration.
* Removed AccessType enumeration.
* Changed DateAndTimeDecoder implementation.
* ISmiType interface is added.
* Performance boost and memory usage reduction by upgrading compiler engine.
* Fixed NameBit bug.
* GetLastType extension method is added to ISmiType.
* SearchResult.Definition can now be null.
* Counter32Type, Counter64Type, Gauge32Type, IpAddressType, TimeTicksType are added.
* Changed how NotResolvedException are created.

## #SNMP MIB Compiler Pro

1. New warnings

   * Revision related warnings are added.
   * Table/entry access warnings are added.

2. New errors

   * write-only now triggers an error.
   * SMI v1 and v2 incompatibility errors are added.
   * Table entry related errors are added.

Also note that unhandled exceptions are better caught in the compiler to avoid frequent crashes.

The online documentation at http://help.sharpsnmp.com is going to be updated very soon, due to some technical issues.

The offline version can be downloaded from Dropbox. Stay tuned.