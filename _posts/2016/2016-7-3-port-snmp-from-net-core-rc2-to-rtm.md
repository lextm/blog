---
layout: post
title: "Port #SNMP from .NET Core RC2 to RTM"
description: "This post is about how I port #SNMP Library from .NET Core RC2 to RTM."
tags: SNMP .NET
permalink: /port-snmp-from-net-core-rc2-to-rtm-76234f61be98
excerpt_separator: <!--more-->
---
Well, I thought this might be a long post, but in fact it would be pretty short.

For a library like #SNMP Library, [the only changes](https://github.com/lextudio/sharpsnmplib/commit/0c7341addb8cbc158aaed08ba55bb235df6ee88f) I need to make are in the project.json file.
<!--more-->

By removing `–rc2-*` from this file, and revise the package version based on `dotnet build` hints, this library now targets the latest .NET Core bits.

One last thing I want to mention is that I did not add a reference to .NET Standard Library (NETStandard.Library), simply because this library sits in the same layer (similar to System.Net.Http).

Thus, now the library version has been bumped to 10 Beta 1. Should soon finally the API surface and release it officially.
