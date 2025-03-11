---
layout: post
title: "CatPaw Rumors: We Are Truly Mono Ready Part II"
description: "This post is about #SNMP Mono support"
tags: SNMP Mono
permalink: /catpaw-rumors-we-are-truly-mono-ready-part-ii-ac852a26aa5
excerpt_separator: <!--more-->
---
This is a MoMA scan report on snmpd.exe. Though there are so many issues reported, in fact this SNMP agent runs fine on both Windows/.NET and openSUSE/Mono.
<!--more-->

| Assembly | Version | Missing | Not Implemented | Todo | P/Invoke |
| -------- | ------- | ------- | --------------- | ---- | -------- |
| Crad.Windows.Forms.Actions.dll | 1.1.1.0 | 0 | 0 | 0 | 0 |
| log4net.dll | 1.2.10.0 | 0 | 0 | 6 | 3 |
| Microsoft.Practices.ServiceLocation.dll | 1.0.0.0 | 0 | 0 | 0 | 0 |
| Microsoft.Practices.Unity.Configuration.dll | 2.0.315.0 | 0 | 0 | 0 | 0 |
| Microsoft.Practices.Unity.dll | 2.0.315.0 | 0 | 0 | 21 | 0 |
| Mono.Posix.dll | 2.0.0.0 | 0 | 0 | 0 | 407 |
| SharpSnmpLib.Controls.dll | 5.0.10419.0 | 0 | 0 | 0 | 0 |
| SharpSnmpLib.dll | 5.0.10419.0 | 0 | 0 | 0 | 0 |
| snmpd.exe | 5.0.10419.2 | 0 | 0 | 0 | 1 |
| Total | | 0 | 0 | 27 | 411 |

Along our way to be Mono ready, the following Mono issues have been found and reported,

```
595552
Min
P5
openSUSE 11.2
monodevelop-bugs@lists.ximi…
NEW
IDE does not handle app.config in Visual Studio/SharpDevelop way
The workaround is to manually build using xbuild. I think when MD starts to use xbuild the issue is resolved automatically.

599488
Nor
P5
openSUSE 11.2
mono-bugs@lists.ximian.com
NEW
Why SocketException with ErrorCode == 10035 means Operation timed out? It breaks .NET compatibility
The workaround is to test whether Mono is in use and then check against 10035 or 10060.

599462
Nor
P5
openSUSE 11.2
mono-bugs@lists.ximian.com
NEW
System.NotSupportedException from System.Drawing.GDIPlus.CheckStatus (Status status) for #SNMP Agent
The workaround is to ignore the icon file for snmpd.exe main form.

599449
Nor
P5
openSUSE 11.2
mono-bugs@lists.ximian.com
NEW
"cannot be inferred from the usage" when compiling #SNMP
The workaround is to convert LINQ expression back to normal lines.

599486
Nor
P5
openSUSE 11.2
jankit@novell.com
NEW
xbuild does not honor extra tag
Well, at least MD or xbuild compiles the solution without any error. I just remember to build periodically from Windows to update the version numbers.

599454
Nor
P5
openSUSE 11.2
jankit@novell.com
NEW
xbuild cannot create folders
The workaround is to manually create those folders.
```
