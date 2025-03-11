---
layout: post
title: "How to Use NuGet on Mono, Part IV"
description: "This post described how we should patch NuGet so that it works better on Mono."
tags: .NET Mono
permalink: /how-to-use-nuget-on-mono-part-iv-65d6349aa5dc
excerpt_separator: <!--more-->
---

[Update: Microsoft starts to officially support Mono, so please simply use latest NuGet executable such as 3.5]

> In [part I]({% post_url 2013/2013-1-27-how-to-use-nuget-on-mono-part-i %}) and [part II]({% post_url 2013/2013-1-28-how-to-use-nuget-on-mono-part-ii %}) I have already mentioned the steps you need to follow. [Part III]({% post_url 2013/2013-1-31-how-to-use-nuget-on-mono-part-iii %}) is about Mono packaging. This post described how we should patch NuGet so that it works better on Mono.

I have opened a bug of NuGet on its homepage earlier today. I noticed it when I attempted to build my open source project #SNMP on Mono/Linux, as NuGet seems to ignore installed packages, which leads to multiple downloads of the same package and hurt performance significantly.

<!--more-->

Therefore, I downloaded NuGet source code on Mono/Linux and planed to build it. Failed. Alright, this is not a NuGet issue right now, as xbuild is not strong enough to support the build, which have been reported a long time ago and multiple times. Sadly Mono guys do not yet resolve it.

Anyway, I then downloaded the source code (NuGet 2.2 release, not master) to Windows, and used Visual Studio 2012 to build it. After that, I copied the instrumented binary (with Console.WriteLine everywhere necessary) to my Linux box. Guess what? This triggers a very strange error message, which I could not find any information on the web,

``` bash
Mono: gc took 15 usecs
Mono: Assembly Loader probing location: '/usr/lib/mono/4.0/mscorlib.dll'.
Mono: Image addref mscorlib[0x9960ab0] -> /usr/lib/mono/4.0/mscorlib.dll[0x99601b8]: 2
Mono: AOT failed to load AOT module /usr/lib/mono/4.0/mscorlib.dll.so: /usr/lib/mono/4.0/mscorlib.dll.so: cannot open shared object file: No such file or directory

Mono: Assembly Loader loaded assembly from location: '/usr/lib/mono/4.0/mscorlib.dll'.
Mono: Config attempting to parse: '/usr/lib/mono/4.0/mscorlib.dll.config'.
Mono: Config attempting to parse: '/etc/mono/assemblies/mscorlib/mscorlib.config'.
Mono: Assembly mscorlib[0x9960ab0] added to domain NuGet.exe, ref_count=1
Mono: Config attempting to parse: '/etc/mono/config'.
Mono: Config attempting to parse: '/home/lextm/.mono/config'.
Mono: Assembly Loader probing location: 'NuGet.exe'.
Mono: Image addref NuGet[0x99adcf8] -> /home/lextm/Downloads/ConsoleApplication3/.nuget/NuGet.exe[0x99ad030]: 2
Mono: Assembly NuGet[0x99adcf8] added to domain NuGet.exe, ref_count=1
Mono: AOT failed to load AOT module /home/lextm/Downloads/ConsoleApplication3/.nuget/NuGet.exe.so: /home/lextm/Downloads/ConsoleApplication3/.nuget/NuGet.exe.so: cannot open shared object file: No such file or directory

Mono: Assembly Loader loaded assembly from location: 'NuGet.exe'.
Mono: Config attempting to parse: '/home/lextm/Downloads/ConsoleApplication3/.nuget/NuGet.exe.config'.
Mono: Config attempting to parse: '/etc/mono/assemblies/NuGet/NuGet.config'.
Mono: Assembly Loader probing location: 'NuGet.exe'.
Mono: AOT failed to load AOT module /home/lextm/Downloads/ConsoleApplication3/.nuget/NuGet.exe.so: /home/lextm/Downloads/ConsoleApplication3/.nuget/NuGet.exe.so: cannot open shared object file: No such file or directory

Mono: Assembly Ref addref NuGet[0x99adcf8] -> mscorlib[0x9960ab0]: 2
Mono: Assembly Loader probing location: '/home/lextm/Downloads/ConsoleApplication3/.nuget/NuGet.Core.dll'.
Mono: Image addref NuGet.Core[0x99b5038] -> /home/lextm/Downloads/ConsoleApplication3/.nuget/NuGet.Core.dll[0x99b4708]: 2
Mono: Assembly NuGet.Core[0x99b5038] added to domain NuGet.exe, ref_count=1
Mono: AOT failed to load AOT module /home/lextm/Downloads/ConsoleApplication3/.nuget/NuGet.Core.dll.so: /home/lextm/Downloads/ConsoleApplication3/.nuget/NuGet.Core.dll.so: cannot open shared object file: No such file or directory

Mono: Assembly Loader loaded assembly from location: '/home/lextm/Downloads/ConsoleApplication3/.nuget/NuGet.Core.dll'.
Mono: Config attempting to parse: '/home/lextm/Downloads/ConsoleApplication3/.nuget/NuGet.Core.dll.config'.
Mono: Config attempting to parse: '/etc/mono/assemblies/NuGet.Core/NuGet.Core.config'.
Mono: Assembly Ref addref NuGet[0x99adcf8] -> NuGet.Core[0x99b5038]: 2
Mono: Assembly Ref addref NuGet.Core[0x99b5038] -> mscorlib[0x9960ab0]: 3
Missing method .ctor in assembly /home/lextm/Downloads/ConsoleApplication3/.nuget/NuGet.exe, type System.Runtime.CompilerServices.ExtensionAttribute
Mono: The class System.Runtime.CompilerServices.ExtensionAttribute could not be loaded, used in NuGet
Can't find custom attr constructor image: /home/lextm/Downloads/ConsoleApplication3/.nuget/NuGet.exe mtoken: 0x0a000018
```

If you happen to meet the same exception message after following http://docs.nuget.org/docs/contribute/setting-up-the-nuget-development-environment, please don't panic as this is by design. The NuGet site steps will generate binaries compiled against .NET 4.5 profile, which is not yet available in Mono stable releases (2.10.\*). You have to use Visual Studio 2010 to build the binaries (Core and CommandLine projects).
[Update: the exception is not Mono alone. If you run a .NET 4.5 program on .NET 4 you might hit the same, http://www.mattwrock.com/post/2012/02/29/What-you-should-know-about-running-ILMerge-on-Net-45-Beta-assemblies-targeting-Net-40.aspx]

Well, if you find that you cannot open the two projects correctly in VS2010, please go to `Build\NuGet.Settings.targets` file, and change

``` text
$(MSBuildExtensionsPath)\..\Microsoft Visual Studio 11.0\Common7\IDE
```

to something invalid, such as

``` text
$(MSBuildExtensionsPath)\..\Microsoft Visual Studio 12.0\Common7\IDE
```

Then VS2010 should be able to open the two projects correctly.

Finally the instrumented binary told me that `PhysicalFileSystem.GetDirectory` and `PhysicalFileSystem.GetFiles` do not work as expected. Why? I laughed when I opened this method,

``` csharp
private static string EnsureTrailingSlash(string path)
{
    if (!path.EndsWith("\\", StringComparison.Ordinal))
    {
        path += "\\";
    }
    return path;
}
```

OK. If you are familiar with [this guide](http://www.mono-project.com/Guidelines:Application_Portability), it is obvious that `\\` is the culprit. You should use Path.DirectorySeparatorChar to replace it.

Right now I am ready to fork NuGet, fix this issue, and send back a pull request.

[Update: Luckily NuGet guys already fixed it in master branch on Dec 5, 2012. Hope its 2.3 release comes soon.]

After so many struggles, I finally finish the series of this topic, and hope you also learn a lot from my experience like I did.
