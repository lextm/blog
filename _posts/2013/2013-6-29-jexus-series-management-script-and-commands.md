---
layout: post
title: "Jexus Series: Management Script and Commands"
description: "This post talks about Jexus management script and commands."
tags: Jexus-Manager Linux
permalink: /jexus-series-management-script-and-commands-2d0b8eaf673e
excerpt_separator: <!--more-->
---
Starting Jexus 5.3 the commands are merged into one Shell script, /usr/jexus/jws.
<!--more-->

This script provides the following functionality,

| Command | Description |
| ------- | ----------- |
| jws start | Start Jexus server. |
| jws start site_name | Start a single web site. Note that site_name must match one of the configuration files under configuration directory. |
| jws restart | Restart Jexus server. |
| jws restart site_name | Restart a single web site. |
| jws stop | Stop Jexus server. |
| jws stop site_name | Stop a single web site. |
| jws regsvr | Register Jexus assembly in GAC. Note that this is only required to be executed once during installation. |
| jws status | Report Jexus runtime status. |
| jws -v | Display Jexus version number. The script should be set to executable during installation. The commands can only be executed by root. |
