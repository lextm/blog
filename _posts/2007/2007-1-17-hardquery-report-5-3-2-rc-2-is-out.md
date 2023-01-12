---
layout: post
title: "HardQuery Report: 5.3.2 RC 2 is out"
description: "This post is about HardQuery Report 5.3.2 RC 2."
tags: Code-Beautifier-Collection Delphi
permalink: /hardquery-report-5-3-2-rc-2-is-out-c8484fd58ff8
excerpt_separator: <!--more-->
---
(CSDN Jan 17, 2007)

Today I received a letter from Pierre-Jean.Robin. In fact, it is a bug report.

Hello,

I have just installed Code Beautifier V5.3.1.1123 and have a problem with beautifying a document (i run Delphi 2006): the source code is a Delphi unit with 2500 lines. Pressing ctrl+W starts de beautifier but it deletes the end of the source code ! It deletes approximately the last 200 lines of the unit… I have problems with smaller source code. What's wrong ??

Pierre-Jean
<!--more-->

Since the description is so clear, I can easily reproduce the bug using a OTA source file ToolsAPI.pas. And for this 5000+ lines file, the bug is even clearer, because only about 50 lines left!

After debugging for a while, I found that jcf.exe worked fine, so I knew it was something wrong inside CBC. FillBufferWithFile was tested first, and it was okay. Then I was sure CreateFileFromBuffer was the problem. As a matter of fact, these two functions were implemented by David for Sharp Builder Tools and both of them contained bugs.

Now the bug is fixed and I am releasing a new build.

I'd like to say thank you again for all my dear friends for your support. And what I can do to pay back is working hard on this project in the future.

Stay tuned.

P.S.

This bug affects all versions from 5.2.0 to 5.3.1, and 5.3.2.1001. If you are using one of this versions I recommend you download this RC.
