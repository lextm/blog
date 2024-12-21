---
layout: post
title: "DockPanel Suite: More About Theming"
description: "This post is about how new themes are developed and distributed in the future."
tags: DockPanel-Suite .NET
permalink: /dockpanel-suite-more-about-theming-48864f47892c
excerpt_separator: <!--more-->
---
Ever since I finished integrating the VS 2012 light theme into DPS, we see demands on other themes. The community is much stronger than we thought and new theme authors are now with us.
<!--more-->

## VS 2013 Blue Theme from Thijs Elenbaas

Thijs developed this blue theme earlier this year, and successfully covered many elements (dock pane tabs and so on). So now we can see the sample project running in this blue theme.

There are still many more elements to tune, but at least now it looks good.

The changes are now in a separate branch for incubation. More details can be found at [#316](https://github.com/dockpanelsuite/dockpanelsuite/issues/316).

## VS 2012 Dark Theme from Various Sources

I knew DPS has been forked multiple times already, but never realized so many people are interested in the dark theme. But now we can find three different forks containing dark themes. I didn't have time to evaluate their completeness, but created an task to track down their progress in the future. More details can be found in [#317](https://github.com/dockpanelsuite/dockpanelsuite/issues/317).

## Themes in Separate Assemblies

Probably this is not about a new theme, but it is about how new themes can be developed and distributed in the future, so let's see how it works.

In the past, all themes are shipped in the main assembly of DPS. This design has a few limitations,

1. With new themes such as the VS 2013 blue one coming, it would be pretty crowded to put everything there.
1. It would be a waste of spaces if DPS users only use a single theme or a selected set, by shipping all themes together.
1. For theme authors, it would also be a pain to create new themes and send us pull requests, as they might change tons of files.

When I introduced the theming classes a while ago, one unfulfilled goal is to actually split themes to their own assemblies. Today, I am glad to announce that this goal is done, and we have separate projects for themes.

Except that VS 2005 theme stays in DPS main assembly for compatibility, all other themes are moved out.

This brings a few advantages,

1. New themes can be created without affecting the main assembly. Some types might need to change to public in the main assembly so that in themes they can be reused, but such changes should be trivial and easier to be accepted in PR.
1. New themes can be developed gradually from existing ones. The VS 2013 blue theme is an example, which currently reuses many elements from VS 2012 light theme. The project structure demonstrates how to achieve this without breaking the VS 2012 light theme.
1. New themes can be shipped as separate assemblies and NuGet packages. This should help DPS users a lot, as they just need to pack up necessary themes, but not all.

If you would like to write a new theme, now it is the time.
