---
layout: post
title: "Alternative Avalon Universe: Open Alternatives to Closed-Source Tooling"
description: "A guide to community-built alternatives around Avalonia and the wider XAML ecosystem, with a focus on open tooling, independent governance, and why community forks matter."
tags: .net open-source visual-studio visual-studio-code
categories: [Tools and Platforms]
excerpt_separator: <!--more-->
image:
  path: /images/avalon.png
  alt: Avalon illustration.
---

Avalonia's tooling and governance have changed considerably since this post was first published. The old Accelerate branding has since been reorganized, while the [Community Spaces Policy](https://avaloniaui.net/legal/community-moderation) introduced in August 2026 now states explicitly that Avalonia is not community-owned or foundation-governed. It also defines Avalonia-operated spaces, including official GitHub repositories and discussions, as company-operated infrastructure.

Against that background, this post maps the open alternatives that have emerged around Avalonia and the wider XAML ecosystem, and explains why independent tooling and community forks matter.

<!--more-->

## Open alternatives that work today

The community has already shipped viable alternatives for several common gaps for users that prefer open-source and independently maintained tooling. Many of these projects are in active use and continue to evolve independently.

### MediaPlayer, DataGrid, TreeDataGrid, and DevTools

This open source [MediaPlayer](https://github.com/wieslawsoltes/MediaPlayer) provides media playback building blocks for Avalonia, with multiple backend options and a reusable sample application layer.

[ProDataGrid](https://github.com/wieslawsoltes/ProDataGrid) is a fork that addresses gaps many desktop developers encounter. Maintained by Wiesław Šoltés under the MIT license, it evolves independently from Avalonia's built-in DataGrid. [TreeDataGrid](https://github.com/wieslawsoltes/TreeDataGrid) is another component in the same ecosystem.

The inclusion of ProDiagnostics DevTools matters too, because debugging layout, binding, and control behavior is where teams spend a great deal of time in complex Avalonia codebases. ProDiagnostics includes features such as remote control and a 3D exploded view, showing how far a community fork can evolve once maintainers are free to explore a different direction.

### Visual Studio extension fork

[AXAML Viewer](https://marketplace.visualstudio.com/items?itemName=SuessLabs.Avalonia-Lite-VS) is an open fork of the legacy Visual Studio extension.

It can be useful for developers who prefer a community-maintained Visual Studio extension with its source available.

### AXSG Tooling

[AXSG Tooling is shipping a new VS Code extension](https://marketplace.visualstudio.com/items?itemName=wieslawsoltes.axsg-language-server), but right now it needs projects to fully migrate to AXSG to work.

XAML Source Generator (XSG) is a relatively new concept. Uno Platform and MAUI are exploring it heavily. [Wiesław Šoltés is building an open-source AXSG implementation that targets the open source Avalonia framework](https://github.com/wieslawsoltes/XamlToCSharpGenerator). Like the default XamlX/XamlIl tooling, AXSG is pluggable and can be used in parallel with the existing XAML toolchain. It is designed to be a drop-in replacement for the XAML compilation step, generating C# code directly from AXAML files. This brings a new AXAML language server, Hot Reload engine, live previewer, and MCP server.

AXSG started with VS Code, but there is a clear path to support Visual Studio and Rider as well. The architecture is designed to be flexible and adaptable to different IDEs and build systems.

### What if you hit issues?

When you hit a blocker with any of these tools, you can file issues and contribute fixes via pull requests. Their priorities are set by their maintainers and contributors rather than by a vendor's commercial roadmap. That can mean faster experimentation in some areas and fewer guarantees in others, which is a normal tradeoff in community-maintained software.

### Why community forks matter

Fragmentation has real costs: duplicated maintenance, competing packages, and more choices for users to evaluate. But forks are also one of the safety valves built into open source.

When upstream priorities change, a fork lets others preserve an existing direction, experiment with a different one, or continue work that the original maintainers no longer want to pursue. It does not require hostility toward the upstream project, and it does not require the vendor's approval.

If "fragmentation" simply means that development happens outside the vendor's control, the term becomes much less useful. Independent implementations and community forks are normal outcomes of permissive open-source licensing.

People make real decisions based on what is publicly supported and where investment is going. If official tooling moves toward closed, registered, or vendor-controlled paths, it is natural that the community explores alternatives. That is not hostility. It is how open ecosystems adapt.

## Alternative frameworks and directions

If you are evaluating whether Avalonia is still the right choice, consider these frameworks and related directions.

### WPF and LibreWPF

For Windows-only applications, [Microsoft WPF](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/) remains mature and stable. It will not run on Linux or macOS, but if your target is Windows, the ecosystem is deep and well documented. [The XSG tooling for WPF is also being maintained](https://github.com/lextudio/wxsg), but depends on people's willingness to help shape it further in the open.

[LibreWPF](https://github.com/wieslawsoltes/LibreWPF) takes a different route. It is a community fork of Microsoft's open-source WPF codebase. Its current cross-platform work reuses as much managed WPF code as possible, including the application model, dependency properties, layout, controls, data binding, documents, XAML, resources, themes, and the XAML compiler, while replacing Windows-only rendering and platform layers with portable implementations based on [ProGPU](https://github.com/wieslawsoltes/ProGPU)/WebGPU and Silk.NET.

Existing WPF applications are intended to switch to the LibreWPF SDK while keeping normal WPF source code and XAML unchanged, except where an application depends on Windows-specific interop or unsupported native graphics APIs.

That lineage matters. LibreWPF is a fork of Microsoft's open-source WPF repository. It is taking WPF in a cross-platform direction that Microsoft itself is not currently pursuing.

This is exactly the kind of experimentation that open-source WPF makes possible. Microsoft does not need to pursue cross-platform WPF itself for another community to explore that direction. [Building an active community around WPF and its forks](https://github.com/wieslawsoltes/LibreWPF/issues/2) can keep that ecosystem healthy while allowing new ideas to develop independently.

### MAUI

Microsoft's [MAUI](https://dotnet.microsoft.com/en-us/maui) remains a solid choice for cross-platform desktop and mobile development. It has commercial backing and clear licensing under MIT. Microsoft continues to improve it in each major .NET release, and XSG-based tooling is being developed to enrich the MAUI ecosystem:

- [Simpler XAML syntax](https://devblogs.microsoft.com/dotnet/simpler-xaml-in-dotnet-maui-10/) by Microsoft in .NET 10
- [C# Expressions in XAML](https://github.com/dotnet/maui/blob/main/docs/specs/XamlCSharpExpressions.md) by Microsoft in .NET 11
- [GTK4, WPF, and AppKit bindings, with the new CLI and DevFlow tooling](https://github.com/dotnet/maui-labs)

### Uno Platform

If registration is not a problem for you, or you can work without commercial tooling, [Uno Platform](https://platform.uno/) is another option for building cross-platform applications with a single codebase.

It is not difficult to migrate WPF components to Uno Platform, and there are new examples:

- [UnoEdit](https://github.com/lextudio/UnoEdit), AvalonEdit port to WinUI/Uno Platform
- [UnoDock](https://github.com/lextudio/UnoDock), AvalonDock port to WinUI/Uno Platform
- [WindowsShims](https://github.com/lextudio/WindowsShims), bridging WPF controls to WinUI/Uno Platform, such as DataGrid, RichTextBox, ToolBar, and more. This allows developers to leverage existing WPF components while building cross-platform applications with WinUI/Uno Platform.
- [UnoDevelop](https://github.com/lextudio/UnoDevelop), SharpDevelop port to WinUI/Uno Platform. This project is archived now in favor of OpenDevelop on LibreWPF, but it remains a large example of a full IDE port to Uno Platform and demonstrates what is involved in migrating a complex WPF application.

### MewUI

[MewUI](https://dev.to/al6uiz/i-wanted-to-ship-a-gui-without-the-net-runtime-two-months-with-mewui-a-cross-platform-ui-17ae) is an AI-native cross-platform UI framework built around Native AOT. It ships a single executable without requiring a .NET runtime installation, targets minimal deployment size, and already supports GDI, Direct2D, and OpenGL backends.

MewUI represents a different philosophy: lightweight, C# markup, and Native AOT first. For small tools and utilities, it may be worth evaluating alongside others.

## What you can do

- **Visual Studio users:** Evaluate [AXAML Viewer](https://marketplace.visualstudio.com/items?itemName=SuessLabs.Avalonia-Lite-VS) and see if it fits your workflow.
- **VS Code users:** Evaluate [AXSG for VS Code](https://marketplace.visualstudio.com/items?itemName=wieslawsoltes.axsg-language-server) and see how it integrates with your development workflow.
- **MediaPlayer users:** Evaluate [MediaPlayer](https://github.com/wieslawsoltes/MediaPlayer) for your media playback needs.
- **DataGrid users:** Evaluate [ProDataGrid](https://github.com/wieslawsoltes/ProDataGrid) for your grid needs.
- **TreeDataGrid users:** Evaluate the open [TreeDataGrid](https://github.com/wieslawsoltes/TreeDataGrid) fork and decide whether its direction fits your application.
- **Dev Tools users:** Evaluate ProDiagnostics and the additional diagnostics capabilities it offers.
- **New projects:** Consider whether Avalonia is still the right choice, or whether WPF/LibreWPF, MAUI, Uno Platform, or MewUI better fit your needs.
- **Contributors:** The ecosystem needs maintainers, testers, and advocates. Even small contributions help independent projects establish themselves.

## Closing thoughts

Open-source licensing and open governance are two different things. A framework can remain fully open source while its governance, infrastructure, and community spaces are controlled by a single commercial entity.

Avalonia's Community Spaces Policy reveals more details about AvaloniaUI OÜ's chosen governance model. It does not invalidate the open-source license, but it changes the role that independent community spaces and forks need to play.

Community forks preserve choice when upstream and community priorities diverge — giving developers somewhere else to experiment, maintain existing ideas, and build new ones.

This is also why the earlier [discussion about handing legacy projects to community maintainers](https://github.com/AvaloniaUI/Avalonia/discussions/19653) remains important.

Open alternatives are ecosystem infrastructure. Long-lasting platforms benefit from room for independent experiments, forks, competing tools, and different governance models.

If you prefer clear licensing, independent governance, and the ability to participate without depending on a single vendor's roadmap, these alternatives are worth evaluating.

To explore more posts about .NET and open source, check out all posts tagged [.NET]({{ site.baseurl }}/tags/net/) and [open-source]({{ site.baseurl }}/tags/open-source/).
