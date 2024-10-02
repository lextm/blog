---
layout: post
title: "How to Build .NET Core Solutions on AppVeyor"
description: "This post would show you how to build .NET Core solutions on AppVeyor, and a complete example."
tags: .NET
permalink: /how-to-build-net-core-solutions-on-appveyor-95cda0b15724
excerpt_separator: <!--more-->
---

I have recently upgraded #SNMP Library to .NET Core. And to the extreme, I get rid of the classic class library projects, and use a single .NET Standard 1.3 class library instead. Then it becomes a challenge to build the code base on AppVeyor, so I think it is worth the while to document what I have changed.
<!--more-->

## The Whole Manifest

The whole manifest can be found [here](https://github.com/lextudio/sharpsnmplib/blob/8e1d5b7e99a9d91c20d0dccc2d339afeacd809a3/appveyor.yml).

## The Image

It is very important to use Visual Studio 2017 image. It has all the development dependencies installed (Xamarin, .NET Core SDK, as well as Git and NuGet bits).

## Build Script

You cannot use the default MSBuild tasks from AppVeyor, so I suggest you use a custom script like I do.

If your solution only contains .NET Core projects or .NET Framework projects, you can now even use dotnet command to perform the operations,

``` bash
dotnet restore somesolution.sln
dotnet clean somesolution.sln
dotnet build somesolution.sln
```

But due to some unknown reason (I think it is a bug), currently you cannot do so if the solution contains Xamarin projects. You might hit error messages similar to this,

``` bash
dotnet restore SharpSnmpLib.NetStandard.sln
C:\Users\lextm\Downloads\sharpsnmplib\SharpSnmpLib\SharpSnmpLib.iOS.csproj(55,3): error MSB4019: The imported project "C:\Program Files\dotnet\sdk\1.0.3\Xamarin\iOS\Xamarin.iOS.CSharp.targets" was not found. Confirm that the path in the <Import> declaration is correct, and that the file exists on disk.
C:\Users\lextm\Downloads\sharpsnmplib\SharpSnmpLib\SharpSnmpLib.Android.csproj(61,3): error MSB4019: The imported project "C:\Program Files\dotnet\sdk\1.0.3\Xamarin\Android\Xamarin.Android.CSharp.targets" was not found. Confirm that the path in the <Import> declaration is correct, and that the file exists on disk.
```

An easy workaround is available, which I use here,

``` bash
msbuild /t:Restore somesolution.sln
msbuild /t:Clean somesolution.sln
msbuild somesolution.sln
```

## Test Script

The default AppVeyor unit test runner configuration does not yet support .NET Core runners. Thus, again we have to use a custom script right now.

I simply use `dotnet test` as it is the easiest.

Hope this post saves you some time.
