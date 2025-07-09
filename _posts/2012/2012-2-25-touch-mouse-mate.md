---
layout: post
title: "Touch Mouse Mate"
description: "This post is about a new open source project I am working on this weekend, named Touch Mouse Mate."
tags: Windows
permalink: /touch-mouse-mate-74b8fe2ec7e1
excerpt_separator: <!--more-->
---
Here I announce a new open source project I am working on this weekend, named Touch Mouse Mate.
<!--more-->

Microsoft releases a product called Touch Mouse early last year (August 2011 per http://www.zdnet.com/blog/btl/hands-on-review-microsoft-touch-mouse/54264).

http://www.microsoft.com/hardware/en-us/products/touch-mouse/microsite/

Compared to a normal mouse, it is slightly different in the following way,

* It supports multi-touch
* It supports gestures
* BAD, it does not support middle click (Arc Touch Mouse supports that)
* WOW, it has an SDK

I should have done better analysis before buying it (Artist Edition) last week but it only costs 299RMB now (roughly 47USD) so I still think it is a good deal.

To work around the middle click issue, I came across a utility authored by J5, an Italian developer,
http://www.blogtecnologico.it/2011/12/how-to-enable-middle-click-on-microsoft-touch-mouse/

However, like the comments pointed out, there are a few issues with the code base. As it drew my attention and I was really willing to fix the issues, I created a fork last night and started my typical weekend hacking tour this time on Touch Mouse SDK.

Now my first day achievement is out there on GitHub, released under MIT/X11 license,
https://github.com/lextm/touchmousemate

And its CodePlex homepage is being prepared and will be online in the coming days.

If you cannot wait until the installers are available on CodePlex, you can compile the code base following the instructions in readme.txt.

Stay tuned.