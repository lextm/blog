---
layout: post
title: "Cleaning Up .NET on Your Desktop: From Command Line to Visuals"
description: A practical guide to safely uninstalling old .NET SDKs and runtimes across macOS and Windows—why versions accumulate (global.json pins, previews, hosting bundles, architectures), what the official uninstall tool does and doesn’t surface, and how a lightweight cross‑platform UI adds the missing context for confident cleanup.
image:
  alt: DotUninstall Social Preview.
  path: https://github.com/lextudio/dotuninstall/raw/main/social-preview.png
tags: .net microsoft
categories: [Programming Languages and Frameworks]
excerpt_separator: <!--more-->
---

When I recently ran `dotnet --info` on my Mac, I wasn’t expecting to see a scroll of SDKs and runtimes stretching back through years of projects. And I realized: it’s cleanup time—again.

<!--more-->

## Why So Many Versions?

Over time, every .NET developer builds up a graveyard of SDKs and runtimes. Some are pinned via `global.json`, some were installed for one-off projects, others came as part of hosting bundles or preview experiments. Unless you proactively clean house, they pile up—and it’s not always clear which ones are safe to remove.

Here’s a snippet from my own `dotnet --info`:

```text
.NET SDKs installed:
  6.0.428 [/usr/local/share/dotnet/sdk]
  7.0.410 [/usr/local/share/dotnet/sdk]
  8.0.413 [/usr/local/share/dotnet/sdk]
  9.0.305 [/usr/local/share/dotnet/sdk]
  10.0.100-preview.3.25201.16 [/usr/local/share/dotnet/sdk]
  10.0.100-preview.6.25358.103 [/usr/local/share/dotnet/sdk]
  10.0.100-rc.1.25451.107 [/usr/local/share/dotnet/sdk]

.NET runtimes installed:
  Microsoft.AspNetCore.App 6.0.36 [/usr/local/share/dotnet/shared/Microsoft.AspNetCore.App]
  Microsoft.AspNetCore.App 7.0.20 [/usr/local/share/dotnet/shared/Microsoft.AspNetCore.App]
  Microsoft.AspNetCore.App 8.0.19 [/usr/local/share/dotnet/shared/Microsoft.AspNetCore.App]
  Microsoft.AspNetCore.App 9.0.9 [/usr/local/share/dotnet/shared/Microsoft.AspNetCore.App]
  Microsoft.AspNetCore.App 10.0.0-rc.1.25451.107 [/usr/local/share/dotnet/shared/Microsoft.AspNetCore.App]
  Microsoft.NETCore.App 6.0.36 [/usr/local/share/dotnet/shared/Microsoft.NETCore.App]
  Microsoft.NETCore.App 7.0.20 [/usr/local/share/dotnet/shared/Microsoft.NETCore.App]
  Microsoft.NETCore.App 8.0.7 [/usr/local/share/dotnet/shared/Microsoft.NETCore.App]
  Microsoft.NETCore.App 8.0.19 [/usr/local/share/dotnet/shared/Microsoft.NETCore.App]
  Microsoft.NETCore.App 9.0.9 [/usr/local/share/dotnet/shared/Microsoft.NETCore.App]
  Microsoft.NETCore.App 10.0.0-rc.1.25451.107 [/usr/local/share/dotnet/shared/Microsoft.NETCore.App]
```

Each line tells a story of a project, a test run, or a temporary requirement. But when the story ends, the SDKs and runtimes stay behind.

## Microsoft’s Official Tool (dotnet-core-uninstall)

Surprisingly, the `dotnet` CLI itself offers no built-in way to manage installed versions. There’s no `dotnet uninstall`, no GUI, not even a command to list everything.

Instead, Microsoft provides a [separate uninstall tool](https://learn.microsoft.com/dotnet/core/additional-tools/uninstall-tool) called `dotnet-core-uninstall`. It’s a command-line utility that lets you remove SDKs and runtimes with filters like `--all-previews` or `--sdk 7.0.100`.

While powerful, it assumes you already know what’s safe to remove. And unless you document your installations, that’s rarely the case. There’s no visual context, no preview of dependencies, and in some setups (especially on Windows), not all items are even visible.

## What About Community Tools?

There’s [Dots](https://github.com/nor0x/Dots), a community-maintained GUI, but it only manages SDKs—not runtimes. Its UI also feels overly complex for casual cleanup. I wanted something lighter and more approachable.

So I built one.

## Introducing: DotUninstall

[DotUninstall](https://github.com/lextudio/dotuninstall) is a cross-platform Uno Platform app that gives you a clear, visual overview of installed .NET SDKs and runtimes—and lets you remove them with confidence.

![DotUninstall screenshot](https://github.com/lextudio/dotuninstall/raw/main/DotUninstall.png)

It started as a wrapper over Microsoft’s command-line tool, but turned into something deeper and more flexible.

## What I Learned Building It

### macOS: Simple Paths, Simple Life

On macOS, .NET installations live in predictable folders (`/usr/local/share/dotnet`). Uninstalling them is as easy as deleting those directories. DotUninstall reads those paths and gives you a simple list.

### Windows: MSI Mysteries

Windows, on the other hand, is another story.

Many SDKs and runtimes are installed via MSI packages—some standalone, some bundled (like in the ASP.NET Hosting Bundle). Their presence is tied to complex MSI product codes and registry entries, making uninstalling them a delicate operation.

I had no prior experience with MSI internals, but by digging into the source code of `dotnet-core-uninstall`, I learned how to query and safely remove these components. DotUninstall now reuses that logic directly (via submodule) so users don’t need to install Microsoft’s tool separately.

> ⚠️ Note: Some SDKs/runtimes might still not show up in DotUninstall if they were installed as part of a larger package. This is by design—to avoid breaking other installations or apps (especially Visual Studio for Windows).

### Platform Gaps in Microsoft’s Tools

Interestingly, Microsoft ships ARM64 and x64 versions of `dotnet-core-uninstall` for macOS—but **only** x86 for Windows. That means ARM64 or x64-native users on Windows would need to build the CLI from source just to use it. That’s not an acceptable situation, especially when the problem is clutter caused by the platform itself.

DotUninstall sidesteps this by embedding the logic directly and building natively for each platform and architecture. It works out-of-the-box.

### Release & EOL Nuances (Runtime vs Workload)

Not every layer shares the same end‑of‑life date:

- The base runtime and core SDK follow the published LTS / Current lifecycle.
- Workloads (like .NET MAUI) can end support earlier than the runtime they sit on.
- Downstream frameworks (e.g., Uno Platform) may drop a runtime line once a key workload on it is EOL—even if the runtime itself still has time left.

Practical effect: you can’t look only at “Is .NET 8 still LTS?”—you also need “Are the workloads I rely on still supported there?” I only noticed this sharply when an Uno Platform release (6.3) planned to drop .NET 8 because MAUI for that wave had already passed its own support window.

Cleanup rule: treat a workload’s end of life (EOL) as an early prompt to upgrade and avoid keeping that runtime line unless you need it for legacy code.

> DotUninstall 1.0.5 now highlights MAUI specific EOL status.

## A Smarter Way to Clean

Here’s what DotUninstall currently offers:

- Lists SDKs **and** runtimes  
- Highlights preview versions and older releases  
- Shows detailed product names and version numbers  
- Lets you safely uninstall selected entries  
- Works across macOS, Windows (x64/ARM64)  

## Looking Ahead

The desire for a first-party `dotnet uninstall` command is real—just check out [this GitHub issue](https://github.com/dotnet/sdk/issues/22925). But until Microsoft bakes this into the CLI, we’ll have to patch the gaps ourselves.

I’ll continue improving DotUninstall. If you want to contribute, suggest features, or report bugs, please [open an issue on GitHub](https://github.com/lextudio/dotuninstall/issues).

In the meantime, if `dotnet --info` makes you sigh, give DotUninstall a try.

With the right tools and a bit of context, keeping your .NET environment tidy becomes much less troublesome.
