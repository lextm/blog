---
layout: post
title: "Net-SNMP snmpd.exe Crash On Windows"
description: "This post is about Net-SNMP snmpd.exe crash on Windows and how to resolve it."
tags: SNMP Windows
permalink: /net-snmp-snmpd-exe-crash-on-windows-9d03bab1b105
excerpt_separator: <!--more-->
---
Well, there are already posts on the Internet about this issue, that snmpd.exe crashes on Windows. I am using Windows Vista SP2 and I also notice this issue.
<!--more-->

In Windows Event Log (Application category) it is too easy to locate the crash information,

(On a Chinese Windows Vista SP2 machine)
``` text
错误应用程序 snmpd.exe，版本 0.0.0.0，时间戳 0x4abf748e，错误模块 unknown，版本 0.0.0.0，时间戳 0x00000000，异常代码 0xc0000005，错误偏移量 0x00000000， 进程 ID 0x1a14，应用程序启动时间 0x01cbc2a468461494。
```

0xc0000005 means access violation, but it cannot tell you what is the root cause.

I was planning to troubleshoot it further, but suddenly I found this paragraph on OpenSSL site, http://www.slproweb.com/products/Win32OpenSSL.html

About OpenSSL 1.0.0: Today (May 4, 2010), the 1.0.0 builds are released. Finally. Developers can begin testing against it. Users should still consider this beta and upgrade ASAP. For most software, upgrading won't be an issue.

> If your SSL-enabled software works for you under 1.0.0, then great, if not, downgrade to 0.9.8n. We are now in a transitionary phase to the 1.0.0 series. Developers: In order to keep things simpler, 0.9.8n will be removed in a few months.

Therefore, I tried to uninstall OpenSSL 1.0.0c and install 0.9.8q instead.

Guess what? Yes, everything starts to work fine.

So if you plan to use Net-SNMP agent on Windows, remember that choosing a proper version of OpenSSL is what you should consider.

BTW, I have fired a bug report to OpenSSL guys, and hope they can find out a solution.
