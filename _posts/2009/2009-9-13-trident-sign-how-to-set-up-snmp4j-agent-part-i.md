---
layout: post
title: "Trident Sign: How to Set Up SNMP4J Agent, Part 1"
description: "This post is about how to set up SNMP4J Agent."
tags: SNMP
permalink: /trident-sign-how-to-set-up-snmp4j-agent-part-1-9354ddb8868a
excerpt_separator: <!--more-->
---
To enrich #SNMP v3 support, I am going to use snmp4j agent. But due to lack of documentation for me, a Java blind, I have to learn about it bit by bit.
<!--more-->

Below is a summary of my steps,

1. Download and install Java runtime from http://java.com. I install it to C:\Program Files (x86)\Java\jre6.
1. Configure JAVA_HOME like this (http://wso2.org/project/wsas/java/1.1/docs/setting-java-home.html) and add C:\Program Files (x86)\Java\jre6\bin to PATH.
1. Download snmp4j agent ZIP package from here (http://snmp4j.org/html/download.html). I use 1.3.1 version.
1. Unzip this package and copy all JARs from `lib` to `dist\lib`.
1. Create a launch.bat in `dist\lib` and use the following content.
1. Execute this batch file to launch the agent. To stop it, simply close the console window.

Batch file content is,

``` text
java -cp SNMP4J-agent.jar;SNMP4J.jar;log4j-1.2.9.jar org.snmp4j.agent.test.TestAgent
pause
```

I will spend more time on this agent and post future findings later.
