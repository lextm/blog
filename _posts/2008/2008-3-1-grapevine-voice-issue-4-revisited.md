---
layout: post
title: "GrapeVine Voice: Issue 4 Revisited"
description: This post talks about the changes in 6.0 Update 1.
tags: Code-Beautifier-Collection Delphi
permalink: /grapevine-voice-issue-4-revisited-17f7247ca063
excerpt_separator: <!--more-->
---
I reopened issue 4 earlier today, and luckily I fixed it again in an hour. The real problem behind the scene is how to determine a DLL is .NET.

http://code.google.com/p/lextudio/issues/detail?id=4&can=1

It is easy to do it with SDK tools such as Ildasm.exe and corflags.exe, but I want to do it in C#. And after reading so much articles at last I prefer this function,

``` csharp
/// 
/// Verifies whether it is a .NET file.
/// 
/// File name
/// true if it is .NET, false if else.
public static bool IsDotNetAssembly(string fileName) {
    bool result = true;
    try {
            System.Reflection.Assembly.LoadFrom(fileName);
    } catch (BadImageFormatException ex) {
        int errorCode = System.Runtime.InteropServices.Marshal.GetHRForException(ex);
        if (errorCode == COR_E_ASSEMBLYEXPECTED)
        {
            result = false;
        }
    }

    return result;
}

private const int COR_E_ASSEMBLYEXPECTED = -2146234344;
```

I know it is also possible to read CLR header but I do not know how. A code sample I found did not work for DLL files.

I am going to release a RC build of 6.0 Update 1 later this month. Stay tuned.
<!--more-->
