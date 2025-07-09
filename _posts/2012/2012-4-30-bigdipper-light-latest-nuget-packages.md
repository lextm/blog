---
layout: post
title: "BigDipper Light: Latest NuGet Packages"
description: "This post is about the latest NuGet packages for #SNMP."
tags: SNMP
permalink: /bigdipper-light-latest-nuget-packages-805787c264ff
excerpt_separator: <!--more-->
---
#SNMP started to provide 7.0 NuGet package last October. It was my first attempt, so there were a few issues with that package,

* Dependency on log4net was not explicitly listed.
* Only assemblies for .NET 3.5 were provided.
<!--more-->

Therefore, after learning how to do better NuGet packaging for Crad's ActionList for .NET, I decided to apply the tips to #SNMP. So now you can see an updated #SNMP package versioned 7.0.0.2. This number is for the NuGet package, as the binary version number is still #SNMP 7.0 RTW version number. It contains the following changes,

* Explicitly depends on log4net 1.2.10.
* Assemblies for both .NET 3.5 and 4.0 are included.

About how to install it, you can refer to

https://nuget.org/packages/Lextm.SharpSnmpLib/7.0.0.2

To accompany #SNMP 7.5 RC2, another NuGet package is also published, which contains the latest binaries,

https://nuget.org/packages/Lextm.SharpSnmpLib/7.5.0-alpha

It depends on log4net 2.0 and ANTLR C# runtime 3.4.1.
