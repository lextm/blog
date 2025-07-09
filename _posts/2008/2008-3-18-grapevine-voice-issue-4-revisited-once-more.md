---
layout: post
title: "GrapeVine Voice: Issue 4 Revisited Once More"
description: This post talks about the changes in 6.0 Update 1.
tags: Code-Beautifier-Collection Delphi
permalink: /grapevine-voice-issue-4-revisited-once-more-9fb06f8d6638
excerpt_separator: <!--more-->
---

This is an interesting issue because it touches one of the .NET essentials, PE format. So even though [I talked about it in this post earlier]({% post_url 2008/2008-3-1-grapevine-voice-issue-4-revisited %}), I think another post is worthwhile.

<!--more-->

Yes, using the sample code in last post I was able to determine if a file is .NET assembly but it was not efficient. Because of a well known .NET bug that assemblies loaded by reflection cannot be unloaded easily. Thus, if you try to verify a thousand files, then you may waste a lot of memory unexpectedly.

It is quite lucky that today NDepend author Patrick Smacchia talked about a similar topic here. Suddenly I realize that I should drop System.Reflection and try Mono.Cecil instead.

http://codebetter.com/blogs/patricksmacchia/archive/2008/03/18/mono-cecil-vs-system-reflection.aspx

So right now I use this sample code in 6.0 Update 1 RC,

``` csharp
public static bool IsDotNetAssembly(string fileName)
{
    bool result = true;
    Mono.Cecil.AssemblyDefinition myLibrary = null;
    try
    {
        myLibrary = Mono.Cecil.AssemblyFactory.GetAssembly (fileName);
    }
    catch (Mono.Cecil.Binary.ImageFormatException)
    {
        // for win32 dll
        result = false;
    }
    catch (ArgumentOutOfRangeException)
    {
        // for win32 exe
        result = false;
    }

    return result && myLibrary != null;
}
```
