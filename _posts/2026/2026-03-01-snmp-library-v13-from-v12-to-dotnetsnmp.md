---
layout: post
title: "C# SNMP Library 13.0: Why v13 Matters in the Age of Modern .NET Networking"
description: "Microsoft’s push for modern .NET networking (ASP.NET Core/Kestrel) made a new foundation practical for v13, enabled SNMP over TCP, and turned a risky rewrite into a meaningful step forward."
tags: .net snmp open-source csharp
categories: [Programming Languages]
excerpt_separator: "<!--more-->"
image:
  path: /images/cibc-square-after-rain.jpg
  alt: Copyright © Lex Li. CIBC Square after rain in Toronto.
---

The v12 line of C# SNMP Library has been reliable for years. It was already modernized in the 12.5 era when Microsoft improved the runtime significantly in .NET 6, and for most users it simply worked. So why did we decide to do v13 at all?

Over the last few years, Microsoft has poured real effort into modern networking on .NET. If you build services on ASP.NET Core and Kestrel, you’ve seen it: better performance, better diagnostics, better primitives, and a clearer path for building high-throughput network servers without living in a swamp of legacy APIs.

Once that shift became obvious, staying on the old foundation started to feel like we were freezing C# SNMP Library in amber. SNMP is “old” as a protocol, but the way people deploy it today is not. You run it in containers. You run it beside web services. You run it with modern observability and modern security expectations. If .NET networking is moving forward, SNMP tooling should not be the thing that drags your stack backward.

That’s the real reason v13 had to happen.
<!--more-->

## The moment the rewrite started to make sense

In v12, we carried a lot of historical weight. It wasn’t just about features. It was about what the implementation was built on, and what kinds of improvements were realistically possible without turning the codebase into a patchwork.

When Microsoft’s newer networking work (and the ecosystem around it) became the default choice for server developers, we finally had a good answer to the question “what are we modernizing toward?”

v13 is our move to that world: a version of C# SNMP Library that fits naturally into a modern .NET service environment.

## System.Formats.Asn1: choosing a better foundation

System.Formats.Asn1 is a modern, high-performance ASN.1 library from Microsoft, when it was needed by the .NET runtime itself to handle ASN.1 parsing for things like TLS and X.509. It’s designed for performance, correctness, and security in mind, and it’s maintained as part of the .NET platform ever since.

DotNetSnmp was the first public experiment with System.Formats.Asn1 in the SNMP space, and it showed that it could handle the ASN.1 structures in SNMP with good performance and reliability. That gave us confidence that it was a solid foundation for v13.

Therefore, when we started the v13 rewrite, we made the decision to build the core ASN.1 handling on System.Formats.Asn1 instead of maintaining our own custom implementation. That was a big architectural change, but it was the right one for the long-term health of the library.

We naturally started with the DotNetSnmp core and expanded its capabilities to cover all the features we already shipped in v12. That way, we could ensure that the new foundation was solid.

## System.Threading.Channels and SNMP over TCP

Microsoft also invested in System.Threading.Channels, which is a modern, high-performance producer-consumer library for .NET. It’s designed for building pipelines and handling asynchronous data flows efficiently. Years of real-world use in ASP.NET Core and other high-throughput scenarios have proven its value, so it was a natural choice for building the transport layer in v13.

Another benefit of using Channels is that it made implementing SNMP over TCP much more practical. In v12 and before, we focused on SNMP over UDP, which is the most common transport for SNMP. But SNMP over TCP has some advantages in certain scenarios, such as better reliability and support for larger messages, and it's supported by some devices and use cases. So, while adopting Channels was primarily about improving the core architecture, it also opened the door to adding SNMP over TCP support in a way that fit well with the rest of the library.

## Compatibility, but with sane boundaries

One trap in a rewrite is pretending nothing changes. Another trap is breaking everything and calling it “progress.”

We tried to do something more boring and more useful: preserve what can be preserved, but draw clear boundaries where modern .NET choices are non-negotiable.

The biggest one is platform support.

v13 targets modern .NET (aka, .NET 8+) and drops .NET Framework. That decision is not a moral judgment about .NET Framework. It’s a practical recognition that the future of .NET networking and server hosting is not there.

Since v13 was built upon DotNetSnmp with its own set of public APIs, we have to include v12 compatibility shims to make sure existing users can upgrade without breaking changes. But we also have to be honest about the fact that some of those shims are just that: compatibility layers that allow old code to run, but they won’t get the full benefits of the new architecture in early builds. Over time, we expect to evolve those shims and determine if both DotNetSnmp and the v12 compatibility layer can coexist, or if we need to make a more explicit break.

## Performance: the strongest proof that v13 was worth it

The final performance story is better than I expected: v13 shows major gains in almost all measured paths.

In the full matrix runs, representative `v13 beta 2` numbers versus v12 showed:

| Test Name | Latency | Allocation |
|-----------|---------|-----------|
| ParseV1 | -76.87% | -83.49% |
| ParseV2 | -76.22% | -83.52% |
| ParseV3Auth | -50.99% | -69.57% |
| ParseMixedBatch | -72.57% | -77.69% |
| DataFactoryV2 | -92.51% | -92.73% |
| EncodeV2Get | -38.49% | -73.02% |

The practical takeaway is clear: this rewrite did not just modernize architecture. It also delivered measurable speed and allocation improvements where users spend most of their runtime.

## Beta timeline (what to expect, not a changelog)

The v13 beta line is moving in small, test-backed steps. You’ll see features land as they become reliable, not as one huge risky merge.

As of the first betas in late February 2026, the focus has been:

- establishing the new foundation (ASN.1 + core alignment),
- keeping SNMPv3 flows correct and fast,
- bringing in transport work like SNMP over TCP,
- and validating everything through integration tests.

If you’re watching the releases closely, you’ll notice the theme: correctness and performance together first, and only then convenience APIs.

## Closing thoughts

v13 exists because modern .NET server development exists.

Microsoft’s investment in networking and server infrastructure changed what “good” looks like for .NET libraries. For C# SNMP Library, that made a rewrite meaningful instead of just risky. It’s not about chasing novelty. It’s about making sure SNMP tooling fits into the stacks people actually run in 2026.

If you build SNMP tools or services on .NET, v13 is our attempt to meet you where you are now, not where the ecosystem was a decade ago.

## More C# SNMP stories

To explore more on this topic, check out all posts tagged [SNMP]({{ site.baseurl }}/tags/snmp/).
