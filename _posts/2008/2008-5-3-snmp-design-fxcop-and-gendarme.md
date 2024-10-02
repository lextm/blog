---
layout: post
title: "#SNMP Design: FxCop and Gendarme"
description: This post talks about the tools I use to keep the code clean.
tags: SNMP
permalink: /snmp-design-fxcop-and-gendarme-8bca59a85563
excerpt_separator: <!--more-->
---
It is really hard to keep rules in mind when drown in the developer passion. I am a human so I can help drowning, too. Therefore, I always asks for help.
<!--more-->

FxCop was the only helper available in the past for a long time. It carefully analyses the code and provides me a lot of guidelines that I must obey.

Then when I ran through Mono, I met Gendarme. I thought it was not that useful until this afternoon. In fact, it provides some rules that FxCop lacks.

The only issue is that Gendarme does not officially support Windows. The snapshot installer here has a small bug so you can not run the executables on Windows. I have just created a patch for the console application here.

I think Mono is a nice project. If Microsoft don't like to open source FxCop in the future, I believe I will use Gendarme more often.

So why I write so much about these two? Today, I finally have time to clean up #SNMP 0.5 code base and the result is all critical issues reported by FxCop and Gendarme are fixed well.
