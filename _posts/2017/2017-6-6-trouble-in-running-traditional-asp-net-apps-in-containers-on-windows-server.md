---
layout: post
title: Trouble in Running Traditional ASP.NET Apps in Containers on Windows Server 2016
description: "This post is about how to run traditional ASP.NET apps in containers on Windows Server 2016."
tags: Docker IIS ASP.NET Windows
permalink: /trouble-in-running-traditional-asp-net-apps-in-containers-on-windows-server-2016-43b755611337
excerpt_separator: <!--more-->
---
Microsoft collaborates with Docker to introduce container support in both Windows 10 and Windows Server 2016. However, due to some unknown reasons, the user experience differs so much that if you find everything is nice and smooth on Windows 10, then things are so painful on Windows Server 2016.
<!--more-->

## Basic Installation

While on Windows 10 you probably need only Docker for Windows, on Windows Server 2016 you need to install Docker engine following [this article](https://docs.docker.com/docker-ee-for-windows/install/#install-docker-ee).

Yup, the PowerShell installation is a little tricky to follow.

## Docker Compose
But that's not enough if you run Visual Studio 2017 to develop Docker based projects, as it would complain about missing docker-compose like

``` bash
Severity Code Description Project File Line Suppression State
Error MSB4018 The "PrepareForBuild" task failed unexpectedly.
Microsoft.DotNet.Docker.CommandLineClientException: Unable to run 'docker-compose'. Verify that Docker for Windows is installed and running locally. For troubleshooting, please review http://aka.ms/DockerToolsTroubleshooting. --> System.ComponentModel.Win32Exception: The system cannot find the file specified
at System.Diagnostics.Process.StartWithCreateProcess(ProcessStartInfo startInfo)
at System.Diagnostics.Process.Start()
at Microsoft.DotNet.Docker.CommandLineClient.<>c__DisplayClass0_0.<ExecuteAsync>b__0()
at System.Threading.Tasks.Task`1.InnerInvoke()
at System.Threading.Tasks.Task.Execute()
-- End of stack trace from previous location where exception was thrown --
at System.Runtime.CompilerServices.TaskAwaiter.ThrowForNonSuccess(Task task)
at System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)
at Microsoft.DotNet.Docker.DockerComposeClient.<ExecuteAsync>d__18.MoveNext()
-- End of inner exception stack trace --
at Microsoft.DotNet.Docker.DockerComposeClient.<ExecuteAsync>d__18.MoveNext()
-- End of stack trace from previous location where exception was thrown --
at System.Runtime.CompilerServices.TaskAwaiter.ThrowForNonSuccess(Task task)
at System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)
at Microsoft.DotNet.Docker.DockerComposeClient.<GetDockerComposeDocumentCacheAsync>d__15.MoveNext()
-- End of stack trace from previous location where exception was thrown --
at System.Runtime.CompilerServices.TaskAwaiter.ThrowForNonSuccess(Task task)
at System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)
at Microsoft.DotNet.Docker.DockerComposeClient.<GetDockerComposeDocumentAsync>d__13.MoveNext()
-- End of stack trace from previous location where exception was thrown --
at System.Runtime.CompilerServices.TaskAwaiter.ThrowForNonSuccess(Task task)
at System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)
at Microsoft.DotNet.Docker.DockerWorkspace.<GetDockerServiceDebugProfilesAsync>d__12.MoveNext()
-- End of stack trace from previous location where exception was thrown --
at System.Runtime.CompilerServices.TaskAwaiter.ThrowForNonSuccess(Task task)
at System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)
at Microsoft.DotNet.Docker.DockerWorkspace.<PrepareForBuildAsync>d__13.MoveNext()
-- End of stack trace from previous location where exception was thrown --
at System.Runtime.CompilerServices.TaskAwaiter.ThrowForNonSuccess(Task task)
at System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)
at Microsoft.DotNet.Docker.BuildTasks.DockerBaseTask.Execute()
at Microsoft.Build.BackEnd.TaskExecutionHost.Microsoft.Build.BackEnd.ITaskExecutionHost.Execute()
at Microsoft.Build.BackEnd.TaskBuilder.<ExecuteInstantiatedTask>d__26.MoveNext() docker-compose C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\MSBuild\Microsoft\VisualStudio\v15.0\Docker\Microsoft.VisualStudio.Docker.Compose.targets 153
```

The error message is more suitable for Windows 10 users, but totally misleading for Windows Server 2016 users. The steps to install docker-compose are different, as [documented here](https://docs.docker.com/compose/install/).

## Low Disk Space Error

Even if you have that installed, you might hit another error message,

``` bash
Severity Code Description Project File Line Suppression State
Error MSB4018 The "PrepareForLaunch" task failed unexpectedly.
Microsoft.DotNet.Docker.CommandLineClientException: Building fullfxweb
Service 'fullfxweb' failed to build: failed to register layer: re-exec error: exit status 1: output: BackupWrite \\?\C:\ProgramData\docker\windowsfilter\c9581b4e19c69827e1360a27530db816849bbc0ee0345f5503dd2765ba2313d4\Files\ProgramData\Microsoft\Windows Defender\Definition Updates\Default\MpAsBase.vdm: There is not enough space on the disk..
For more troubleshooting information, go to http://aka.ms/DockerToolsTroubleshooting --> Microsoft.DotNet.Docker.CommandLineClientException: Building fullfxweb
Service 'fullfxweb' failed to build: failed to register layer: re-exec error: exit status 1: output: BackupWrite \\?\C:\ProgramData\docker\windowsfilter\c9581b4e19c69827e1360a27530db816849bbc0ee0345f5503dd2765ba2313d4\Files\ProgramData\Microsoft\Windows Defender\Definition Updates\Default\MpAsBase.vdm: There is not enough space on the disk.
at System.Runtime.CompilerServices.TaskAwaiter.ThrowForNonSuccess(Task task)
at System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)
at Microsoft.DotNet.Docker.DockerComposeClient.<ExecuteAsync>d__18.MoveNext()
-- End of inner exception stack trace --
at Microsoft.DotNet.Docker.DockerComposeClient.<ExecuteAsync>d__18.MoveNext()
-- End of stack trace from previous location where exception was thrown --
at System.Runtime.CompilerServices.TaskAwaiter.ThrowForNonSuccess(Task task)
at System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)
at Microsoft.DotNet.Docker.DockerWorkspace.<PrepareForLaunchAsync>d__14.MoveNext()
-- End of stack trace from previous location where exception was thrown --
at System.Runtime.CompilerServices.TaskAwaiter.ThrowForNonSuccess(Task task)
at System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)
at Microsoft.DotNet.Docker.BuildTasks.DockerBaseTask.Execute()
at Microsoft.Build.BackEnd.TaskExecutionHost.Microsoft.Build.BackEnd.ITaskExecutionHost.Execute()
at Microsoft.Build.BackEnd.TaskBuilder.<ExecuteInstantiatedTask>d__26.MoveNext() docker-compose C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\MSBuild\Microsoft\VisualStudio\v15.0\Docker\Microsoft.VisualStudio.Docker.Compose.targets 192
```

The cause is in fact simple, as my test machine is low on disk space. The traditional ASP.NET web apps require an image `microsoft/aspnet` to be used, which is pretty large,

![img-description](/images/microsoft-aspnet-docker-image.png)
_Figure 1: Docker Image `microsoft/aspnet`._

Thus, only after freeing enough space, everything starts to move on.

## Visual Studio Debugger Error

Next you might see an error as below ("Unable to start debugging on the web server. The remote server returned an error: (403) Forbidden."),

![img-description](/images/vs-docker-error.png)
_Figure 2: Docker Debugger Error._

So what can be the cause? It is very important now to check the docker container state, so please dig into the Docker logging in Visual Studio Output panel like below,

``` bash
docker ps --filter "status=running" --filter "name=dockercompose1104660429_fullfxweb_" --format {{.ID}} -n 1
c5739cb5ab3b
docker inspect --format="{{.NetworkSettings.Networks.nat.IPAddress}}" c5739cb5ab3b
172.19.8.203
docker exec c5739cb5ab3b cmd /c "C:\Windows\System32\inetsrv\appcmd.exe set config -section:system.applicationHost/applicationPools /[name='DefaultAppPool'].processModel.identityType:LocalSystem /commit:apphost & C:\Windows\System32\inetsrv\appcmd.exe set config -section:system.webServer/security/authentication/anonymousAuthentication /userName: /commit:apphost"
Applied configuration changes to section "system.applicationHost/applicationPools" for "MACHINE/WEBROOT/APPHOST" at configuration commit path "MACHINE/WEBROOT/APPHOST"
Applied configuration changes to section "system.webServer/security/authentication/anonymousAuthentication" for "MACHINE/WEBROOT/APPHOST" at configuration commit path "MACHINE/WEBROOT/APPHOST"
docker exec c5739cb5ab3b powershell -Command if ((Get-Process msvsmon -ErrorAction SilentlyContinue).Count -eq 0) { Start-Process C:\msvsmon\x64\msvsmon.exe -ArgumentList /noauth, /anyuser, /silent, /nostatus, /noclrwarn, /nosecuritywarn, /nofirewallwarn, /nowowwarn, /timeout:2147483646}
```

Note that it uses an IP address of `172.19.8.203`, so I launch a web browser to check the page,

``` text
Server Error in '/' Application.
Runtime Error
```

![img-description](/images/vs-docker-error-2.png)
_Figure 3: Docker Yellow Page of Death._

Make sure you now go back to Visual Studio and add the following tag to web.config,

``` xml
<configuration>
  <system.web>
    <customErrors mode="Off"/>
  </system.web>
</configuration>
```

Then try to debug again and this time your browser should show a more meaningful page,

``` text
Server Error in '/' Application.
Configuration Error
Description: An error occurred during the processing of a configuration file required to service this request. Please review the specific error details below and modify your configuration file appropriately.
Parser Error Message: The 'targetFramework' attribute in the <compilation> element of the Web.config file is used only to target version 4.0 and later of the .NET Framework (for example, '<compilation targetFramework="4.0">'). The 'targetFramework' attribute currently references a version that is later than the installed version of the .NET Framework. Specify a valid target version of the .NET Framework, or install the required version of the .NET Framework.
```

![img-description](/images/vs-docker-error-3.png)
_Figure 4: Docker Configuration Error._

In my case, this project happens to target .NET Framework 4.7, while it seems the Docker image does not support it. So after switching back to 4.5, everything finally works.
