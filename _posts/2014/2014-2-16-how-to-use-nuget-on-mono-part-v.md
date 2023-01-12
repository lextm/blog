---
layout: post
title: "How to Use NuGet on Mono, Part V"
description: "This post talks about how to use NuGet on Mono, Part V."
tags: .NET Mono
permalink: /how-to-use-nuget-on-mono-part-v-e9918bb954c2
excerpt_separator: <!--more-->
---
[Update: Microsoft starts to officially support Mono, so please simply use latest NuGet executable such as 3.5]

This is a latest report on NuGet on Mono (assuming you are using Mono 3.2.7)

NuGet pack still breaks. I am still investigating on what's wrong.
NuGet package restore still breaks, due to [a Mono xbuild bug](https://bugzilla.xamarin.com/show_bug.cgi?id=17802), which I just reported.
<!--more-->

Thus, if you meet the following error message during a build, you hit exactly the same bug,

``` text
/home/lextudio/sharpsnmplib/SharpSnmpLib.Mono.sln (default targets) ->
(Build target) ->
/home/lextudio/sharpsnmplib/SharpSnmpLib/SharpSnmpLib.csproj (default targets) ->
/home/lextudio/sharpsnmplib/.nuget/NuGet.targets (RestorePackages target) ->

/home/lextudio/sharpsnmplib/.nuget/NuGet.targets: error : Command 'mono --runtime=v4.0.30319 /home/lextudio/sharpsnmplib/.nuget/NuGet.exe install "" -source "" -RequireConsent -solutionDir "/home/lextudio/sharpsnmplib/"' exited with code: 1.
```

If Mono guys fix this issue, I will test again to see if everything works as expected.

(Update on March 1) Well, 17802 has been fixed, but two more issues are found,

* Mono bug #28106

* NuGet bug #4051

Will track down the progress on these two in the next few weeks.
