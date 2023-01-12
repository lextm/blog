---
layout: post
title: "#SNMP Design: Incomplete Agent Demo"
description: "This post is about how to create a simple but incomplete SNMP agent."
tags: SNMP
permalink: /snmp-design-incomplete-agent-demo-5550acc8f1e4
excerpt_separator: <!--more-->
---

> Update: This post is obsolete. For #SNMP 6+, please read [this new post]({% post_url 2010/2010-11-14-honeycell-drops-snmp-pipeline-and-our-agent-demo %}).

I started to increase agent side support in #SNMP, but soon I found that I could not do that fast. It is really a big topic. But I owe everyone who voted on the poll a detailed post, so here comes it.

<!--more-->

I am now guiding you to create a WinForms application that can simply handle one SNMP request as an SNMP agent. You may follow the steps to see how many pieces are still missing in the map. By the way, if you are interested in this field and want to contribute, drop me a comment so I can contact you.

## Project Initiated

Create a new WinForms application called AgentDemo in Visual Studio or SharpDevelop.

Then add #SNMP library project into this solution.

Now you can add a project reference in AgentDemo to SharpSnmpLib.

## Basic GUI Setup

If you take a look at the Toolbox at this moment, you can see three new components.

Please drag the Agent component onto your Form.

Also you need to add two buttons like this.

So the simplest UI is done.

## Simplest Code

So now let's see how to bind event handlers. The Start button must do this,

``` csharp
private void btnStart_Click(object sender, EventArgs e)
{
    agent1.Start(161);
}
```

while the Stop button does this,

``` csharp
private void btnStop_Click(object sender, EventArgs e)
{
    agent1.Stop();
}
```

Note: If you don't explicitly specify the port number in Agent.Start, 161 will be used by default.

And the hardest part is the agent related. Thus, I handle the GET requests here for demo.

This is the simplest GET request handler I can think of,

``` csharp
private void agent1_GetRequestReceived(object sender, Lextm.SharpSnmpLib.GetRequestReceivedEventArgs e)
{
    GetRequestMessage message = e.Request;
    MessageBox.Show("A request is received from " + e.Sender.Address);
}
```

## Why Not Response?

Now I will show you how to response to a simple request. Modify GetRequestReceived handler like this,

``` csharp
private void agent1_GetRequestReceived(object sender, Lextm.SharpSnmpLib.GetRequestReceivedEventArgs e)
{
    GetRequestMessage message = e.Request;
    // you may validate message version number and/or community name here.
    if (message.Variables.Count != 1)
    {
        return;
    }

    if (message.Variables[0].Id != sysDescr)
    {
        return;
    }

    GetResponseMessage response = new GetResponseMessage(message.SequenceNumber, message.Version, e.Sender.Address, message.Community, new List() { new Variable(sysDescr, new OctetString("Test Description")) });
    response.Send(e.Sender.Port);
}

private static ObjectIdentifier sysDescr = new ObjectIdentifier("1.3.6.1.2.1.1.1.0");
```

In this way, AgentDemo.exe should be able to reply simple requests about its system description.

You can also send out INFORM or TRAP messages by calling Agent.Send\* static methods to SNMP managers.

Note: You may find this code cannot compile even if latest source code is used. Sorry, you have to add the following code to GetRequestMessage.cs,

``` csharp
///
/// Version.
///
public VersionCode Version
{
    get { return _version; }
}

///
/// Sequence number.
///
public int SequenceNumber
{
    get { return _sequenceNumber; }
}

///
/// Community name.
///
public OctetString Community
{
    get { return _community; }
}
```

## The Problems

Although this small demo works, I cannot say #SNMP can be used to develop agents. There are serious problems,

- There is no built-in support to store managed objects in #SNMP, so you have to store them yourself.
- It is not easy to query these objects and generate proper response messages. You have to write a lot of code to realize the queries and message generation.
- If you need to manage a lot of objects, there is no support to generate code from MIB documents for you like other commercial libraries.

It takes us a long way to get here (wow, six months has passed), but more work is ahead.
