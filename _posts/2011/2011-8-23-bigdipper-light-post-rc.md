---
layout: post
title: "BigDipper Light: Post RC"
description: "This post is about the latest RC build of #SNMP 7."
tags: SNMP
permalink: /bigdipper-light-post-rc-fc68076fa85c
excerpt_separator: <!--more-->
---
Long time not see, my friends. Now the 7.0 release of #SNMP is coming.

The RC build is still hot, and it already contains all new stuffs you can enjoy for the following months. And I am still working on the release notes (with help of NDepend of course). As the breaking changes are significant, it will take a few days for me to finish the document.
<!--more-->

So what can we expect for 8.0? I think the very first piece should be a new MIB compiler.

Yes, it has been promised for a few releases but I could not make it possible because Antlr may not be the correct choice after all. So now I think we may try out Gammatica. This parser generator powers Mibble MIB Parser (Java based) already, so it is very likely that we can use it for #SNMP targeting .NET. The only problem is that the ASN.1 grammar is licensed under GPL. If we use it, it means the new compiler will be licensed under GPL (I will consult the author first to see if there is any hope of less constraint license choice).

I did not have any other feature planning for 8.0 yet. Let's see what may come out then.

Stay tuned.
