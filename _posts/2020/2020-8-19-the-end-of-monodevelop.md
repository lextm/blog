---
categories: [Frameworks and Libraries]
description: Discover why Microsoft abandoned MonoDevelop, the implications for cross-platform .NET development, and what alternatives developers should consider using instead.
excerpt_separator: <!--more-->
image:
  alt: Copyright © Lex Li. River side, Montreal.
  path: /images/riverside.jpg
layout: post
permalink: /the-end-of-monodevelop-80b383dab34b
tags: .net linux microsoft mono visual-studio xamarin visual-studio-code open-source
title: The End of MonoDevelop
---
Microsoft abandoned [MonoDevelop GitHub repository](https://github.com/mono/monodevelop/graphs/contributors) earlier this year, and we can see no commit was pushed since February. However, there is no official announcement from any Microsoft channel on why that happened.

<!--more-->

As a long time Mono observer, I wrote two blog posts in the past regarding MonoDevelop's status,

- [The Rough History of MonoDevelop]({% post_url 2019/2019-5-20-brief-history-of-monodevelop %})
- [Status of MonoDevelop/Xamarin Studio]({% post_url 2017/2017-7-24-status-of-monodevelop-xamarin-studio %})

I will explain below why I don't think the sudden change is sudden, and provide my personal opinions.

## The Value of MonoDevelop for Microsoft

Most Microsoft developers are on Windows without a doubt. And recently via VS Code and VS for Mac, Microsoft has been able to reach developer communities on macOS and Linux. But one fact we must consider is that Linux desktop market share is rather small (<1% by certain stats), so VS for Linux has been requested but never fulfilled. Therefore, there is no obvious ROI for Microsoft to keep investing in MonoDevelop for Linux, and we saw more and more issues in the past few years,

1. No more binary package of MonoDevelop for various Linux distributions.
1. Many issues to compile the latest code base on Linux.
1. The repository was polluted by Microsoft private NuGet feeds and private code repositories (though some repos became open sourced later on).

## The Investment on MonoDevelop from Microsoft

While no clear revenue comes from Linux user base, MonoDevelop has been the foundation of VS for Mac. So Microsoft can still earn something back from macOS users.

However, to keep MonoDevelop as a full feature IDE for different operating systems (Windows, macOS, and Linux), the developers must spend time fixing Windows/Linux related issues, which most of the times does not contribute much to the revenue.

Most importantly, to keep MonoDevelop open sourced, Microsoft had to release certain code base from VS for Windows (such as vstest, and part of the code editor) under an open source license. This often requires a lengthy internal process with legal guys, and lots of efforts to clean up the code.

Another factor to consider is that competitors in the same field might make use of the newly released code to compete with Visual Studio. For example, JetBrains Rider reused vstest code base to implement MSTest support, which was never part of Rider before. (Recently JetBrains decided to switch from vstest to its brand new testing infrastructure though.)

## Conclusion

A company like Microsoft might not be able to continue its investment when the revenue does not meet the expectation. So it is a natural move to stop contributing to the open source MonoDevelop.

That does not mean VS for Mac is impacted negatively, but good news,

1. VS for Mac can continue its evolution without releasing changes to GitHub.
1. More VS for Windows code can be reused in VS for Mac, and no more pressure to release such to the public.

There might be some difficulty for VS for Mac extension developers, as they lose a good reference on how VS for Mac works internally, but there are alternative ways.

> There has been an attempt to revive MonoDevelop by the community, or at least keep it as it was for the existing users, so let's see what happens next there on [GitHub](https://github.com/dotdevelop/dotdevelop/issues).

If you have to stay on Linux and want to program in .NET, please switch to VS Code or Rider.

This is the end of an important MonoDevelop chapter, and I start to wonder what might happen to Mono when .NET 5 is released later this year. I will write about that when the time is right.

Stay tuned.

> Update: Microsoft finally marked the MonoDevelop repository as archived on GitHub. That confirms the end of this open source IDE on its side.
