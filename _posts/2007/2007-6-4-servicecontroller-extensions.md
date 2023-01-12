---
layout: post
title: "ServiceController Extensions"
description: "This post describes how to get the executable name of a Windows service."
tags: Windows .NET
permalink: /servicecontroller-extensions-de5af7a92903
excerpt_separator: <!--more-->
---

In the afternoon I had to do something with Windows services. As a result a better `ServiceController` should be used to know the executable name.

I searched on CodeProject.com. Yes, there is an old article. In the comments section, the technique was mentioned that `System.Management `should be used.

https://www.codeproject.com/Articles/7665/Extend-ServiceController-class-to-change-the-Start

Fine, everything works well as expected. Thanks a lot, Mohamed Sharaf.
<!--more-->

BTW, it is still not easy to use the code in the sample because I need to call `ServiceController.GetServices()` so I write a static function instead,

``` csharp
public static string GetServicePath(ServiceController service)
{
    //construct the management path
    string path = "Win32_Service.Name='" + service.ServiceName + "'";
    ManagementPath p = new ManagementPath(path);
    //construct the management object
    ManagementObject ManagementObj = new ManagementObject(p);
    if (ManagementObj["pathName"] != null)
    {
        return ManagementObj["pathName"].ToString();
    }
    else
    {
        return null;
    }
}
```
