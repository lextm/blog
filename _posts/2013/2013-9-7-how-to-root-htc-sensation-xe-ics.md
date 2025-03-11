---
layout: post
title: "How to Root HTC Sensation XE (ICS)"
description: "This post talks about how I rooted HTC Sensation XE with ICS."
tags: Android
permalink: /how-to-root-htc-sensation-xe-ics-892ca9881b8c
excerpt_separator: <!--more-->
---
I bought an HTC Sensation XE phone last year. Generally speaking it was a nice model. However, like any old enough model it started to suffer performance issues only after a few months of using. Luckily HTC shipped an upgrade to Android 4.0 (ICS) some time in May and after the upgrade the performance got better.

Time flied and this year the phone finally aged and experienced a second wave of slowness which I could not get rid of. Because the warranty wore off, I attempted to flash in CyanogenMod ROM to it. The wonderful thing is that I have been enjoying super fast performance ever since, and never want to go back to HTC's one. I should have blogged about my attempt a long time ago, but I hope now is not too late.
<!--more-->

## General Info on Android

So before we begin, let's visit some general information on how Android is flashed into a phone, as that will give you some ideas on why the following steps are important.

You might not know that on a typical HTC Android phone, there are three ROMs shipped,

* Bootloader
* Recovery
* System (aka the Android we often refer to)

We rarely take a look at the Bootloader as it starts first at phone bootup, and soon switches to System. Often when you see the white background with HTC logo showing on the screen, your phone is executing the Bootloader.

Based on my experiments, System starts roughly when the red BeatsAudio logo appears.

Recovery only appears when you boot the phone (press volume down and power together) to recovery mode.

## Install HTC Sync and Other Preparation

Please go to http://www.htc.com/www/support/ and download HTC Sync (not Sync Manager). Install it on your Windows so that the necessary drivers are installed to the system.

Connect your phone to your PC in USB drive mode and backup your files on the SD card to your PC.

Go to Android Rooted section and download the .zip package for SuperSU if you want to root your phone. Save the package to the root of your SD card, and go back here.

Go to Bootloader S-OFF section and get Ubuntu Live CD and the wire ready. If you are not familiar with Ubuntu, learn about it from http://www.ubuntu.com/ or find a friend to assist.

Go to CyanogenMod Install section and download the .zip packages for CM 10 and Google Apps. Save the packages to the root of your SD card, and go back here.

Go to Settings > Developer Options and turn on USB Debugging.

Go to Settings > Power > Fast boot menu. Uncheck the Fast boot option.

Switch the connection mode from USB to Charge Only.

Before we move on, make sure you fully charge your phone.

## Bootloader Unlock

HTC locks the phones by default. This gives the vendor a chance to ensure that during warranty phase end users do not change the phone at firmware level. You can imagine what happens if it does not lock it up, as nobody can support millions of users who choose from that tons of custom ROMs. Who can tell whether an issue is caused by HTC components or that custom ROMs? It is a good way to guarantee customer service quality.

But HTC is kind enough to provide end users [a chance to unlock the Bootloader](http://htcdev.com/bootloader).

Please follow the steps to unlock your phone, as that's the first milestone you need to hit.

After unlocking, you will have to re-enable USB debugging and disable fast boot again.

## Recovery Image Hack

HTC's default recovery ROM does not have any significantly useful feature. So once you unlock your phone, you should flash a custom recovery ROM.

For me, I choose CWM (aka ClockworkMod), a quite famous option,

http://www.clockworkmod.com/rommanager

The version I use was [5.0.2.0 for HTC Sensation](http://download2.clockworkmod.com/recoveries/recovery-clockwork-5.0.2.0-pyramid.img) (which also applies to XE). The download is an .img file (which is the ROM in raw format).

Then you need to download Android SDK toolkit, and extract it to a path such as C:\android-sdk-windows\tools .

Copy the above .img file we downloaded to the SDK folder, and rename it to recovery.img.

Now let's go to the phone. Boot the phone to Bootloader by holding the volume down button and pressing the power button. After a few seconds your phone will boot into a screen that gives you several options, including fastboot and recovery. Choose fastboot.

Connect the phone to your PC via USB cable.

Open a command prompt and navigate to the SDK folder. We need to execute

``` text
fastboot flash recovery recovery.img
```

This command flashes CWM to the phone and replace the default recovery ROM. Wait till the flashing finishes.

## Backup HTC Sense ROM

Go back to the phone and select Bootloader in the main hboot menu. Scroll to Recovery and select it by clicking the Power button on the phone.

For the first time your phone boots into CWM, and please create a backup via Backup and Restore menu.

## Android Rooted (Optional)

Well, you might have heard the term root a thousand times but never know what it is. Android is based on Linux. The phone vendor removes the root access from their ROMs, but you can add it back by some hack. As that gives root access back, we call the phone is rooted.

I personally chose SuperSU, http://forum.xda-developers.com/showthread.php?t=1538053. We need to download a .zip package from http://download.chainfire.eu/350/SuperSU/UPDATE-SuperSU-v1.60.zip

To install the .zip package, use CWM *install from zip* menu, and then choose UPDATE-SuperSU-v1.60.zip. Choose *Yes - install ****.zip* option. Once done, go back and select Reboot menu.

## Bootloader S-OFF

Now is the most difficult part (I really mean it, as it is very very difficult, so be patient!), in which we will modify the Bootloader in a way called S-OFF. By default, the Bootloader only loads a System image which is signed and verified. That mode is called S-ON. By acquiring S-OFF, we allow the Bootloader to load any ROM we like.

For Sensation XE with ICS upgraded, I can only get [JuopunutBear S-OFF script](http://unlimited.io/juopunutbear.htm) working (all other attempts failed), so you should also take a look at it.

It requires to be running on Linux, which you can easily get by using an Ubuntu Live CD. The steps must be strictly followed, and at last you need to perform [the wire trick](http://forum.xda-developers.com/showpost.php?p=31148857&postcount=343). HTC locks the phone so strict that only the wire trick (which discharge a capacitor) can help us get S-OFF.

My suggestion is that you prepare the wire as indicated, and learn the wire trick from this YouTube video. There are many other video clips but only this one shows the time interval clearly enough for me to follow. Once done, you finished all hacks before installing CM.

## CyanogenMod Install

CM is probably the cleanest custom ROM for phones, as it is almost the same as Google's open source code base. For HTC Sensation XE, you can now use CM 10,

http://wiki.cyanogenmod.org/w/Pyramid_Info

I am now using the nightly, http://download.cyanogenmod.org/?type=nightly&device=pyramid. You go straightly downloading the .zip package. You also need to download Google Apps from http://wiki.cyanogenmod.org/w/Gapps (note that we need to download the one for CM 10, not else).

To install CM 10, you need to also boot into CWM, choose "wipe data" and "wipe cache". Then use "install from zip" twice (first for CM 10, and then for Google Apps).

Aha, the last step is to reboot from CWM, and wait till CM welcomes you.

## Warnings

* Don't be afraid of the steps, man!
* Make sure you read from the beginning to the end and get prepared of what you are supposed to prepare.
* The steps above work for my phone. Whether it applies to your phone perfectly is unknown as HTC does not reveal anything about the slight differences in its models.
