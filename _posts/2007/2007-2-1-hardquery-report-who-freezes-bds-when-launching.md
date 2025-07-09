---
layout: post
title: "HardQuery Report: Who freezes BDS when launching"
description: "This post reports a problem when launching CBC in Delphi 2006."
tags: Code-Beautifier-Collection Delphi
permalink: /hardquery-report-who-freezes-bds-when-launching-cba788e99b53
excerpt_separator: <!--more-->
---
(CSDN Feb 01, 2007)

Hi Lex,

I tried to use your CBC in D2006 but it prevents D2006 from opening.

Completely freezers up the loading process.

I would like to have a look when you get this resolved so please keep me

posted.

Kind Regards

Grant Brown
<!--more-->

==========================

This is another email sent from a CBC's user. Thanks Grant.

And the following is my reply:

==========================
Grant,

Thanks for reporting this.

When I worked on older versions of CBC, I already met this hundreds of times. The only work around I see so far is to kill the bds.exe process in Windows Task Manager, and then restart Delphi 2006. For me this works fine. You can have a try to see if it works for you.

I have been digging to see what is the matter but I find out that it is csc.exe (the C# compiler) process that actually blocks Delphi 2006. If you kill this process at first, the frozen Delphi 2006 will be active. As a result, I think it is something wrong inside the compiler, not CBC.

However, I guess there may be some bugs left inside the InDate feature. So if the workaround above does work, you can turn off InDate feature in the Plus Manager of CBC to see whether anything else goes fine.

Thanks again for your report.

Best regards

Lex Li

2007.01.31

====================

Why I post the emails here?

1. Wish you could send me bug report every time you meet one bug.

2. Quick reply from me may not be included in the Readme.pdf shipped along the installer. Adding entries to this blog may be quicker.

BTW, you can send me feature requests or suggestions, too.
