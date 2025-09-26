---
layout: post
title: Cleaning Up .NET on Your Desktop: From Command Line to Visuals
description: A practical guide to safely uninstalling old .NET SDKs and runtimes across macOS and Windows—why versions accumulate (global.json pins, previews, hosting bundles, architectures), what the official uninstall tool does and doesn’t surface, and how a lightweight cross‑platform UI adds the missing context for confident cleanup.
tags: .net microsoft
categories: [Programming Languages and Frameworks]
excerpt_separator: <!--more-->
---

On an ordinary evening I ran `dotnet --info` on my Mac and it threw a rather long list at me. And that's when I realized "oh, another time?" So, the story begins.

<!--more-->

## The Installed Versions

As I looked at the output, it became clear that I had accumulated a significant number of SDKs and runtimes over time. Each entry represented a decision made in the past, often with good reason. I still develop on .NET, and many projects target different versions (.NET 8/9/10 at this moment), so from time to time I need to install new SDKs or runtimes. Unless Microsoft has a better way to manage this, I end up with a lot of versions.

## The New Tool

Sadly .NET CLI (aka `dotnet`) does not provide a built-in way to visualize or manage this accumulation, nor is there a .NET SDK Global Tool for this purpose yet.

Microsoft decided to ship a separate command line tool called [.NET uninstall tool, dotnet-core-uninstall](https://learn.microsoft.com/dotnet/core/additional-tools/uninstall-tool) that can remove specific versions. Last round I used it, I had to manually figure out which versions to remove, which was error-prone and time-consuming.

There is an open source project called [Dots](https://github.com/nor0x/Dots) that might help with .NET SDKs, but since it doesn't support runtimes, I didn't find it useful for my scenario. Besides, it has too complex a UI for my taste.

Therefore, I decided to vibe up a simple visual tool with Uno Platform that simply wraps over dotnet-core-uninstall, and you can find it on [GitHub](https://github.com/lextudio/dotuninstall).

## Findings

### Missing Artifacts of .NET Uninstall Tool from Microsoft

The initial version of .NET Uninstall Tool UI was quite basic, and simply wrapped over the command line tool. However, that approach only worked for macOS, where Microsoft did ship both ARM64 and x64 versions of the uninstall tool. On Windows, only the x86 version was available, which meant that users on x64 or ARM64 devices couldn't use it without compiling from source code.

This limitation prompted me to give up the idea of wrapping over the command line tool and instead consuming the uninstall logic directly in the UI tool via submodule. This way, I could ensure that users on all architectures could benefit from the tool without any hassle. Of course, they don't need to install the command line tool anymore.

### The Design of the Uninstall Logic

On macOS, the uninstall logic is relatively straightforward, as everything follows the file system layout. We read the installed SDKs and runtimes from the file system, and we can remove them by deleting the corresponding directories.

However, on Windows, the uninstall logic is more complex due to the presence of MSI product codes and Add/Remove Programs entries. The uninstall logic needs to coordinate with these components to ensure a smooth uninstallation process. That's where I used to have no idea but now learned a lot from the source code of the uninstall tool. So, even if you can see a lot of runtimes/SDKs from `dotnet --info`, you might not be able to find all of them in .NET Uninstall Tool UI, because some of them might have been installed as part of another MSI package (like Hosting Bundle). .NET Uninstall Tool UI only shows the ones that can be uninstalled directly, so that Windows won't be messed up. But this does create some confusion.

## The Future

I will keep enhancing the tool to make it more useful. If you have any suggestions or feedback, please feel free to open an issue or a pull request on the GitHub repository.

This blog post will be updated as well if new findings are made.
