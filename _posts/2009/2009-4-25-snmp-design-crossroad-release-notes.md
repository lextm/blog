---
layout: post
title: "#SNMP Design: CrossRoad Release Notes"
description: "This post is the release notes of CrossRoad release."
tags: SNMP
permalink: /snmp-design-crossroad-release-notes-2deb83b7318f
excerpt_separator: <!--more-->
---
> Last release is TwinTower 1.5 on Jan 17.

This release takes more than three months and please grab a copy from here,
<!--more-->

It contains the following changes (bug fixes are not listed, so please check our issue tracker for information):

1. \* browser and compiler are now under MIT license.
1. \* SnmpDataFactory is now DataFactory.
1. \- Silverlight port is obsolete due to too many missing things in SL2.
1. \+ TraceSource is used for logging.
1. \+ new constructors added in ISnmpData derived classes.
1. \* ISnmpMessage is no longer derived from ISnmpPdu.
1. \- ToBytes method in ISnmpData derived classes are now obsolete.
1. \- TypeCode is removed from ISnmpMessage.
1. \+ Unity is used in browser and compiler.
1. \+ Objects property is added in Manager.
1. \* table OID validation process is disabled temporarily.
1. \+ notification panel is added in browser.
1. \* sample projects are improved.
1. \+ #SNMP MIB compiler is added and enhanced.
1. \+ Listener component is added.
1. \- TrapListener component is obsolete.
1. \* API changes are introduced to match RFC 1448.
1. \+ walk operation now makes use of GET BULK for SNMP v2 calls.
1. \+ command line version of SNMP utilities are added, such as snmpget, snmpset, and snmpgetnext.
1. \* SharpSnmpLib.dll is split to three parts: SharpSnmpLib.dll, SharpSnmpLib.Mib.dll, and SharpSnmpLib.Controls.dll.
1. \+ Discoverer component is added.
1. \+ IP v6 support is added and tested.
1. \+ MS Help 2 version of class references is shipped.
1. \* Many patches from Chris are merged so as to tune performance.
There must be a few items I missed. If you meet any incompatible issues (from 1.5 to 2.0), please feel free to let me know via our discussion board.

\+ for new features
\* for changed features
\- for obsolete or removed features

## Notice:

Obsolete items are to be removed post this release. So please follow the advice to move away from them.

