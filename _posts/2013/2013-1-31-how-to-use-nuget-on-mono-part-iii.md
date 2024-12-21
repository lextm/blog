---
layout: post
title: "How to Use NuGet on Mono, Part III"
description: "This post shows how to find out that Microsoft.Build.dll is missing."
tags: Mono .NET
permalink: /how-to-use-nuget-on-mono-part-iii-bc1d14e79db4
excerpt_separator: <!--more-->
---

[Update: Microsoft starts to officially support Mono, so please simply use latest NuGet executable such as 3.5]

> In [part I]({% post_url 2013/2013-1-27-how-to-use-nuget-on-mono-part-i %}) and [part II]({% post_url 2013/2013-1-28-how-to-use-nuget-on-mono-part-ii %}) I have already mentioned the steps you need to follow. This post only described how to find out that Microsoft.Build.dll is missing.

On openSUSE (12.2) it is easy to find that `xbuild` and `Microsoft.Build.Framework.dll` is available under `mono-devel` package,

``` bash
lextm@linux-gtil:~> rpm -ql mono-devel | grep xbuild
```

Then it is obvious that Microsoft.Build.dll is not within this package,

``` bash
lextm@linux-gtil:~> rpm -ql mono-devel | grep Microsoft.Build*
```

For Ubuntu, the package structure is different. xbuild is in mono-xbuild, while Microsoft.Build.\* are split into several packages such as mono-xbuild, lib-mono-microsoft-build-framework4.0-cil, and so on. I have to use which xbuild and dpkg -S /usr/bin/xbuild to locate the package name, which is not intuitive.

<!--more-->
