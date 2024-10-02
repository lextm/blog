---
layout: post
title: "Running FastAPI Web Apps on IIS with HttpPlatformHandler"
description: A post about how to create a simple FastAPI web app and host it on IIS with HttpPlatformHandler
tags: IIS Windows Python FastAPI HttpPlatformHandler
excerpt_separator: <!--more-->
---

HttpPlatformHandler can help IIS host Java/Python/Node.js/Go applications, so in this post we wil see how to configure a Python/FastAPI web app on IIS and troubleshoot the common issue.

It becomes very important for Python developers to learn HttpPlatformHandler, because [Microsoft no longer recommends FastCGI](https://docs.microsoft.com/visualstudio/python/configure-web-apps-for-iis-windows?view=vs-2022#configure-the-fastcgi-handler),

> "We recommend using HttpPlatform to configure your apps, as the WFastCGI project is no longer maintained."

<!--more-->

## Prerequisites

To follow this post, you need to have the following software installed,

* Windows 10 or Windows Server 2016 or later (IIS 10 or later)
* HttpPlatformHandler v1.2 (from Microsoft) or [v2.0 (from LeXtudio)]({% post_url 2024/2024-4-8-httpplatformhandler-v2 %})

## Basic FastAPI Setup

No doubt we will start from a sample application as below,

``` python
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

If we save it as `C:\test-fastapi\main.py`, then on a Windows machine with Python and FastAPI installed, a simple command `uvicorn main:app --reload` in the directory of `C:\test-fastapi\` can launch the application at port 8000,

``` batch
$ C:\Users\lextudio\AppData\Local\Programs\Python\Python310\python.exe -m uvicorn main:app --reload  
INFO:     Will watch for changes in these directories: ['C:\\test-fastapi']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [11128] using StatReload
INFO:     Started server process [10864]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

> If Python and FastAPI are not yet installed, you can search for guides.

## HttpPlatformHandler Setup

Now let's download and install HttpPlatformHandler on IIS, and add a `web.config` in `C:\test-fastapi`,

``` xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <system.webServer>
        <handlers>
            <add name="httpPlatformHandler" path="*" verb="*" modules="httpPlatformHandler" resourceType="Unspecified" requireAccess="Script" />
        </handlers>
        <httpPlatform stdoutLogEnabled="true" stdoutLogFile=".\python.log" startupTimeLimit="20" processPath="C:\Users\<user name>\AppData\Local\Programs\Python\Python310\python.exe" arguments="-m uvicorn --port %HTTP_PLATFORM_PORT% main:app">
        </httpPlatform>
    </system.webServer>
</configuration>
```

With all settings in place, I can go back to IIS Manager and create a site (I chose *:8013 as site binding) to point to `C:\test-fastapi`. By opening a web browser and navigate to `http://localhost:8013/`, I should now see `{"Hello":"World"}`.

## Troubleshooting

Well if you hit any error instead of the JSON response, please refer to [my old post]({% post_url 2022/2022-7-10-running-flask-web-apps-on-iis-with-httpplatformhandler %}) for troubleshooting tips.

## FastAPI on IIS Express

You can take a look at the [new open source HttpPlatformHandler v2.0 from LeXtudio]({% post_url 2024/2024-4-8-httpplatformhandler-v2 %}).

## Other Languages on IIS?

If you want to learn more about HttpPlatformHandler and how to host other languages (Go/Node.js/Java) or frameworks (Django/Flask), you can read [this post]({% post_url 2023/2023-4-7-the-rough-history-of-iis-httpplatformhandler %}).
