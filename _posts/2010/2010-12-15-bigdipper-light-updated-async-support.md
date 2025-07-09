---
layout: post
title: "BigDipper Light: Updated Async Support"
description: "This post is about the updated async support in #SNMP."
tags: SNMP
permalink: /bigdipper-light-updated-async-support-76d3c950066e
excerpt_separator: <!--more-->
---
Starting from our latest change set, you need to provide one more argument to BeginGetResponse. That was the missing piece, state object.

As state object is a requirement of Microsoft .NET asynchronous pattern, now I can announce that #SNMP fully supports it. :)
<!--more-->

Below is the updated sample code, which simply passes null as state object.

``` csharp
using System;
using System.Collections.Generic;
using System.Net;
using Lextm.SharpSnmpLib;
using Lextm.SharpSnmpLib.Messaging;
using Lextm.SharpSnmpLib.Security;

namespace TestAsyncGet
{
    class Program
    {
        static void Main(string[] args)
        {
            GetRequestMessage message = new GetRequestMessage(0,
                VersionCode.V1,
                new OctetString("public"),
                new List<Variable> {new Variable(new ObjectIdentifier("1.3.6.1.1.1.0"))});
            var endpoint = new IPEndPoint(IPAddress.Loopback, 161);
                message.BeginGetResponse(endpoint, new UserRegistry(),endpoint.GetSocket(),
                ar => {
                    var response = message.EndGetResponse(ar);
                    Console.WriteLine(response);
                }, null);
            Console.Read();
        }
    }
}
```