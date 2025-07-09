---
layout: post
title: "GrapeVine Voice: Unhandled Exceptions Revisited, Part I"
description: This post talks about how to handle unhandled exceptions.
tags: Code-Beautifier-Collection Delphi
excerpt_separator: <!--more-->
---
I have used Mauro's library to handle unhandled exceptions for years. However, lately I decided to improve my usage and added some advanced features such as sending exception logs to my mail box so that I can collect and analyse them.

http://cc.codegear.com/Item/24014

According to Mauro's source code, this should be done by using TExceptionManager.AddInfoManagerType. However, I find a bug there in version 2.3, so I have to modify the source code myself and create a customized 2.3.1 version.

http://gforge.oss.org.cn/frs/download.php/200/24014_unhandledexceptionmanager_for_.net.zip

For 2.3.1 version, if you want to change the default exception dialogue, please create a form that implements IExceptionInfoManager. Then you can set TExceptionManager.DefaultInfoManagerType to type of your form. In my case, the source code is,

``` csharp
TExceptionManager.DefaultInfoManagerType = typeof(UnhandledExDlgForm);
TExceptionManager.Initialize();
TExceptionManager.UserContinue = true;
```

An interesting discovery is that Delphi for .NET compiler automatically merges Borland.Delphi.dll into my modified UnhandledExceptionManager.dll. So ILMerge is not needed here.

Also I find a issue that signing a Delphi for .NET assembly is so hard. First, IDE cannot generate a key file for you. Second, signing the debug version does not mean the release version is signed automatically for you. OMG, it seems that using Delphi for .NET is quite inconvenient.
<!--more-->
