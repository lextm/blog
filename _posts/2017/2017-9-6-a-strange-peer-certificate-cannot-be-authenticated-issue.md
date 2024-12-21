---
layout: post
title: "A Strange 'Peer Certificate Cannot Be Authenticated' Issue"
description: This post is about a strange issue when using .NET Core related to time synchronization.
tags: Linux .NET
permalink: /a-strange-peer-certificate-cannot-be-authenticated-issue-a7f47193699
excerpt_separator: <!--more-->
---

I built a Debian machine a while ago to test out MonoDevelop, and now I am trying to test .NET Core on it. But such an exception happened.
<!--more-->

``` shell
parallels@debian-8:~/Downloads/sharpsnmplib$ ./travis.sh

/usr/share/dotnet/sdk/2.0.0/NuGet.targets(102,5): error : Unable to load the service index for source https://api.nuget.org/v3/index.json. [/home/parallels/Downloads/sharpsnmplib/SharpSnmpLib.NetStandard.macOS.sln]

/usr/share/dotnet/sdk/2.0.0/NuGet.targets(102,5): error : An error occurred while sending the request. [/home/parallels/Downloads/sharpsnmplib/SharpSnmpLib.NetStandard.macOS.sln]

/usr/share/dotnet/sdk/2.0.0/NuGet.targets(102,5): error : Peer certificate cannot be authenticated with given CA certificates [/home/parallels/Downloads/sharpsnmplib/SharpSnmpLib.NetStandard.macOS.sln]
```

So how to troubleshoot such issues? I thought I should sync the CA certificates, right? But no matter what I tried, the error wouldn't go away.

Finally I hit a post that used curl command to dig more details from SSL/TLS connection,

``` shell
parallels@debian-8:~/Downloads/sharpsnmplib$ curl -v https://api.nuget.org/v3/index.json
* Hostname was NOT found in DNS cache
* Trying 72.21.81.200…
* Connected to api.nuget.org (72.21.81.200) port 443 (#0)
* successfully set certificate verify locations:
* CAfile: none
CApath: /etc/ssl/certs
* SSLv3, TLS handshake, Client hello (1):
* SSLv3, TLS handshake, Server hello (2):
* SSLv3, TLS handshake, CERT (11):
* SSLv3, TLS alert, Server hello (2):
* SSL certificate problem: certificate is not yet valid
* Closing connection 0
* SSLv3, TLS alert, Client hello (1):
curl: (60) SSL certificate problem: certificate is not yet valid
More details here: http://curl.haxx.se/docs/sslcerts.html
curl performs SSL certificate verification by default, using a "bundle"
of Certificate Authority (CA) public keys (CA certs). If the default
bundle file isn't adequate, you can specify an alternate file
using the --cacert option.
If this HTTPS server uses a certificate signed by a CA represented in
the bundle, the certificate verification probably failed due to a
problem with the certificate (it might be expired, or the name might
not match the domain name in the URL).
If you'd like to turn off curl's verification of the certificate, use
the -k (or --insecure) option.
```

OK, so this time using "curl: (60) SSL certificate problem: certificate is not yet valid" as keyword Google started to provide good explanations.

No doubt I am using a suspended VM on Parallel, so the machine thought it was still on July 9,
``` shell
parallels@debian-8:~/Downloads/sharpsnmplib$ date
Sun Jul 9 14:29:08 EDT 2017
```

By syncing the time, the issue was resolved.

Thus, the tip here is that don't guess the cause before collecting enough details, guys.
