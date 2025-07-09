---
layout: post
title: "A Call to The Community: DockPanel Suite History and Future"
description: "This post is about the history and future of DockPanel Suite."
tags: DockPanel-Suite
categories: [History, .NET]
permalink: /a-call-to-the-community-dockpanel-suite-history-and-future-ec3b9ab8bdc9
excerpt_separator: <!--more-->
---
This post may be revised and finally published to https://github.com/dockpanelsuite/dockpanelsuite/wiki. Please visit there if you want to receive updates.

DockPanel Suite homepage is now at http://dockpanelsuite.com.
<!--more-->

Microsoft first introduced the docking panel layout in Visual Studio .NET (2002), and soon it became popular in application design. Many commercial .NET component vendors started to provide docking libraries initially, but there was no good free and open source alternative, until WeiFen Luo released DockPanel Suite (DPS for short) on SourceForge.net in 2006.

## WeiFen Luo's Efforts and Early Years

Its 1.0 release was available on Feb 13, 2006, one day before the Valentine's day [1]. From the SVN repository we could no longer find the commits earlier than Mar 2, 2007. Therefore, we don't know exactly when WeiFen decided to implement this docking library and the day he started.

This release has been downloaded more than 57,000 times on SF.net alone (binaries + source package), which is a huge success.

After that, WeiFen published several new releases. Release 2.2 was available on Nov 04, 2007 (more than 68,000 downloads)[2], and release 2.3 was available on May 08, 2009 (more than 68,000 downloads)[3].

Danilo Corallo wrote an article titled "A Visual Studio 2005-like Interface"[4] on CodeProject.com initially on Jun 06, 2006 to introduce this library for broader audience. The article has been reviewed for more than 586,000 times with an average rate of 4.89. This article was last updated on 22 Jan, 2007, so it only targets DPS 1.0. However, DPS 2.0 and above do contains breaking changes, so the sample of this article does not work with newer DPS releases.

SharpDevelop [5], the open source C#/VB.NET IDE, has chosen DPS as its docking library for years (till SD 4.0 migrates to WPF and uses AvalonDock [6] instead of DPS). It is interesting that from SD code base, DPS source files appeared as early as Jan 04, 2005 [7].

On Aug 16, 2009, WeiFen wrote in a discussion thread, that he would like to move this project to CodePlex.com [8]. However, this move was never carried out. But in this thread WeiFen linked one of his important blog posts on DPS [9], which documented his ideas on why WPF based docking library is better. WeiFen's interest has been moved to WPF side product called WPF Docking [10].

## Extended Maintenance by Steve Overton

Steve Overton stepped up and started to maintain this library in 2010 [11]. He managed to release 2.4 on Oct 30, 2010 with a few patches [12]. For the first time, DPS is released with binaries/source code/release notes. This release has been downloaded over 8000 times. Soon release 2.5.0 (with RC1 flag) was available on Nov 25 the same year with more patches included [13]. This is the last stable release that can be found on SF.net with accumulated downloads of 61,000.

## Sidenote on My Work

I have been a DockPanel Suite user since 2007, where I used this great library in a commercial product. DPS is also used in my open source project #SNMP [14]. My main interest is how to use it on Mono and other operating systems. My attempt was initialized in May 2010 [15], and finalized in Feb 2012 [16].

This patch, as well as many other patches of DPS, has not been reviewed or merged to the trunk, which makes it again difficult for users to make use of them.

## Sidenote on New Implementation

There is a new implementation published on CodePlex for DPS [17]. It claims that with the changes it resolves many DPS known issues. But whether its changes can be ported back to DPS is still under investigation.

## New Hope and A Call to The Community

Frustrated DPS users started to discuss about the future of this project [18], and soon some agreed to create a fork on GitHub [19].

The new repository was created using svn2git [20] by me, and now is hosted on GitHub under dockpanelsuite organization,

The short term plan is to merge all existing/known patches for DPS 2.5 release, and prepare a 2.6 release. New features may appear in 3.0 release [21].

As NuGet becomes a new channel to distribute libraries, DPS 2.6 will also be available via NuGet [22].

If you have any patch to share, or you would like to help contribute to this new fork, please consider the following,

## Guide on Submitting Patches

Note that you don't need to create any issue, as a new issue will be automatically created when you finish step 4.

1. Learn about GitHub via http://help.github.com/.
1. Create your own fork from https://github.com/dockpanelsuite/dockpanelsuite.
1. Make the changes on your fork, and test it fully.
1. Create a pull request back.

Patches will be reviewed and merged as early as possible.

## Guide on Reporting Bugs/Starting Discussions

Note that if you already have a patch for the issue you meet, please follow "Guide on Submitting Patches".

1. Learn about GitHub via http://help.github.com/.
1. Create a new issue on https://github.com/dockpanelsuite/dockpanelsuite/issues.

You may also use SF.net tracker [23], but it is not recommended. Issues recorded on SF.net may be gradually fixed in this fork.

## References

[1][DockPanel Suite 1.0.0.0]
[2][DockPanel Suite 2.2]
[3][DockPanel Suite 2.3.1]
[4][A Visual Studio 2005-like Interface]
[5][ICSharpCode]
[6][AvalonDock]
[7][SharpDevelop on GitHub]
[8][DockPanel Suite Forum Topic 1]
[9][WPF vs Windows Forms]
[10][WpfDocking Overview]
[11][DockPanel Suite Forum Topic 2]
[12][DockPanel Suite 2.4.0]
[13][DockPanel Suite 2.5.0 RC1]
[14][Sharp SNMP Library]
[15][DockPanel Suite Tip]
[16][DockPanel Suite Patch]
[17][Guo Yong Rong on Codeplex]
[18][DockPanel Suite Forum Topic 3]
[19][DockPanel Suite Forum Topic 4]
[20][svn2git on GitHub]
[21][DockPanel Suite Issues]
[22][DockPanel Suite Pull Request]
[23][SourceForge Tracker]

[DockPanel Suite 1.0.0.0]: http://sourceforge.net/projects/dockpanelsuite/files/DockPanel%20Suite/1.0.0.0/
[DockPanel Suite 2.2]: http://sourceforge.net/projects/dockpanelsuite/files/DockPanel%20Suite/2.2/
[DockPanel Suite 2.3.1]: http://sourceforge.net/projects/dockpanelsuite/files/DockPanel%20Suite/2.3.1/
[A Visual Studio 2005-like Interface]: http://www.codeproject.com/Articles/14336/A-Visual-Studio-2005-like-Interface
[ICSharpCode]: http://www.icsharpcode.net/OpenSource/SD/Default.aspx
[AvalonDock]: https://github.com/xceedsoftware/wpftoolkit/wiki/AvalonDock
[SharpDevelop on GitHub]: https://github.com/icsharpcode/SharpDevelop/tree/c4336b038c23fa37ee19bdd7d27bfa29b575a4a4/src/Libraries/DockPanel_Src
[DockPanel Suite Forum Topic 1]: http://sourceforge.net/projects/dockpanelsuite/forums/forum/402316/topic/3368441
[WPF vs Windows Forms]: http://www.devzest.com/blog/post/WPF-vs-Windows-Forms-From-Control-Authoring-Perspective.aspx
[WpfDocking Overview]: http://www.devzest.com/WpfDocking.aspx?Show=Overview
[DockPanel Suite Forum Topic 2]: http://sourceforge.net/projects/dockpanelsuite/forums/forum/402316/topic/3879095
[DockPanel Suite 2.4.0]: http://sourceforge.net/projects/dockpanelsuite/files/DockPanel%20Suite/2.4.0/
[DockPanel Suite 2.5.0 RC1]: http://sourceforge.net/projects/dockpanelsuite/files/DockPanel%20Suite/2.5.0%20RC1/
[Sharp SNMP Library]: http://sharpsnmp.com
[DockPanel Suite Tip]: {% post_url 2010/2010-5-2-dockpanel-suite-tip-5-we-can-go-mono %}
[DockPanel Suite Patch]: {% post_url 2012/2012-2-17-dockpanel-suite-patch-to-support-lite-mode-on-mono %}
[Guo Yong Rong on Codeplex]: http://guoyongrong.codeplex.com/
[DockPanel Suite Forum Topic 3]: http://sourceforge.net/projects/dockpanelsuite/forums/forum/402316/topic/5080422
[DockPanel Suite Forum Topic 4]: http://sourceforge.net/projects/dockpanelsuite/forums/forum/402316/topic/5271451
[svn2git on GitHub]: https://github.com/nirvdrum/svn2git
[DockPanel Suite Issues]: https://github.com/dockpanelsuite/dockpanelsuite/issues
[DockPanel Suite Pull Request]: https://github.com/dockpanelsuite/dockpanelsuite/pull/8
[SourceForge Tracker]: https://sourceforge.net/tracker/?group_id=110642