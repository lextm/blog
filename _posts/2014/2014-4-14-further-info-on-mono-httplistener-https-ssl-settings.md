---
layout: post
title: "Further Info on Mono HttpListener HTTPS/SSL Settings"
description: "This post talks about how to configure Mono HttpListener HTTPS/SSL settings."
tags: Mono
permalink: /further-info-on-mono-httplistener-https-ssl-settings-d4cf0bfc4211
excerpt_separator: <!--more-->
---
I think this blog post has already covered the key things you need to know, http://joshua.perina.com/geo/post/using-ssl-https-with-mono-httplistener
<!--more-->

To repeat the steps,

1. Get the certificate and private key ready (http://www.sslshopper.com/article-how-to-create-and-install-an-apache-self-signed-certificate.html).
1. Convert the private key file to Microsoft PVK format (http://www.drh-consultancy.demon.co.uk/pvk.html). Make sure you use -nocrypt to generate a key file without encryption, as httpcfg does not support encrypted files (in fact it should, but requires some code changes, which I am going to send a pull request to Mono guys).
1. Use Mono httpcfg command to register the certifcate to the port. Note that you need to use root account to run this command, or your HttpListener does not work afterward. As httpcfg does not warn you about that, I am going to send another pull request to Mono guys.

Of course, if I finish Jexus Manager 1.0, I might spend some time to wrap the above steps in a single tool (which generates test certificates and associates them to ports). That should save most people from struggling.
