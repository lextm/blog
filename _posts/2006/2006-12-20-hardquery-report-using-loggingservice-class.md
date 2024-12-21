---
layout: post
title: "HardQuery Report: Using LoggingService class"
description: "This article describes how to use LoggingService class in HardQuery."
tags: Code-Beautifier-Collection Delphi
permalink: /hardquery-report-using-loggingservice-class-64c6cacc48e4
excerpt_separator: <!--more-->
---
CSDN Dec 20, 2006)

## What is LoggingService

LoggingService is a new unit I create lately to replace Marc Clifton's wonderful Debug/Dbg unit used in early versions of CBC. This new unit is a wrapper on log4net, an amazing logging library. But it is more than a wrapper, and makes thing even easier in certain aspects. As a result, I use it across CBC now. You can find it in the source package under src/lextm/diagnostics/loggingservice.cs. It is covered by LGPL.
<!--more-->

## Configuration

When using log4net, you have to do something configuration ahead. You can place the settings in exe.config or web.config. Even when you cannot touch those two, you can use a totally different file in the same format and loading it at runtime to configure the loggers and the appenders. Because I cannot modify either exe.config or web.config in CBC, I choose the last approach which affects LoggingService heavily.

When you start to use LoggingService, write you settings file and send the path to Start function as the only parameter. For example,

``` csharp
LoggingService.Start("C:\cbc.exe.config");
```

## Leaving messages in the log

Then you can use LoggingService's Debug, Info, Error, Fatal, and Warn functions to log any important steps inside your code. Because they are just wrappers of ILog's Debug, Info, Error, Fatal, and Warn functions.

## Key improvements

What makes LoggingService easier to use is that you don't need to define a logger per unit using

ILog log = LogManager.GetLogger(MethodBase.GetCurrentMethod().DeclaringType);

LoggingService manages that for you internally.

Other new features are .NET Framework Debug and Trace unit style functions, Indent and Unindent. I add two useful functions, EnterMethod and LeaveMethod. By their names you know you can use them to log StackTrace information easily. You can write the following code

``` csharp
void Sample() {

LoggingService.EnterMethod();

//….

LoggingService.LeaveMethod();

}
```

Then in your log file you will see
``` text
→SomeClass.Sample

//…

←SomeClass.Sample
```

I love this kind of hint when I use CodeSite, and now successfully I bring it into LoggingService.

Wish you love this unit. It will be available soon.
