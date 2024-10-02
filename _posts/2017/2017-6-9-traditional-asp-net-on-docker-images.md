---
layout: post
title: "Traditional ASP.NET on Docker: Images"
description: "This post is about how to analyze the layers of a Docker image, and use ASP.NET container images as example."
tags: IIS .NET
permalink: /traditional-asp-net-on-docker-images-1af3b72eeaaf
excerpt_separator: <!--more-->
---

> Update: due to the recent changes by Microsoft, the actual images can be different, but the way of analyzing the layers should remain the same. You are welcome to write a new blog post to replace this.

When you add Docker support to a traditional ASP.NET project (like WebForms), you probably notice a Dockerfile is added,

```docker
FROM microsoft/aspnet
ARG source
WORKDIR /inetpub/wwwroot
COPY ${source:-obj/Docker/publish} .
```

<!--more-->

We can easily see that this file defines a new image, which is derived from an image of `microsoft/aspnet`.

Information about `microsoft/aspnet` can be found at [Docker Hub](https://hub.docker.com/r/microsoft/aspnet/). Its corresponding Dockerfile can be found at [GitHub](https://github.com/Microsoft/aspnet-docker),

```docker
FROM microsoft/iis

RUN powershell -Command Add-WindowsFeature NET-Framework-45-ASPNET; \
powershell -Command Add-WindowsFeature Web-Asp-Net45; \
powershell -Command Remove-Item -Recurse C:\inetpub\wwwroot\*
```

In turn, `microsoft/aspnet` image is derived from [`microsoft/iis`](https://hub.docker.com/r/microsoft/iis/). The IIS image Dockerfile is at [GitHub](https://github.com/Microsoft/iis-docker),

```docker
FROM microsoft/windowsservercore
RUN powershell -Command Add-WindowsFeature Web-Server
ADD ServiceMonitor.exe /ServiceMonitor.exe
EXPOSE 80
ENTRYPOINT ["C:\\ServiceMonitor.exe", "w3svc"]
```

The Docker image composition can be drawn like below,

![img-description](/images/aspnet-docker-images.png)
_Figure 1: Docker Image Composition._

So, we can learn the following key points from Microsoft's Dockerfile files,

- Everything starts from a black box OS server image (windowsservercore in this case).
- The IIS image loads the OS image, adds Web Server role, and opens port 80. If we simply run this image, we should be able to see the default web site running on IIS.
- The ASP.NET image loads the IIS image, adds ASP.NET related role services, and then removes the contents of default web site. So if we run this image, there would be nothing served.
- The final image for our web app loads the ASP.NET image, and puts the published web contents to the physical path of the web site. Thus, when the final image is run, our web app would be well served.

You should notice that except the base image of "windowsservercore", we can prepare our own IIS/ASP.NET images to suit our own needs,

- Instead of adding the whole Web Server role, we can further select which are the role services to go. (I blogged about that in [this post]({% post_url 2017/2017-5-28-install-iis-10-on-windows-via-powershell %}).
- Instead of open only port 80, we can open any suitable port(s).
- We can further tune IIS configuration to define our own site (and its applications), and are not limited by default web site.
