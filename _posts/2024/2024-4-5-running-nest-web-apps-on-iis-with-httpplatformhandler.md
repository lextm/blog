---
layout: post
title: "Running Nest Web Apps on IIS with HttpPlatformHandler"
description: A post about creating a simple Nest web app and deploy it on IIS with HttpPlatformHandler
tags: IIS Windows JavaScript Node.js Nest HttpPlatformHandler
excerpt_separator: <!--more-->
---

When Microsoft developed HttpPlatformHandler more than a decade ago to enable non-Microsoft web technologies on Windows/IIS, they didn't know that one day

* Microsoft can embrace Linux in Azure
* Some Microsoft users stick to IIS with their Java/Python/Node.js/Go applications.

Thus, HttpPlatformHandler still plays an important role in the ecosystem and won't go away easily. However, the landscape keeps evolving so this post tries to capture some latest changes on Nest (NestJS) and show you how to proper set up everything needed and more critically how to troubleshoot if issues occur.
<!--more-->

## Prerequisites

To follow this post, you need to have the following software installed,

* Windows 10 or Windows Server 2016 or later (IIS 10 or later)
* HttpPlatformHandler v1.2 (from Microsoft) or [v2.0 (from LeXtudio)]({% post_url 2024/2024-4-8-httpplatformhandler-v2 %})

## Basic Nest Setup

> The steps below are mostly copied from [the official Nest documentation](https://docs.nestjs.com/).

First, use `nest new` to create a new Next project,

``` bash
cd C:\
mkdir test-nest
npm i -g @nestjs/cli
nest new project-name
```

If you choose every option by default, you get a simple Nest web app in `project-name` folder.

Then to run this Nest web apps locally, you know you can use `npm run start` command.

``` bash
$ cd project-name
$ npm install
$ npm run build
$ npm run start:prod

> project-name@0.0.1 start:prod
> node dist/main

[Nest] 13260  - 2024-04-05, 10:06:27 p.m.     LOG [NestFactory] Starting Nest application...
[Nest] 13260  - 2024-04-05, 10:06:27 p.m.     LOG [InstanceLoader] AppModule dependencies initialized +17ms
[Nest] 13260  - 2024-04-05, 10:06:27 p.m.     LOG [RoutesResolver] AppController {/}: +9ms
[Nest] 13260  - 2024-04-05, 10:06:27 p.m.     LOG [RouterExplorer] Mapped {/, GET} route +3ms
[Nest] 13260  - 2024-04-05, 10:06:27 p.m.     LOG [NestApplication] Nest application successfully started +4ms
```

Note that `npm run start:prod` actually called `node dist/main`, and by default the development server starts on port 3000. This is controlled by `main.ts` file.

``` typescript
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  await app.listen(3000);
}
bootstrap();
```

Now let's modify the `main.ts` file to listen on `process.env.PORT` instead of a fixed port number.

``` typescript
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  const port = process.env.PORT || 3000; // Read the PORT environment variable or default to 3000
  await app.listen(port);
}
bootstrap();
```

## HttpPlatformHandler Setup

When you want to host the web app on IIS, you just need to create a `c:\test-nest\project-name\web.config` as below and invoke `node dist/main` properly,

``` xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <system.webServer>
        <handlers>
            <add name="httpPlatformHandler" path="*" verb="*" modules="httpPlatformHandler" resourceType="Unspecified" requireAccess="Script" />
        </handlers>
        <httpPlatform stdoutLogEnabled="true" stdoutLogFile=".\node.log" startupTimeLimit="20" processPath="C:\Users\<user name>\AppData\Roaming\nvm\v18.20.1\node.exe" arguments=".\dist\main">
            <environmentVariables>
                <environmentVariable name="PORT" value="%HTTP_PLATFORM_PORT%" />
                <environmentVariable name="NODE_ENV" value="Production" />
            </environmentVariables>
        </httpPlatform>
    </system.webServer>
</configuration>
```

> Here I assume you use `nvm` to manage your Node.js versions and the active version is v18.20.1.

Now go to IIS Manager and create a new site to point to `C:\test-nest\project-name` folder with site binding on localhost port 8016. Then you can browse the site and see the Nest web app running.

## Troubleshooting

If you encounter any issues, you can check the troubleshooting tips I wrote in [my previous post on Node.js]({% post_url 2022/2022-6-11-running-nodejs-web-apps-on-iis-with-httpplatformhandler %}).

## Side Notes

### Deployment Artifacts

You must run `npm run build` (wrapper over `nest build`) to generate the artifacts before deploying to IIS. Besides, you can delete source files and only leave `dist`, `node_modules` and `web.config` in the deployment folder.

### Nest on IIS Express

You can take a look at the [new open source HttpPlatformHandler v2.0 from LeXtudio]({% post_url 2024/2024-4-8-httpplatformhandler-v2 %}).

## Other Languages on IIS?

If you want to learn more about HttpPlatformHandler and how to host other languages (Go/Python/Java) or frameworks (Next.js/Nuxt.js), you can read [this post]({% post_url 2023/2023-4-7-the-rough-history-of-iis-httpplatformhandler %}).
