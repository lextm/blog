---
layout: post
title: "#SNMP Design: Obsolete Methods"
description: "This post is about the obsolete methods in #SNMP 1.5 RC3."
tags: SNMP
permalink: /snmp-design-obsolete-methods-c3549a6c18d9
excerpt_separator: <!--more-->
---

I did not pay much attention to compatibility in the past, because previous releases (0.9, 1.0, and 1.1) are concept oriented which make sure that SNMP can be implemented in such a way. Therefore, I have changed the API several times. Well, that can be bad to some users if they have hundreds of lines to modify all in a day.

<!--more-->

So from now on, I will pay more attention to that. You may already notice this by compiling your project against the latest bits in the repository as the compiler suddenly tells you some methods are obsolete.

Sorry, this is a direct consequence when I start to pay back some [design debts]({% post_url 2008/2008-10-19-snmp-design-one-api-design-flaw %}). For example, some obsolete constructors such as GetRequestMessage's require IPAddress parameters, but the parameters are not used until Send methods are called. Non-sense. Why not pass them until Send?

Another case is Send, which hides the GetResponseMessage instance. This can be very restricted when you try to access that instance to customize the behavior.

Here comes the warning. Although obsolete methods will be delivered in 1.5 final, they are not likely to appear in later releases. Please make a schedule to migrate. Thanks.

Stay tuned.
