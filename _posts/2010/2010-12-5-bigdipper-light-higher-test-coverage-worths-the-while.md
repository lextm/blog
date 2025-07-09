---
layout: post
title: "BigDipper Light: Higher Test Coverage Worths the While"
description: "This post is about the value of high test coverage."
tags: SNMP
permalink: /bigdipper-light-higher-test-coverage-worths-the-while-267c5d979e44
excerpt_separator: <!--more-->
---
The first time I read about high test coverage, I was curious about two points,

1. Is it possible?
1. Does it worth the while?

The longer I had been applying TDD in my development, the easier it seemed to make the impossible-to-test code testable. However, I still didn't trust the ROI of high test coverage until I dived into #SNMP 7.0, the BigDipper release.
<!--more-->

On the first day I performed a few crazy actions on the code base and it may introduce millions of bugs if no unit cases is available. Believe me. As least three times I broke several cases in those hours, and debugging those small test cases made it super fast to resolve the issues in only a few minutes. Once NUnit gave me all green, I knew I was done. That also feels good.

I could not believe that there were still so many bugs in the code base until this weekend I started to pay special attention to coverage. Typically existing test cases ensure the code works in a way I want under ordinary scenarios. But how does it work under all exceptional scenarios? Is there any misbehavior that I can foresee? I don't know as that's what is missing in test cases.

To test out the exception handling part, new test cases were added, and more lines were visited by NUnit and PartCover. Then existing issues revealed themselves,

* Missing null argument checking.
* Wrong ToString implementation.
* Ambiguous exception handling.
* So many others …

It is so hard to write new test cases :) as I have to create exceptional scenarios, which sometimes requires mocking. But the fun I find is really priceless, and now I get a better understanding how #SNMP behaves under those scenarios.

Well, increasing test coverage takes time, and I hope we can make core #SNMP 100% covered by next April. Then 7.0 release can be fabulous.

Stay tuned.