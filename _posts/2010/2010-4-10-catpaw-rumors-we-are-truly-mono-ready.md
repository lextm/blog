---
layout: post
title: "CatPaw Rumors: We Are Truly Mono Ready :)"
description: "This post is about the Mono support of #SNMP Library"
tags: SNMP
permalink: /catpaw-rumors-we-are-truly-mono-ready-7c2a1d07835d
excerpt_separator: <!--more-->
---
From the very beginning of this project, I tried to keep it compliant to both Microsoft .NET and Novell Mono. However, at that time I was a Ubuntu fan and Mono did not work fine on it. Therefore, I had to utilize MoMA on Windows to see which #SNMP pieces can be fully "supported". That's why I can announce the Library supports Mono at that time.
<!--more-->

Now we are truly Mono ready. I mean we can check out the source code to openSUSE Linux and build from there. I already know the command line tools work, as they are so simple to experience any problem. But MoMA reports our major tools (the Browser, Compiler, and Agent) are not Mono compliant due to third party dependencies. So is that true? Luckily the answer is "No."

In fact now I am sure our Agent works fine on openSUSE after only a few tunings. They are,

1. We must build the project TestAgent.csproj via xbuild command line tool. Due to a MonoDevelop bug I reported (http://bugzilla.novell.com/show_bug.cgi?id=595552), MD does not copy app.config over for you.

2. We have to change MainForm.cs a little bit to work around another Mono bug. It seems that Mono does not like the Icon file format, so I will report it later once I have a smaller sample to reproduce the issue.

3. We must run snmpd.exe as administrator (`root` in Linux term). I found I could not use `sudo mono snmpd.exe`. But if I executed `su` to enter root mode first, then I could execute `mono snmpd.exe` to launch our Agent. Otherwise, SocketException "access denied" will be raised as snmpd has no enough rights to monitor ports who numbers are less than 1024. (Refer to http://go-mono.com/forums/#nabble-td1497458).

This indicates the issues reported by MoMA on Microsoft Unity do not affect #SNMP Agent. I guess that's because we do not use those features.

The Browser and Compiler still fail on openSUSE, as DockPanel Suite is Windows dependent. Mono Invoke was announced a very long time ago, but now we see no news. Maybe that's because it is too huge to be implemented. Who knows.

Stay tuned.

(Updated: snmpd in the repository is now fully Mono/openSUSE compliant. We will keep updating it till release 5.0 is shipped. With a lite version of DPS, now the Browser and Compiler are also Mono ready.)
