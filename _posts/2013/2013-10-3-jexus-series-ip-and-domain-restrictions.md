---
layout: post
title: "Jexus Series: IP and Domain Restrictions"
description: "This post talks about Jexus IP and Domain Restrictions."
tags: Jexus-Manager
permalink: /jexus-series-ip-and-domain-restrictions-c04db4ff4060
excerpt_separator: <!--more-->
---
Jexus does not yet support dynamic IP restriction as IIS 7+ do, but its IP address restriction support is feature complete.

> For more information on Jexus/IIS comparison you can go to https://github.com/jexuswebserver/jexus-contrib/blob/master/comparison.en.md

To configure IIS IP and Domain Restrictions, you need to follow [this article](http://www.iis.net/configreference/system.webserver/security/ipsecurity).
<!--more-->

It is very easy to translate the steps to Jexus.

## Scenario 1

When we specify `<ipSecurity allowUnlisted="true" />` on IIS and add deny entries

* 192.168.100.1
* 169.254.0.0 with subnet mask 255.255.0.0

Then in Jexus configuration we should use

``` ini
denyfrom=192.168.100.1,169.254.0.0/16
```

> Note that Jexus supports several ways of IP range, such as
>
> 1. 169.254.0.0–169.254.255.255 (IP start to end)
> 1. 169.254.0.0/16 (with prefix size)
> 1. 169.254.*.* (with wildcard)

## Scenario 2

When we specify `<ipSecurity allowUnlisted="false" />` on IIS and add allow entries

* 192.168.100.1
* 169.254.0.0 with subnet mask 255.255.0.0

Then in Jexus configuration we should use

``` ini
allowfrom=192.168.100.1,169.254.0.0/16
```

## Scenario 3

If in Jexus settings we have

``` ini
allowfrom=192.168.100.1,169.254.0.0/16
denyfrom=192.168.100.1
```

Then the effective IP range becomes 169.254.0.0/16 only.