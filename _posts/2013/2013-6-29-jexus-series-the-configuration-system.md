---
layout: post
title: "Jexus Series: The Configuration System"
description: "This post talks about Jexus configuration system."
tags: Jexus-Manager
permalink: /jexus-series-the-configuration-system-108aa9e471b0
excerpt_separator: <!--more-->
---
The Jexus configuration system is more similar to Apache/Nginx, rather than IIS.
<!--more-->

## Server Configuration

The configuration file, which contains most of Jexus settings, is located in Jexus installation folder (usually /usr/jexus) and named jws.conf.

Unlike IIS which uses XML to store settings, the Jexus settings are stored in key-value pair, for example

``` ini
SiteLogDir=log
SiteConfigDir=siteconf
```

The description of each settings is listed as below,

| Setting | Mandatory? | Description |
| ------- | ---------- | ----------- |
| SiteConfigDir | yes | The directory that holds web site configuration files. Relative paths to jws.exe can be used. |
|SiteLogDir | yes | The directory that holds the log files. Relative paths to jws.exe can be used. |
| Runtime | no | Application pool ASP.NET runtime version. For example, Runtime=v4.0.30319 |
| httpd.user | no | Application pool identity. For example, httpd.user=www-data |

The first two settings are mandatory.

The log directory must give Jexus process permissions to write, as Jexus server log and web site access logs are all generated and stored there.

In default installation, /usr/jexus/siteconf is used as configuration directory, while /usr/jexus/log is used as log directory.

## Web Site Configuration

Jexus supports multiple web sites running on the same server. The web sites use individual bindings to distinguish from each other.

The web site configuration files must be saved in the configuration directory set in jws.conf (aka SiteConfigDir). The configuration file name is used as site name (site name is only used in Jexus commands), which should not contain spaces. Note that all files in configuration directory are treated as web site configuration files. Thus, don't leave anything else there.

In default installation, a default web site is created. Its configuration file is /usr/jexus/siteconf/default. Just like jws.conf, the web site configuration is also stored in key value pair, and the description of each settings is as below,

| Setting | Mandatory? | Description |
| ------- | ---------- | ----------- |
| port | yes | The port number used for this web site. Default is port=80. |
| hosts | no | The host header accepted by this web site. Default is hosts=\*, which means any host header is accepted. Wildcard is also supported, such as \*.mysite.com. |
| root | yes | The directory mapping. The default is root=/ /var/www/default, which maps physical directory /var/www/default that contains the web site contents to web site root. |
| indexes | no | Default document name list. For example, when indexes=index.aspx,index.htm is used, access to / will be resolved to index.aspx if it exists, and then index.htm if exists, and 404 if none of them exists. When this setting is not set, Jexus uses its built-in name list. See (\*1)for more details. |
| rewrite | no | URL rewrite rule. For example, rewrite=^/.+?\.(asp|php|cgi)$ /404.html means any access to classic ASP/PHP/CGI pages is rewritten to /404.html. To use multiple rules, use multiple lines of rewrite=. |
| denyfrom | no | IP address restriction. For example, when denyfrom=111.222.111.\*,1.1.1.1 is used, access from the IP addreses are denied. Mask is also supported, such as denyfrom=192.168.1.0/255.255.255.0. |
| DenyDirs | no | Hidden segments. When DenyDirs=bin,App_code is used, access to such URL paths is denied. |
| checkquery | no | Query strings restriction. Jexus uses built-in logic to perform query safety check. The default is checkquery=true. Note that by setting this to true, there is some impact on Jexus performance. |
| nofile | no | NOFILE is a Jexus specific feature. It is similar to IIS custom error pages for 404. When nofile=/mvc/controller.aspx is used, access to non-existent files is redirected to /mvc/controller.aspx. Note that the original URL is passed via X-Real-Uri server variable. |
| nolog | no | Logging flag. The default is nolog=false. When set to true, Jexus stops generating log files for this web site. |
| keep_alive | no | HTTP keep-alive flag. The default is keep_alive=true. |
| reproxy | no | Reverse proxy rule. When reproxy= /abc/ http://www.xxxx.com:890/abc/ is used, requests on /abc/ (source) will be redirected to http://www.xxxx.com:890/abc/ (destination). The destination can be multiple, so that Jexus randomly picks one from them, which is similar to load balancing. For example, reproxy=/abc/ http://192.168.0.3/abc/,http://192.168.0.4/abc/. |
| fastcgi.add | no | FastCGI rule. For TCP connections, typical setting is fastcgi.add=php,php3|tcp:127.0.0.1:9000, which forwards requests of .php or php3 extensions to 127.0.0.1:9000 via TCP. For UNIX sockets, typical setting is fastcgi.add=php,php3|socket:/tmp/phpsvrusegzipnoGZip compression flag. The default is usegzip=true. |
| usehttps | no | SSL flag. To enable HTTPS, this setting must be set to true, and port must be set to 443 at the same time. The default is usehttps=false. See (*2) for more details. |

*1 The Jexus built-in default document name list is as below,

* index.aspx
* Index.aspx
* default.aspx
* Default.aspx
* index.htm
* Index.htm
* default.htm
* Default.htm
* index.html
* Index.html
* default.html
* Default.html
* index.php
* Index.php
* default.php
* Default.php

*2 To enable HTTPS, please follow the steps in this blog post.

TODO:
