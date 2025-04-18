---
description: Step-by-step tutorial for setting up remote management of IIS instances running in Windows Server Core containers, including network configuration and security setup.
excerpt_separator: <!--more-->
image:
  alt: Copyright © Lex Li. Winter trees in Montreal.
  path: /images/winter-trees.jpg
layout: post
permalink: /remote-management-of-containerized-iis-instances-on-windows-server-core-f6864c74917f
tags: iis microsoft windows powershell
categories: [Tools and Platforms]
title: Remote Management of Containerized IIS Instances on Windows Server Core
---
You might want to run some applications on a Windows Server Core machine for quick testing. Instead of using a full virtual machine, running a Docker container can be easier. But in the meantime, why not enable IIS remote management so that IIS Manager can be used to tune the settings? However, the steps won't look obvious. In this post, I am going to show you the key steps.
<!--more-->

## Launch The Container

A single command to launch the container,

``` batch
docker network create --driver=nat --subnet=172.28.0.0/16 lextudio
docker run --name aspnet_sample -it -p 80 -p 443 -p 8172 --network lextudio --ip 172.28.253.71 mcr.microsoft.com/dotnet/framework/samples:aspnetapp
```

So we ask Docker engine to create a container named `aspnet_sample`, based on a Microsoft image `mcr.microsoft.com/dotnet/framework/samples:aspnetapp`. Three ports are opened, 80, 443, and 8172. This container uses a static IP address `172.28.253.71`.

Now open a web browser and navigate to `http://172.28.253.71` and we should see the ASP.NET test page.

> Note that if your host machine uses ports 80 and 443 for other purposes, then you need to change the mappings to use other ports of the host.

## Enable IIS Remote Management

Now attach to that container and open PowerShell,

``` bash
$ docker exec -ti aspnet_sample powershell
```

From this PowerShell console, create a new administrator,

``` bashh
$ net user /add testuser Password01!
$ net localgroup administrators testuser /add
```

install and start IIS Remote Management feature,

``` powershell
Install-WindowsFeature web-mgmt-service
Set-ItemProperty -Path HKLM:\SOFTWARE\Microsoft\WebManagement\Server -Name EnableRemoteManagement -Value 1
Set-Service WMSVC -StartupType Automatic
net start WMSVC
```

And from the host we can use IIS Manager to connect to `172.28.253.71:8172` and use user credentials of testuser to perform management tasks.

> That's why at the beginning I chose to open port 8172.

> Exercise: Can you try to add an HTTPS binding to Default Web Site, and then a web browser from the host can navigate to `https://172.28.253.71`?
>
> That's why at the beginning I chose to open port 443.
>
> A few hints:
>
> * You might use the SSL certificate WMSVC-SHA2 for testing.
> * When the web browser complaints about the certificate, simply ignore that and continue.

## The End

OK, now we can stop the container to save some energy,

``` bash
$ docker stop aspnet_sample
```

Later we can easily start the container again,

``` bash
$ docker start aspnet_sample
```

When we no longer need the container, we can remove it,

``` bash
$ docker rm aspnet_sample
```

## Side Notes

The command to set static IP address for an existing container is,

``` bash
$ docker network connect --ip 172.28.253.71 lextudio aspnet_sample
```
