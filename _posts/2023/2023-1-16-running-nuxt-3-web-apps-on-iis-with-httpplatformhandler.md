---
description: Step-by-step guide for deploying Nuxt 3 web applications on Windows IIS using HttpPlatformHandler, including sample project setup, configuration, and troubleshooting tips for Node.js applications on Microsoft's web server.
excerpt_separator: <!--more-->
layout: post
tags: azure iis windows httpplatformhandler
categories: [Tools and Platforms]
title: Running Nuxt 3 Web Apps on IIS with HttpPlatformHandler
---
When Microsoft developed HttpPlatformHandler more than a decade ago to enable non-Microsoft web technologies on Windows/IIS, they didn't know that one day

* Microsoft can embrace Linux in Azure
* Some Microsoft users stick to IIS with their Java/Python/Node.js/Go applications.

Thus, HttpPlatformHandler still plays an important role in the ecosystem and won't go away easily. However, the landscape keeps evolving so this post tries to capture some latest changes on Nuxt 3 and show you how to proper set up everything needed and more critically how to troubleshoot if issues occur.
<!--more-->

## Sample Project Preparation

Compared to Nuxt 2.x releases, 3.0 introduced brand new steps so you must stick to [the official guide](https://nuxt.com/docs/getting-started/installation#new-project) closely,

``` batch
npx nuxi init test-nuxt
cd test-nuxt
npm install
npm run build
```

> Note that
>
> * I chose `npx` and `npm` steps, while you can use `pnpm` or `yarn`.
> * I used `C:\` as the start point, so `C:\test-nuxt` contains the source code, and `C:\test-nuxt\.output` contains the generated artifacts for deployment.

## Add IIS Configuration

Simply create a `web.config` file at the root (`C:\test-nuxt` in my case) with the following content,

``` xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <system.webServer>
        <handlers>
            <add name="httpPlatformHandler" path="*" verb="*" modules="httpPlatformHandler" resourceType="Unspecified" requireAccess="Script" />
        </handlers>
        <httpPlatform stdoutLogEnabled="true" stdoutLogFile=".\node.log" startupTimeLimit="20" processPath="C:\Users\<user name>\AppData\Roaming\nvm\v16.13.2\node.exe" arguments=".output\server\index.mjs">
            <environmentVariables>
                <environmentVariable name="PORT" value="%HTTP_PLATFORM_PORT%" />
                <environmentVariable name="NODE_ENV" value="Production" />
            </environmentVariables>
        </httpPlatform>
    </system.webServer>
</configuration>
```

With all settings in place, I can go back to IIS Manager and create a site (I chose *:8030 as site binding, but as a normal IIS site you can configure any bindings you like) to point to `C:\test-nuxt`. By opening a web browser and navigate to `http://localhost:8030/`, I can see "Welcome to Nuxt" page as expected.

If you are not familiar with the contents and hit any IIS error, please read [my previous post on Node.js]({% post_url 2022/2022-6-11-running-nodejs-web-apps-on-iis-with-httpplatformhandler%}) to learn how to troubleshoot.

## Side Notes

### Nuxt 3 on Azure App Service

Clearly you can easily move this web app to Azure App Service (Windows) with minimal changes.

### Nuxt 3 on IIS Express

You can take a look at the [new open source HTTP Bridge Module for IIS from LeXtudio]({% post_url 2024/2024-4-8-httpplatformhandler-v2 %}).

## Other Languages on IIS?

If you want to learn more about HttpPlatformHandler and how to host other languages (Go/Python/Java) or frameworks (Next.js), you can read [this post]({% post_url 2023/2023-4-7-the-rough-history-of-iis-httpplatformhandler %}).

## Related HttpPlatformHandler Articles

> This article is part of a series on using HttpPlatformHandler with IIS. To explore all related articles, please visit the [httpplatformhandler tag page]({{ site.baseurl }}/tags/httpplatformhandler/) for the complete collection of guides and tutorials.
