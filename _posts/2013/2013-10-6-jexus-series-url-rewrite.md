---
layout: post
title: "Jexus Series: URL Rewrite"
description: "This post talks about Jexus URL Rewrite."
tags: Jexus-Manager
permalink: /jexus-series-url-rewrite-408e97900999
excerpt_separator: <!--more-->
---
Jexus does not support outbound rules (unlike IIS URL Rewrite module), but it supports simple inbound rules.

> For more information on Jexus/IIS comparison you can go to https://github.com/jexuswebserver/jexus-contrib/blob/master/comparison.en.md

To configure IIS URL Rewrite, you might follow [this article](http://www.iis.net/learn/extensions/url-rewrite-module/creating-rewrite-rules-for-the-url-rewrite-module).
<!--more-->

Assume that we have the following rule defined on IIS,

``` xml
<rewrite>
    <rules>
        <rule name="Rewrite to article.aspx">
            <match url="^article/([0–9]+)/([_0–9a-z-]+)" />
            <action type="Rewrite" url="article.aspx?id={R:1}&amp;title={R:2}" />
        </rule>
    </rules>
</rewrite>
```

The rule can be translated to Jexus style as

``` ini
rewrite=^/article/([0–9]+)/([_0–9a-z-]+) /article.aspx?id=$1&amp;title=$2
```

Compared to IIS, Jexus inbound rule contains less features right now. Below are the things it does not yet support,

* Actions such as Redirect or AbortRequest
* Conditions
* Ability to break from cascading rules
