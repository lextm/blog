---
layout: post
title: "CatPaw Rumors: Post Release Summary, Part II"
description: This post is about the command line utilities.
tags: SNMP
permalink: /catpaw-rumors-post-release-summary-part-ii-40534cb5326e
excerpt_separator: <!--more-->
---
Our agent, snmpd.exe, supports all three SNMP versions. Then how to get data from it?
<!--more-->

## SNMP v1 and v2c

The community strings for both GET and SET operations are the same, `public`.

## SNMP v3

Community names are obsolete, so snmpd.exe supports three users (to match three modes).

* `neither` is the user for noAuthNoPriv mode. If you use it, remember to use default authentication provider and default privacy provider.
* `auth` is the user for authNoPriv mode. It uses MD5 authentication provider whose phrase is `authentication`. Its privacy provider is still the default one.
* `privacy` is the user for authPriv mode. It uses MD5 authentication provider whose phrase is `authentication`, but its privacy provider is the DES privacy provider whose phrase is `privacyphrase`.

Now let's see if you are going to test out snmpd.exe using our command line tools what commands should be used.

## SNMPGET

For SNMP v1 and v2c, typical command is

snmpget -v=1 -c=public localhost 1.3.6.1.2.1.1.1.0

For SNMP v3, typical command is

snmpget -v=3 -l=authPriv -a=MD5 -A=authentication -x=DES -X=privacyphrase -u=privacy localhost 1.3.6.1.2.1.1.1.0

## SNMPSET

For SNMP v1 and v2c, typical command is

snmpset -v=1 -c=public localhost 1.3.6.1.2.1.1.6.0 s Shanghai

For SNMP v3, typical command is

snmpset -v=3 -l=authPriv -a=MD5 -A=authentication -x=DES -X=privacyphrase -u=privacy localhost 1.3.6.1.2.1.1.1.0 s Shanghai

## SNMPBULKGET

For SNMP v2c, typical command is

snmpbulkget -v=2 -c=public -Cr=10 localhost 1.3.6.1.2.1.1.1.0

For SNMP v3, typical command is

snmpbulkget -v=3 -l=authPriv -a=MD5 -A=authentication -x=DES -X=privacyphrase -u=privacy -Cr=10 localhost 1.3.6.1.2.1.1.1.0

## SNMPGETNEXT

For SNMP v1 and v2c, typical command is

snmpgetnext -v=1 -c=public localhost 1.3.6.1.2.1.1.1.0

For SNMP v3, typical command is

snmpgetnext -v=3 -l=authPriv -a=MD5 -A=authentication -x=DES -X=privacyphrase -u=privacy localhost 1.3.6.1.2.1.1.1.0

## SNMPTRANSLATE
Typical command is

snmptranslate 1.3.6.1.2.1.1.1.0

## SNMPWALK

For SNMP v1, typical command is

snmpwalk -v=1 -c=public -m=subtree localhost 1.3.6.1.2.1.1

For SNMP v2c, typical command is

snmpwalk -v=2 -c=public -Cr=10 -m=subtree localhost 1.3.6.1.2.1.1

For SNMP v3, typical command is

snmpwalk -v=3 -l=authPriv -a=MD5 -A=authentication -x=DES -X=privacyphrase -u=privacy -Cr=10 -m=subtree localhost 1.3.6.1.2.1.1

(Update: Two more bugs were found and fixed during the authoring of this article. So we will refresh CatPaw again, and it should be 5.2.)
