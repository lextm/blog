---
layout: post
title: "What Is Missing in Firefox 3 Beta 4 Release Notes"
description: This post talks about what is missing in Firefox 3 Beta 4 release notes.
tags: Windows
permalink: /what-is-missing-in-firefox-3-beta-4-release-notes-d31cec0a145d
excerpt_separator: <!--more-->
---
I skipped a few important FF milestones after trying Alpha 1. But last month I installed Firefox 3 Beta 3 and suddenly found it stable and super fast. And today Beta 4 is out so I simply navigated to the download page and wanted to download the installer.

SUDDENLY, a pop up told me that FF had found an update, the Beta 4, so it could help me install it in the easy way. Yes, it is just like installing 2.0.0.12 update over 2.0.0.11 so everything is automatic. Wonderful.
<!--more-->

However, no section in the announcement mentions this important thing that could save my time.

http://developer.mozilla.org/devnews/index.php/2008/03/10/firefox-3-beta-4-now-available-for-download/

Also I found that NASA Night Launch theme can work with Beta 4 correctly, even though by default FF told you it is not compatible. Yes, modifying install.rdf can solve it. In my case the file located at C:\Documents and Settings\liyang2\Application Data\Mozilla\Firefox\Profiles\hktxkuf2.default\extensions\nasanightlaunch@example.com\install.rdf. Simply change 3.0b4pre to 3.0b5pre.

http://forums.mozillazine.org/viewtopic.php?t=547498

However, after modifying the file, FF may continue to tell you it is not compatible. A workaround is,

1. switch to default theme and close FF.
1. copy all content of folder C:\Documents and Settings\liyang2\Application Data\Mozilla\Firefox\Profiles\hktxkuf2.default\extensions\nasanightlaunch@example.com\ to a temporary folder.
1. launch FF and close it.
1. copy all content back.
1. launch FF and this time you should be able to apply NASA them.

Stay tuned. I am going to play with Beta 4 until the first RC comes.
