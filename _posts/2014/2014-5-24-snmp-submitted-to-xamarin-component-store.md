---
layout: post
title: "#SNMP Submitted to Xamarin Component Store"
description: This post covers the steps I did to make the store submission and hope to show other developers how to properly make their components ready for Xamarin platforms.
tags: SNMP Mono
permalink: /snmp-submitted-to-xamarin-component-store-9a22d7d1e9f8
excerpt_separator: <!--more-->
---
You probably noticed that #SNMP repository has been quiet for a while, except a new folder named xamarin_support added in January. Yes, I have been working on official Xamarin support for a few weeks now, though the progress is really slow. This post is going to cover the steps I did to make the store submission and hope to show other developers how to properly make their components ready for Xamarin platforms.
<!--more-->

## Step 1: Binary Preparation

For #SNMP, it is pretty easy to create a Xamarin.Android project and add all existing C# source file to it. As Xamarin.Android uses .NET 4.5 profile, a recompile gives me the required SharpSnmpLib.Android.dll, which is exactly the Android port of SharpSnmpLib.dll.

## Step 2: Metadata Preparation

To make a component package, a lot of extra stuffs need to be prepared. The Xamarin guidelines documentation provide [some (very limited) information](https://components.xamarin.com/guidelines).

But you can check our repository to get better understanding of what are required,

https://github.com/lextudio/sharpsnmplib/tree/master/xamarin_support

## Step 3: Sample Projects

The most important thing you need to prepare is the sample project(s), but sadly no Xamarin documentation (including the forum) includes enough materials for you to get started.

If you submit an iOS component, you need to provide one or more Xamarin.iOS samples. This also applies to Android. I will show details on how to prepare an Android sample.

1. Create a Xamarin.Android project in Xamarin Studio. I use the Android Application template.
1. Change its Android settings as below, so that it is compiled against an old enough target, such as Android 2.3.
1. Check ABI options for Release build, so that it can be deployed to phones (not simulators).
Make sure this sample can run in simulator and a real phone. Then it can be included in the submission package.

## Step 4: Packaging

I created [a simple batch file](https://github.com/lextudio/sharpsnmplib/blob/8.5/xamarin_support/pack.bat) to automate the packaging.

Note that by specifying clearly the sample solution path, xamarin-component.exe can smartly pick up all necessary source files in the solution and include them in the final .xam package.

## Step 5: Upload

OK, the last step is to upload the package and [make a few more clicks](https://components.xamarin.com/submit/).

The reviewers will review the materials and let you know the result in a few days. They will inform you if anything is not correct, and you can update the package later.

Good luck :)
