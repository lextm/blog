---
layout: post
title: "Tuning Skills Needed"
description: This post talks about tuning skills to configure LaTeX environment.
tags: Java
permalink: /patching-texlipse-ec5908768adf
excerpt_separator: <!--more-->
---
I use Texlipse with EasyEclipse for C/C++ to maintain Code Beautifier Collection documents. However, since I was forced to use Windows Vista, a lot of problems have prevents me from doing my job.
<!--more-->

First, I could not use CTeX any more. And I found MiCTeX soon to fill in the blank.

Then, I could not make latex.exe run correctly. I found out it needs elevation.

Last, I could not build TeX with Texlipse any more because it does not support Vista well. There were patching methods, but I could not build the project from source myself at that moment.

And it was just yesterday I knew how to build Texlipse easily, so I finally made Texlipse running on Vista.

Here is the steps you must take,

Download an Eclipse distribution that supports RCP development. There are a lot of choice. I use Eclipse Europa RCP.

Create a new project from CVS. When the wizard pops up, please enter information like this.

Eclipse will start to download all latest source file from SourceForge. Then you can build the project by right clicking on the project node and Refresh.

Open the project folder and navigate to bin folder, there is a generated folder named net that contains all necessary binary files to patch Texlipse 1.1.0 build.

Now we start to create a patched texlipse.jar. First rename the original texlipse.jar to texlipse.zip. Open this zip package and delete the folder net in it. Here we add the net folder mentioned in last paragraph into the zip file. At last rename texlipse.zip back to texlipse.jar.

I was told that a new release of Texlipse is coming so I think the patch is only temporary.

You can also download the patch I made [here](http://gforge.oss.org.cn/frs/download.php/166/texlipse.jar).

Somebody said in the forums that using Eclipse in compatibility mode is a workaround, I tried but I failed.

Even if you install the patched version of Texlipse, you still need to run Eclipse elevated. This is because latex.exe cannot run properly without elevation.

If you still have problems, please drop a comment here.
