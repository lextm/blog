---
layout: post
title: ".NET OTA: Fewer try-catch lines are needed in an .NET OTA wizards"
description: "This article describes how to use UnhandledExceptionManager to catch unhandled exceptions in .NET OTA wizards."
tags: Code-Beautifier-Collection Delphi
excerpt_separator: <!--more-->
---
(CSDN Oct 08, 2006)

I believe most of people using the .NET OTA have read this article many times, "The C#Builder Open Tools API" by Erik Berry. Yes, it is a great introduction. However, since I have already done a lot of development on .NET OTA, I think something mentioned in that article is no longer correct/convenient.
<!--more-->

For example, Erik wrote:

If one of your menu event handlers throws an uncaught exception, the only indication the user will see is the somewhat unhelpful message "Exception has been thrown by the target of an invocation". This is because native code deep inside the IDE is making calls into your .NET object to signal the menu item being selected and the .NET event invocation framework is catching .NET exceptions and re-throwing them with the above message. For this reason, it might be prudent to wrap your menu event handlers in a try/catch block, show the real exception message to the user, and then handle the exception as appropriate.

It was good walk-around but now a simple UnhandledExceptionManager can catch the exceptions for us.

What is unhandled exceptions? Mauro Venturini wrote:

When a .NET application hits an unhandled exception the default behaviour is to show a very poor dialog (Form1.jpg). Therefore, it is (or should be) common practice to hook UnhandledException event of the current AppDomain and ThreadException event of Application.

Unfortunately, there are security restrictions on these hooks that prevent their direct use inside applications that will be run without full trust (and even Local Intranet group does NOT have full trust).

A solution is to delegate the hooks to a full trusted assembly inside the GAC and reference it. UnhandledExceptionManager is an assembly that implements the technique.

Yes, when I followed his steps and used UnhandledExceptionManager, now unhandled exceptions are caught. I leave all of you an example. When you open the About form of CBC, double click the title "Beautify the code, delight the work", an exception is thrown and I write no try-catch lines inside the menu event handler. However, since I use UnhandledExceptionManager, it handles the exception for me. This really simplifies the menu handlers.

UnhandledExceptionManager is for general purposes. You can use it anywhere necessary. however, follow Marco's steps. If that assembly is not inside GAC, it may not work well.
