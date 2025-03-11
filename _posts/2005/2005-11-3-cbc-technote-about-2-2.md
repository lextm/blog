---
layout: post
title: "CBC TechNote: About 2.2"
description: A post about the latest version 2.2 of CBC.
tags: Code-Beautifier-Collection Delphi
permalink: /cbc-technote-about-2-2-754f219938dc
excerpt_separator: <!--more-->
---
(Originally published to CSDN on Nov 03, 2005)

I think about this lately, and find there are still lots of stuffs. So maybe I should spend more time on learning .NET programming. Today, I studied TreeView and Splitter basics. Now the options dialog looks much clearer. It looks like the BDS options dialog a bit now. Vow!
<!--more-->

Also I add an About dialog. But it is still simple now.

I should make an installer if I won't follow marc's smart way. That should be convenient. But I cannot make sure whether the compiled assemblies I provide could run well on other's BDS. I need more experiments on these subjects.

What else? I should make a more detailed user manual. In that manual, I should add a lot of pictures/screenshots, and more measures users should take. I don't want to include a help file (hlp or chm). First I never make one before. Second, it may not be as beautiful as a manual. Luckily, CBC is such a simple wizard that there is no need to tell the users a lot.

I am rushed to my feet when releasing this 2.1 version although I've done a lot of release candidates this time. I add a lot of changes but I haven't waited until I test every piece. Now a lot of tiny problems out there.

The debug versions work alright, but the release versions not. The users should delete the default namespace `Lextm` in the options/application in order to correct this problem.

Next time when I release 2.2, I should pay more attention to testing. I do more testing now. I first did a demo to learn the new technique I need, and then port its lines into CBC. So I can be sure that it works in my way. It is a good approach. And I should use CBC a relative long time myself before releasing a build. If I did this last time, I should have found this bug earlier (but now I posted it with the bug on BDN! Many users should be sad, and I am really sorry).

After all, it works. And I believe it is usable.

I am learning a lot there days. Thanks to CBC period, and it is the best time of my life.

Now I am happy to add that, 2.2 has already been done on my dev machine. Soon it should be release to replace the buggy 2.1 on your PC.
