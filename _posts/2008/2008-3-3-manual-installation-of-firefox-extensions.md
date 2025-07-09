---
layout: post
title: "Manual Installation of Firefox Extensions"
description: This post talks about the manual installation of Firefox extensions.
tags: Firefox
permalink: /manual-installation-of-firefox-extensions-9ba8b416ce8a
excerpt_separator: <!--more-->
---
I tried the NASA Night Launch theme this morning at office and fell in love with it immediately. You may have a try, too. The only issue I met is that the default contrast is not as clear as Microsoft Expression Studio, so you could not easily recognize the grayed-out text.

However, at home due to the limited bandwidth I just could not download the theme in the Firefox way tonight. Therefore I saved it as a file and tried to install it manually.

Don't be fooled by the theme package even though its extension is jar. It is not a Java executable but a zip file. The installation steps are,

1. Open install.rdf file in Notepad, and see the value (in this case, nasanightlaunch@example.com).
1. Create a folder named nasanightlaunch@example.com under C:\Users\lextm\AppData\Roaming\Mozilla\Firefox\Profiles\b9zwtf39.default\extensions (this path may be different on your machine).
1. Extract content of nasa_night_launch_*-fx.jar to this newly created folder.
1. Restart Firefox and now you can switch to that theme.

The process is not as hard as I was expecting, so I start to wonder whether I could write an extension of my own some day.
<!--more-->
