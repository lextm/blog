---
layout: post
title: "Alternative Avalon Universe: Open Alternatives to Closed-Source Tooling"
description: "Why community forks around Avalonia face long-term maintenance risk, and which more open frameworks are worth evaluating instead, starting with LibreWPF."
tags: .net open-source visual-studio visual-studio-code
categories: [Tools and Platforms]
excerpt_separator: <!--more-->
image:
  path: /images/avalon.png
  alt: Avalon illustration.
---

This post was first published in March 2026 as a list of community tools around Avalonia. It has been rewritten since, because the situation those tools live in has changed.

The short version: the community forks are still useful today, but I would not bet a long-lived project on them. If you are choosing a framework now, there are more open options.

<!--more-->

## Why the forks carry long-term risk

Avalonia is an open-source framework, but it is developed by a company, AvaloniaUI OÜ, which I will call AvaloniaUI from here on. Its [Community Spaces Policy](https://avaloniaui.net/legal/community-moderation), effective 24 August 2026, states that "Avalonia is not a community-owned project and is not governed by a foundation." It also covers GitHub repositories, issues, discussions, and related project infrastructure as spaces operated by AvaloniaUI. A company is entitled to run its framework that way, but it shapes what a community fork can count on. AvaloniaUI decides the roadmap and how its own rules are read, and a fork maintainer has no neutral body to appeal to.

Most of these forks also depend on one or two people. Several of the Visual Studio and VS Code forks are no longer actively developed, and I no longer maintain [VS Code Tools for AXAML](https://marketplace.visualstudio.com/items?itemName=lextudio.vscode-axaml) myself. IDE support for Avalonia is built by AvaloniaUI and the IDE vendors, so a community language server or compiler replacement works beside that stack, not inside it. [AXSG](https://github.com/wieslawsoltes/XamlToCSharpGenerator), for example, requires a project to migrate fully to its generator.

The ground can also shift. In September 2025 AvaloniaUI opened a [call for maintainers](https://github.com/AvaloniaUI/Avalonia/discussions/19653) for the legacy Visual Studio extension and TreeDataGrid. It described the Avalonia Community organization as a possible "neutral, community-driven home" and said it would "support a smooth handover" if maintainers came forward. Six weeks later, an AvaloniaUI representative wrote in the same thread that no roadmap would be defined for community maintainers, and that they "won't spend time coordinating community forks," as they were "not our responsibility". Its explanation was that nobody stepped up in time. Today both [AvaloniaVS](https://github.com/AvaloniaUI/AvaloniaVS) and [TreeDataGrid](https://github.com/AvaloniaUI/Avalonia.Controls.TreeDataGrid) are archived under the AvaloniaUI organization, and neither lives in the community one.

Forks of controls and tooling also sit close to what AvaloniaUI sells, so their room to operate depends on how broadly it chooses to read its branding and community rules. I am not claiming these projects will disappear. I am saying the ground they stand on can change, and that is a real cost for anything you plan to maintain for years.

## More open options

### LibreWPF and WPF

[LibreWPF](https://github.com/wieslawsoltes/LibreWPF) is my first recommendation. It is a community fork of Microsoft's open-source WPF repository that takes WPF cross-platform. It reuses as much managed WPF code as possible, including the application model, dependency properties, layout, controls, data binding, XAML, and the XAML compiler, and replaces the Windows-only rendering and platform layers with portable implementations based on [ProGPU](https://github.com/wieslawsoltes/ProGPU)/WebGPU and Silk.NET. Existing WPF applications are meant to switch to the LibreWPF SDK with their source and XAML unchanged, except where they depend on Windows-specific interop or native graphics APIs.

What makes it attractive is the lineage. It starts from a mature, MIT-licensed framework with a huge body of code, controls, and documentation, and it does not depend on any single vendor's product plans. [Building an active community around it](https://github.com/wieslawsoltes/LibreWPF/issues/2) would keep it healthy. For Windows-only applications, [Microsoft WPF](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/) itself remains mature and stable, and [XSG tooling for WPF](https://github.com/lextudio/wxsg) is maintained in the open as well.

### MAUI

Microsoft's [MAUI](https://dotnet.microsoft.com/en-us/maui) is a solid choice for cross-platform desktop and mobile development. It is developed in the open under the MIT license, and [.NET 11](https://github.com/dotnet/maui/releases/tag/11.0.100-rc.2.26513.2) is already at release candidate stage. XAML source generation is now the default, [C# Expressions in XAML](https://github.com/dotnet/maui/blob/main/docs/specs/XamlCSharpExpressions.md) arrive with it, and [XAML Incremental Hot Reload](https://www.infoq.com/news/2026/08/dotnet-11-preview7-maui/) is on by default for Debug builds as a preview feature.

Preview 7 also added a cross-platform passkeys API, Shell route templates, and Hot Reload on physical iOS devices through `dotnet watch`. [CollectionView2 arrived on Windows, and Shell on Android was rebuilt on standard handlers](https://www.infoq.com/news/2026/07/net-maui-11-preview-6/), although the Shell change is Android-only for now. The experimental [maui-labs](https://github.com/dotnet/maui-labs) repository adds GTK4, WPF, and AppKit backends, a CLI, and DevFlow tooling, with the caveat that these packages are not covered by the MAUI support policy.

### Uno Platform

If registration is not a problem for you, or you can work without commercial tooling, [Uno Platform](https://platform.uno/) lets you build cross-platform applications from a single codebase, and migrating WPF components to it is not difficult. It has been moving fast in areas that matter for real products. [Uno 6.6](https://platform.uno/blog/uno-platform-6-6/) lets Skia-rendered apps work with screen readers on Windows, macOS, and WebAssembly, and adds IME composition on six platforms and automatic fallback fonts.

Uno is also now a [formal co-maintainer of SkiaSharp](https://platform.uno/blog/skiasharp4-whats-new/). SkiaSharp 4.x is opt-in in Uno 6.6, with up to 30% faster rendering reported in early testing. A [pluggable drawing backend](https://github.com/unoplatform/uno/pull/24153) merged in September 2026 adds an opt-in WebGPU renderer, and the repository already tracks a 7.0 milestone, so I would treat the WebGPU work as preview-grade until that release ships.

### MewUI

[MewUI](https://github.com/aprillz/MewUI) is an MIT-licensed, code-first cross-platform UI framework built around Native AOT. It ships a single executable without a .NET runtime installation and uses C# markup instead of XAML. Recent releases moved quickly, with [retained-mode rendering](https://github.com/aprillz/MewUI/releases/tag/v0.22.0) in 0.22 so that a window repaints only what changed, and [browser support on WebAssembly and WebGL2](https://github.com/aprillz/MewUI/releases/tag/v0.21.1) in 0.21. Version [0.22.1](https://github.com/aprillz/MewUI/releases/tag/v0.22.1) added typed drag and drop across Windows, Linux, and macOS.

It is still pre-1.0, with an API that can break between minor releases, and the author is targeting 1.0 in January 2027. You can try the [gallery in your browser](https://www.aprillz.net/MewUI/Gallery/) before installing anything.

## If you have good reasons to stay with Avalonia

These community projects still work today. Treat them as best-effort, and check their recent activity before you depend on them. [AXAML Viewer](https://marketplace.visualstudio.com/items?itemName=SuessLabs.Avalonia-Lite-VS) is an open fork of the legacy Visual Studio extension, and [AXSG for VS Code](https://marketplace.visualstudio.com/items?itemName=wieslawsoltes.axsg-language-server) is a language server and Hot Reload engine that requires full migration to AXSG. [ProDataGrid](https://github.com/wieslawsoltes/ProDataGrid) and [TreeDataGrid](https://github.com/wieslawsoltes/TreeDataGrid) cover grids, [MediaPlayer](https://github.com/wieslawsoltes/MediaPlayer) covers media playback, and ProDiagnostics offers DevTools with remote control and a 3D exploded view.

## Closing thoughts

Open source and open governance are not the same thing. A framework can be fully open source while one company controls its roadmap, infrastructure, and community spaces. For a long-lived project, I would look at both.

To explore more posts about .NET and open source, check out all posts tagged [.NET]({{ site.baseurl }}/tags/net/) and [open-source]({{ site.baseurl }}/tags/open-source/).
