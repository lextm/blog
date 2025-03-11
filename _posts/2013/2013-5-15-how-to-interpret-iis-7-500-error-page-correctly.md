---
layout: post
title: "How to Interpret IIS 7+ 500 Error Page Correctly"
description: "This post talks about how to interpret IIS 7+ 500 error page correctly."
tags: IIS
permalink: /how-to-interpret-iis-7-500-error-page-correctly-187fe536993c
excerpt_separator: <!--more-->
---
> Well, this blog post is a summary of [my IIS.net discussion with a user](http://forums.iis.net/t/1198073.aspx/1?Orginal+Url+are+written+instead+of+User+Friendly+Url+in+log+on+IIS+7+5+when+using+Current+RewritePath+).

So what should we do when IIS reports 500 error? You first idea might be posting "I meet an IIS 500 error" somewhere on IIS.net or StackOverflow.com. But is that enough to get the answer and help you want? Of course not. Of all IIS status codes, 500 is probably a category of its own, which can be caused by tons of root causes,

http://support.microsoft.com/kb/943891

Thus, I love the new design of IIS 7+ (7.0, 7.5, and 8.0) which provides a detailed error page for such issues. Sometimes by properly interpreting the error messages, you might identify the problem fully on your own.
<!--more-->

OK, below is an example,

> **Error Summary**\
> HTTP Error 500.0 - Internal Server Error\
> Internal Server Error\
> **Detailed Error Information**\
> Module URLRewrite\
> Notification BeginRequest\
> Handler PageHandlerFactory-Integrated-4.0\
> Error Code 0x800703e9\
>
> IIS received the request; however, an internal error occurred during the processing of the request. The root cause of this error depends on which module handles the request and what was happening in the worker process when this error occurred.\
>
> IIS was not able to access the web.config file for the Web site or application. This can occur if the NTFS permissions are set incorrectly.\
> IIS was not able to process configuration for the Web site or application.
> The authenticated user does not have permission to use this DLL.
> The request is mapped to a managed handler but the .NET Extensibility Feature is not installed.
> Ensure that the NTFS permissions for the web.config file are correct and allow access to the Web server's machine account.
> Check the event logs to see if any additional information was logged.
> Verify the permissions for the DLL.
> Install the .NET Extensibility feature if the request is mapped to a managed handler.
> Create a tracing rule to track failed requests for this HTTP status code. For more information about creating a tracing rule for failed requests, click here.
>
> **Links and More Information** This error means that there was a problem while processing the request. The request was received by the Web server, but during processing a fatal error occurred, causing the 500 error.

How to interpret the above error page? I have already highlighted the portion we should focus on.

We start from the error code, as by using a simple command line tool published by Microsoft, you can easily know the meaning of it,

http://www.microsoft.com/en-us/download/details.aspx?id=985

Please download and extract the err.exe from this package. Running it at command prompt and ask what is 0x800703e9, you instantly know that stack overflow happened,

``` text
E:\Green\err>err 800703e9
## for hex 0x800703e9 / decimal -2147023895 :
COR_E_STACKOVERFLOW corerror.h
## MessageText:
## Is raised by the EE when the execution stack overflows as
## it is attempting to ex
## 1 matches found for "800703e9"
```

Do you know what is stack overflow? Wikipedia shows it clearly. Do you also know what is URL Rewrite? Microsoft makes it clear here. So if you are familiar with both like me, the root cause is almost clear. Right! If the rewrite rules lead to infinite redirection then the stack overflow is expected.

Next time when you hit a 500 error page, please make sure you digest the information inside actively. Only after that you can post your problem to an online forum and expect assistance from others. Or if you are lucky enough, you can locate the culprit before anyone else.
