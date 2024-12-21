---
layout: post
title: "How to Use ANTLR on .NET, Part III"
description: "This post is about how to use ANTLR on .NET."
tags: .NET ANTLR
permalink: /how-to-use-antlr-on-net-part-iii-18a2457eee84
excerpt_separator: <!--more-->
---
C# Project Settings for ANTLR 3
<!--more-->

Now let's see how to use ANTLR 3 in a C# project by analyzing SharpSnmpLib.AST.csproj in #SNMP,

https://github.com/lextudio/sharpsnmplib/blob/de58f7c050a0976654e7ee4b90a9217e99af6ae3/SharpSnmpLib/SharpSnmpLib.AST.csproj

The above lines (75–79) use ANTLR MSBuild tasks. The PropertyGroup tag sets two paths: the first is the folder that contains AntlrBuildTask.dll; the second is the path for Antlr3.exe. The Import tag tells MSBuild engine that this extra .targets file needs to be loaded.

This C# project contains two ANTLR grammar files,

``` xml
<Antlr3 Include="Mib\Smi.g" />
<None Include="Mib\Smi_no_action.g" />
```

The Antlr3 tag means Smi.g is the grammar file that needs to be converted to C# code by Antlr3.exe. Under DEBUG mode, the converted C# files will locate in obj folder.

The None tag means Smi_no_action.g is not in use. About why it is not in use, I will describe later.

You might notice that this project does add Antlr3 C# runtime as a reference,

``` xml
<Reference Include="Antlr3.Runtime, Version=3.4.1.9004, Culture=neutral, PublicKeyToken=eb42632606e9261f, processorArchitecture=MSIL">
  <SpecificVersion>False</SpecificVersion>
  <HintPath>..\packages\Antlr.Unofficial.3.4.1.0\lib\Antlr3.Runtime.dll</HintPath>
</Reference>
```

In this project I use the ANTLR 3 NuGet package. If you don't want to use NuGet, you can simply add lib\ANTLR\Antlr3.Runtime.dll instead.

OK. After analyzing this project I think you know how to add a grammar file to your C# project, and then configure related project level settings properly. In next post I am going to document what you need to pay attention to at code level. #SNMP will still be our example.

Stay tuned.
