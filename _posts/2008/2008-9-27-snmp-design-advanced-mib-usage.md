---
layout: post
title: "#SNMP Design: Advanced MIB Usage"
description: "This post talks about advanced MIB usage in #SNMP Library."
tags: SNMP
permalink: /snmp-design-advanced-mib-usage-30a13924564f
excerpt_separator: <!--more-->
---
It was in July that I talked about this topic simply in this thread with Scott, "Whether MIB documents are mandatory". I did not have much time then, so the answer from me was quite simply and it missed a lot of details. Therefore, now I try to provide more information in this post.
<!--more-->

## MIB Document Content
I believe everyone that reads an SNMP book before knows that MIB documents contain manageable object definitions. Simply speaking, you can find what you can do with the device by analysing the documents carefully.

For example, in SNMPv2-MIB.txt there are several general objects defined, such as sysLocation. By reading DESCRIPTION sections of their definitions, you can get an idea what information these objects provide.

``` csharp
sysLocation OBJECT-TYPE
    SYNTAX DisplayString (SIZE (0..255))
    MAX-ACCESS read-write
    STATUS current
    DESCRIPTION

    "The physical location of this node (e.g., 'telephone
    closet, 3rd floor'). If the location is unknown, the
    value is the zero-length string."

    ::= { system 6 }
```

## Basic Usage on Manager Side
On manager side, it is usual to extract numerical forms of OID and use them in source code.
For example, during my first few experiments on SNMP I was the "human MIB parser" who provided the numbers used in source files. #SNMP 0.5 forced a lot of users to follow me because there was no MIB support then.

``` csharp
Variable test = new Variable(new ObjectIdentifier(new uint[] { 1, 3, 6, 1, 2, 1, 1, 1, 0 }));
Variable variable = Manager.Get(VersionCode.V1, new IPEndPoint(IPAddress.Parse(ip), 161), new OctetString("public"), new List() {test}, 5000)[0];
```

## Advanced Usage on Manager Side
It is rather difficult to understand the source code and maintain the numbers whenever the MIB documents are updated, which is a common case during private MIB development process where nobody can foresee the final document.

So as to make the MIB document alive and let it behave like a contract among team members, in later versions of #SNMP, textual OID support is added.

``` csharp
Variable test = new Variable(new ObjectIdentifier("SNMPv2-MIB::sysLocation"));
```

From then on, numbers can be replaced by ::. MIB documents are parsed so translation between textual form and numerical form can be achieved. The benefits are,

* numbers can be changed in MIB as long as the names remain the same.
* the source code with names now is more readable than with numbers.

## Usage on Agent Side (Coding)
In common practices, it is not necessary to set up a complete object repository for all objects in the MIB files on manager side because not all objects are required.

However, on agent side it is a must to host all objects in an inventory. Everything defined in the MIB documents must be present. Otherwise your work is not yet accomplished.

Therefore, agent developers must first decide which documents are going to be supported. Then they can set up an object inventory and fill it with all objects. At last, provide a facade to handle any incoming SNMP requests.

Other SNMP frameworks provide tools to generate an inventory structure out of a MIB document (yes, like CodeSmith). In this way you can make sure all objects are in the structure with predefined standard behaviours defined. All you need to do is fill in the blank and customize the behaviours with extra code.

Sadly at this moment, #SNMP does not yet have plan on such tools. So it is the developers' role to design the inventory from scratch.
