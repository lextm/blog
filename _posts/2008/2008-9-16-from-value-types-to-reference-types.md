---
layout: post
title: "From Value Types to Reference Types"
description: "This post talks about what you must pay attention to when you design a library and have to change a few types from value types to reference types."
tags: .NET
permalink: /from-value-types-to-reference-types-93912062163c
excerpt_separator: <!--more-->
---

I have a few C# books at hand, but a topic cannot be found in them. This topic is what you must pay attention to when you design a library and have to change a few types from value types to reference types. Both fortunately and unfortunately, I have come across this issue with a lot of headaches so in this post I'd like to provide you some tips I find out.

<!--more-->

First, why I need to change those value types to reference types? Surely it is because of boxing. You can find more details [in this post]({% post_url 2008/2008-9-12-snmp-design-locating-boxing-the-standard-way %}). Throughout #SNMP Library, those value types were used via ISnmpData interface. Thus, changing them to reference types should eliminate a lot of boxing operations.

Second, after changing keyword struct to class what else to be done? Just like System.String, the newly converted reference types should behavior similar to their value type ancestors. Thus, I still need to override Equals, GetHashCode, ==, and !=. The differences are, this time attention must be paid to null references.

For example, in ObjectIdentifier.cs, now both == and Equals check for null references. The biggest problem right now is how to provide correct implementation for them. (Forgive me, the current implementation sucks as it leads to stack overflow exceptions.)

To correctly implement those methods, System.String's implementation should be referred to every time you feel puzzled. Because Microsoft released its source code under a non-open source license, I recommend you refer to this Mono implementation (which is covered by X11/MIT).

http://ftp.novell.com/pub/mono/sources-stable/

I am going to fix Work Item 2991 again tonight completely. Stay tuned.
