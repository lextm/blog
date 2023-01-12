---
layout: post
title: "Android Support Repository and Xamarin.Android"
description: "This post is about how Android Support Repository works with Xamarin.Android."
tags: .NET
permalink: /android-support-repository-and-xamarin-android-4d7de680bcf2
excerpt_separator: <!--more-->
---
I have been playing with Xamarin.Android a little bit recently, and discovered some interesting facts about its compilation. This post focuses on the issues and also digs out the details behind the error messages.
<!--more-->

## Downloading Android Support Repository

If you haven't installed Android bits properly, the very first compilation of an Android project (in my case, a Xamarin.Forms project) would take a very long time. This initially seemed to be horrible, and even more for me as I am behind the Great Firewall of China, but I soon found out Xamarin Studio was trying to download one of the Android packages from Google, android_m2repository_r29.zip, aka Android Support Repository. The version number might be different on your machine based on a few factors (Xamarin.Android version I think).

It is rather strange in my case that Xamarin Studio wants to download release 29, while I have already installed release 30 from Android SDK Manager.

## Construction of Cache Folders

Once that file is downloaded, it would be renamed and placed in ~/.local/share/Xamarin/zips folder on OS X (on Windows the path is %homepath%\AppData\Local\Xamarin\zips). Then Xamarin Studio would automatically extract its contents and create a sequence of folders under ~/.local/share/Xamarin.

It turns out that such folders contain Java source files. Probably Xamarin.Forms uses them to simulate native controls on older releases of Android.

## Error Messages Related

Now comes the interesting part, where several error messages can appear if the above cache folder construction fails. Tons of posts are about them over the Internet, but few or none receives the necessary explanation from experts.

> Typical Error 1: "_Unzipping failed. Please download https://dl-ssl.google.com/android/repository/android_m2repository_r29.zip and extract it to the .local/Xamarin/Xamarin.Android.Support.v4/23.3.0.0/content directory."

The exact cause of the above error, is that during the download process, something broke the ZIP package. Then Xamarin Studio would not be able to extract the necessary files to construct the folders.

Solutions can be,

* Remove the corrupt ZIP package under ~/.local/share/Xamarin/zips and try to compile again. This will trigger another download and it might work fine.
* Or you manually download the ZIP package, and use it to replace the corrupt ZIP package under ~/.local/share/Xamarin/zips. Note that the file name must match, or Xamarin Studio will start to download it again. Don't follow the error message to extract to …/content folder, as that won't work.

The version number might not be 29 in your case, and then simply use the version required by the error message.

> Typical Error 2: "Android resource directory .local/Xamarin/Xamarin.Android.Support.v4/23.3.0.0/embedded doesn't exist"

The cause is quite similar to case 1. The solution is to clean the solution and recompile. It should trigger the download automatically. Then if you hit case 1, you can follow the solutions above.

Overall, it is much more difficult to set up Xamarin.Android compared to Xamarin.iOS, but hope you enjoy the fun to develop mobile apps in C#.
