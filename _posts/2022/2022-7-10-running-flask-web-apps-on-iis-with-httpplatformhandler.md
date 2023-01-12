---
layout: post
title: "Running Flask Web Apps on IIS with HttpPlatformHandler"
description: A post about how to create a simple Flask web app and host it on IIS with HttpPlatformHandler
tags: IIS Windows Python Flask HttpPlatformHandler
excerpt_separator: <!--more-->
---

HttpPlatformHandler can help IIS host Java/Python/Node.js/Go applications, so in this post we wil see how to configure a Python/Flask web app on IIS and troubleshoot the common issue.

It becomes very important for Python developers to learn HttpPlatformHandler, because [Microsoft no longer recommends FastCGI](https://docs.microsoft.com/visualstudio/python/configure-web-apps-for-iis-windows?view=vs-2022#configure-the-fastcgi-handler),

> "We recommend using HttpPlatform to configure your apps, as the WFastCGI project is no longer maintained."

<!--more-->

## Prerequisites

To follow this post, you need to have the following software installed,

* Windows 10 or Windows Server 2016 or later (IIS 10 or later)
* HttpPlatformHandler v1.2 (from Microsoft) or [v2.0 (from LeXtudio)]({% post_url 2024/2024-4-8-httpplatformhandler-v2 %})

## Basic Flask Setup

No doubt we will start from a sample application as below,

``` python
from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"

    return app
```

If we save it as `C:\flask-test\app.py`, then on a Windows machine with Python and Flask installed, a simple command `flask run` in the directory of `C:\flask-test\` can launch the application at port 5000,

``` text
PS C:\flask-test> ~\AppData\Local\Programs\Python\Python310\python.exe -m flask run
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
```

> If Python and Flask are not yet installed, you can search for guides.

## HttpPlatformHandler Setup

Now let's download and install HttpPlatformHandler on IIS, and add a `web.config` in `C:\flask-test`,

``` xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <system.webServer>
        <handlers>
            <add name="httpPlatformHandler" path="*" verb="*" modules="httpPlatformHandler" resourceType="Unspecified" requireAccess="Script" />
        </handlers>
        <httpPlatform stdoutLogEnabled="true" stdoutLogFile=".\python.log" startupTimeLimit="20" processPath="C:\Users\<user name>\AppData\Local\Programs\Python\Python310\python.exe" arguments="-m flask run --port %HTTP_PLATFORM_PORT%">
        </httpPlatform>
    </system.webServer>
</configuration>
```

With all settings in place, I can go back to IIS Manager and create a site (I chose *:8086 as site binding) to point to `C:\flask-test`. By opening a web browser and navigate to `http://localhost:8086/`, I should now see "Hello, World!". Ah, what happened?

## Troubleshooting

### 0x8007005
Yeah I am not able to see "Hello, World!" but a Bad Gateway error page with the Error Code of `0x80070005`,

![img-description](/images/python-access-denied.jpeg)
_Figure 1: Bad Gateway error page of 0x80070005_

``` text
> .\Err.exe 80070005
# No results found for hex 0x4c5c575 / decimal 80070005
# for hex 0x80070005 / decimal -2147024891
  COR_E_UNAUTHORIZEDACCESS                                       corerror.h
# Access is denied.
  DIERR_OTHERAPPHASPRIO                                          dinput.h
  DIERR_READONLY                                                 dinput.h
  DIERR_HANDLEEXISTS                                             dinput.h
  DSERR_ACCESSDENIED                                             dsound.h
  STIERR_READONLY                                                stierr.h
  STIERR_NOTINITIALIZED                                          stierr.h
  E_ACCESSDENIED                                                 winerror.h
# General access denied error
# as an HRESULT: Severity: FAILURE (1), FACILITY_WIN32 (0x7), Code 0x5
# for hex 0x5 / decimal 5
  ERROR_ACCESS_DENIED                                            winerror.h
# Access is denied.
# 9 matches found for "80070005"
```

This isn't hard to understand, because anything under `C:\Users\<user name>\` is protected and accessible only by that user account by default, not `IIS_IUSRS`.

### The Infinite Loading
Once I grant `IIS_IUSRS` read access to `C:\Users\<user name>\AppData\Local\Programs\Python\Python310\python.exe`, the browser seems to work as it is trying to load the web page. However, I notice that now this page takes for ever to load and the `python.exe` process keeps crashing.

No doubt Process Monitor is the best tool to use right now and by using a filter of process name `python.exe` I can see lots of access denied errors on different files in `C:\Users\<user name>\AppData\Local\Programs\Python\Python310\`.

So I go back and grant `IIS_IUSRS` read access on the whole directory, not just `python.exe`.

### Switch to Production Application Server
At this moment, a refresh in the web browser leads me to the expected "Hello, World!" message. Now I know that Python/Flask is working.

To move further, I might want to remove the warning of "This is a development server. Do not use it in a production deployment". For that I have to switch to another Python application server, such as waitress.

> Use `pip install waitress` to install it.

To allow waitress to identify the web app entry, add a file called `wsgi.py` in the directory,

``` python
from app import create_app

application = create_app()
```
and then the command line `waitress-serve` can be used to launch the server,

``` text
PS C:\flask-test> ~\AppData\Local\Programs\Python\Python310\python.exe -m waitress --port 9000 wsgi:application
INFO:waitress:Serving on http://0.0.0.0:9000
```

With all the help from waitress, I can modify `web.config` as below as final version,

``` xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <system.webServer>
        <handlers>
            <add name="httpPlatformHandler" path="*" verb="*" modules="httpPlatformHandler" resourceType="Unspecified" requireAccess="Script" />
        </handlers>
        <httpPlatform stdoutLogEnabled="true" stdoutLogFile=".\python.log" startupTimeLimit="20" processPath="C:\Users\lextudio\AppData\Local\Programs\Python\Python310\python.exe" arguments="-m waitress --port %HTTP_PLATFORM_PORT% wsgi:application">
        </httpPlatform>
    </system.webServer>
</configuration>
```

## Side Notes

### Flask Web App Under an IIS Site
With HttpPlatformHandler you can definitely host a Flask web app (such as `/flask`) under an IIS site, but you must understand that IIS/HttpPlatformHandler dispatches requests with full URLs to the Python process, so your route definitions in Flask should include the extra application name.

``` python
@app.route("/flask")
def hello_world_app():
    return "<p>Hello, World from /flask IIS application!</p>"
```

### Flask on Azure App Service
With some minimal changes, you can host such a Python/Flask application on Azure App Service (Windows).

### Flask on IIS Express
You can take a look at the [new open source HttpPlatformHandler v2.0 from LeXtudio]({% post_url 2024/2024-4-8-httpplatformhandler-v2 %}).

### Flask with Socket.IO
You might easily hit issues with WebSocket and Socket.IO if you try to host a Python web app on IIS, as many of the Python package authors might not have a Windows machine for testing. You might find the following links useful, but I didn't see a complete solution yet.

* [Python WebSocket package requires compression to be disabled](https://github.com/python-websockets/websockets/issues/1192)
* [Python WebSocket debugging](https://websockets.readthedocs.io/en/stable/howto/cheatsheet.html#debugging)
* [Flask Socket.IO doesn't work well with IIS](https://stackoverflow.com/questions/77771538/flask-socketio-gevent-or-eventlet-windows-iis-do-these-things-work-tog)

## Other Languages on IIS?

If you want to learn more about HttpPlatformHandler and how to host other languages (Go/Node.js/Java) or frameworks (Django/FastAPI), you can read [this post]({% post_url 2023/2023-4-7-the-rough-history-of-iis-httpplatformhandler %}).
