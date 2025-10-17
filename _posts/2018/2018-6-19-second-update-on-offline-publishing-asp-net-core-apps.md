---
description: Step-by-step guide on upgrading ASP.NET Core applications from 2.0.6 to 2.1.0 in offline environments, including project file changes and publishing command adjustments.
excerpt_separator: <!--more-->
image:
  alt: Copyright © Lex Li. Place des Canotiers, Quebec City
  path: /images/place-des-canotiers.jpg
layout: post
permalink: /second-update-on-offline-publishing-asp-net-core-apps-e79c682fd287
tags: .net asp.net visual-studio microsoft
categories: [Programming Languages]
title: Second Update on Offline Publishing ASP.NET Core Apps
---
I [posted about offline publishing ASP.NET Core web apps]({% post_url 2018/2018-3-21-update-on-offline-publishing-asp-net-core-apps %}) earlier. It was a migration from 2.0.5 to 2.0.6. And now we need a new post, to upgrade from 2.0.6 to 2.1.0.

<!--more-->

Microsoft has [a very long article](https://docs.microsoft.com/aspnet/core/migration/20_21?view=aspnetcore-2.1) on the migration steps in general. But you might find I didn't follow all their steps.

## Project File Changes

I only changed `TargetFramework` and `PackageReference` parts, so the project file looks like this,

``` xml
<Project Sdk="Microsoft.NET.Sdk.Web">
  <PropertyGroup>
    <TargetFramework>netcoreapp2.1</TargetFramework>
  </PropertyGroup>
  <ItemGroup>
    <PackageReference Include="Microsoft.AspNetCore.App" />
  </ItemGroup>
</Project>
```

It is quite simple to follow.

## Publishing Command

This time `RuntimeFrameworkVersion` is no longer needed,

``` batch
$ dotnet publish -r win-x64 --self-contained
```

## NuGet Packages

Of course, it asks for new version 2.1.0 of the following,

- `runtime.win-x64.Microsoft.NETCore.App`
- `runtime.win-x64.Microsoft.NETCore.DotNetHostPolicy`
- `runtime.win-x64.Microsoft.NETCore.DotNetHostResolver`
- `runtime.win-x64.Microsoft.NETCore.DotNetAppHost`

You should notice that even if the ASP.NET Core MVC sample was created in 2.0 time frame, compiling and running it using 2.1 toolchain changes the behaviors. For example, now this app listens on both `http://localhost:5000` and `https://localhost:5001`. And that's why when you first compile it, the dotnet command would display the following message,

> ## ASP.NET Core
>
> Successfully installed the ASP.NET Core HTTPS Development Certificate.
>
> To trust the certificate run `dotnet dev-certs https --trust` (Windows and macOS only). For establishing trust on other platforms refer to the platform specific documentation.
>
> For more information on configuring HTTPS see [this article](https://go.microsoft.com/fwlink/?linkid=848054).
