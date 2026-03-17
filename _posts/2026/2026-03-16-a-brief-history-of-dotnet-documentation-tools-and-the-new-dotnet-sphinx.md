---
layout: post
title: "A Brief History of .NET Documentation Tools, and Why I Built dotnet-sphinx"
description: "A journey through .NET documentation tooling history—from NDoc to Sandcastle to modern gaps, and how Lunet and dotnet-sphinx bridge the ecosystem for open source projects."
tags: .net open-source documentation
categories: [Tools and Platforms]
excerpt_separator: <!--more-->
image:
  path: /images/documentation.png
  alt: "API Documentation illustration"
---

A few community projects in the Avalonia ecosystem started using Lunet for .NET documentation generation, so I began experimenting with it for C# SNMP Library. I quickly realized that while Lunet can extract and shape API-oriented content, it doesn't solve the broader problem of how .NET projects can generate documentation that is easy to customize. Lunet itself is a broader static site and documentation tool built around Scriban templates, not just an API extractor, and in my experiments I still found its theming and customization story too limited for what I wanted.

All LeXtudio Inc. documentation sites are built on open-source infrastructure centered around Sphinx. Naturally, I wanted to find a way to integrate .NET API documentation generation with Sphinx, which led to the creation of dotnet-sphinx. But why is this necessary? Why can't we just use existing .NET documentation tools?

The answer requires understanding what happened to .NET documentation tools over the past 25 years. This is a story about ecosystem fragmentation, shifting priorities, and how the open-source .NET community eventually had to build its own solutions.

<!--more-->

## The NDoc Era: Excitement and Silence (2001-2006)

The .NET documentation story begins with NDoc, an early community project from the beginning of the 2000s associated with Jason Diamond, Jean-Claude Manoli, Kral Ferch, and later maintainers such as Kevin Downs. NDoc was innovative for its time. The C# compiler could emit XML documentation comments alongside compiled .NET assemblies, and NDoc turned those inputs into professional-looking reference documentation in a variety of formats, including unusual ones like LaTeX, with multiple presentation styles. For open-source .NET projects, it was *the* tool, much like JavaDoc for Java. Its design was pragmatic, extensible, free, and open source. For years, it was the obvious choice for .NET API documentation.

But NDoc ran into an architectural wall when .NET Framework 2.0 arrived in late 2005. Generic types were a major part of the problem, but not the only one. In a 2005 mailing-list post, maintainer Kevin Downs explained it bluntly: "Generics" had "a *huge* number of edge-cases," while "practically every detail" in the SDK doc format had changed, and the framework itself had become a "moving-target". At that time neither the compiler nor the framework was open source, so community maintainers had limited visibility into how all these changes were evolving. The result was predictable: NDoc's .NET Framework 2.0 support stalled, and the project could not keep pace with the platform anymore.

That old mailing-list thread is still worth reading because it captures the frustration in the authors' own words, not in hindsight. Kevin Downs was not complaining about one missing feature. He was describing a whole documentation pipeline that had become much harder to maintain all at once. That is a much better explanation for NDoc's decline than the oversimplified story that "it just didn't support generics."

> **Why this matters**: When a documentation tool is tightly coupled to a specific language version or runtime, it becomes vulnerable to changes in that language or runtime. If the tool can't evolve with the language, it becomes obsolete. This is what happened to NDoc when .NET evolved faster than its architecture could handle.

At the same time, independent maintainers had no reliable support path from Microsoft for community documentation tooling. When the original NDoc effort stalled in 2006, many open-source .NET projects lost the tool they had come to rely on, with no clear official successor in sight.

But that was not the end of the story. NDoc kept getting revived by different people in different forms. SourceForge later described NDoc3 as being "based on NDoc" with the goal of supporting newer .NET language features, and GitHub still hosts a small merged `NDoc + NDoc3` repository. That persistence matters historically. Even when the original project had effectively died, developers kept trying to resurrect the idea rather than abandon it completely.

That recurring pattern says something important about the ecosystem. NDoc was not just a tool that failed. It was a tool whose problem space remained unsolved badly enough that people kept trying again. The repeated revivals also help explain why many .NET developers remained attached to the older NDoc and Sandcastle style of API documentation long after Microsoft's official attention moved elsewhere.

## Sandcastle: Microsoft's Answer and the Community Afterlife (2006-2015)

Microsoft's response was swift but narrow in scope. In July 2006, just days after NDoc's end-of-life announcement, Microsoft released Sandcastle on CodePlex, an in-house tool that had been developed for generating documentation for the .NET Framework itself and other .NET libraries. Sandcastle was more powerful than NDoc: it had been built in the .NET Framework 2.0 era, understood generics, supported multiple help output formats and themes, and had been battle-tested on one of the largest API surfaces in existence.

But Sandcastle came with a serious early credibility problem: it was initially released on CodePlex without source code, even though CodePlex was presented as an open-source project hosting site. That mismatch created immediate suspicion. InfoQ summarized the mood in 2008 as "an uproar over hosting Sandcastle, a closed-source tool, on the open source site CodePlex." Microsoft eventually published the source in July 2008, but the early confusion had already weakened trust among open-source maintainers.

> **Why this matters**: Licensing uncertainty damages adoption. A powerful tool under an unclear license is often less useful than a weaker tool with clear legal standing, especially for open-source projects that may need to customize or fix it themselves.

Sandcastle also had a second problem: it was heavy, especially on memory. It required running multiple transformation pipelines while holding the entire documentation model in memory simultaneously. This consumed massive amounts of RAM and made the tool slow to run. For large corporate projects with dedicated documentation teams and premium hardware, Sandcastle could be made to work. For small open-source projects, it was often prohibitive overhead.

The emergence of modern and diverse .NET frameworks (.NET Compact Framework, Silverlight, Windows Phone, Portable Class Library, and others) led to more complexity in generating the right kind of documentation, and the .NET documentation landscape started to fragment. Some projects used slowly evolving Sandcastle. Others used commercial solutions or built their own. Some abandoned the problem entirely and documented their APIs through tutorials and blog posts instead of generated reference docs.

> **The key insight**: When a language evolves faster than its tooling, the tooling becomes a bottleneck rather than a solution. Projects stop generating reference documentation and rely on IntelliSense and tutorials instead.

Gradually, Sandcastle gave way to a new generation of documentation tools that were more lightweight and more flexible.

And yet Sandcastle did not simply vanish when Microsoft walked away. Eric Woodruff's Sandcastle Help File Builder had already become the practical front end many users relied on, and after Microsoft ended official development, the Sandcastle tools were effectively folded into that community-maintained world. Woodruff's own documentation states that the last official Microsoft release was in June 2010, that Microsoft ceased support in October 2012, and that the tools were then merged into the Sandcastle Help File Builder project for future development and support. So while Microsoft's stewardship ended, Sandcastle itself survived by being handed over, in practice, to a community maintainer who kept the ecosystem alive.

That handoff deserves to be part of the story because it complicates the easy narrative. Sandcastle was never the open, lightweight answer many community projects wanted. But unlike some abandoned Microsoft tooling, it did get a real afterlife. The center of gravity shifted from Microsoft to Eric Woodruff and the broader SHFB ecosystem. That is one reason Sandcastle still lingers in real projects today instead of existing only as a historical footnote.

## DocFX: The Internal Pivot (2015+)

When Microsoft pushed the broader .NET ecosystem forward again and made .NET Core a reality, that evolution made it harder for older documentation tools to keep up, and harder for projects to generate documentation that accurately reflected what developers actually needed to know. This period also saw the rise of alternative documentation hosting in other language ecosystems. Read the Docs and Sphinx became one of the most recognizable documentation stacks in open source, especially in the Python world.

Sphinx was built for Python. It had no built-in understanding of .NET types, namespaces, or API structures. If you wanted to use Sphinx for .NET documentation, you had to work around it. Interestingly, the ASP.NET 5 documentation site at docs.asp.net was "hosted and built" at Read the Docs "using Python and Sphinx" when Scott Hanselman noted this in 2015. So the idea of pairing .NET documentation with Sphinx was not purely hypothetical. It did appear once in part of Microsoft's ecosystem, but Microsoft's broader documentation strategy soon standardized on DocFX instead, and Sphinx fell out of favor for .NET API reference generation.

DocFX supported Markdown input, could be integrated into CI/CD pipelines, and understood .NET constructs natively. For projects willing to invest in building and deploying their documentation, DocFX could work well.

But for many independent maintainers, DocFX often felt optimized for Microsoft-scale documentation workflows rather than the lighter, more customizable setups that smaller projects wanted. It also never fully replaced Sandcastle's strengths for everyone. Sandcastle had a mature ecosystem around presentation styles, help-file workflows, and tools such as Sandcastle Help File Builder. DocFX moved in a different direction, and depending on your needs that could feel like simplification or regression. The frustration around its roadmap also dragged on for years. In 2021 users were still asking "are there any news regarding a planned release date for docfx v3?" and in 2024 a maintainer closed one public issue by saying that "docfx v3 has been moved as an internal project to support Microsoft Learn only." Later, the public repository README stated that "Microsoft Learn no longer uses docfx" and that the project had transitioned to the .NET Foundation. That is a strange little saga even by documentation-tool standards.

> **The communication problem mattered as much as the technical one**: From my vantage point as a long-time community participant, the rationale behind the roadmap shift was never clearly communicated to the broader .NET community. That opacity damaged trust beyond the technical issues themselves.

So yes, there is plenty to criticize here. Missing features compared to Sandcastle, long-lived issues, roadmap confusion, and years of uncertainty around the public future of major workstreams all made DocFX harder to trust than its technical ambitions suggested. Even when it worked, it often felt like you were borrowing part of somebody else's internal machinery rather than adopting a tool that truly treated outside users as first-class citizens.

This pattern has shown up in several public .NET tools as well. Try .NET, .NET Interactive, Polyglot Notebooks, and Azure Data Studio all illustrate a similar trust problem: tools that were useful to the wider community eventually lost momentum or were retired once they no longer aligned with Microsoft's current priorities. Layoffs and cost pressure likely made that environment even less friendly to long-tail community tooling. For independent maintainers, the lesson is not that every Microsoft-backed tool is doomed. It is that building on tools controlled by a single vendor always carries risk.

There was no clear, accessible path for an independent open-source .NET project to generate professional API reference documentation and host it on the open infrastructure that other language communities took for granted. One of LeXtudio Inc.'s open-source projects, C# SNMP Library, had been using DocFX for a while but fell back to Sandcastle for API reference documentation.

## The Lunet Discovery and the dotnet-sphinx Option (2026+)

Lunet has been around for years and was started by Alexandre Mutel. It can generate documentation within its own Scriban-centered workflow, and it is useful—I do not want to undersell that. But when I evaluated it for C# SNMP Library, I realized it wasn't specifically designed to make .NET API content feel native inside the Sphinx ecosystem. My own evaluation ended with the same practical conclusion: I still wanted a cleaner bridge into Sphinx, better theme choices, and a documentation stack that felt more natural for the kind of open-source sites I like to maintain.

Sphinx is a documentation generator used by Python, Django, Pallets, NumPy, and thousands of open-source projects. It has mature themes (PyData, Furo, Alabaster), integrates seamlessly with Read the Docs, and has a decades-long track record of producing professional documentation. When you publish documentation built with Sphinx, readers get a familiar, well-designed experience.

That gap had attracted multiple experiments over the years. Projects like [SphinxForDotNet](https://github.com/hach-que/SphinxForDotNet) (archived March 2022) and others attempted to bridge .NET and Sphinx, but none matured into a widely adopted solution that stayed actively maintained. Most were archived or stalled after their creators moved on.

dotnet-sphinx is the latest attempt to connect .NET to this ecosystem. You run `dotnet sphinx`, which generates the API metadata and converts it into Sphinx-compatible output. Your documentation sits alongside your narrative posts, examples, and guides. The rest is processed by the well-established Sphinx documentation system.

### See It In Action: C# SNMP Documentation

Look at the [C# SNMP documentation repo](https://github.com/lextm/sharpsnmp_docs) as an example. It uses dotnet-sphinx generated API reference files (`.rst`). The generated documentation integrates seamlessly with Sphinx. You get the Furo theme, consistent navigation, and the built-in search and sidebar that Sphinx provides.

This matters because it means an open-source .NET project can now say: "Our documentation is built with the same kinds of tools as many popular Python projects, hosted on the same infrastructure, and follows familiar conventions." In that setup, generated `.rst` files live beside hand-written guides, while Sphinx handles navigation, search, and theming.

### The Pipeline: From Assembly to Published Docs

The pipeline is straightforward:

1. **Run** `dotnet sphinx` (the .NET SDK Global Tool)
2. **Extract metadata**: It generates `*.api.json` files containing type information
3. **Generate documentation**: It reads the JSON and outputs RST or Markdown
4. **Process with Sphinx**: Your documentation build system processes the output alongside your other hand-crafted materials
5. **Publish**: Read the Docs or any Sphinx-compatible host publishes the result

dotnet-sphinx focuses on one job: translating .NET constructs into Sphinx-compatible markup. It doesn't try to be a full documentation generator. It doesn't manage themes. It doesn't handle deployment. Sphinx already does all of that better than ever.

Note that while DocFX can also generate Markdown files, its output is optimized for DocFX's own publishing pipeline. DocFX-generated Markdown would require additional conversion or tweaking to work cleanly with Sphinx's cross-references, directives, and link formats. dotnet-sphinx generates ReStructuredText and Markdown specifically tailored for Sphinx compatibility from the start. The output integrates seamlessly with Sphinx themes, MyST extensions, and the broader Sphinx ecosystem without requiring post-processing.

### Design Philosophy

This is the key philosophical difference from earlier .NET documentation tools. Rather than trying to solve the entire problem—extraction, formatting, theming, hosting—the approach embraces the principle of composition. Lunet owns extraction: it understands .NET assemblies and produces clean JSON. dotnet-sphinx owns translation: it converts that JSON into Sphinx-compatible markup. Sphinx owns publishing: it handles themes, search, navigation, and the rest of the infrastructure.

Each tool is focused. Each does one thing well. Together, they solve the problem that NDoc, Sandcastle, and even DocFX never quite addressed: making .NET documentation generation feel natural within the open-source ecosystem.

### For .NET Library Authors Who Care About Documentation

If you're maintaining an open-source .NET library and want to generate professional API reference documentation without being locked into a proprietary tool or heavy infrastructure, dotnet-sphinx offers a reliable solution. You can generate content in ReStructuredText for Sphinx, integrate it with Read the Docs and community-friendly themes, and keep your entire documentation workflow simple and composable.

But the choice of documentation infrastructure should belong to you, not to a single vendor's strategic priorities. dotnet-sphinx generates Markdown as well, so you can use the API reference output with any static site generator or documentation tool that supports Markdown. Hugo, 11ty, MkDocs, Astro—whatever ecosystem you prefer. The goal is to extract your API reliably and then let you choose where it goes.

> **For commercial teams as well as open-source maintainers**: Free and open-source solutions like Sphinx produce professional results without vendor lock-in. Given what happened to DocFX, Try.NET, and Polyglot Notebooks—tools that were public until Microsoft's internal priorities changed—you're not betting your documentation infrastructure on whether a vendor's strategic focus will shift. Mature themes, active community support, and full customization make the cost-benefit analysis straightforward.

## Why This Matters: Building for Resilience

The history of .NET documentation is a cautionary tale about ecosystem fragmentation, shifting priorities, and how the open-source .NET community eventually had to build its own solutions.

Python succeeded partly because Sphinx grew into a mature, reusable documentation system that worked across many hosting platforms and inspired tooling for other languages. Java's ecosystem thrived because JavaDoc was standardized and well-understood. .NET spent years with tools that were either too restrictive, too heavy, or too proprietary—often controlled by a single vendor with shifting priorities.

Lunet offers one path with native .NET-oriented generation and styling. dotnet-sphinx offers another: integration with Sphinx. Together they show that the .NET community does not need to reinvent documentation wheels from scratch. We can build on established, community-driven ecosystems instead.

dotnet-sphinx is not trying to replace every .NET documentation tool. It is trying to make .NET documentation feel at home in an ecosystem that already solved publishing, theming, navigation, and hosting remarkably well.

## Further Reading and Sources

### NDoc Era (2001-2006)

- [NDoc on Wikipedia](https://en.wikipedia.org/wiki/NDoc)
- [Kevin Downs on .NET Framework 2.0 support in the NDoc mailing list](https://sourceforge.net/p/ndoc/mailman/ndoc-users/thread/001301c5c982%244b9bf290%240200a8c0%40D9100/)
- [NDoc3 on SourceForge](https://sourceforge.net/projects/ndoc3/)
- [The merged NDoc + NDoc3 repository on GitHub](https://github.com/twpol/ndoc)

### Sandcastle Era (2006-2015)

- [Sandcastle on Wikipedia](https://en.wikipedia.org/wiki/Sandcastle_%28software%29)
- [InfoQ: Sandcastle source release](https://www.infoq.com/news/2008/07/Sandcastle-Rerelease/)
- [Sandcastle Help File Builder on GitHub](https://github.com/EWSoftware/SHFB)
- [Eric Woodruff's Sandcastle/SHFB documentation](https://ewsoftware.github.io/SHFB/html/bd1ddb51-1c4f-434f-bb1a-ce2135d3a909.htm)

### Sphinx and the .NET Gap (2015+)

- [Read the Docs on Sphinx hosting](https://about.readthedocs.com/tools/sphinx/)
- [Scott Hanselman on docs.asp.net and Sphinx](https://www.hanselman.com/blog/aspnet-5-and-net-core-rc1-in-context-plus-all-the-connect-2015-news)
- [SphinxForDotNet on GitHub (archived)](https://github.com/hach-que/SphinxForDotNet)

### DocFX: Promise and Internal Pivot

- [DocFX repository README](https://github.com/dotnet/docfx)
- [DocFX issue #7050: asking about v3 release timing](https://github.com/dotnet/docfx/issues/7050)
- [DocFX issue #9901: v3 moved to internal Microsoft Learn effort](https://github.com/dotnet/docfx/issues/9901)

---

If you enjoyed this historical overview, explore more history-focused posts in the [History category]({{ site.baseurl }}/categories/history/). You'll also find related deep-dives under the [.NET]({{ site.baseurl }}/tags/net/) and [open-source]({{ site.baseurl }}/tags/open-source/) tag pages.