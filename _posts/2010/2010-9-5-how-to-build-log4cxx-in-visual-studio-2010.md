---
layout: post
title: "How To Build Log4cxx In Visual Studio 2010"
description: This post is about how to build log4cxx in Visual Studio 2010.
tags: Visual-Studio
permalink: /how-to-build-log4cxx-in-visual-studio-2010-a69d9bbd65d7
excerpt_separator: <!--more-->
---
Daniel mentioned how he managed to build log4cxx in Visual Studio. However, he did not provide more details. So this blog post serves as a detailed explanation.

http://old.nabble.com/Unable-to-build-with-VS2010-td28519743.html

We are going to follow the steps here, http://logging.apache.org/log4cxx/building/vstudio.html. However, we must make changes to adapt to Visual Studio 2010.
<!--more-->

## Preparation

1. Download the log4cxx ZIP package from here, http://logging.apache.org/log4cxx/download.html, and extract its content.
1. Download apr and apr-util ZIP packages from here, http://apr.apache.org/download.cgi.
1. Now let's translate the original commands into manual steps,

``` text
unzip apr-1.2.11-win32-src.zip      -> manually extract this zip
rename apr-1.2.11 apr               -> rename the extracted folder
unzip apr-util-1.2.10-win32-src.zip -> manually extract this zip
rename apr-util-1.2.10 apr-util     -> rename this folder too
cd apache-log4cxx-0.10.0
configure                           -> execute configure.bat
configure-aprutil                   -> see below*
```
\* as the sed tool is not available on Windows, you must do the following,

1. Open `apr-util\include\apu.hw`.
1. Find the line starting with `#define APU_HAVE_APR_ICONV`.
1. Change this constant to 0 and save.
1. Open `apr-util\include\apr_ldap.hw`.
1. Find the line starting with `#define APR_HAS_LDAP`
1. Change this constant to 0.

The changes mean that we won't use APR ICONV and LDAP support.

## Building log4cxx.dll

Now we have to convert *.dsw to *.cxproj. In order to make it smooth, you may launch Visual Studio 2010 and open log4cxx.dsw.

VS will ask if you like to convert everything. Simply click Yes.

xml, apr, and apr-util projects may build without any problem. If apr fails, and you find out _WIN32_WINNT is less than _WIN32_WINNT_WINXP, you may go to its Properties->Configuration Properties->C/C++->Preprocessor. Then you edit Preprocessor Definitions and add _WIN32_WINNT=_WIN32_WINNT_WINXP.

log4cxx.dll must fail with hundreds of errors. But don't mind it. The root cause is that VC++ has a bug (http://connect.microsoft.com/VisualStudio/feedback/details/473882/error-message-c-c-optimizing-compiler-stopped-working) and VC++ team decided to generate this error. Well, that forces all of us to take the workaround.

LOG4CXX_LIST_DEF macro is used to define classes. As error C2252 is there, we have to move such macro usages out of any classes. That's what Daniel meant in point 1.

Point 2 is necessary because we moved the nested classes out of their parent classes. Now we can use KeySet instead of LoggingEvent::KeySet.

Point 3 and 4 are also necessary. Note that for point 4 you may find all generated lib/dll from Output panel in Visual Studio after building xml, apr, and apr-util. Then you can modify Linker settings for log4cxx to include such folders and lib files.

Once you fixed all things, you should have log4cxx compiled successfully on your machine.

(Update: Thanks for who has commented this post. You might check out the comments, as many of them are very valuable by providing more details on one of the steps or alternative approaches.)
