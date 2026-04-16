---
layout: post
title: "My Emails to AvaloniaUI"
description: "Several emails I sent to the AvaloniaUI team, covering business inquiries and proposed collaboration details. The purpose of sharing these emails is to promote transparency and provide reference to avoid misunderstandings in the community."
tags: .net open-source visual-studio-code
categories: [Tools and Platforms]
excerpt_separator: <!--more-->
---

Today I’m sharing several outbound emails I sent to the AvaloniaUI team last year. They cover our initial outreach and a collaboration proposal around VS Code tooling. I’m publishing them as a reference so future discussions can cite the original text instead of second-hand summaries.

<!--more-->

## Notes

The content below contains only my original outbound emails. I am not publishing any replies, and I am not quoting private correspondence from the other side.

Redactions are intentional. I removed personal contact details, outdated links, and anything that could identify our clients.

My goals in publishing these emails are straightforward:

- Correct public misunderstandings about what I proposed.
- Show that the fork and the outreach were motivated by practical VS Code user needs, not drama.
- Document the collaboration options I offered (and the constraints I agreed to), so future discussions can reference the original text instead of second-hand summaries.

This is not a callout post. It is a reference post.

## Why publish now?

These emails are from August 2025. I’m publishing them now for three reasons:

- The ecosystem has continued to evolve, including new community tooling such as the AXSG toolset (XamlToCSharpGenerator) that made modern XAML tooling more practical.
- Public discussions later referenced these emails, sometimes with significant mischaracterizations.
- Having the original text available makes it easier to discuss the topic based on facts rather than paraphrases.

## What I wanted to achieve

At the time, the outcome I hoped for was simple: a healthier VS Code tooling path for developers who choose Avalonia, ideally with an upstream-friendly collaboration model that reduced fragmentation and made responsibilities clear. That did not materialize, and we moved forward independently.

---

## Email One

**Context**: At this time, the official Avalonia VS Code extension hadn't received updates in months. Several of our clients were asking us to maintain an alternative, suggesting a real gap in the ecosystem. This email was meant to understand Avalonia's intentions before we further proceeded independently.

Time sent: August 18, 2025

Recipient: AvaloniaUI

Subject: Question on Future of Avalonia VS Code Support

Email body:

> Hi xxxx,

We’ve been following your team’s work on the upcoming Visual Studio 2022 extension and the recent licensing discussions with great interest.

For many developers, including some of our key clients, VS Code (on macOS/Linux) and VS 2022 (on Windows) are the critical environments for Avalonia UI–based apps — Rider is typically not part of their workflow.

We’ve noticed that the official VS Code extension hasn’t been updated for some time. Could you share whether there are plans to revisit VS Code tooling after the VS 2022 extension ships?

At the request of our clients, our team has started maintaining a fork of the Avalonia VS Code extension:

(link to the fork made by LeXtudio Inc.)

where we’ve investigated and resolved most of the known issues in the past few days. Naturally, we’re curious about what happens next.

Best regards,  
Lex Li  
Director of Engineering  
LeXtudio Inc.  

---

## Email Two

**Context**: This is where I outlined the collaboration proposal. Note the three-tier model: a community edition (well maintained, no registration required), a commercial/Accelerate edition (premium features), and shared maintenance responsibilities with clear role separation. The goal was to avoid ecosystem fragmentation while respecting Avalonia's strategic interests.

Time sent: August 19, 2025

Recipient: AvaloniaUI

Subject: Re: Question on Future of Avalonia VS Code Support

Email body:

> Hi xxxx,

Thank you for your thoughtful reply and for clarifying Avalonia’s position on trademarks and contribution preferences. We’ll make sure to adjust our naming and attribution to align with Avalonia’s guidelines.

I’d also like to share a bit more context around why we created a fork. While we initially intended to contribute directly, we noticed that many PRs in the official VS Code repo had remained pending for months without review or merging, which is concerning. In addition, some of our changes required coordination across multiple repositories (VS Code extension + AvaloniaVS), which made it difficult to deliver timely fixes. Given our clients’ urgent needs, we decided to fork everything and ship updates quickly.

That said, we would much prefer to see our improvements merged upstream and avoid any fragmentation of the ecosystem. The open question for us is whether Avalonia tooling — including the language server — will ultimately remain open source in a way or strictly move into a closed-source model. That direction is important to understand so we can align our work appropriately.

Looking ahead, we’d like to propose a collaboration model that supports both community adoption and Avalonia’s sustainability goals:

- Community Edition: A maintained VS Code extension with essential features, ensuring accessibility for all developers.
- Commercial/Accelerate Edition: Premium features integrated with Avalonia’s Accelerate program, with revenue supporting Avalonia’s long-term goals.
- Shared Maintenance: LeXtudio can take the lead on day-to-day VS Code extension maintenance, while Avalonia defines the roadmap, manages the language server, and ensures alignment with your overall strategy.
- Brand Alignment: Extensions and related tooling clearly co-branded and trademark-compliant, so there’s no confusion in the ecosystem.

This approach avoids duplication, ensures developers have reliable VS Code tooling, and gives Avalonia a path to monetize premium features without losing the open-source adoption that drives growth.

My team bring experience maintaining large-scale VS Code ecosystems (e.g., the reStructuredText/Sphinx extension and its affiliated extensions with 700k+ active users), delivering both open and commercial language servers, and providing premium enterprise support with global partners. We’d be glad to put this expertise behind Avalonia’s tooling roadmap.

Would you be open to a follow-up conversation on how we could make this work together?

Best regards,  
Lex Li  
Director of Engineering  
LeXtudio Inc.  

---

## Email Three

**Context**: When Avalonia responded with feedback on their trademark and branding expectations, we immediately acted. This email shows that we: (1) accepted their concerns, (2) began rebranding our fork, (3) offered to contribute via pull requests within their guidelines. This is the opposite of a "hard fork", we respected their boundaries and worked to align with their direction.

Time sent: August 20, 2025
Recipient: AvaloniaUI
Subject: Re: Question on Future of Avalonia VS Code Support
Email body:

> Hi xxxx,

Thank you for your clear response. We understand and respect AvaloniaUI OÜ’s updated trademark guidelines.

As requested, we have already started the cleanup process through two new releases of our VS Code extension under a different name, with the Avalonia icon and any references that could cause confusion removed. The fork was created in good faith, but we fully recognize the need to avoid confusion and ensure the Avalonia brand remains exclusively under your control. If helpful, your team is welcome to review and suggest any additional adjustments.

Our motivation was to enrich the VS Code developer experience for Avalonia users, particularly at a time when official updates had stalled and many issues remained unresolved. While we appreciate Avalonia’s full control of trademarks and official tooling, we also believe that a healthy ecosystem benefits from new contributors.

If the collaboration options I mentioned previously are not the right fit, we are very open to learning what kinds of contributions or community involvement you would prefer. To that end, we are cleaning up our code changes and plan to start sending pull requests in the coming weeks — assuming such contributions are welcome and there is a clear roadmap for the VS Code extension.

We would be glad to align our work with Avalonia’s direction and avoid duplication while respecting your trademarks and official ecosystem boundaries.

Best regards,  
Lex Li  
Director of Engineering  
LeXtudio Inc.  

---

## Where things stand now

There is no further email in this series since no reply was received after the last outbound mail.

We continue to maintain our open source VS Code extension and coordinate with the AXSG toolset as it evolves. If future discussions reference these emails, this post exists so readers can verify what was actually written.

---

## On the misquotations

Recently, claims have surfaced that my proposal was: *"commercialize the VS Code extension so we pay you to maintain it."*

This is inaccurate. The actual proposal outlined can be seen from the second email above. The model was never "pay us to maintain your fork." It was "create a sustainable path where both tiers coexist, and the community benefits from continuous updates."
