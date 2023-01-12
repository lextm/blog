---
layout: post
title: "How to Use ANTLR on .NET, Part IV"
description: "This post is about how to use ANTLR on .NET."
tags: .NET ANTLR
permalink: /how-to-use-antlr-on-net-part-iv-62174f93bde0
excerpt_separator: <!--more-->
---
Part IV: ANTLR Grammar Tricks for C#
<!--more-->

## Tip 1: Twin Files Approach

If you have followed the series, you know already that ANTLR syntax heavily relies on Java. So if you are writing a new grammar and want to use it on .NET, make sure you write the grammar first with Java rules. Then you can easily test the grammar elements in ANTLRWorks (debugging).

I did the same for #SNMP, and Smi_no_action.g was my starting point. You can find that Smi.g is simply a slightly modified Smi_no_action.g with C# actions. Every time a grammar issue is found, I can first debug on Smi_no_action.g with ANTLRWorks. Once fixed, the change is applied to both grammar files. It is a pity that ANTLR grammar debugging is only easy on Java, so using these twin files is the only workaround I can think of. My experience proves it a feasible way so far.

https://github.com/lextudio/sharpsnmplib/blob/de58f7c050a0976654e7ee4b90a9217e99af6ae3/SharpSnmpLib/Mib/Smi.g

https://github.com/lextudio/sharpsnmplib/blob/de58f7c050a0976654e7ee4b90a9217e99af6ae3/SharpSnmpLib/Mib/Smi_no_action.g

Comparing the above two files you can see a few obvious difference. For example, the action used to skip an item is called skip() in Java while Skip() in C#. That is because the C# runtime follows the .NET naming conventions while the Java runtime follows the Java naming conventions. If you know of the two languages, it is not hard to overcome such slight changes.

So gradually you can convert your Java targeting grammar file to a C# targeting one.

## Tip 2: Exception Handling

Currently #SNMP throws all exceptions if it cannot handle, which is configured in Smi.g like this,

``` csharp
// Alter code generation so catch-clauses get replace with
// this action.
@rulecatch{
catch (RecognitionException)
{
    throw;
}
}
```

In this way any ANTLR parsing exceptions (derived from RecognitionException) will pop out.

Of course, there are other approaches which you can learn from the Java projects (Hibernate for example). Before learning them, make sure you already read related runtime API documentation.

## Tip 3: Use Partial Class Smartly

If you have reviewed Java targeting grammar files with actions, you can see a lot of Java code has to be embedded in the grammar file to enhance the generated parser class. In C#/.NET, partial class can be used to remedy this ugly issue.

https://github.com/lextudio/sharpsnmplib/blob/de58f7c050a0976654e7ee4b90a9217e99af6ae3/SharpSnmpLib/Mib/SmiParser.cs

The above source file contains a portion of SmiParser class. By using the partial keyword in class definition, I intentionally ask C# compiler to combine this class with the ANTLR generated SmiParser class. As a result, here functions such as statement() can be accessed freely.

Finally SmiParser class can be used in other projects to parse SMI/MIB files.

## (Updated) Tip 4: Exception Handling Extra

ANTLR 3 has built-in support for token recovery which might generate error node and attach them to the final AST. Such recovered errors won't be caught even if we apply Tip 2.

The proper way to turn off error node construction is mentioned in this article,

https://theantlrguy.atlassian.net/wiki/display/ANTLR3/Tree+construction

* Create a derived class from CommonTreeAdaptor.
* Override ErrorNode method and return null.
* Set TreeAdaptor property of your generated parser class to a new instance of the derived class.

Sadly I don't have any sample code for this newly added tip.

In next post, I am going to discuss the tips on debugging. Stay tuned.
