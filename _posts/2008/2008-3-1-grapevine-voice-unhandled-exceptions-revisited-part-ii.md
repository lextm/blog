---
layout: post
title: "GrapeVine Voice: Unhandled Exceptions Revisited, Part II"
description: This post talks about how to handle unhandled exceptions.
tags: Code-Beautifier-Collection Delphi
permalink: /grapevine-voice-unhandled-exceptions-revisited-part-ii-c9972b3f8478
excerpt_separator: <!--more-->
---
This is a customized exception dialogue I wrote based on Vitaly Zayko's UnhandledExDlgForm. I did not replace UnhandledExceptionManager.dll because Vitaly's implementation cannot work well on Windows Vista (the exception is caught by Vista instead of Vitaly's class).

http://www.codeproject.com/KB/exception/UnhandledExceptionClass.aspx

Compared to original exception dialogue, this customisation allows users to send reports to me. If Send Error Report button is pressed, then an email will be generated.
<!--more-->

To summarize, there are several ways to implement a reporter like this.

ReSharper uses a web service maintained by JetBrains. Windows error reporting is similar. However, I do not have resources to build such a web service.

The second way is to send a mail by SMTP. I tried but I found that I need to register another mail box for CBC in order to keep my personal mail boxes safe and I have to publish the password because I could not hide it. Thus, I gave it up.

At last, I know I can use this article to setup a mail message. So that is how I enable Send Error Report button.

http://www.codeproject.com/KB/IP/SendFileToNET.aspx
