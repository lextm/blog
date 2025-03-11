---
layout: post
title: ASP.NET Core Crashes and Burns
description: A post about ASP.NET Core common issues that you should be aware of
tags: Windows .NET Visual-Studio
excerpt_separator: <!--more-->
---

Getting start with ASP.NET Core is in fact easy, if you let it crash and burn. Every errors help you get better understanding of different aspects.

Don't believe it? Let's give it a try.
<!--more-->

## The Initial Steps

You can always open a Terminal first,

* Command prompt or PowerShell on Windows.
* Terminal on macOS or Linux.

and let's run

``` batch
mkdir test
cd test
dotnet --info
```

## .NET Core SDK
I expect something to break here, as you might not have .NET Core SDK installed.

So if you see the output,

``` bash
$ dotnet --info
zsh: command not found: dotnet
```

You need to go and install .NET Core SDK from [Microsoft](https://dot.net).

Be patient, as you might hit several issues here to get .NET Core SDK installed properly. But over the internet you can find all the help you need.

Ultimately I expect you see something similar to the following,

``` bash
$ dotnet --info
.NET SDK (reflecting any global.json):
 Version:   6.0.100-preview.7.21379.14
 Commit:    22d70b47bc

Runtime Environment:
 OS Name:     Mac OS X
 OS Version:  11.5
 OS Platform: Darwin
 RID:         osx.11.0-x64
 Base Path:   /usr/local/share/dotnet/sdk/6.0.100-preview.7.21379.14/

Host (useful for support):
  Version: 6.0.0-preview.7.21377.19
  Commit:  91ba01788d

.NET SDKs installed:
  5.0.100 [/usr/local/share/dotnet/sdk]
  5.0.201 [/usr/local/share/dotnet/sdk]
  5.0.203 [/usr/local/share/dotnet/sdk]
  5.0.301 [/usr/local/share/dotnet/sdk]

.NET runtimes installed:
  Microsoft.AspNetCore.App 5.0.0 [/usr/local/share/dotnet/shared/Microsoft.AspNetCore.App]
  Microsoft.AspNetCore.App 5.0.4 [/usr/local/share/dotnet/shared/Microsoft.AspNetCore.App]
  Microsoft.AspNetCore.App 5.0.6 [/usr/local/share/dotnet/shared/Microsoft.AspNetCore.App]
  Microsoft.AspNetCore.App 5.0.7 [/usr/local/share/dotnet/shared/Microsoft.AspNetCore.App]  
  Microsoft.NETCore.App 5.0.0 [/usr/local/share/dotnet/shared/Microsoft.NETCore.App]
  Microsoft.NETCore.App 5.0.4 [/usr/local/share/dotnet/shared/Microsoft.NETCore.App]
  Microsoft.NETCore.App 5.0.6 [/usr/local/share/dotnet/shared/Microsoft.NETCore.App]
  Microsoft.NETCore.App 5.0.7 [/usr/local/share/dotnet/shared/Microsoft.NETCore.App]

To install additional .NET runtimes or SDKs:
  https://aka.ms/dotnet-download
```

## Test Site

Now you can create your initial site at the terminal,

``` bash
$ dotnet new mvc
```

and it generates the simplest ASP.NET MVC site in the `test` folder created earlier.

You might want to study the source code to see how ASP.NET Core looks like, but that requires knowledge on C#/Razor and a little bit HTML/CSS. I skip all details right now, as you can find tons of tutorials over the internet.

Why do I suggest you start with a brand new site from the default template here? Because any custom template or a random project you found over the internet can break for its own issues. The default MVC template from Microsoft is expected to work in all cases.

## Web Pages in Browser

At the terminal, run the last command,

``` bash
$ dotnet run
```

This kicks out all the tools behind the scene to compile the source code and start the application.

You might see a very lengthy output, but it should end with something similar to,

``` bash
$ dotnet run
Building...
info: Microsoft.Hosting.Lifetime[0]
      Now listening on: https://localhost:5001
info: Microsoft.Hosting.Lifetime[0]
      Now listening on: http://localhost:5000
info: Microsoft.Hosting.Lifetime[0]
      Application started. Press Ctrl+C to shut down.
info: Microsoft.Hosting.Lifetime[0]
      Hosting environment: Development
info: Microsoft.Hosting.Lifetime[0]
      Content root path: /Users/lextm/Projects/test
```

Now open your web browser and navigate to `https://localhost:5001`. You should see the site running properly.

If things break here, there can be several kinds of issues,

* Failed to restore NuGet packages.
* Failed to compile the source code.
* Failed to launch Kestrel at port 5000/5001.

But again, with the keywords and error messages you can find guides over the internet to help.

## The End or The Start

It might sound like the end of this post, but just the start of your ASP.NET Core adventure.

With a live site running in your web browser now, you might want to explore the following,

* How about using `dotnet watch` instead of `dotnet run`? So what is the magic behind `dotnet watch`?
* How about using another template, such as `dotnet new signalr`?
* How about editing the code to make your own site?

Hope you enjoy the new world ahead. Stay tuned.
