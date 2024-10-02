---
layout: post
title: "Porting #SNMP Library to .NET Core Once Again"
description: "This post is about porting #SNMP Library to .NET Core once again."
tags: SNMP .NET
permalink: /porting-snmp-library-to-net-core-once-again-aaa649431215
excerpt_separator: <!--more-->
---

You probably know that I have ported this library to .NET Core a few months ago,

* Initial attempt
* RC1 to RC2
* RC2 to RTM

Overall things work as Microsoft promised, but the process was rather painful. So instead of quickly moving everything to .NET Core, I decided to stay on .NET Framework and move a few goodies from the .NET Core migration attempt back to 9.0.x series.

It turns out to be a smart choice as Microsoft later shipped Visual Studio 2017 RC (refreshed a few days ago), and today I can use an IDE to migrate once again. But I do hit a few different issues, so I'd like to list below.
<!--more-->

## MSBuild Project

First I created an empty .NET standard 1.3 class library project, and then put it into SharpSnmpLib folder. The new format of MSBuild scripts allow the project to automatically include all C# source files without my manually adding them all. But immediately I hit an error that many existing attributes are duplicate such as,

> error CS0579: Duplicate 'System.Reflection.AssemblyCompanyAttribute' attribute.

I was able to find similar posts on Stack Overflow and GitHub, but my solution is to add conditionals in AssemblyInfo.cs to exclude certain attributes from .NET Core compilation.

## Missing Packages

The remaining errors are so common that still classes or methods are missing. And I have to manually edit .csproj to add necessary packages in Visual Studio Code, where I can run `dotnet restore` and `dotnet build` at integrated terminal to observe errors,

``` xml
<ItemGroup>
<PackageReference Include="NETStandard.Library" Version="1.6" />
<PackageReference Include="System.AppDomain" Version="2.0.11" />
<PackageReference Include="System.ComponentModel.TypeConverter" Version="4.1.0" />
<PackageReference Include="System.Net.NetworkInformation" Version="4.1" />
<PackageReference Include="System.Runtime" Version="4.1" />
<PackageReference Include="System.Runtime.Serialization.Primitives" Version="4.1.1" />
<PackageReference Include="System.Threading.Thread" Version="4.0.0" />
</ItemGroup>
```

You might notice [a quite strange package](https://www.nuget.org/packages/System.AppDomain/) `System.AppDomain`, which comes from a third party, . So Microsoft does have AppDomain support in CoreCLR but intentionally hides that in CoreFX. This package exposes some important API, but not all.

## Conditionals

Still I have to leave conditional compilation from time to time, but compared to the previous attempts, the number has decreased, which is quite a pleasure. I no longer need to remove the sync versions of the Socket related methods, as the underlying API is back in .NET standard 1.3.

You can check [the whole commit here](https://github.com/lextudio/sharpsnmplib/commit/a26d8af07f04d095c903d61ee923ce66286dd316)

## Sidenote
I also hit [one Visual Studio 2017 limitation](https://developercommunity.visualstudio.com/content/problem/9051/microsoftnugettargets-error-when-compiling-a-pcl-p.html) where after compiling the .NET standard solution, the classic solution cannot be compiled properly.

Luckily a workaround was found and documented in the link above.

Hope you enjoy Visual Studio 2017 RC as I do. .NET Core is becoming mature, and the prime time is coming. Stay tuned.