---
layout: post
title: "DockPanel Suite: A Summary on Visual Studio 2012 Light Theme"
description: "This post talks about the Visual Studio 2012 Light theme of DockPanel Suite."
tags: DockPanel-Suite
permalink: /dockpanel-suite-a-summary-on-visual-studio-2012-light-theme-a8391c84c769
excerpt_separator: <!--more-->
---

Previously I have posted about the new theme several times, such as

- [Overall experience]({% post_url 2013/2013-3-22-dockpanel-suite-design-the-theming-experience %})
- [How to write new themes]({% post_url 2013/2013-3-17-dockpanel-suite-how-to-write-a-new-theme %})

Today I made a few more changes to the theme and I believe it is a stable milestone. So this post will serve as a summary of all the works on this new theme.

Visual Studio 2012 Light theme can be seen as one of the biggest features we will introduce in DockPanel Suite upcoming 3.0 release. The story of it is very interesting.

<!--more-->

## Initial Patches Received at GitHub

8 months ago @wvdvegt posted an issue on GitHub asking whether anyone has a new skin for DPS. At that time, both Ryan and I were busy working on other tasks, so we could not spare time on this specific one.

3 months ago, we suddenly received a lot of patches from another guy (I don't want to name him/her and you will see why). I was really interested in the patches, as they look fantastic and we could finally turn DPS to look modern and awesome.

Well, it is strange that when we tried to discuss with the submitter so as to better understand the patches, he/she no longer replied. We were able to work with other contributors in the past and we appreciated those valuable conversations, but this time was really unexpected.

I had to create a separate branch to maintain the patches and started my own hacking on it from time to time.

## The Real Patch Owner at CodePlex

I frequently perform Internet search of DockPanel Suite, in order to understand whether our fork right now becomes popular enough. It was a month ago that I suddenly noticed a CodePlex project called DockPanel Suite VS2012 Look. I began to wonder if I had discovered where the patches originally come from. I sent a mail to its author

> Hi,
>
> I just noticed your project on CodePlex. Are you `https://github.com/******`?
>
> I am writing to see if you can review our changes made in this branch,
>
> https://github.com/dockpanelsuite/dockpanelsuite/tree/gh59
>
> We attempted to incorporate most patches submitted to us by `@******`,
>
> https://github.com/dockpanelsuite/dockpanelsuite/issues/59
>
> However, we are not certain whether all necessary changes are made.
>
> Wish you can reply soon.
>
> Regards,\
> Lex Li

and got a reply as below,

> Hi Lex,
>
> I'm not the owner of `https://github.com/******`?
>
> My project at Codeplex is thought to implement only VS2012 visual style for DockPanel. However it doesn't incorporate the latest changes form https://github.com/dockpanelsuite/dockpanelsuite.
>
> Greetings,\
> Kamen

My guess was confirmed 3 days ago when I finally had time to review all the source code. Every line of changes now can be tracked down and gladly I could tell that I made almost all changes correctly.

Thus I immediately sent a second mail to Kamen,

> Hi Kamen,
>
> Thank you for your explanation.
>
> I have done a review of your patches to DockPanel Suite 2.5. I can confirm that the patches we got from `@******` in fact all come from you.
>
> Thus, I added you to our contributor list.
>
> I have done necessary refactoring to integrate the theme into our latest DPS code base (development_3.0 branch) and also tuned a few settings to better match VS2012. So if you like you can take a look.
>
> Thanks again for your great contribution.
>
> Lex

Of course, Kamen kindly replied again,

> Hi Lex,
>
> I've looked at the code of development_3.0 branch. It is definitely my code. You have done a good job integrating it, and creating a new theme files. I have noticed that you have not ported the colors of the theme as they were, may be to prevent from hardcoding them. The whole theme now looks "lightgrey" without the typical blue for VS2012. If that was your intention, it is fine for me.
>
> Another issue is inherited from my code, and i could not fix it till now, so I've filed an issue report at the GIT hub (https://github.com/dockpanelsuite/dockpanelsuite/issues/124).
>
> Greetings,\
> Kamen

He pointed out two new issues and confirmed that our changes look good,

1. The flicker problem (GitHub#124), which I fixed earlier today.
1. The changes I made to some of the colors, which I revisited and re-tuned earlier today (I have to uninstall Productivity Power Tools as it makes extra changes to the theme).

I would like to thank him again, as without his initial works or his review we could not get so far on this important feature.

## Close Button on Document Tabs (Updated: May 5)

Well, I did not expect that in such a short period of time I finished the last important bit of VS2012 Light theme, the close button on document tabs.

It was more than 2 years ago that a guy (paralleloeter) [posted on SF.net his patches](http://sourceforge.net/p/dockpanelsuite/discussion/402316/thread/c45070d3) for DPS to add close button on tabs.

Well, that patch was not accepted by the coordinator Steve Overton, because DPS only had VS 2003/2005 themes then. I support Steve's decision, as it really looks weird to have close button on tabs.

However, Microsoft seems to choose such a design in Visual Studio 2010/2012, so to finish a complete VS 2012 theme, we will have to revisit this patch.

24 days ago, @dotAge sent us a pull request on GitHub, which he/she claimed contains the original patch by paralleloeter. Both Ryan and I reviewed the pull request, and we could not accept it at that time.

A few hours ago, I was finally passionate enough to continue working on this patch, as hacking on tab colors and resolving #124 have given me enough knowledge on how the strip was designed. So this time I could better control when this close button should appear. Interestingly, it should appears on active tabs, both focused and not focus, and inactive tabs, only when the tab is under mouse. The button also changes color when mouse is hovered. So totally we need to handle five different states.

To avoid flickers when either the tab color or the close button state changes, the calls to Invalidate has also been minimized.

## Dock Indicators (Updated: May 11)

In previous alpha builds the dock indicators for VS2012 theme are still those for VS2005. This has been a major problem but we could not do much due to the following technical challenges,

- VS 2012 dock indicators use transparency, which cannot be simulated by DPS using the current PictureBox based image containers. One possible approach is to use transparency enabled controls (which I did for M8 Theme Builder project), but I did not yet have time to fully explore in that area.
- VS 2012 adds some new dock indicator elements (in fact since VS 2010), such as the nine element dock indicator. This has no counter part in DPS, as DPS only implements a five element dock indicator to simulate VS 2005.

Thus, it is really not easy to implement all required elements for VS 2012 theme in a short period of time without performing heavy refactoring.

Luckily today I spared several hours in this field, and did some initial work

1. Make dock indicator replaceable via theme.
1. For VS 2012 theme, replace VS 2005 images with VS 2012 images.

In the near future I might investigate on how to tune the architecture so as to support the new VS 2012 elements and hope we can finally support the nine-element indicator.

## Final Words

Please download and try out the latest Alpha 6 of DockPanel Suite 3.0 and let us know if there is any issue you meet,

https://nuget.org/packages/DockPanelSuite/3.0.0-alpha6

We will keep working hard on this new theme to make it even better. There are only a few minor issues remaining, which should be easy to solve.

Note that if you use a custom tool strip renderer the final look can be even closer to Visual Studio 2012,

I have added such a renderer to DPS sample project, which is based on the pre-defined color scheme included in ToolStrip Customizer.

Stay tuned.

## Updated on Oct 22, 2015

There is [a new post]({% post_url 2015/2015-10-5-dockpanel-suite-more-about-theming %}) covering VS 2013 Blue theme and separation of core and themes,

## Updated on Sept 5, 2016

Color palettes completely change how a theme can be designed, so I urge all readers to read [the latest post]({% post_url 2016/2016-9-3-dockpanel-suite-theme-reloaded %}).
