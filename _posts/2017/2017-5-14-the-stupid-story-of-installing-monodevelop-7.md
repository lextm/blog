---
layout: post
title: "The Stupid Story of Installing MonoDevelop 7"
description: "This post is about how to install MonoDevelop 7 on Linux and all remaining issues."
tags: Mono
permalink: /the-stupid-story-of-installing-monodevelop-7-223c1420915b
excerpt_separator: <!--more-->
---

Finally Parallels decided to make its Mac product a Lite edition and freely available if you do only run non-Windows guest OS. I accepted this offer and install CentOS for the very second time in my lifetime. Visual Studio Code worked fine on it, but soon I found that I could not run MonoDevelop, as there is no FlatPak for CentOS!
<!--more-->

Thus, after so many days of ignorance, I decided earlier today to try again, by installing a Fedora box. Well, then you will find that how ugly [the existing documentation](https://fedoraproject.org/wiki/MonoDevelop) is.

Yes, isn't it well written? Nope, till you try the steps you immediately hit lots of issues.

My machine runs FlatPak 0.6.12, and it does not like the `--from` syntax at all and keep saying

> "error: Operation not supported"

And it was only via Google I learned that maybe I should first use wget to download the links to text files and then feed them to the naughty flatpak command. It really sucks if its developers never realize such issues.

Then another error happened

> error: runtime/org.freedesktop.Platform/x86_64/1.4 not installed

So that I had to ask Google again and found this fix,

``` bash
flatpak install gnome org.freedesktop.Platform/x86_64/1.4
```

And at last I got all the necessary bits and this MonoDevelop instance started to work.

But wait... even with this IDE installed, I could hardly do any serious projects, like debugging a console project.

I gave up at this stage.

Hope it helps you out when you attempt the same.

BTW, I went and voted on "Visual Studio for Linux" feature [here](https://visualstudio.uservoice.com/forums/121579-visual-studio-ide/suggestions/18433768-visual-studio-for-linux-os). If that's Microsoft's solution to the MonoDevelop 7 mess, I wish it can be there ASAP.
