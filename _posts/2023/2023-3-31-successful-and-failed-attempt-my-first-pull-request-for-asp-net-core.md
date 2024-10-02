---
layout: post
title: "Successful and Failed Attempt: My First Pull Request for ASP.NET Core"
description: A post about my first pull request for ASP.NET Core related to Windows 11 ARM64 and the roller coaster experience.
tags: .NET Visual-Studio Windows IIS
excerpt_separator: <!--more-->
---

I was fortunate enough to be able to contribute to a lot of open source projects, not only the ones I own, but many others as well. I wrote about some of the important stories such as [this one for SharpDevelop]({% post_url 2012/2012-7-25-opencover-addin-for-sharpdevelop %}) and [this one for Mono]({% post_url 2014/2014-5-29-how-to-create-certificates-in-c-via-mono-security %}). There are more such pull requests and I acknowledge that not all of them were accepted due to various reasons. In this post, I will write about my recent experience with ASP.NET Core on Windows 11 ARM64, and my first pull request for the repo.

## Apple Silicon, ARM64, and Windows ARM64

Clearly ARM64 first caught my eyes when Apple used it (Apple A7 chip) in iPhone 5S in 2013, the first such chip used in a flagship consumer product. iOS developers were requested to build their apps for ARM64 and package them into the Universal Binary format. The challenges were huge as many dependencies might not be compatible with ARM64 at that time. The same thing happened when Apple shipped the first Mac with ARM64 Apple Silicon in November 2020 (Mac mini M1, which is what I am using now to write this). But since M1/M2 are quite successful, developers are now with all compatible tools and frameworks, and end users rarely experience big issues.

However, Microsoft was late to the party. While Windows started to support ARM chips as early as 2016, only in 2021 ARM64 support landed with the release of Windows 11. Even now, the first quarter of 2023 ends, the special Windows 11 ARM64 builds are still in preview without a clear release date. A few hardware vendors such as Samsung and Lenovo have released ARM64 Windows 11 laptops, but they are not cheap and far from widely available.

I decided to take a further look when participating in [a thread](https://learn.microsoft.com/answers/questions/1183655/unable-to-run-net-4-8-apps-on-iis-using-arm-proces), and built a virtual machine on my Mac mini M1 with VMware Fusion. The journey started then.

## Windows ARM64 Installation and Configuration

There are tons of tutorials you can find over the internet, so I won't duplicate the contents. One critical thing I learned is to disconnect the VM fro the internet during the installation (otherwise, you cannot bypass the initial setup screens). Make sure to open the soft keyboard so that I can type the necessary key combination and launch the command prompt.

Once I was able to see your desktop, things became familiar and I could easily turn on IIS features (except ASP.NET 3.5 and anything related). .NET Framework 4.8 has been ported to ARM64, so as expected ASP.NET 4.x works flawlessly there. .NET Framework 3.5 is just too old to be ported over, but Microsoft didn't yet remove its legacy things from various places.

## ASP.NET Core on Windows ARM64, Tough Start

Next, I could install .NET 6/7/8 SDK on this virtual machine and played out .NET apps. Note that .NET 6 does not have native ARM64 support, so from SDK bits to apps, everything is either x86 or x64 and runs in emulation mode. .NET 7 and 8 ship with native ARM64 support, so that I can build apps that run natively on ARM64.

The most challenging part is to run ASP.NET Core apps on IIS, because when I chose all the default settings on IIS to create a site and mapped it to a published `win-arm64` self contained ASP.NET Core 7 app, IIS failed to start it surprisingly.

![ASP.NET Core 7 500 Error Page](/images/aspnetcore7-iis-500.png)
_Figure 1: 500 error page of ASP.NET Core 7_

As I am familiar with ASP.NET Core troubleshooting, the actual error was recorded in Windows event log, and the error message was clear.

![ASP.NET Core 7 500 Error in Event Viewer](/images/aspnetcore7-iis-500-2.png)
_Figure 2: ASP.NET Core module log entry in Windows event log_

If I published the artifacts as `win-arm64`, then the culprit can only be that IIS worker process (`w3wp.exe`) was running in non-ARM64 mode. To learn more about this, I opened up IIS Manager and checked the application pool settings.

![IIS ARM64 New Setting](/images/iis-arm64-setting.png)
_Figure 3: IIS application pool new setting for ARM64_

No doubt there is now a new setting called "Enable Emulation on ARM64" which is set to `True` by default. Combining it with "Enable 32-Bit Applications" (which is `False` by default), IIS worker process for this pool was indeed running in x64 mode. And that explains the crash.

By changing the new setting to `False`, IIS could then start the worker process in ARM64 mode, and the app ran successfully afterward.

> You might wonder why "Enable Emulation on ARM64" is set to `True` by default. I think it is because most existing web apps are x64 compatible, so it is better to run them in x64 mode initially. .NET 6 web apps are good examples and you can find existing threads like [this one](https://stackoverflow.com/questions/71317484/asp-net-core-6-app-fails-to-start-up-on-iis-in-windows-11-arm-os) over the internet.

## More Bitness Issues Ahead

To play further with the application pool settings, I also published the same web app as `win-x86` and `win-x64` self contained apps and hosted them on IIS with x86 and x64 application pools respectively. Naturally I assumed that they work fine, but I was totally wrong.

The x86 application pool crashed, and which again indicated something was wrong with the bitness of the worker process. Further investigation showed that the Windows Server hosting bundle mistakenly installed the ARM64 build of `aspnetcorev2.dll` and related to the x86 Program Files folder. This is clearly a bug and I decided to include it in the bug report later.

The x64 application pool also crashed, which raises a bigger question that where should the x64 build of `aspnetcorev2.dll` go during installation. So, it is a huge surprise to me that Windows 11 does not have a x64 Program Files folder like the x86 one. How can that be possible?

## The Magic of Windows 11 ARM64, Arm64X

By reading further through Microsoft Docs, I finally learned that instead of extending the old WOW64 emulation layer (the trick around x86 Program Files and so on), Microsoft engineers developed [a new approach called Arm64X](https://learn.microsoft.com/windows/arm/arm64x-pe) so that binaries can be built by merging x64 (ARM64EC) and ARM64 bits together in the same Portable Executable (PE) file. This is a very good idea (similar to Universal Binary used by Apple), so I could then understand why there is no x64 Program Files folder on Windows 11 ARM64.

Therefore, to fix the x64 application pool crash, I thought I needed to produce an Arm64X build of `aspnetcorev2.dll` and put it in the right place. I cloned the code base and started to dig further. However, I couldn't move much further even after fixing many common challenges in the C++ project files, because the compilation seems to need Arm64X build of ASP.NET Core runtime itself, which isn't available.

> I felt lucky that for one of my previous employers there was a project based on ASP.NET Core module source code, so I used to dig into the code base and understood roughly how it works. Otherwise, I wouldn't have dared to build it as Arm64X.

A hint called ["Arm64X pure forwarder DLL"](https://learn.microsoft.com/windows/arm/arm64x-build) was then the only option on the table, and I decided to try it out. Luckily after producing my own pure forwarders and reorganizing the ASP.NET Core bits in the Program Files folder, I can get the x64 application pool running properly.

> This article had some mistakes in it, so I sent a pull request to fix the contents separately, which was merged and published. You are now reading the fixed version.

## Out-Of-Process Challenges Remain

With ASP.NET Core in-process mode test cases passed, I expected out-of-process mode to work as well. However, I was wrong again. The out-of-process mode was still not working for x64 and ARM64, and I wonder why pure forwarder approach can work for in-process mode but not out-of-process mode.

Even though Visual Studio 2022 can be installed on Windows 11 ARM64 to assist me debugging further, I was trying to use a simple tool like [Process Monitor](https://docs.microsoft.com/sysinternals/downloads/procmon) to see what's going on.

Without much effort I found that in out-of-process mode ASP.NET Core module was trying to load `aspnetcorev2_outofprocess.dll` from the wrong location and failed. It did load the pure forwarder DLL from the Program Files folder but didn't scan the same folder for the out-of-process module dependencies, the actual ARM64 and x64 binaries.

> Note that you must use the native ARM64 build of Process Monitor to capture the events.

By reviewing the C++ code, I found that the call to `LoadLibrary` indeed does not ask Windows to load dependencies from the right folder. I added this finding to my bug report.

I patched ASP.NET Core module to load dependencies via `LoadLibraryEx` and set the `LOAD_LIBRARY_SEARCH_DLL_LOAD_DIR` flag, and my patched module was then working properly in out-of-process mode.

## The One Pull Request to Rule Them All

After finishing the investigation, time to put everything together and conclude with a pull request.

First, I needed to revise the WiX installer to install the correct x86 bits, and that was very simple.

Second, I needed to upgrade the WiX installer to install the x64 and ARM64 bits along with Arm64X pure forwarders. This was a bit more challenging because the build process must then add extra steps to product the pure forwarder DLLs. Visual C++ does not yet have a project template to produce such binaries, so I had to write a custom build script to do the job, which took me quite a while as I needed to figure out all the details like how to locate the installed VC++ toolchain in my script.

Third, I needed to add my one-line patch on `LoadLibrary` to ASP.NET Core module itself.

Finally, I opened [a new issue on GitHub](https://github.com/dotnet/aspnetcore/issues/47115) and attach [a pull request](https://github.com/dotnet/aspnetcore/pull/47290) to it.

## The Not-So-Happy Ending

The pull request was reviewed but closed because the team currently didn't see Windows 11 ARM64 a strategical platform that they put more resources into.

Instead of leaving any future brave Windows ARM64 explorers like me in the same situation, I decided to create simple PowerShell scripts to patch the flawed ASP.NET Core installation by reusing the existing binaries and you can visit this [new GitHub repo](https://github.com/lextm/ancm-arm64) to learn more.

Thanks for reading this far, as it is such a long post and I rarely write in this way for a very long time. Hope now you understand more about Windows 11 ARM64 and ASP.NET Core.
