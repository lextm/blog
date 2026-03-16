---
description: This post talks about how to get Windows Service executable name and
  path.
excerpt_separator: <!--more-->
layout: post
permalink: /windows-service-file-name-56f73788dcb9
tags: .net windows
categories: [Programming Languages]
title: Windows Service File Name
---
When you get a ServiceController instance, how do you know the executable name and path? WMI makes it possible. You can use this GetServicePath function to query service executable name and path.
<!--more-->

``` csharp
private static string GetServicePath(ServiceController service)
{
    //construct the management path
    string path = "Win32_Service.Name='" + service.ServiceName + "'";
    ManagementPath p = new ManagementPath(path);
    //construct the management object
    ManagementObject ManagementObj = new ManagementObject(p);
    if (ManagementObj["pathName"] != null)
    {
        return ManagementObj["pathName"].ToString().Replace("\"", null);
    }
    else
    {
        return null;
    }
}
```