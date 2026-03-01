---
layout: post
title: "Obfuscar 3.0: A Late System.Reflection.Metadata Migration, Finally Done"
description: "This post shares the real engineering story behind Obfuscar 3.0: why the SRM migration started later even after ILSpy had already blazed the trail, how AI tools accelerated day-to-day refactoring and test work, what breaking changes users should expect, and how performance tuning moved real-world slowdown from about 2.0x toward a much smaller gap."
tags: .net csharp open-source obfuscar
categories: [Programming Languages]
excerpt_separator: "<!--more-->"
image:
  path: /images/obfuscar-in-ilspy.png
  alt: Obfuscar inspected in ILSpy.
---

If you have followed Obfuscar for a while, you probably remember that 2.2 lasted much longer than many people expected. It kept receiving practical fixes, and I also wrote about some details along the way, such as [global tool support]({% post_url 2018/2018-3-9-make-obfuscar-a-global-tool-in-net-core %}) and [local-variable expectations]({% post_url 2022/2022-12-27-obfuscar-question-on-local-variables %}).

So why only now for 3.0 and System.Reflection.Metadata? The short answer is: I knew the direction for a long time, but only recently had the right momentum to execute it end to end.
<!--more-->

## What is System.Reflection.Metadata (SRM)?

For many years, Mono.Cecil was the practical foundation for tools that needed to read and rewrite IL. It offered a friendly object model, broad compatibility, and enough flexibility to power decompilers, weavers, and obfuscators. Tools like NDepend and Obfuscar lived in that world. The architecture was productive, and the ecosystem around Cecil was mature enough that most problems had known patterns and known workarounds.

IKVM.Reflection became another option when the Mono compiler stack started to shift toward it. But it was more of a niche choice, and the Mono compiler ecosystem itself was not as dominant.

Microsoft open-sourced its compiler platform as the Roslyn project, and with it came a new metadata API: System.Reflection.Metadata (SRM). This is a modern low-level metadata stack: fast readers, predictable memory usage, and APIs designed for compiler/tooling scenarios. It first appeared publicly as a prerelease NuGet package in **2014** (`1.0.17-beta`, Oct 10, 2014), and reached its first stable package in **2015** (`1.0.21`, May 11, 2015). Over time, SRM became a serious option for heavy-duty tooling, not just an experimental API.

ILSpy, a widely used .NET decompiler, moved from Mono.Cecil to SRM years ago, and that migration produced real-world lessons on metadata reading, type/member resolution, etc. I monitored that process closely, and it was clear that SRM was the future for .NET tooling. So I had the direction in mind for a long time, but the actual migration only made sense when the timing and resources finally aligned.

## Obfuscar's long tail on Mono.Cecil

Release 2.x had a stable user base and predictable behavior. With millions of downloads on NuGet.org, it was clear that many users relied on it for production obfuscation.

The key reason this migration to SRM waited so long is that Obfuscar was not using Cecil in a shallow way. It was deeply integrated with Cecil's object model and behaviors:

- assembly/module/type/method traversal logic was built around Cecil APIs,
- renaming and reference-update flows relied on Cecil-specific metadata shapes,
- resolver behavior and many edge-case fixes were tuned against Cecil semantics over years of bug reports.

So moving to SRM was not a simple "swap one library for another." It required rebuilding core assumptions in multiple layers:

- metadata abstraction and reader/writer pipeline,
- assembly resolution strategy,
- rename/reference correctness for generics, inheritance, and attributes,
- broad regression test expansion for real assemblies.

That takes significant resources: design time, implementation time, benchmark/profiling time, and support time after release.

Most importantly, the risk is carried by end users if migration quality is not high enough. A core metadata rewrite can break production flows in painful ways like compatibility and performance regressions.

As long as 2.2 could keep moving with targeted fixes, it was hard to justify taking all those risks at once. "Knowing what to do" and "doing it without burning users" are very different tasks.

## What changed recently

Recently, AI tools made the mechanical part of the migration much faster and became the real accelerator. I still made all architectural decisions myself, but AI drastically reduced the time spent on repetitive work:

- drafting first-pass refactors,
- generating and expanding test cases,
- surfacing missing branches in control flow,
- helping compare behaviors between old and new implementations.

In other words, AI did not replace engineering judgment. It removed much of the typing and iteration friction. Once the work started in earnest, the beta timeline moved quickly.

I deliberately chose some breaking changes. The most visible ones are in configuration and attribute semantics.

First, configuration is now strict:

- absolute paths are required for key settings and path attributes,
- `$(...)` placeholders are rejected at runtime.

I know this can hurt old build scripts. But permissive path behavior was a long-term source of environment-specific surprises.

Second, `ObfuscationAttribute(ApplyToMembers=false)` now follows strict semantics in 3.0. If you use `MarkedOnly=true`, you may need explicit member-level attributes where 2.2 behavior used to feel "implicit."

These changes are less convenient in the short term, but more predictable in the long term.

If you are moving from 2.2 to 3.0:

1. Convert Obfuscar config paths to absolute paths.
2. Expand `$(...)` values before runtime and feed Obfuscar the final generated config.
3. Audit `ObfuscationAttribute` usage if you rely on `MarkedOnly=true`.
4. Test against representative real assemblies, not only sample projects.

## Closing

Obfuscar 3.0 is late only if you look at the calendar. From the engineering side, it arrived when the project finally had enough pressure to justify the rewrite and enough tooling leverage to finish it at speed.

The ILSpy SRM migration showed the direction years ago. AI tooling helped turn that known direction into shipped code.

## More Obfuscar stories

To explore more on this topic, check out all posts tagged [Obfuscar]({{ site.baseurl }}/tags/obfuscar/).
