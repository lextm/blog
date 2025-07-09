---
layout: post
title: "GrapeVine Voice: Pass FxCop And NDepend"
description: This posts talks about FxCop and NDepend generated reports.
tags: Code-Beautifier-Collection Delphi
permalink: /grapevine-voice-pass-fxcop-and-ndepend-ad7cbe830db2
excerpt_separator: <!--more-->
---
Why I did not release GrapeVine 6.0 yet? I thought I'd better review the source code carefully so FxCop and NDepend were used to analyse the code base.

As expected there were a lot of critical issues in the reports. So I planed to spend the last few weeks fixing most of them.
<!--more-->

If you know FxCop, you must notice FxCop 1.36 Beta 2 is a significant improved version. Not only does it make use of multi-threading carefully, but it has more rules included as well. What's more? Every rules has a detailed description available online. Wish the team can further improve the descriptions and samples because I found items like this (I cannot find the corrected code so have to navigate elsewhere) are not fully/well documented.

Today I have fixed most FxCop reported issues. From tomorrow on, I shall start to fix NDepend issues. So if everything goes fine, the Final will be released in January.

Stay tuned.

BTW, if you are developing a .NET application, FxCop and NDepend verifications should be done periodically so as to keep common coding issues away.
