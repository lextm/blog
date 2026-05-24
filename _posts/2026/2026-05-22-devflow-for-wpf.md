---
layout: post
title: "DevFlow for WPF: Modern tooling for .NET 8+ desktop apps"
categories: [Frameworks and Libraries]
tags: .net visual-studio-code open-source visual-studio
description: "DevFlow is the modern developer loop Microsoft has been building around MAUI. This post explains how LeXtudio is bringing the same live, runtime-aware workflow to WPF on .NET 8+."
image:
  path: /images/devflow_poster.png
  alt: "DevFlow for WPF poster"
excerpt_separator: <!--more-->
---

For a long time, some of the best .NET UI development experiences were also the hardest to reuse.

Visual Studio gave XAML developers powerful tools: XAML Hot Reload, Live Visual Tree, Live Property Explorer, Live Preview, visual designers, and debugging helpers. These tools gave developers a window into a running application that source code alone could not provide.

But there was a catch. Most of that experience lived inside Visual Studio. It was powerful and useful, but also IDE-centered, closed source, and difficult for the wider ecosystem to extend.

That model made sense when Visual Studio was the center of .NET development. It feels much more limiting today.

<!--more-->

## The Old World: Powerful, But Locked Inside the IDE

WPF developers have seen this pattern for years.

If you stayed inside Visual Studio, you could get a rich workflow. You could inspect the running UI tree, look at runtime properties, apply XAML changes, and debug layout or binding problems with help from the IDE.

If you wanted the same class of capability from another editor, a test runner, a command-line workflow, or a community tool, the story was much weaker.

The application runtime knew a lot about the UI, but that knowledge was mostly exposed through Visual Studio-specific experiences. The result was a strange split: the platform was mature and widely used, but the best development loop was difficult to reproduce outside Microsoft’s own IDE.

That was not only a WPF problem. Similar tensions appeared across other XAML stacks over time who tried to replicate Microsoft's closed source approach. Their official tooling could be impressive, but it was often hard for the community to acquire or build on the same primitives.

## The Tide Has Changed

Modern software development has been moving in a different direction.

Many other languages and platforms have embraced richer open-source tooling, command-line interfaces, and reusable infrastructure to please developers and ecosystem stakeholders.

So, for Microsoft, while keeping many components of .NET open source, the pressure to open up the entire developer loop has been growing. For years it resisted changes in this direction, and we saw controversies around things like the JetBrains .NET Core debugger, dotnet watch, and C# Dev Kit. But recently, the introduction of DevFlow for .NET MAUI has been a clear signal that a desire exists to embrace a more open, reusable model for runtime-aware UI development and the fruit of those efforts is starting to show.

The newer model is healthier:

- a few open source command line tools expose the basic workflow
- IDEs and editors become clients of reusable tooling
- communities can inspect, extend, and integrate the pieces
- automation and AI agents can participate without pretending to be a human clicking through an IDE

In other words, the future can be no more “Visual Studio owns the workflow.” It is closer to “the workflow is built from open, reusable pieces, and Visual Studio is one of the best front-ends for them.”

## Why DevFlow Matters

This is why DevFlow is interesting.

In spirit DevFlow is not completely new. It belongs to the same family of ideas as Visual Studio’s XAML Live Visual Tree, Live Property Explorer, and Live Preview: inspect a running app, understand its runtime UI state, and close the loop between editing and verification.

What is new is the packaging.

Instead of being mainly an IDE-only, human-facing feature, DevFlow exposes runtime inspection and interaction through its command-line and protocol-based surfaces. That makes the same kind of capability useful for automation, troubleshooting, testing, editor integrations, and AI-assisted workflows.

Microsoft’s current DevFlow work is happening around .NET MAUI, where the team is also exploring other ways to modernize the UI developer experience. Since .NET 10, MAUI has been making a lot of noise: simpler XAML and C# expression work driven by XAML Source Generator efforts, broader platform experiments around native bindings, and now DevFlow as a latest addition to the development loop.

The important part is not only that MAUI gets another tool. The important part is the direction: runtime-aware UI tooling can move out of a single IDE and become infrastructure, and it is open source as well.

## Why WPF Should Be Part of This Story

WPF is not new, but it is not dead either.

Many teams still build and maintain serious desktop applications with WPF. A lot of those applications have moved, or are moving, to modern .NET. These teams deserve a modern developer loop too.

WPF has its own runtime model, XAML semantics, layout system, binding behavior, and desktop application shape. A useful WPF DevFlow cannot be just a generic desktop automation layer. It needs to understand what makes WPF applications different.

At the same time, WPF should not remain trapped in a Visual Studio/Blend-only mental model. If runtime UI inspection is useful, it should be useful from Visual Studio, VS Code, Rider, command-line tools, test automation, and AI agents.

That is the gap our WPF Labs is trying to explore.

## LeXtudio's WPF Labs

LeXtudio’s WPF Labs project experiments with bringing DevFlow-style ideas to WPF and related desktop XAML technologies.

The goal is to expose a running app in ways that external tools can understand:

- runtime UI state through a DevFlow agent
- live UI tree and element inspection
- screenshot capture from a running desktop app
- basic interaction and automation hooks
- shared infrastructure where it makes sense across WPF, WinUI, Uno Platform, and MewUI

In a prototype workflow, a WPF app can expose runtime APIs such as:

```text
GET  /api/v1/agent/status
GET  /api/v1/ui/tree
GET  /api/v1/ui/element?id=<id>
GET  /api/v1/ui/screenshot
POST /api/v1/ui/tap
POST /api/v1/ui/actions/scroll
```

Those endpoints are intentionally simple. The point is not to recreate the entire Visual Studio experience overnight. The point is to make the running application inspectable and interactive through open surfaces that other tools can build on.

Once that exists, many workflows become possible:

- a CLI tool can capture the current UI tree
- an editor extension can select and inspect runtime elements
- a test tool can collect screenshots and state when a UI test fails
- an AI agent can ask the app what is actually on screen instead of guessing from source code
- community projects can experiment without waiting for a private Visual Studio feature to become extensible

## A Simple WPF DevFlow Scenario

A practical WPF DevFlow might look like this:

1. Start a WPF app built on modern .NET.
2. Open `MainWindow.xaml` in your preferred editor.
3. Change a layout, style, or control property.
4. Keep the app running while you verify the change.
5. Query the runtime UI tree to find the updated element.
6. Capture a screenshot to confirm the visual result.
7. Iterate without losing the context of the running app.

That is the same basic loop developers already want: edit, run, inspect, fix, and repeat quickly.

The difference is that the loop no longer has to belong to one IDE.

## Open Source Changes the Equation

The open-source part matters as much as the command-line part.

When this kind of tooling is closed, the ecosystem can only wait. When it is open, the community can study it, adapt it, port it, and integrate it into other tools.

Microsoft can build a great experience on top of these ideas. So can the community. So can editor authors, test framework authors, and AI tooling vendors.

That is the real shift towards a more open and reusable model for the .NET UI developer loop.

Visual Studio can remain a great front-end, but it should not be the only doorway into runtime-aware UI development.

## What Comes Next

The WPF DevFlow story is still early. There is plenty of work ahead: richer WPF-aware inspection, better editor integration, stronger automation support, and a cleaner model for connecting runtime state back to XAML and code.

But the direction is clear. Combining with our ongoing work on XAML Source Generators for WPF and Visual Studio Code Tools for WPF, we are trying to build a modern developer loop for WPF that is open, reusable, and powerful, and most importantly accessible for everything.

We are not limited to WPF either. We are trying to build shared infrastructure that can be used across WPF, WinUI, Uno Platform, and even emerging UI frameworks like MewUI. The goal is to make it easier for the entire desktop/mobile ecosystem to benefit from these ideas.

## Where to Learn More

Microsoft’s DevFlow work for MAUI is here:

<https://github.com/dotnet/maui-labs>

LeXtudio’s WPF Labs work for WPF, WinUI, Uno Platform, and MewUI is here:

<https://github.com/lextudio/wpf-labs>
