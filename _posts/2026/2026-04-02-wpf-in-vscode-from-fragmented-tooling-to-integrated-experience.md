---
layout: post
title: "WPF in VS Code: From Fragmented Tooling to Integrated Experience"
date: 2026-04-02 00:00:00 +0000
categories: [.NET, WPF, Tooling, VS Code]
tags: [wpf, vs-code, xaml, net-framework, open-source, component-reuse, c-sharp]
description: "How fragmented C# and XAML tooling left WPF developers in VS Code without a complete solution—and how integrating community-built components creates the modern experience that was missing."
image:
  path: https://lextudio.com/images/wpf-designer.png
  alt: "VS Code Tools for WPF visual designer showing XAML editing and design-time preview"
---

When VS Code first emerged as a serious development environment for .NET, it was designed with modern .NET in mind. Over time, a broader ecosystem of developers—working with .NET Framework, WPF, and other mature but "legacy" technologies—tried to use VS Code but found themselves navigating a fragmented tooling landscape. They faced competing extensions, unclear guidance about what to install, and gaps where no tool existed at all.

This fragmentation had consequences. Developers working on mature frameworks lost autonomy—locked into Visual Studio not because the framework needed it, but because the ecosystem around the framework made it the only practical choice. SharpDevelop 4 was a good alternative in the past, but it was archived and no longer maintained. The ecosystem of tools that once supported WPF development outside of Visual Studio had withered away, leaving a single dominant option. This is unhealthy for any ecosystem, but especially for mature frameworks like WPF that still have large user bases and active development.

But that story is changing. This post explains how the fragmentation across modern .NET tooling created ecosystem confusion, how XAML support became a separate desert, and how assembling community-built components creates the integrated WPF experience that was missing.

<!--more-->

## Part 1: Modern .NET/C# in VS Code, The Controversy

The foundation of C# development in VS Code is the [C# extension](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csharp) (powered by OmniSharp). It provides:

- IntelliSense and code completion
- Go to Definition and Find References
- Syntax highlighting and diagnostics

For years, this was *the* way to develop C# in VS Code. In 2024-2025, Microsoft released **C# Dev Kit**, which promised to modernize and enrich the C# development experience with additions like Solution Explorer, testing support, and premium features like IntelliCode.

But C# Dev Kit introduced two problems:

1. **Modern .NET only** — C# Dev Kit uses new project model assumptions that .NET Framework projects violate. Installing it alongside the C# extension for .NET Framework work creates conflicts, so you need to pay attention.

2. **Closed source and licensing constraints** — C# Dev Kit is not open source. It's treated as part of VS for Windows licensing, requiring either Community Edition restrictions or paid commercial licenses. Meanwhile, improvements to the open-source C# extension itself remain under-resourced.

The result: developers face a fragmented choice. Use the aging C# extension (open source but limited), or upgrade to C# Dev Kit (better featured but closed source, licensing-constrained, and incompatible with .NET Framework).

> **Why this split happened**: Microsoft's 2016 pivot to .NET Core meant that investment followed new frameworks. When .NET Core became .NET 5+, tools like C# Dev Kit were optimized for that future. But the decision to make C# Dev Kit closed source (rather than extending the open C# extension) reflects broader governance choices: proprietary licensing maximizes revenue and control. The open-source C# extension remains important but receives minimal investment. Developers working on mature .NET projects (Framework, WinForms, WPF) are left in the gaps.

The ecosystem response was predictable: **community alternatives emerged.**

Projects like **dotBlur** and others are attempting to provide unified C# development experiences that work across .NET Framework and modern .NET without the fragmentation. These efforts acknowledge that the Microsoft tooling split leaves a real gap: developers working on mature .NET projects have no clear, unified path. They must choose between:

1. **Use the C# extension alone** (works for .NET Framework, but designed for modern .NET)
2. **Use C# Dev Kit** (modern .NET only, excludes .NET Framework)
3. **Seek community alternatives** (inconsistent, evolving, not vendor-backed)

None of these is a satisfying answer. The fragmentation is real, and it drives frustration across the ecosystem.

> **The broader pattern**: When official tooling splinters by framework version, the ecosystem splinters too. Developers spend time choosing tools instead of writing code. Community fill-in solutions emerge but lack resources. The overall developer experience degrades, and so does enthusiasm for those frameworks.

## Part 2: XAML Tooling, A Desert Specific to No Framework

On top of the C# tooling confusion sits an even larger problem: **WPF XAML support in VS Code barely exists, and what does exist is hacky, not WPF-focused.**

VS Code provides syntax highlighting for XAML, but that's it. No IntelliSense for elements or properties. No binding validation. No designer. No Hot Reload. For WPF developers, this is a hard stop.

Over the years, various projects attempted to fill this gap:

- **OpenSilver** built a web-based XAML designer (targeting Silverlight API initially and filling WPF gaps bit by bit). It works for some scenarios but lacks full WPF-specific knowledge. Its developers intended to help WPF developers, but more to migrate to OpenSilver than to support WPF itself.
- **Community language server experiments** tried to provide XAML IntelliSense by parsing XML and understanding type systems. Without framework-specific knowledge, the results were clunky and unreliable. One XML schema based attempt was nice for basic syntax but failed to understand WPF's complex property system, attached properties, and design-time behaviors.
- **Individual extension attempts** tried to solve pieces of the problem. None matured into a comprehensive solution.

Why did these all fail? Because building a complete XAML experience requires understanding:

- A specific framework's property system (WPF's attached properties and dependency properties are not the same as MAUI's, WinUI/Uno Platform's or Avalonia's)
- Type resolution and namespace semantics
- Markup extensions and custom processors
- Design-time behavior and rendering
- Binding expressions and data contexts

This is not small work. **SharpDevelop spent years building this expertise into their XAML designer.** Modern frameworks like Uno Platform invested heavily in their own design tools like Hot Design, each with framework-specific knowledge. But no one stepped in to modernize WPF's XAML tooling ecosystem.

The result: XAML tooling exists for other frameworks. But not for WPF. The ecosystem saw WPF as "mature" (read: no longer strategic) and invested elsewhere.

> **Why frameworks matter for tooling**: A XAML language server for Avalonia doesn't work well for WPF because the type systems, binding semantics, and design-time behaviors are different. Generic XAML support is like generic programming language support. It covers syntax but misses semantics. WPF needed framework-specific tools. The ecosystem never provided them.

## Part 3: The Solution, VS Code Tools for WPF

On March 29, 2026, LeXtudio Inc. released [VS Code Tools for WPF](https://marketplace.visualstudio.com/items?itemName=lextudio.vscode-wpf), a response to this fragmentation. Rather than building everything from scratch, the extension integrates existing open-source components that already solve individual problems well.

### Component 1: The SharpDevelop WPF Designer

The core designer experience comes from **SharpDevelop's WPF designer**, the same component that powered SharpDevelop for years before that project was archived. The designer codebase remains available and mature.

Rather than build a visual designer from scratch, the extension bundles SharpDevelop's designer as a separate process (`XamlDesigner.exe`). When you request a design-time experience, the extension launches this process, and you see a proper visual editor—drag-and-drop, property inspector, design-time resources.

This reflects a fundamental insight: **XAML designers are hard to build correctly, and good ones are rare. When one exists and works well, preserving and reusing it is smarter than reinventing it.**

It's not lite integration we achieved. We innovated on the communication protocol to enable event handler creation and Hot Reload to designer support, to ensure that the designer is fully aware of your edits and vice versa.

### Component 2: XSG Language Server for WPF XAML Semantics

The extension integrates a custom build of [XSG Language Server](https://github.com/wieslawsoltes/XamlToCSharpGenerator) to provide semantic understanding of WPF XAML:

- Real-time XAML validation
- IntelliSense for elements and properties
- Binding expression validation
- Go-to-definition for custom types

XSG emerged from the Uno Platform and MAUI community as a source-generation approach to XAML compilation. It providers compiler-grade semantic understanding. Even though AXSG toolset was initially designed for Avalonia, its core language service is framework-agnostic enough to apply to WPF, so we collaborate with its maintainer to enable XSG for WPF and keep it improved.

### Component 3: Runtime Hot Reload Architecture

The innovation that fills the last big gap is **XAML Hot Reload**. Early prototypes attempted a debugger-based approach based on SharpDbg, but turned out to be heavy. The solution: inject a .NET assembly (`WpfHotReload.Runtime.dll`) at startup using `DOTNET_STARTUP_HOOKS`. This helper runs a named-pipe server that listens for XAML changes from VS Code. When you push XAML changes, the runtime applies it safely on the WPF Dispatcher thread, reflected instantly in the running application.

This is the same pattern used by other frameworks: injection rather than introspection, named pipes rather than debugger APIs, direct runtime control rather than debug-session intermediation.

We will further explore this architecture in a future post, but the key point is that it provides a robust, low-overhead way to enable Hot Reload for WPF without needing to build a full debugger integration.

### Why Component Integration Matters

What ties these components together is a philosophy: **community-built open-source tools are valuable enough to preserve and reuse, even across project boundaries.**

SharpDevelop is archived, but its designer lives on in VS Code Tools for WPF. AXSG language server was designed for Avalonia, but it now enhances WPF development as well. SharpDbg is part of SharpIDE's IDE effort, but it's available as a standalone component. None were built for this extension, and they were created to solve problems elsewhere. But they're all good enough that reusing them is smarter than replacing them.

This is the opposite of vendor lock-in. The WPF extension is assembled from pieces, each maintained separately, each improvable independently, each reusable in other contexts.

> **The component reuse pattern**: When you build tools from community components, you reduce duplication, increase surface area for contribution, and create clearer boundaries where different maintainers can focus on their specialty. The downside is integration complexity. But for mature, proven components, that trade-off is worth it.

## Part 4: .NET Framework Support—WPF Developers Matter

VS Code Tools for WPF was built specifically for .NET Framework 4.0+, not as an afterthought to modern .NET support. This matters.

WPF applications remain in active development across enterprises. Thousands of teams maintain and evolve large WPF codebases. They deserve tooling choices. They should be able to use VS Code if they prefer. They should not be locked into Visual Studio because no one else invested in their framework.

VS Code Tools for WPF demonstrates that building for .NET Framework developers is worth doing. It shows that mature frameworks can be tools-agnostic when the ecosystem commits to making them so. It proves that community-built components can fill the gaps that official tooling abandons.

That's not a small statement.

## Getting Started with VS Code Tools for WPF

Install from the VS Code Marketplace: [VS Code Tools for WPF](https://marketplace.visualstudio.com/items?itemName=lextudio.vscode-wpf).

See it in action:

<video width="100%" controls style="max-width: 800px; margin: 20px 0;">
  <source src="https://lextudio.com/videos/wpf-hot-reload.mp4" type="video/mp4">
  Your browser does not support the video tag. Download the video from <a href="https://lextudio.com/videos/wpf-hot-reload.mp4">wpf-hot-reload.mp4</a>.
</video>
