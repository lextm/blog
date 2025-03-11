---
layout: post
title: "BigDipper Light: First Asynchronous Sample"
description: "This post is about the first asynchronous sample for Sharp SNMP Library."
tags: SNMP
permalink: /bigdipper-light-first-asynchronous-sample-cb5b4cb15dfd
excerpt_separator: <!--more-->
---
Microsoft invents a series of patterns for .NET asynchronous API design. However, no every pattern meet all requirements. For #SNMP, currently the Begin/End pattern is still the most suitable as it can be used in extension methods.
<!--more-->

Today I built the first sample for our asynchronous API and soon detected a few issues. Luckily the issues were resolved in our latest change set and below is the sample code,

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
            message.BeginGetResponse(endpoint,
                new UserRegistry(),
                endpoint.GetSocket(),
                ar => {
                    var response = message.EndGetResponse(ar);
                    Console.WriteLine(response);
            });
            Console.Read();
        }
    }
}
```
