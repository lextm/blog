---
layout: post
title: "CatPaw Rumors: Release Notes for 5.0 Release"
description: This post is about the release notes for 5.0 release.
tags: SNMP
permalink: /catpaw-rumors-release-notes-for-5-0-release-d51fb1c07c1b
excerpt_separator: <!--more-->
---
We did analysis on #SNMP 4.0 before. This post is the latest one for 5.0.
<!--more-->

## A view of the work achieved

``` sql
SELECT METHODS WHERE CodeWasChanged OR WasAdded
```

The codebase keeps evolves fast, and the picture shows a lot.

You can see a lot of highlighted areas, because

1. We migrated to Visual Studio 2010, so many generated code has been changed.
1. We changed a lot of GUI code in order to support Mono/openSUSE.
1. Agent side SNMP v3 support introduces many underlying changes in the Library.
1. Browser side SNMP v3 support introduces a few changes in itself.

## New Core Public Types

``` sql
SELECT TYPES FROM ASSEMBLIES "SharpSnmpLib","SharpSnmpLib.Controls", "SharpSnmpLib.Mib"
WHERE IsPublic AND WasAdded
```

Only three new types are introduced in 5.0,

* MalformedMessage: It is used to represent an SNMP v3 message received by the listener, which cannot be decrypted successfully due to several reasons.
* DecryptionException: An exception raised when an SNMP v3 message cannot be decrypted successfully.
* ListenerBinding: We introduce this class, so you can ask a Listener class to monitor on several IP address:port number bindings.

## New Assemblies

``` sql
SELECT ASSEMBLIES WHERE WasAdded
```

Only one assembly is added to our binary release package. That is snmptranslate, a utility to show how to use compiled MIB documents to do OID translation.

## New Public Types

``` sql
SELECT TYPES WHERE WasAdded AND IsPublic
```

We have a few new types here except for the three mentioned above,

* OutputPanelAppender: This is a custom log4net appender used in the Browser and the Compiler. It logs all necessary information into the output panel.
* RollingFileAppender: This is a custom log4net rolling file appender that outputs log file names in IIS similar pattern.

## Rambling

Our biggest changes are,

1. The Agent and the Browser now support SNMP v3.
1. The Agent, the Browser and the Compiler supports both .NET/Windows and Mono/openSUSE now.
1. VB.NET samples are added.

## Breaking Changes

Removed types are,

* BitString
* Bool
* GeneralString
* Real

Moved types are,

* ISnmpMessage
* IEntity
* IDefinition
* IModule
* IObjectRegistry
* IObjectTree
* SearchResult
* DefinitionType
* IConstruct
