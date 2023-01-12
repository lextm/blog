---
layout: post
title: "How to Use NuGet on Mono, Part II"
description: "In this part, we document how to get NuGet package restore working."
tags: .NET Mono
permalink: /how-to-use-nuget-on-mono-part-ii-1e71e55757bd
excerpt_separator: <!--more-->
---
[Update: Microsoft starts to officially support Mono, so please simply use latest NuGet executable such as 3.5]

> In part I we see how to get the command line tool running. In this part, we document how to get NuGet package restore working.

So how can we get package restore running, assuming you already have this enable for your solution?
<!--more-->

There are several steps needed,

1. Set the required environment variable,

   ``` bash
   export EnableNuGetPackageRestore=true
   ```

1. Go to .nuget folder and replace NuGet.targets with a new version.
1. Copy Microsoft.Build.dll to .nuget folder if you did not yet. (Please refer to part I)
1. Now the most difficult step comes. Please go to all .csproj/.vbproj files and modify
to
Now xbuild should be able to help build your solution and ask NuGet to restore packages.

Note that the wrong case issue of NuGet Visual Studio addin has been fixed only in its master branch, and is marked as part of upcoming 2.3 release. We still need to wait for that, and manually edit project files at this moment.
