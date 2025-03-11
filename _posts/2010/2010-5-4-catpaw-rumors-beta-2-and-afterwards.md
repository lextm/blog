---
layout: post
title: "CatPaw Rumors: Beta 2 and Afterwards"
description: "This post is about future plans of #SNMP 5."
tags: SNMP Mono
permalink: /catpaw-rumors-beta-2-and-afterwards-ce41cef93014
excerpt_separator: <!--more-->
---
#SNMP 5 goes on smoothly. I just had two items to work on when I started,

1. SNMP v3 support in the Agent.
1. SNMP v3 support in the Browser.

However, many hard things jump in the way, especially Mono support, so though we are now at Beta 2, a lot of interesting items are now in the list.
<!--more-->

On April 10, I finally found some courage to boot openSUSE and tested #SNMP against Mono. The journey started with Mono issues, and I hardly believed more and more issues were waiting ahead. Well, I posted about them in an earlier post, but even that was not complete since I reported two more later. It is happy to see that Mono team actively involved and fixed many of them. Besides, almost all issues I found can be worked around. So before Mono 2.8 hits the road, #SNMP will use those workarounds.

The Agent was ported to Mono/openSUSE first, and that's because it has only one form. And I gained a lot of experience from this migration, such as platform dependent code separation, workaround identification. Then when suddenly I decided to port the Browser and the Compiler, I have some confidence on what I should pay much attention to.

Porting DockPanel Suite must be the hardest thing I ever thought of, but my plan worked out very smooth. It's so lucky that we simply commented out what cannot be ported easily and such changes only affect drag and drop, a feature #SNMP does not really rely on. As things sped up so soon, we are able to see a full port to Mono/openSUSE in 5.0 Beta 2.

Today I finished a lot of project file cleaning. The project files were initially created in SharpDevelop and Visual C# 2005 Express, and then upgraded to Visual C# 2008 Express. It was recently that we migrated again to Visual C# 2010 and MonoDevelop. Though MSBuild script is used for csproj files, we must confess that different IDE vendors choose to make use of it differently (even VS generates terrible csproj structure if I dig the files further). So price was paid when I had to avoid csproj file changes from MonoDevelop. Soon I gave up SharpDevelop. Now I recreated all the project files in VS2010 and will only check in csproj file changes from Visual Studio or Notepad. Note that I did not mean I don't use MonoDevelop or SharpDevelop. I just never accept their changes to the projects.

Upgrading old projects also show me how .NET evolves. In the past, resource files are embedded into resx files in BASE64 formatted bytes. But now resx files are much smaller, as we only define in them which files will be fetched and embedded. So I have to delete all old resx files and recreated them cleanly.

Besides, the project structure is heavily changed and useless projects are finally removed. As now we have official VB.NET and C# samples, VB.NET developers can learn how to use #SNMP easier. Personally I would like to also add Delphi Prism samples as I love this language, but I just don't have a license of it yet.

SNMP v3 support in the Agent is almost finished. We will see if authorization can be added beautifully in 5.0 release. If not, it will be delayed to 6.0.

SNMP v3 support in the Browser is 80% complete. I still need to check how to implement v3 WALK. Luckily I have some ideas now and I just need time to put them down to C# code. :)

Stay tuned.
