---
layout: post
title: "Doing USB In .NET Easily"
description: This post talks about how to do USB in .NET easily.
tags: .NET
permalink: /doing-usb-in-net-easily-93c79c888f01
excerpt_separator: <!--more-->
---
It is quite funny that even though Microsoft wants Visual C++ and Visual Basic developers to move to C#, it does not provide certain classes in .NET that college students need. For example, when I was at college, I found that no serial port related classes were there in .NET 1.x (they are added until 2.0 such as SerialPort). Up to now, we don't see USB related classes yet in 3.5. Therefore, how can we do USB development easily?
<!--more-->

Thus, how to manipulate USB easily? I recommend SharpUsbLib, a wrapper over libusb.

http://www.icsharpcode.net/OpenSource/SharpUSBLib/default.aspx

## Deployment

Since it is a wrapper, so when you deploy your application, libusb must be deployed besides SharpUsbLib. On Windows platform, you should use LibUsb-Win32. (Notice: it does not officially support Windows Server 2003, Vista, and Server 2008).

http://libusb-win32.sourceforge.net/

## Usage

Even though the demo project in SharpUsbLib does not read or write data through USB, it illustrates how to query Device instances connected to the PC. If you take a look at Device class, you can find I/O functions such as BulkRead, BulkWrite and so on. So it is in fact quite easy to learn and use in your applications.

## License

As a reminder, please notice that SharpUsbLib is published under GPL or LGPL. So if you want to use it in a commercial application, please follow the restrictions of LGPL carefully.
