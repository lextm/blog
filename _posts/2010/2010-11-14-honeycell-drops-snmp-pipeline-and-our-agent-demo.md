---
layout: post
title: "HoneyCell Drops: SNMP Pipeline And Our Agent Demo"
description: "This post is about #SNMP's agent side technical details."
tags: SNMP
permalink: /honeycell-drops-snmp-pipeline-and-our-agent-demo-89986da1a5da
excerpt_separator: <!--more-->
---

> A long time ago I wrote an agent demo for #SNMP. It is interesting to know how far we were away from a complete demo. You can still find [the post here]({% post_url 2008/2008-10-18-snmp-design-incomplete-agent-demo %}).
>
> More than two years passed and now we have 6.0 release out. How about a new post on our agent technical details? This one is for snmpd.

If this is the first time you download #SNMP source code, you will find that snmpd folder is named strangely. Well, our SNMP agent uses a UNIX name :)

When you open snmpd.csproj in Visual Studio (or another IDE), you should first check what are its references.

<!--more-->

## Dependencies

There are several references you should pay attention to,

- `SharpSnmpLib*.dll` are our #SNMP Library components.
- `*Unity*.dll` are Microsoft Unity Application Block components.

## IoC, Facade, and Pipeline

As Unity is used, all necessary construction is performed by it. We no longer need to construct an Agent object, because that class is too old to be used. We try to construct an SnmpEngine instead.

SnmpEngine is the facade that you should put on top. It is a very complex class that replaces our old Agent. To construct it, we need: an EngineGroup object, which contains all engine global objects; A Listener object, which monitors incoming SNMP message; An SnmpApplicationFactory, who manages the pipelines.

SnmpApplicationFactory creates new pipelines when its pipeline pool is full of busy pipelines. The objects we pass to its constructor finally goes into each pipeline as they are shared among them (at this moment).

A pipeline is in fact an SnmpApplication object. It has several processing phases and each phase utilizes a few helper classes, which you can extend.

An SNMP message captured by Listener will be packaged as an SnmpContext object. This context object is passed to the pipeline and processed in each phase to generate a correct response message.

## Pipeline in Details

Currently (in 6.0) we only have four phases in the pipeline,

- Authentication
- Request handler mapping
- Request handler executing
- Logging request

After phase 4, the pipeline is reused by SnmpApplicationFactory for future messages.

We may add an authorization phase to achieve user based authorization, but it is not yet designed and implemented.

### Authentication

Via app.config you can see how the primary membership provider (ComposedMembershipProvider) is created and injected into the pipeline. The request is checked by the provider and dropped if it does not contain a proper community name.

ComposedMembershipProvider is a special membership provider, who allows you to support different SNMP versions. If you only target a specific version, you can use the version specific provider as primary one.

### Request handler mapping

For authenticated message, in this phase it is verified again and mapped to a message handler.

Message handlers are injected to the pipeline, too. So you can analyze app.config to know how many handlers are there already, and how each registers its interested message (SNMP version and verb).

For example, GetV1MessageHandler is only interested in v1 GET messages, while GetMessageHandler in v2 and v3 GET messages.

Carefully configure the existing handlers, you can achieve different SNMP engine configurations, so as to meet different requirements.

### Request handler executing

Once a message handler is found for the message, in this phase the handler performs the requested operation and generate a response message.

You should notice that \*V1MessageHandler classes follow RFC 1157 specification to handle v1 messages, while other handler classes follow RFC 3416 to handle v2 and v3 messages.

### Logging request

In this phase the response message is sent back, while the logger logs the processing into log files.

## ObjectStore and ISnmpObject

When a handler tries to do a typical SNMP operation, it looks into the ObjectStore object to locate the specified object.

Currently we only have a few sample objects created, to test out the pipeline. You can find them under Lextm.SharpSnmpLib.Objects namespace.

If you want to write more objects, you can follow our sample ones.

ObjectStore is not yet thread safe, which will be improved in the future.

## The Last Words

You should take a look at MainForm.cs and read what extra lines are required to configure the SnmpEngine object, how to start and stop it.

As the sample is released under MIT license, you can feel free to use it as a starting point of your own SNMP agent.

Our browser sample also uses the pipeline to handle trap messages, and once you are familiar with snmpd, you can switch to it to learn how to construct a browser side pipeline accordingly.

The pipeline greatly enhances our message processing infrastructure, and you should spare some time to go through its current status.

A lot of improvements will be provided in the future to further enhance this useful design.

Stay tuned.
