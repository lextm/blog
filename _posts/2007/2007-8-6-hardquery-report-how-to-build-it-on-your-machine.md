---
layout: post
title: "HardQuery Report: How To Build It On Your Machine"
description: "This post talks about how to build HardQuery source code on your machine."
tags: Code-Beautifier-Collection Delphi
permalink: /hardquery-report-how-to-build-it-on-your-machine-8659b530e522
excerpt_separator: <!--more-->
---
If you master MSBuild, you can manually modified *.proj files in source package in order to build CBC successfully. If you are not familiar with MSBuild, please carefully follow the steps,

> Notice, please do not modify installation folders. My MSBuild scripts assume you install the tools to default folders.
<!--more-->

## Phase I:

1. Install .NET Framework 2.0. It contains MSBuild, which is a build engine now pseudo standardized on Windows Platform.
1. Install MSBee, which enables you build .NET 1.1 assemblies with MSBuild.

> If you have 1, and 2 installed, you can run make.debug.bat to test. Run ExpertManager.bat and add Lextm.CodeBeautifierCollection.Framework.dll to BDS 2006 Expert list, then you can see CBC loaded by BDS.

## Phase II:

The following are tools you need to run make.all.bat.

1. Install Sandcastle, which generates documentation for LeXDK.
1. Install Sandcastle Help File Builder, which helps generate documentation.
1. Install CTeX, which compiles documentation.
1. Install Inno Setup, which generates the installer.
1. Install MSBuild Community Tasks, which zips up packages.

The installer created in setup folder can be used to install CBC.

> If you build CBC on Vista, please run make.all.bat in an elevated command prompt.

Yes, I make use of a lot of Open Source projects or free tools. Thanks for all the authors.

If you have any questions or comments, feel free to leave a word here. I will update this article later.

(Updated: I did not release my public-private key file in the zip package, so you need to either manually remove Sign.cs from the projects or make a key file yourself.

You should try to build the solution file in SharpDevelop 2.2 before running make.*.bat to ensure that everything can be compiled without errors.)

