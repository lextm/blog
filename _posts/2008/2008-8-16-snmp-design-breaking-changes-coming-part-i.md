---
layout: post
title: "#SNMP Design: Breaking Changes Coming, Part I"
description: "This post talks about the breaking changes coming in the next release."
tags: SNMP
permalink: /snmp-design-breaking-changes-coming-part-i-8246379c2d24
excerpt_separator: <!--more-->
---
Every time I read Manager.cs, I feel bad. Like I expressed on the discussion board, I hated overloading functions a little bit. Yes, imagine if you are new to #SNMP, which one of these Get, Set, or GetTable should be called? I thought I could move overloading methods to a separate assembly like the unit tests. However, Extension Method is only a .NET 3.5 feature. In order not to bother those .NET 2.0 guys, I delay this move.
But the upcoming release, TwinTower, has breaking changes in these methods. I think it is not bad because you no longer need to pass two parameters (an IPAddress instance for agent address and an Int32 for port number). Instead, an IPEndPoint replaces them all. It is also more meaningful as you are managing a remote endpoint.
It is the first significant change. Stay tuned.

(Updated: Suggested by Michael, the changes described in this post is going to be rolled back. The final overloads presented in 1.5 final may look different. Another post will be provided before that release to state the new approach.)
<!--more-->