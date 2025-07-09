---
layout: post
title: "How to Use ANTLR on .NET, Part II"
description: "This post is about how to use ANTLR on .NET."
tags: .NET ANTLR
permalink: /how-to-use-antlr-on-net-part-ii-d6b4514b0970
excerpt_separator: <!--more-->
---
Environment Setup
<!--more-->

ANTLR on Java heavily relies on Eclipse (though it also supports other Java IDE). So you can assume using it on .NET relies on Visual Studio. The following things can be helpful,

## ANTLR Language Support (optional)

http://visualstudiogallery.msdn.microsoft.com/25b991db-befd-441b-b23b-bb5f8d07ee9f

This is an extension for Visual Studio 2010 and 2012, which provides

* Syntax highlighting, including within actions and semantic predicates
* Outlining support for quickly collapsing rules
* Dropdown bars listing parser and lexer rules within the current grammar
* Support for Autocomplete, Quick Info, and Go To Definition

Note that this extension is optional (not required if you are using Visual Studio 2005/2008 or your Visual Studio edition does not support extensions or any other IDE).

## ANTLR C# Runtime/Tools (mandatory)

http://www.antlr.org/wiki/display/ANTLR3/Antlr3CSharpReleases

I recommend you download antlr-dotnet-tool-3.4.1.9004.7z which contains both the runtime (need to be added as reference in your project), and the tool (ANTLR3.exe which can generate code from .g files, and Antlr3.targets/AntlrBuildTask.dll which provide MSBuild support).

My approach is to put the files in a folder under my project (lib\ANTLR), such as

https://github.com/lextudio/sharpsnmplib/tree/5c721d5de4cc84bbe07b711d999ee55ee3a90533/lib/ANTLR

Then in my C# project I can add references to the dlls, and consume Antlr3.targets in MSBuild script.

## JDK and ANTLRWorks (optional but recommended)

If you haven't watched the video clips I mentioned in part I, please watch them before moving on. If you have watched, I assume you have downloaded and installed JDK from Oracle, and have ANTLRWorks somewhere on your system,

http://antlr.org/download.html

I am using Version 1.4.3 for Windows, Linux and Mac OS X right now.

We need ANTLRWorks because it is still the best way to debug grammar files.

OK, if you have got all above configured, get ready for part III where I will show you how I make ANTLR works for #SNMP.

Stay tuned.
