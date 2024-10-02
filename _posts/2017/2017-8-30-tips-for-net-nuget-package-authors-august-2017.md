---
layout: post
title: "Tips for .NET NuGet Package Authors (August 2017)"
description: This post is about some tips for .NET NuGet package authors such as how to select target platforms, how to prepare source code, how to generate the package, and how to test out the package.
tags: .NET Visual-Studio
permalink: /tips-for-net-nuget-package-authors-august-2017-48f07604e4a0
excerpt_separator: <!--more-->
---
> I have to add "August 2017", as time proves that the tips can go easily out-of-date.

The responsibilities of a NuGet package author are,

* Select the proper target platforms your package would support.
* Prepare your source code so that the necessary assemblies can be prepared.
* Generate the actual package.
* Test out the package.
<!--more-->

## Tips on Target Platform Selection

A few months ago, obviously you should go against .NET Framework and some PCL profiles. I did that too. However, now comes .NET Standard. So, the possible options are,

* .NET Standard 1.x/2.x to support as many platforms as possible (Mono, Xamarin, and so on).
* .NET Framework 4.5(.2) due to many reasons (*).

  > The many reasons can be,
  >
  > 1. Easier for .NET Framework projects to consume your package. Especially for those who still use packages.config. （About all possible issues, you can refer to [this Microsoft article](https://github.com/dotnet/announcements/issues/31).)
  > 1. .NET Standard comes so late, so if you choose for example .NET Standard 1.3 as minimal and the only target platform, .NET Framework 4.5.x users cannot consume the package.

For #SNMP Library 10.0.1 release, I choose

* .NET Standard 1.3, as it offers most API this library relies on.
* .NET Framework 4.5.2, so at least some users on old platforms are still supported.
* Xamarin.iOS and Xamarin.Android, as they provide more APIs.

You can obviously choose your own based on the actual code base. Some libraries can successfully choose .NET Standard 1.0, while some might have to choose .NET Standard 2.0 (or a future version) if it needs too many APIs.

Make sure you go through [this excellent video](https://learn.microsoft.com/events/dotnetconf-2017/t112) to learn more about .NET Standard.

## Tips on Source Code Preparation

I used to use multiple projects (csproj) so each compiles to an assembly targeting an individual target platform. Then a NuGet package can be built manually from a .nuspec file.

It was yesterday that I were brave enough to try .NET Core 2.0 tooling again and its [plural `<TargetFrameworks>` element](https://learn.microsoft.com/dotnet/standard/frameworks#how-to-specify-target-frameworks).

> Note that if you need conditional compilation (like I did for #SNMP Library), this article also shows which constants you might use.

So,

1. Start from a .NET Standard 1.3 project.
1. Manually modify its .csproj file to target .NET Standard 1.3, .NET Framework 4.5.2, and Xamarin ones,

``` xml
<TargetFrameworks>netstandard1.3;net452;xamarinios10;monoandroid44</TargetFrameworks>
```

Luckily this time it did not fail me,

* The project itself compiles successfully.
* By using `<GeneratePackageOnBuild>true</GeneratePackageOnBuild>` a NuGet package can be generated properly.
* Most importantly all projects that hold a project reference to this project do compile and run without any issue. A few weeks ago before .NET Core 2.0 RTM tooling it seemed to kill me often, and I left it untouched.

> MSBuildSdkExtras is required so as to enable Xamarin support in `<TargetFrameworks>`. Make sure you follow the readme to modify your project file.
> 
> Note that 1.1.0 release is not yet published, so you need to use 1.0.9 or 1.1.0 test build instead.

However, do remember that `net*` target frameworks can only be built on Windows right now. Of course, that means your NuGet package can only be produced on Windows.

> You might guess by using the following trick to exclude them on non-Windows OS,

``` xml
<TargetFrameworks Condition=" '$(OS)' == 'Windows_NT' ">netstandard1.3;net452;xamarinios10;monoandroid44</TargetFrameworks>
<TargetFrameworks Condition=" '$(OS)' != 'Windows_NT' ">netstandard1.3</TargetFrameworks>
```
> It does work at command line, but after modification Visual Studio 2017 15.3 won't be able to open the project file correctly.
> 
> Therefore, I don't use conditions in my projects, but instead using `sed` command on macOS/Linux to remove those platforms manually before compilation.

If you need to sign the assemblies, a disappointing fact is that Roslyn cannot fully sign assemblies on non-Windows platforms yet. Thus, Microsoft temporarily introduces a concept called [public signing](https://github.com/dotnet/corefx/blob/master/Documentation/project-docs/public-signing.md).

.NET Core applications have been designed to work well with public signed assemblies. However, .NET Framework based projects (as well as Mono based) cannot consume them. So it is very very important to make sure you manually modify your project files to use the following public signing setting,
``` xml
<PublicSign Condition=" '$(OS)' != 'Windows_NT' ">True</PublicSign>
```

> You no longer need this hack as Microsoft fixes it in a later release, https://github.com/dotnet/roslyn/issues/8210

What might happen if you forget this? Public signing is just similar to delay signing. And when the following is used,
``` xml
<PublicSign>True</PublicSign>
```

Then the compiled assembly might trigger runtime exception for .NET Framework projects that consume it, as "strong name validation failed" will be triggered.

Again, your NuGet package in this case must be generated on Windows before uploading to NuGet.org.

## Tips on NuGet Package Generation

As `<GeneratePackageOnBuild>` can already help generate a package automatically, you can almost directly upload the result to NuGet.org.

If you compare #SNMP Library 10.0.1 release to old releases, you should see some important changes, such as DES/AES encryption. There are part of SNMP v3 protocol documents (AES is experimental, but quite practically in use), but unfortunately too old to be part of .NET Standard (even .NET Standard 2.0 does not support them quite completely). However, .NET Framework/Xamarin platforms do support them, so we need to add proper handling so end users can take necessary actions.

[Here I use](https://github.com/lextudio/sharpsnmplib/blob/0ce6a822bfc6bf8a1b2a89afbb604605e4af3fb5/SharpSnmpLib/Security/AESPrivacyProvider.cs#L51) the Microsoft recommended approach,

* Use conditional compilation to throw PlatformNotSupportedException in those edge cases.
* Add new properties to show if certain features are supported.

For example, AESPrivacyProvider now has an IsSupported static property indicating its platform feasibility. Its Encrypt/Decrypt methods would throw PlatformNotSupportedException if running in .NET Core 1.x/2.0 console apps, where AES algorithm is missing.

## Tips on Package Testing

Currently I manually create several test projects,

* .NET Framework projects (PackageReference and packages.config)
* .NET Core 1.0/1.1/2.0 console projects

So that I know the generated NuGet packages can be consumed correctly.

> Surely I should add Xamarin.iOS and Xamarin.Android projects to the plate some time soon.

Another thing you might be interested in, is how to test out .NET Standard class library projects.

Initially you can create a .NET Core 1.0 console application (with xUnit.net) to contain the test cases for your project, as it provides some confidence. Then you can add other platforms, such as .NET Framework. That can guarantee the code runs fine on all its supported platforms.

> I have just written [a separate post]({% post_url 2017/2017-9-25-tips-for-net-core-unit-testing %}) with more details on that part.

If you are looking for a complete sample, you can go to [#SNMP Library on GitHub](https://github.com/lextudio/sharpsnmplib).

Running the batch file dist.nuget.bat would generate two packages under .nuget folder (run prepare.bat or prepare.sh before compiling the projects).

You might leave a comment if you have any question.
