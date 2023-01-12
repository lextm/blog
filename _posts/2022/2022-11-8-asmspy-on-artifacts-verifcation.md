---
layout: post
title: "AsmSpy on Artifacts Verification"
description: A post about how to use the tool AsmSpy to verify dependent assembly versions to avoid runtime issues
tags: Visual-Studio .NET
excerpt_separator: <!--more-->
---

We often perform artifacts verification via test suites, so for .NET projects NUnit/xUnit.net/MSTest might be quite helpful. However, there is a kind of issues that cannot be easily caught by test suites, and I found AsmSpy a perfect tool in this field. In this post, I will give an example.

<!--more-->

## Out-Of-Control Dependent Assembly Versions

I have shipped multiple versions of PHP Manager for IIS in the past few years, but it was recently that [one issue](https://github.com/phpmanager/phpmanager/issues/53) reported back on `Microsoft.Web.Administration` reference,

``` text
Could not load file or assembly 'Microsoft.Web.Administration, Version=7.9.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35' or one of its dependencies. The system
 cannot find the file specified.
```

I think you might have seen similar exceptions in the past, and not surprised at all. I blogged about [the cause and solution]({% post_url 2015/2015-5-29-whats-microsoft-web-administration-and-the-horrible-facts-you-should-know %}) a long while ago, so fixing the bug was just a few minutes.

## The Long Term Defense

However, this time I started to think about whether I could find a permanent way to prevent it from happening again, such as a verification step in CI manifest. Of course, I can write a tool based on Mono Cecil which won't take much long, but doesn't a tool exist already?

I did search for a while and found many tools in this field relying on project files (`*.csproj`). While they can be useful in some scenarios, clearly they cannot be used for this specific task that relies on assembly scan.

[AsmSpy](https://github.com/mikehadlow/AsmSpy) was not at the top of search results, but turned out to be good enough for my case. Install it via Chocolatey, and then
I can easily generate a report of all referenced assemblies in an output folder. A simple search in that report in AsmSpy console output can identify any unexpected assembly versions. Thus, I added this step in [verify.ps1](https://github.com/phpmanager/phpmanager/blob/v2.9/verify.ps1).

If your projects face similar challenges and want to identify compilation issues early, check out AsmSpy and it's a nice addition to your toolbox.
