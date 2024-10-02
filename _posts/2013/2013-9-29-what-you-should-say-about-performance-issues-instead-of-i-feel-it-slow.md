---
layout: post
title: "What You Should Say About Performance Issues Instead of 'I Feel It Slow'"
description: "This post talks about how to discuss performance issues with others with clear descriptions."
tags: IIS
permalink: /what-you-should-say-about-performance-issues-instead-of-i-feel-it-slow-313b0e871aad
excerpt_separator: <!--more-->
---
It is very often that we see people describe performance issues they meet with similar phrases such as "I feel it slow". Well, this is rather a bad way to discuss with others about web site performance. Then what should we do when a performance issue occurs? At least you should do the following.
<!--more-->

## The Measurement

Slow or not is measurable, but it is a simple fact that many guys neglect. Also there are people who know a lot about web site and web server, but too little about the network.

Generally speaking, the time taken for a web page to be displayed inside a browser tab is composed of three major portions,

* Client: The time used by web browser to send out HTTP requests (note that there are usually multiple requests), receive responses, render elements and execute scripts.
* Server: The time used by web server to handle HTTP requests.
* Wire: The time used by proxy servers, gateways, packet filters/firewalls, and so on.

When something is slow, please make sure you carefully measure each portions and break down the slowness to smaller pieces.

## Check the Right Logs and Use the Right Tools

To perform the slowness breakdown, one typical attempt is to capture network packets on both the client and the server side. Either Wireshark or Network Monitor can be used (Wireshark is more popular as it supports more OS platforms). This should be set as the initial step every time you need to analyze such issues.

If the time spent on the server side is significant, you should check server side log files to see why web server handles such requests slower than imagined. For IIS, web site log files have a field called time-taken from which you can confirm the total time used for IIS to handle a request. Since IIS uses a pipeline (of multiple IIS extensions and modules) to process incoming requests, you can further break down the time consumption by using failed request tracking (for IIS 7 and above), or ETW tracing (IIS 6). After locating the suspicious module, it is your task to find out who developed it and go after that guy.

If the time spent on the browser side is significant, you have to check the browser log. All browser vendors have their own utilities to troubleshoot such issues (IE, Firefox and Chrome for example), and you should check the vendor information and move on.

The most difficult case is that when you find the time spent on the wire is significant. Only if the client and server is in a corporate network you can involve the network operation guys of that firm to assist, as in other cases the wire might go through the Internet which is very difficult to analyze and optimize. We see CDN and similar techniques have been developed to remedy some typical performance issues over the Internet, but we could not yet guarantee that all such problems can be resolved in a similar or cost effective way.

## Conclusion

Let it be short so that next time you won't depend on your feeling. To begin discussion on a performance issue, please collect proper data first. Thanks.
