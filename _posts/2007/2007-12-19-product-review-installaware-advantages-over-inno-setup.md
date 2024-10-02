---
layout: post
title: "Product Review: InstallAware Advantages Over Inno Setup"
description: This post is about InstallAware and why it is better than Inno Setup.
tags: Windows
permalink: /product-review-installaware-advantages-over-inno-setup-f39f8d9c9f2
excerpt_separator: <!--more-->
---
I do not like to do this kind of comparison because IMHO a commercial software should be better than the open source one or it is going to die. But [this post](http://www.hadihariri.com/Blogs/Atozed/20071218A.aspx) makes me speechless so I guess I can at least put down my opinions here.

We all know that CodeGear's partnership with InstallAware does not come easily but in all the decision should be rational. What is unexpected is that part of the current result is happiness while the other part is pain.
<!--more-->

Pros,

* Delphi can be installed without a media kit. This kind of installation experience is cool.
* One installation for all languages.
* InstallAware enables you to debug the installer script with a debugger. Using break point is fantastic and a performance boost.
* Visualization really reduces your time on the script. Support for those runtimes (.NET FX, SDK, and J#) are just a few clicks away.

Cons,

* MSI based installation is slow. Even though Microsoft holds the key, its Visual Studio and Vista SP1 installation is rather slow too.
* Downloading such a large project from Internet kills people who used to fast pace. For me, it is still tolerable.
* MSI installer can kill the author sometimes. There has been a lot of complaints over CodeGear's installer especially for the December Update (and I just cannot install Microsoft SQL Server 2005 Express on my computer).

Can Inno Setup save CodeGear or Delphi users at last? I do not know. What I know is that,

1. I cannot easily debug IS script (some of my script can be debugged in Delphi but that just verifies the algorithm without runtime break point and live information).
1. lack of first class .NET or other runtimes support. I have to search for .NET related script sample here and there.
1. There is not enough visualization so you have to write code most of the time. So the quality of your script is dependent on your experience with IS.

But I believe IS is best in at least one way. The installer created is not MSI based, so it runs as a flash. Pascal script is more capable of MSIcode.

Do not know what CodeGear will do in the near future but wish those guys can make something right that clears the clouds and mists around InstallAware, or switch again to miserable uncertainty.

Long live Delphi

(Update: I do not mean to look down upon Inno Setup, who serves Code Beautifier Collection well for so long. But more evidence is needed to prove it is perfect for CodeGear RAD Studio, isn't it? CodeGear is building something critical for other developers' success, so every step it takes should be careful.)
