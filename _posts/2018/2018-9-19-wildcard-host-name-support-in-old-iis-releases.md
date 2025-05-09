---
description: How to implement wildcard host name support in older IIS versions using Application Request Routing (ARR) and URL Rewrite as an alternative to IIS 10's native support.
excerpt_separator: <!--more-->
image:
  alt: Copyright © Lex Li. City hall, Toronto.
  path: /images/city-hall-toronto.jpg
layout: post
permalink: /wildcard-host-name-support-in-old-iis-releases-8e4448040b5a
tags: iis windows
categories: [Tools and Platforms]
title: Wildcard Host Name Support in Old IIS Releases
---
IIS 10 allows users to easily use [wildcard host names](https://docs.microsoft.com/iis/get-started/whats-new-in-iis-10/wildcard-host-header-support). Well, "why is it so late"? You might ask. I did not work on IIS, so I can only guess that the developers believe you can already support such on previous IIS releases. But how? Recently I have been using ARR a lot, so below I provide an approach to support wildcard host names via ARR.
<!--more-->

## What Is Wildcard Host Name?

Assume that you have two domains, site1.com and site2.com. For each of them, you would like to host a few subdomains,

* test.site1.com
* test1.site1.com
* XXX.site1.com
* test2.site2.com
* test3.site2.com
* YYY.site2.com

and more importantly, all subdomains of site1.com should be served by the same web application, so should all subdomains of site2.com.

OK, if with IIS 10, we just need two web sites. One of them binds to `*.site1.com` and the other `*.site2.com`.

## What To Do on Old IIS Releases?

Firstly, of course you need to install ARR and URL Rewrite module. Later we use them to configure a reverse proxy.

Secondly, create a catch-all site (like the Default Web Site), who binds to `*:80` with no host name. Later, this site takes all incoming HTTP requests, and applies our reverse proxy rules.

> Here I use HTTP sites as examples for simplicity.

Thirdly, create the actual content sites. One for `site1.com` binds to `*:8091` with no host name, while the other for `site2.com` to `*:8092` with no host name. Both sites can be tested now via the bindings given.

Fourthly, on the catch-all site, create the following rules,

``` xml
<system.webServer>
    <rewrite>
        <rules>
            <rule name="site1" stopProcessing="true">
                <match url=".*" />
                <conditions>
                    <add input="{HTTP_HOST}" pattern="^(.*).site1.com$" />
                </conditions>
                <action type="Rewrite" url="http://localhost:8091/{R:0}" />
            </rule>
            <rule name="site2" stopProcessing="true">
                <match url=".*" />
                <conditions>
                    <add input="{HTTP_HOST}" pattern="^(.*).site2.com$" />
                </conditions>
                <action type="Rewrite" url="http://localhost:8092/{R:0}" />
            </rule>
        </rules>
    </rewrite>
</system.webServer>
```

If you are familiar with IIS, these rules are pretty simple.

Lastly, set up ARR proxy mode at server level,

``` xml
<system.webServer>
    <proxy enabled="true" />
</system.webServer>
```

## Side Notes

The reverse proxy approach is slightly complex if we compare to wildcard host name support in IIS 10. Indeed, it takes more steps to set up, and it requires a few sites with no host name in their bindings, which might not look pleasant. Also when we compare the performance metrics, reverse proxy has more overhead (but negligible in most cases).

So, upgrade to IIS 10 if you can. Use the above steps only when you have to stick to an old release.
