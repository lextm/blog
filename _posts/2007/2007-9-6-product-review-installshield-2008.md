---
layout: post
title: "Product Review: InstallShield 2008"
description: "This post is about InstallShield 2008."
tags: Windows
permalink: /product-review-installshield-2008-e80bed2f9336
excerpt_separator: <!--more-->
---
One reseller of InstallShield strongly recommend me about InstallShield 2008. So why not take a look at it?
Nice features of InstallShield are,

1. Dialog Preview. When I work in IA, I need to open a dialog to see what it looks like but that's not yet straight forward. IS generates previews for dialogs so it takes me no time.
1. ISICE & ISBP. They are additional installer validation rule sets added by InstallShield. I am not sure whether IA contains additional rules except Microsoft's standard ICE.
1. RSS feed. Yes, I really want to know why IA does not provide a friendly RSS feed so I can get latest information through Google Reader.

However, after all I prefer InstallAware, because some great features I cannot live without,

* Debuggable MSIcode. I can set break point and watches to locate bugs.
* Ribbon UI. Yes, it is cool.
* Cheap. I can save a lot of money.
* Customization. I can write my own runtime packages easily. I can modify dialog box just like using Delphi.
* Localization Support. You do not need to buy the dearest SKU in order to get localization support.
* Great showcase. CodeGear switches from InstallShield to InstallAware to build installers for Delphi and C++Builder. Because Delphi is one of the most complex application on Windows platform, the new installation experience can reflect that IA is better than IS. Microsoft used IS in the past but since it defines MSI, it seems to use home cooked MSI builder for most of its products.

But of course, you need to learn about what IA is not capable of and whether you can receive good support from the vendor.

If you want open source alternatives, I strongly recommend you consider WiX or Inno Setup.

BTW, IMHO there are some not-so-useful features in InstallShield too,

1. Require EULA Reading. I believe most users like me hate this feature so why IS adds this feature to the installers. I can see no value it adds to my installers. But I know somebody likes that.
1. Visual Studio integration. I'd like to integrate installer creation into continuous integration process but that only requires a command line install script builder. So I really do not think Visual Studio integration is necessary. I enjoy working in InstallAware Studio outside VS because the Ribbon UI is much easier to access than menu and tool bars.

(Updated: Christopher Painter dropped a comment here earlier today. He let me know some important logic behind the scene.

I know little about TFS in fact except I use its service through CodePlex.com. Even if it is possible to do everything in VS as he pointed out, I still want to run a batch file and make everything down. Why? Launching VS on a not-powerful-enough computer wastes a lot of time while running a batch file is much faster. If you like to use a batch file, then VS integration is not that necessary.

About EULA reading, even if installers created by InstallShield require me to scroll down to the end, I do not read those terms to make me silk. In fact, end users are not lawyers so how can they understand those words?)
<!--more-->