---
layout: post
title: "Stack overflow issue of DockPanel Suite on Mono"
description: "This post is about stack overflow issue of DockPanel Suite on Mono and how I investigated on it."
tags: Mono DockPanel-Suite
permalink: /stack-overflow-issue-of-dockpanel-suite-on-mono-514a0c896d98
excerpt_separator: <!--more-->
---

The issue information can be found at https://github.com/dockpanelsuite/dockpanelsuite/issues/16

It was in May 2010 I first attempted to port DockPanel Suite to Mono, so as to [bring #SNMP to Linux]({% post_url 2010/2010-5-2-dockpanel-suite-tip-5-we-can-go-mono %}) and any other operating systems supported by Mono.

But at that time I met two difficulties,

- I could not find a way to let DPS switch to lite mode on Mono, while use full mode on .NET.
- My apps crashed immediately once closed.

Years later [I came across a patch]({% post_url 2012/2012-2-17-dockpanel-suite-patch-to-support-lite-mode-on-mono %}) for the first one in February.

I should have found it earlier, right? But anyway this patch is now part of DPS 2.6 release.

About the second, a workaround was found in 2010 that if all known DockContent objects are closed before disposal starts then the crash won't occur. This workaround has been used in #SNMP, but of course it is very inconvenient.

From the bug report on GitHub you might find that how I attempted to locate the culprit.

<!--more-->

## Initial Attempt

I documented the steps on how to reproduce the crash on Mono. I even got the complete call stack, but it was to hard to analyze and not very useful at that time (well, it is in fact useful, but the information is not obvious enough).

## JArchitect's Patch

Soon I remembered that JArchitect uses DPS on Mono (http://codebetter.com/patricksmacchia/2011/11/07/real-world-feedback-on-a-net-to-mono-migration/), so I wrote to Patrick for help. He kindly introduced JArchitect's Product Manager Issam Lahlali. The story went on unbelievably, as Issam shared with me their build of DPS, and suddenly I noticed they started from my fork of DPS on #SNMP.

https://github.com/dockpanelsuite/dockpanelsuite/issues/18

JArchitect's patch worked as expected, but honestly speaking, they hacked on many Dispose methods and that seems not good to me. Therefore, I decided to pursue my investigation on the root cause.

## Lighting Hit

@jumpinjackie posted his patch last week which tries to avoid multiple calls to the same Dispose method. His changes are in the DockConentHandler.Dispose. That reminds me suddenly of how to identify the culprit. So today I finally found a simple way to get the obvious hint I wanted.

My approach is to add Console.WriteLine to those Dispose methods to mark the enter and leave events. Then once closed, the function calls can be easily analyzed from console output.

Below is the output I got on Windows (configured DockSample project as a console application),

``` text
Enter AutoHideWindowControl 7
Leave 7
Enter DockPanel 5
    Enter MdiClientController 9
    Leave 9
    Enter DockPaneCollection 6
        Enter DockPane 11
            Enter VS2005DockPaneCaption 12
            Leave 12
            Enter VS2005DockPaneStrip 13
            Leave 13
            Enter DockContentHandler 10
Enter DockPane 11
                Leave 11
            Leave 10
        Leave 11
    Leave 6
    Enter DockContentHandler 8
    Leave 8
Leave 5
```

Below is the output I got on Mono/openSUSE,

``` text
Enter AutoHideWindowControl 7
Leave 7
Enter DockPanel 5
    Enter MdiClientController 9
    Leave 9
    Enter DockPaneCollection 6
        Enter DockPane 11
            Enter VS2005DockPaneCaption 12
            Leave 12
            Enter VS2005DockPaneStrip 13
            Leave 13
            Enter DockContentHandler 10
Enter DockPane 11
                    Enter VS2005DockPaneCaption 12
                    Leave 12
                    Enter VS2005DockPaneStrip 13
                    Leave 13
                    Enter DockContentHandler 10
                        Enter DockPane 11
                            Enter VS2005DockPaneCaption 12
```

Fine. Now it is obvious that the culprit is in DockPane.Dispose instead of DockContentHandler.Dispose.

I think Mono and .NET use different disposal implementation, which finally leads to the issue. I might debug further, but decide to stop right now by simply changing DockPane.Dispose.

The new patch has just been committed to GitHub, and will be part of DPS 2.7 release. You can find more information about DPS at http://dockpanelsuite.com

Stay tuned.
