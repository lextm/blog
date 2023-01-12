---
layout: post
title: How to Use ANTLR 4 on .NET in 2023
description: A post about how to use ANTLR 4 on .NET in 2023.
tags: Visual-Studio .NET ANTLR
excerpt_separator: <!--more-->
---

I once blogged heavily about how to use ANTLR on .NET, and you can find all related posts in [here]({{ site.baseurl }}/tags/antlr/).

And [my last blog post on ANTLR]({% post_url 2017/2017-12-22-how-to-use-antlr-4-on-net-in-2017 %}) was in 2017. You can still learn something useful from the old post.

Today it is time to provide some important update.

<!--more-->

## Runtime Responsibility Moved

Sam Harwell has been maintaining ANTLR 4 C# runtime for many years under [a dedicated GitHub repository](https://github.com/tunnelvisionlabs/antlr4cs). My projects have been using the ANTLR NuGet packages from Sam for a very long time.

However, after ANTLR 4.6.6 this repo became idle, and the new runtime NuGet package has become part of [the ANTLR 4 repository](https://github.com/antlr/antlr4). This is a great move, as it makes the runtime development more closely related to the core ANTLR 4 development.

## New Tooling and Migration

So if you have a project that uses Sam's ANTLR packages, how to migrate?

First, verify your project file,

``` xml
  <ItemGroup>
    <PackageReference Include="Antlr4" Version="4.6.6" PrivateAssets="all" />
    <PackageReference Include="Antlr4.Runtime" Version="4.6.6" />
  </ItemGroup>
```

Here the last release from Sam is being used. By replacing them with the following,

``` xml
  <ItemGroup>
    <PackageReference Include="Antlr4.Runtime.Standard" Version="4.13.0" />
    <PackageReference Include="Antlr4BuildTasks" Version="12.2.0" PrivateAssets="all" />
  </ItemGroup>
```

your project should once again be able to compile, and this time against latest ANTLR 4 tooling and runtime.

`Antlr4BuildTasks` is a nice new package created by Ken Domino and successfully fills the gaps. But note that it has a few breaking changes,

``` xml
  <ItemGroup>
    <Antlr4 Include="CLexer.g4" />
    <Antlr4 Include="CParser.g4">
      <Error>true</Error>
      <Listener>false</Listener>
      <Visitor>true</Visitor>
      <Package>Lextm.AnsiC</Package>
      <JavaExec>PATH</JavaExec>
    </Antlr4>
  </ItemGroup>
```

For example, grammar files must be explicitly included, and the settings are different.

## Side Notes

`Antlr4.Runtime.Standard` adn `Antlr4.Runtime` are compatible in most cases, but note that you might have to fix a few minor changes, such as `PredictionMode.Sll` becomes `PredictionMode.SLL`.

If you notice that generated lexer/parser code isn't updated and remains the same (ANTLR 4.6.6), then you need to restart Visual Studio and try again.

## Complete Example

I migrated my ANSI C language server project to the new tooling, and you can find the changes [here](https://github.com/lextm/ansi-c-antlr/commit/cdc3092ef2c533816b474edc6954a1103dd17c8f).

Stay tuned.
