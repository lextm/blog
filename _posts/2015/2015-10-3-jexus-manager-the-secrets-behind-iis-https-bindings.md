---
layout: post
title: "Jexus Manager: The Secret Behind IIS HTTPS Bindings"
description: "This post is about how Jexus Manager finds the proper certificate for an HTTPS binding."
tags: Jexus-Manager IIS
permalink: /jexus-manager-the-secret-behind-iis-https-bindings-5ad3466a6db5
excerpt_separator: <!--more-->
---
If you have ever opened IIS 7+ configuration file (aka applicationHost.config), you probably know that an HTTPS binding of a site looks like below,

``` xml
<site name="php" id="8">
    <bindings>
        <binding bindingInformation="*:58000:localhost" protocol="http" />
        <binding bindingInformation="*:44300:localhost" protocol="https" />
        <binding bindingInformation="*:4431:localhost" protocol="https" />
        <binding bindingInformation="*:4431:lextudio.com" protocol="https" />
    </bindings>
    <application path="/" applicationPool="32bit">
        <virtualDirectory path="/" physicalPath="e:\test" />
    </application>
</site>
```

It is rather strange that no certificate information is available here, while in IIS Manager (or Jexus Manager for IIS Express) we can see the certificate selected for each bindings. So from where does IIS Manager find the proper certificate?
<!--more-->

## IP Based Bindings

If "Require Server Name Indication" is not checked, then this binding is not SNI enabled. It also means for this binding, the certificate is registered to the IP address + port number (in this example, 0.0.0.0:44300). Windows stores the certificate information in a private storage for http.sys to read, which can be queried via `netsh http show sslcert`.

Starting from today's build, Jexus Manager for IIS Express 2 Beta 2 features a new page to show the list too.

So now it is very clear that the certificate mappings are here. Note that IIS Express creates mappings for 0.0.0.0:44300–0.0.0.0:44399 during its installation, so that non administrators can bind HTTPS sites to such mappings.

Due to the limitation of such mappings, we know for a single IP end point, only a single certificate can be registered. That's why when we attempt to host multiple HTTPS sites on a single IP end point we could only use a wildcard certificate or a UC certificate.

## SNI Based Bindings

Starting from Windows 8/IIS 8 and above, we can create SNI based in addition to IP based bindings. This allows multiple certificates to be bind to a single IP end point.

So here when we scroll down to the bottom of the list, we can see SNI based mapping for certificates. They are bind to host name + port number instead of IP end point + port number.

Such SNI based mappings are automatically created by IIS Manager/Jexus Manager when you add SNI based bindings to web sites. They are also removed automatically when such bindings are removed from sites.

## Troubleshoot Tips

Therefore, with this new HTTP API page, you can easily navigate which mappings are currently registered in Windows, and then it can be quite easy to tell whether an HTTPS site has the mappings it needs.

This page can be further enhanced to show which mappings are currently in use, and which are idle. It should be a cool feature in Jexus Manager for IIS Express 2.0 RTW.

Stay tuned.
