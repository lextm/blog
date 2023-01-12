---
layout: post
title: "DockPanel Suite: Story of A Same Old Brand New Theme"
description: "This post is about how I created a new theme for DockPanel Suite."
tags: Code-Beautifier-Collection Delphi
excerpt_separator: <!--more-->
---
You probably know already that we are now publishing DockPanel Suite themes separately in many NuGet packages. Only the VS 2005 theme is built-in, as many DPS elements hook to it too tightly.

It is quite beneficial to split the themes out, as it enables more frequently rolling out of new themes or updated themes without touching the core. And now I even use a new theme to solve the multiple UI thread support.
<!--more-->

So the story began a few years ago, when we were working on the 2.8.0 release in 2012. One patch merged at that time is to modify `LocalWindowsHook` (GitHub 69) so that it works in a multithreading scenarios. Soon we discovered that there were people using multiple UI threads (GitHub 79), but luckily that did not require any further change on our side. It was last year that guys from XO Energy sent us a pull request (GitHub 241) to inform us that they solved a few issues and they were using multiple UI threads in their applications.

I was against the pull request at the very beginning, as the change will mess up the code base not just a little bit. Meanwhile, it would be a concern that how many developers do need such a change. The discussion was fierce, and no further action was taken. I did check the XO Energy fork recently, and noticed that they were following our main repo actively, and had to re-apply their patches over our changes, which probably is a pain for them.

Is there a way out to ease them from custom patches? Well, unbelievably last night I thought that we could do a new theme as an experiment.

Thus, today I applied their patches to the main repo, moved a few classes to a new theme named "VS2005Multithreading", and changed a few tiny things accordingly. Then in just a few hours that theme is ready for testing. All XO Energy changes now are safely isolated in that theme, and no line of change is required in the core assembly.

Hope that they can test out this new theme and let me know if everything works fine.

Stay tuned.
