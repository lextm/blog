---
layout: post
title: "How to Port #SNMP Library to .NET Core"
description: "This post is about how I port #SNMP Library to .NET Core."
tags: SNMP .NET
permalink: /how-to-port-snmp-library-to-net-core-878d29074f9c
excerpt_separator: <!--more-->
---
.NET Core is still a moving target, so don't jump on it unless you are kind of crazy at this stage…
Preparation
Visual Studio 2015 already contains .NET Core Beta 8 bits, but you will have to install the official RC1 bits over it from [Microsoft](https://get.asp.net/).
<!--more-->

Make sure you download the ASP.NET 5 RC one for your platform (assuming you choose Windows here).

Run the installer and it should download some more bits. When all is done, you will have .NET Core RC1 ready.

Now let's update it to RC1 Update 1,

1. Open Visual Studio Command Prompt.
1. Run `dnvm upgrade`
1. Run `dnvm list`

If you are lucky enough, then you should see this,

``` batch
$ C:\Program Files (x86)\Microsoft Visual Studio 14.0>dnvm list
Active Version Runtime Architecture Location Alias
1.0.0-rc1-final clr x86 C:\Users\lextm\.dnx\runtimes
1.0.0-rc1-update1 clr x64 C:\Users\lextm\.dnx\runtimes
* 1.0.0-rc1-update1 clr x86 C:\Users\lextm\.dnx\runtimes default
1.0.0-rc1-update1 coreclr x64 C:\Users\lextm\.dnx\runtimes
1.0.0-rc1-update1 coreclr x86 C:\Users\lextm\.dnx\runtimes
```

## Hacking Starts

Now it is time to go to Visual Studio 2015, and create a new project using the new "Class Library (Package)".

Before adding anything, open project.json. As this project type is .xproj and project.json is the new way to manage references, make sure you forget about our previous experience on .NET (.csproj).

I have [a sample file here](https://github.com/lextudio/sharpsnmplib/blob/netcore5/SharpSnmpLib/project.json)

You can see that it is more like a mixture of NuGet's nuspec (package definition) and .csproj (project references), though in JSON format.

This sample file indicates a NuGet package for #SNMP Library, and targets both .NET Framework 4.5.1 (net451) and .NET Platform Standard 5.4 (dotnet5.4). So once compiled, a NuGet package will be generated, and it will support the two frameworks.

Interestingly that for net451, this library only needs to add one extra reference (System.Runtime.Serialization) as that assembly is not often used, and not in the default assembly list.

For .NET Platform Standard 5.4, almost all dependencies are coming from NuGet packages, so you can see a long list of packages. Then how did I get the names and versions?

The trick is to copy source files from an existing .csproj to this .xproj. Then when Visual Studio indicates a class is missing, use [this site](http://packagesearch.azurewebsites.net) to search for the needed NuGet package and its version (* is used to avoid indicating the revision portion).

Of course, some classes just not yet appear in .NET Core, so I have to remove some #SNMP functionality at this moment (simply delete some #SNMP classes and methods). Once RC2 is available, there might be some new packages/classes added, and then I can port more #SNMP code.

When everything compiles without a problem, then the migration is finished.

## Final Words

A few things to notice are,

* There is a project.lock.json generated from project.json, which shows more about how many NuGet packages are in fact needed by your project, and what are their names and versions. This file is changed every time you modify project.json, so no need to check it in to source control.
* .xproj does not store source files in it. It assumes that all files in the same folder are source files of the project, so you should reorganize your source files to meet this requirements.
* Currently no unit testing integration yet for .xproj file. But RC2 should introduce some more changes.
* It is possible to convert an .csproj to use project.json, but I try to avoid that as that mixes too many things.
* dotnet5.4 is a temporary name, and RC2 changes it to netstandard1.3.
* dotnet5.4 covers a lot of platforms per [this page](https://github.com/dotnet/corefx/blob/master/Documentation/architecture/net-platform-standard.md) so it is quite a suitable moniker to use.

.NET Core RC2 will introduce many important changes, but I only focus on basic RC1 knowledge here to get you started.

Stay tuned.