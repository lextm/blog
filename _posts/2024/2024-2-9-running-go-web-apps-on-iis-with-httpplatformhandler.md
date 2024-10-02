---
layout: post
title: "Running Go Web Apps on IIS with HttpPlatformHandler"
description: A post about how to create a simple Go web app and host it on IIS with HttpPlatformHandler
tags: IIS Windows Go Echo HttpPlatformHandler
excerpt_separator: <!--more-->
---

HttpPlatformHandler can help IIS host Java/Python/Node.js/Go applications, so in this post we wil see how to configure a Go/Echo web app on IIS and troubleshoot the common issue.

<!--more-->

## Prerequisites

To follow this post, you need to have the following software installed,

* Windows 10 or Windows Server 2016 or later (IIS 10 or later)
* HttpPlatformHandler v1.2 (from Microsoft) or [v2.0 (from LeXtudio)]({% post_url 2024/2024-4-8-httpplatformhandler-v2 %})

## Basic Go/Echo Setup

At the beginning, we will start by installing Go on this machine,

``` bash
winget install GoLang.Go
```

After that we will start to make a sample application,

``` batch
cd C:\
mkdir test-go
cd test-go
go mod init test-go
go get github.com/labstack/echo/v4
```

Next, create a file `server.go` with the following content,

``` go
package main

import (
  "net/http"

  "github.com/labstack/echo/v4"
)

func main() {
  e := echo.New()
  e.GET("/", func(c echo.Context) error {
    return c.String(http.StatusOK, "Hello, World!")
  })
  e.Logger.Fatal(e.Start(":1323"))
}
```

> The steps are taken from [Echo documentation](https://echo.labstack.com/docs/quick-start).

Now on this Windows machine with Go and Echo installed, a simple command `go run server.go` in the directory of `C:\test-go\` can launch the application at port 1323.

``` text
PS C:\test-go> go run server.go

   ____    __
  / __/___/ /  ___
 / _// __/ _ \/ _ \
/___/\__/_//_/\___/ v4.11.4
High performance, minimalist Go web framework
https://echo.labstack.com
____________________________________O/_______
                                    O\
⇨ http server started on [::]:1323
```

To make this Go web app works with IIS, we need to modify the code a bit to read the port number from environment variable `HTTP_PLATFORM_PORT`,

``` go
package main

import (
  "flag"
  "net/http"
  
  "github.com/labstack/echo/v4"
)

func main() {
  port := flag.String("port", "1323", "port to listen on")
  flag.Parse()

  e := echo.New()
  e.GET("/", func(c echo.Context) error {
    return c.String(http.StatusOK, "Hello, World!")
  })
  e.Logger.Fatal(e.Start(":" + *port))
}
```

Compile the code to an executable file,

``` bash
go build server.go
```

After compilation, a file `server.exe` is created in the directory.

## HttpPlatformHandler Setup

Now let's download and install HttpPlatformHandler on IIS, and add a `web.config` in `C:\test-go`,

``` xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <system.webServer>
        <handlers>
            <add name="httpPlatformHandler" path="*" verb="*" modules="httpPlatformHandler" resourceType="Unspecified" requireAccess="Script" />
        </handlers>
        <httpPlatform stdoutLogEnabled="true" stdoutLogFile=".\go.log" startupTimeLimit="20" processPath="server.exe" arguments="--port %HTTP_PLATFORM_PORT%">
        </httpPlatform>
    </system.webServer>
</configuration>
```

With all settings in place, I can go back to IIS Manager and create a site (I chose *:8086 as site binding) to point to `C:\flask-test`. By opening a web browser and navigate to `http://localhost:8086/`, I should now see "Hello, World!". Ah, what happened?

## Troubleshooting

### 0x8007005

Yeah I am not able to see "Hello, World!" but a Bad Gateway error page with the Error Code of `0x80070005`.

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

This isn't hard to understand, because anything under `C:\test-go\` is protected and not accessible by IIS application pools by default. So I need to grant read permission to the local group `IIS_IUSRS`.

### 0x8007002

After fixing the file system permission issue, another Bad Gateway error page with the Error Code of `0x80070002` appears.

The cause is actually simple, that Windows/IIS tries to resolve `server.exe` from the system path, but it is not there. So I need to modify `web.config` to use the full path or simply `.\server.exe` to make it work.

## Side Notes

So, at this very moment, the `web.config` should look like this,

``` xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <system.webServer>
        <handlers>
            <add name="httpPlatformHandler" path="*" verb="*" modules="httpPlatformHandler" resourceType="Unspecified" requireAccess="Script" />
        </handlers>
        <httpPlatform stdoutLogEnabled="true" stdoutLogFile=".\go.log" startupTimeLimit="20" processPath=".\server.exe" arguments="--port %HTTP_PLATFORM_PORT%">
        </httpPlatform>
    </system.webServer>
</configuration>
```

## Go on IIS Express

You can take a look at the [new open source HttpPlatformHandler v2.0 from LeXtudio]({% post_url 2024/2024-4-8-httpplatformhandler-v2 %}).

## Other Languages on IIS?

If you want to learn more about HttpPlatformHandler and how to host other languages (Python/Node.js/Java), you can read [this post]({% post_url 2023/2023-4-7-the-rough-history-of-iis-httpplatformhandler %}).
