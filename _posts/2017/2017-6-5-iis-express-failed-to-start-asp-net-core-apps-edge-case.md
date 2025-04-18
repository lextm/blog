---
description: Troubleshooting an edge case where IIS Express fails to start ASP.NET Core applications due to port conflicts with an already running instance, with detailed event log analysis and solution.
excerpt_separator: <!--more-->
layout: post
permalink: /iis-express-failed-to-start-for-asp-net-core-apps-edge-case-78efdc18e1c6
tags: asp.net iis windows visual-studio
categories: [Tools and Platforms]
title: IIS Express Failed to Start ASP.NET Core Apps Edge Case
---
This time with the new documentation site, Microsoft does [provide better coverage on common issues](https://docs.microsoft.com/aspnet/core/publishing/iis#common-errors). However, they still miss one edge case I just hit today and below is the detail.
<!--more-->

You probably have the web app debugged in VS, so there is already an IIS Express process running,

![img-description](/images/iis-express-tray.png)
_Figure 1: IIS Express process launched by Visual Studio._

And then when you manually execute IIS Express (from command prompt or any other way) and try to launch the same site, no doubt there would be an error with messages such as "Error initializing ULATQ, hr = 800700b7" and "Cannot create a file when that file already exists".

![img-description](/images/iis-express-error.png)
_Figure 2: IIS Express error message._

And in Windows event log you can also see more information, like

``` text
Log Name: Application
Source: IIS Express
Date: 6/5/2017 8:09:05 PM
Event ID: 2269
Task Category: None
Level: Error
Keywords: Classic
User: N/A
Computer: lextmserver
Description:
The worker process for app pool 'Clr4IntegratedAppPool', PID='10400', failed to initialize the http.sys communication when asked to start processing http requests and therefore will be considered ill by W3SVC and terminated. The data field contains the error number.
Event Xml:
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
<System>
<Provider Name="IIS Express" />
<EventID Qualifiers="49152">2269</EventID>
<Level>2</Level>
<Task>0</Task>
<Keywords>0x80000000000000</Keywords>
<TimeCreated SystemTime="2017–06–06T00:09:05.569686000Z" />
<EventRecordID>14090</EventRecordID>
<Channel>Application</Channel>
<Computer>lextmserver</Computer>
<Security />
</System>
<EventData>
<Data>Clr4IntegratedAppPool</Data>
<Data>10400</Data>
<Binary>B7000780</Binary>
</EventData>
</Event>
```
and
``` text
Log Name: Application
Source: IIS Express
Date: 6/5/2017 8:09:06 PM
Event ID: 2276
Task Category: None
Level: Error
Keywords: Classic
User: N/A
Computer: lextmserver
Description:
The worker process failed to initialize correctly and therefore could not be started. The data is the error.
Event Xml:
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
<System>
<Provider Name="IIS Express" />
<EventID Qualifiers="49152">2276</EventID>
<Level>2</Level>
<Task>0</Task>
<Keywords>0x80000000000000</Keywords>
<TimeCreated SystemTime="2017–06–06T00:09:06.675647300Z" />
<EventRecordID>14091</EventRecordID>
<Channel>Application</Channel>
<Computer>lextmserver</Computer>
<Security />
</System>
<EventData>
<Binary>B7000780</Binary>
</EventData>
</Event>
```
So next time you hit the same thing, you know what to look for.

The solution is to simply stop the process launched by Visual Studio.
