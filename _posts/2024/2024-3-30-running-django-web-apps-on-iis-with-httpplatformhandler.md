---
layout: post
title: "Running Django Web Apps on IIS with HttpPlatformHandler"
description: A post about how to create a simple Django web app and host it on IIS with HttpPlatformHandler
tags: IIS Windows Python Django HttpPlatformHandler
excerpt_separator: <!--more-->
---

HttpPlatformHandler can help IIS host Java/Python/Node.js/Go applications, so in this post we wil see how to configure a Python/Django web app on IIS and troubleshoot the common issue.

It becomes very important for Python developers to learn HttpPlatformHandler, because [Microsoft no longer recommends FastCGI](https://docs.microsoft.com/visualstudio/python/configure-web-apps-for-iis-windows?view=vs-2022#configure-the-fastcgi-handler),

> "We recommend using HttpPlatform to configure your apps, as the WFastCGI project is no longer maintained."

<!--more-->

## Prerequisites

To follow this post, you need to have the following software installed,

* Windows 10 or Windows Server 2016 or later (IIS 10 or later)
* HttpPlatformHandler v1.2 (from Microsoft) or [v2.0 (from LeXtudio)]({% post_url 2024/2024-4-8-httpplatformhandler-v2 %})

## Basic Django Setup

No doubt we will start from a sample application as below.

``` batch
cd C:\test-django
C:\Users\lextudio\AppData\Local\Programs\Python\Python310\python.exe -m django startproject mysite
```

This generates a Django project in `C:\test-django\mysite`, and now we can use a simple command `python.exe manage.py runserver` in the directory of `C:\test-django\mysite` can launch the application at port 8000,

``` batch
$ cd mysite
$ C:\Users\lextudio\AppData\Local\Programs\Python\Python310\python.exe manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
March 30, 2024 - 21:58:13
Django version 5.0.3, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

> If Python and Django are not yet installed, you can search for guides.

## HttpPlatformHandler Setup

Now let's download and install HttpPlatformHandler on IIS, and add a `web.config` in `C:\test-django\mysite`,

``` xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <system.webServer>
        <handlers>
            <add name="httpPlatformHandler" path="*" verb="*" modules="httpPlatformHandler" resourceType="Unspecified" requireAccess="Script" />
        </handlers>
        <httpPlatform stdoutLogEnabled="true" stdoutLogFile=".\python.log" startupTimeLimit="20" processPath="C:\Users\<user name>\AppData\Local\Programs\Python\Python310\python.exe" arguments="manage.py runserver %HTTP_PLATFORM_PORT%">
        </httpPlatform>
    </system.webServer>
</configuration>
```

With all settings in place, I can go back to IIS Manager and create a site (I chose *:8014 as site binding) to point to `C:\test-django\mysite`. By opening a web browser and navigate to `http://localhost:8014/`, I should now see the default Django welcome page saying "The install worked successfully! Congratulations!".

## Troubleshooting

Well if you hit any error instead of the default page, please refer to [my old post]({% post_url 2022/2022-7-10-running-flask-web-apps-on-iis-with-httpplatformhandler %}) for troubleshooting tips.

## Production Setup with Uvicorn and WhiteNoise

The above setup is for development only, and you should use a production-ready server like Uvicorn and a static file serving mechanism like WhiteNoise when deploying to production.

First, run `python.exe manage.py check --deploy` to see if there are any issues to fix. Typical changes at this stage in `settings.py` include

``` python
DEBUG = False
ALLOWED_HOSTS = ['*']
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'
```

> To learn more about them (and many other key settings), you can visit [this Django checklist](https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/).

Then, install Uvicorn and WhiteNoise.

``` batch
python.exe -m pip install uvicorn whitenoise
```

Finally, enable WhiteNoise in `settings.py`,

``` python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # add WhiteNoise middleware after SecurityMiddleware.
    # ...
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

> The steps were taken from [WhiteNoise docs](https://whitenoise.readthedocs.io/en/stable/#installation).

One extra step needed here is to move all static files to a central folder,

``` batch
python.exe manage.py collectstatic
```

> This is not only applicable to WhiteNoise, but also to other static file serving mechanisms. But you must do this step after enabling WhiteNoise in `settings.py`, as the generated files are different with and without WhiteNoise.

With all these changes, you can now run Uvicorn to serve the Django application,

``` batch
$ python.exe -m uvicorn mysite.asgi:application
INFO:     Started server process [7072]
INFO:     Waiting for application startup.
INFO:     ASGI 'lifespan' protocol appears unsupported.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

> The Django project already has `asgi.py`, which can be used by Uvicorn to start the application.

At this point, your `web.config` should be updated to use Uvicorn instead of Django's development server,

``` xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <system.webServer>
        <handlers>
            <add name="httpPlatformHandler" path="*" verb="*" modules="httpPlatformHandler" resourceType="Unspecified" requireAccess="Script" />
        </handlers>
        <httpPlatform stdoutLogEnabled="true" stdoutLogFile=".\python.log" startupTimeLimit="20" processPath="C:\Users\<user name>\AppData\Local\Programs\Python\Python310\python.exe" arguments="-m uvicorn mysite.asgi:application --port %HTTP_PLATFORM_PORT%">
        </httpPlatform>
    </system.webServer>
</configuration>
```

You can see how smooth the experience is, compared to what other guides suggest.

## Side Notes

Static files can be served by mechanisms other than WhiteNoise, if you dig further into Django documentation.

You can choose other application server other than Uvicorn, but the key is to use HttpPlatformHandler to host the application on IIS.

## Django on IIS Express

You can take a look at the [new open source HttpPlatformHandler v2.0 from LeXtudio]({% post_url 2024/2024-4-8-httpplatformhandler-v2 %}).

## Other Languages on IIS?

If you want to learn more about HttpPlatformHandler and how to host other languages (Go/Node.js/Java) or frameworks (FastAPI/Flask), you can read [this post]({% post_url 2023/2023-4-7-the-rough-history-of-iis-httpplatformhandler %}).
