---
description: Follow my journey of investigating and fixing ASP.NET Core compatibility issues with Windows 11 ARM64, including the technical challenges of creating a pull request for Microsoft's ASP.NET Core repository and developing a workaround for ARM64 systems.
image:
  path: /images/downtown-view-from-fort-york.jpg
  alt: Copyright © Lex Li. Downtown Toronto skyline viewed from Fort York.
excerpt_separator: <!--more-->
layout: post
tags: .net iis visual-studio windows microsoft open-source
categories: [Tools and Platforms]
title: 'Successful and Failed Attempt: My First Pull Request for ASP.NET Core'
---
I was fortunate enough to be able to contribute to a lot of open source projects, not only the ones I own, but many others as well. I wrote about some of the important stories such as [this one for SharpDevelop]({% post_url 2012/2012-7-25-opencover-addin-for-sharpdevelop %}) and [this one for Mono]({% post_url 2014/2014-5-29-how-to-create-certificates-in-c-via-mono-security %}). There are more such pull requests and I acknowledge that not all of them were accepted due to various reasons. In this post, I will write about my recent experience with ASP.NET Core on Windows 11 ARM64, and my first pull request for the repo.

## Apple Silicon, ARM64, and Windows ARM64

Clearly ARM64 first caught my eyes when Apple used it (Apple A7 chip) in iPhone 5S in 2013, the first such chip used in a flagship consumer product. iOS developers were requested to build their apps for ARM64 and package them into the Universal Binary format. The challenges were huge as many dependencies might not be compatible with ARM64 at that time. The same thing happened when Apple shipped the first Mac with ARM64 Apple Silicon in November 2020 (Mac mini M1, which is what I am using now to write this). But since M1/M2 are quite successful, developers are now with all compatible tools and frameworks, and end users rarely experience big issues.

However, Microsoft was late to the party. While Windows started to support ARM chips as early as 2016, only in 2021 ARM64 support landed with the release of Windows 11. Even now, the first quarter of 2023 ends, the special Windows 11 ARM64 builds are still in preview without a clear release date. A few hardware vendors such as Samsung and Lenovo have released ARM64 Windows 11 laptops, but they are not cheap and far from widely available.

I decided to take a further look when participating in [a thread](https://learn.microsoft.com/answers/questions/1183655/unable-to-run-net-4-8-apps-on-iis-using-arm-proces), and built a virtual machine on my Mac mini M1 with VMware Fusion. The journey started then.

## Windows ARM64 Installation and Configuration

There are tons of tutorials you can find over the internet, so I won't duplicate the contents. One critical thing I learned is to disconnect the VM from the internet during the installation (otherwise, you cannot bypass the initial setup screens). Make sure to open the soft keyboard so that you can type the necessary key combination and launch the command prompt.

Once I was able to see my Windows desktop, things became familiar and I could easily turn on IIS features (except ASP.NET 3.5 and anything related). .NET Framework 4.8 has been ported to ARM64, so as expected ASP.NET 4.x works flawlessly there. .NET Framework 3.5 is just too old to be ported over, but Microsoft didn't yet remove its legacy things from various places.

## ASP.NET Core on Windows ARM64, Tough Start

Next, I could install .NET 6/7/8 SDK on this virtual machine and played with .NET apps. Note that .NET 6 does not have native ARM64 support, so from SDK bits to apps, everything is either x86 or x64 and runs in emulation mode. .NET 7 and 8 ship with native ARM64 support, so I could build apps that run natively on ARM64.

### The Initial 500 Error

The most challenging part is to run ASP.NET Core apps on IIS, because when I chose all the default settings on IIS to create a site and mapped it to a published `win-arm64` self contained ASP.NET Core 7 app, IIS failed to start it surprisingly.

![ASP.NET Core 7 500 Error Page](/images/aspnetcore7-iis-500.png)
_Figure 1: 500 error page of ASP.NET Core 7_

As I am familiar with ASP.NET Core troubleshooting, the actual error was recorded in Windows event log, and the error message was clear.

![ASP.NET Core 7 500 Error in Event Viewer](/images/aspnetcore7-iis-500-2.png)
_Figure 2: ASP.NET Core module log entry in Windows event log_

### Discovering the New Application Pool Setting

If I published the artifacts as `win-arm64`, then the culprit can only be that IIS worker process (`w3wp.exe`) was running in non-ARM64 mode. To learn more about this, I opened up IIS Manager and checked the application pool settings.

![IIS ARM64 New Setting](/images/iis-arm64-setting.png)
_Figure 3: IIS application pool new setting for ARM64_

No doubt there is now a new setting called "Enable Emulation on ARM64" which is set to `True` by default. Combining it with "Enable 32-Bit Applications" (which is `False` by default), IIS worker process for this pool was indeed running in x64 mode. And that explains the crash.

By changing the new setting to `False`, IIS could then start the worker process in ARM64 mode, and the app ran successfully afterward.

> You might wonder why "Enable Emulation on ARM64" is set to `True` by default. I think it is because most existing web apps are x64 compatible, so it is better to run them in x64 mode initially. .NET 6 web apps are good examples and you can find existing threads like [this one](https://stackoverflow.com/questions/71317484/asp-net-core-6-app-fails-to-start-up-on-iis-in-windows-11-arm-os) over the internet.

## More Bitness Issues Ahead

To play further with the application pool settings, I also published the same web app as `win-x86` and `win-x64` self contained apps and hosted them on IIS with x86 and x64 application pools respectively. Naturally I assumed that they would work fine, but I was totally wrong.

### The x86 Application Pool Problem

The x86 application pool crashed, and which again indicated something was wrong with the bitness of the worker process. Further investigation showed that the Windows Server hosting bundle mistakenly installed the ARM64 build of `aspnetcorev2.dll` and related to the x86 Program Files folder. This is clearly a bug and I decided to include it in the bug report later.

### The x64 Application Pool Mystery

The x64 application pool also crashed, which raises a bigger question of where should the x64 build of `aspnetcorev2.dll` go during installation. So, it is a huge surprise to me that Windows 11 does not have a x64 Program Files folder similar to the x86 one. How can that be possible?

## The Magic of Windows 11 ARM64, Arm64X

By reading further through Microsoft Docs, I finally learned that instead of extending the old WOW64 emulation layer (the trick around x86 Program Files and so on), Microsoft engineers developed [a new approach called Arm64X](https://learn.microsoft.com/windows/arm/arm64x-pe) so that binaries can be built by merging x64 (ARM64EC) and ARM64 bits together in the same Portable Executable (PE) file. This is a very good idea (similar to Universal Binary used by Apple), so I could then understand why there is no x64 Program Files folder on Windows 11 ARM64.

### Building an Arm64X Solution

Therefore, to fix the x64 application pool crash, I thought I needed to produce an Arm64X build of `aspnetcorev2.dll` and put it in the right place. I cloned the code base and started to dig further. However, I couldn't move much further even after fixing many common challenges in the C++ project files, because the compilation seems to need Arm64X build of ASP.NET Core runtime itself, which isn't available.

> I felt lucky that for one of my previous employers there was a project based on ASP.NET Core module source code, so I used to dig into the code base and understood roughly how it works. Otherwise, I wouldn't have dared to build it as Arm64X.

A hint called ["Arm64X pure forwarder DLL"](https://learn.microsoft.com/windows/arm/arm64x-build) was then the only option on the table, and I decided to try it out. After producing my own pure forwarders and reorganizing the ASP.NET Core bits in the Program Files folder, I was able to get both the x64 and ARM64 application pools running properly.

> Note that this article used to have some mistakes in it, so I sent a pull request to fix the contents separately, which was merged and published. You are now reading the fixed version.
>
> Recent versions of the Visual C++ linker (`link.exe`) have a bug that can affect the creation of pure forwarder DLLs, which may cause unexpected issues. For more details, see [dotnet/aspnetcore#62585](https://github.com/dotnet/aspnetcore/pull/62585).

## Out-Of-Process Challenges Remain

With ASP.NET Core in-process mode test cases passed, I expected out-of-process mode to work as well. However, I was wrong again. The out-of-process mode was still not working for x64 and ARM64, and I wonder why pure forwarder approach can work for in-process mode but not out-of-process mode.

### Debugging with Process Monitor

Even though Visual Studio 2022 can be installed on Windows 11 ARM64 to assist me debugging further, I was trying to use a simple tool like [Process Monitor](https://docs.microsoft.com/sysinternals/downloads/procmon) to see what's going on.

Without much effort I found that in out-of-process mode ASP.NET Core module was trying to load `aspnetcorev2_outofprocess.dll` from the wrong location and failed. It did load the pure forwarder DLL from the Program Files folder but didn't scan the same folder for the out-of-process module dependencies, the actual ARM64 and x64 binaries.

> Note that you must use the native ARM64 build of Process Monitor to capture the events.

### The LoadLibrary Issue

By reviewing the C++ code, I found that the call to `LoadLibrary` indeed does not ask Windows to load dependencies from the right folder. I added this finding to my bug report.

I patched ASP.NET Core module to load dependencies via `LoadLibraryEx` and set the `LOAD_LIBRARY_SEARCH_DLL_LOAD_DIR` flag, and my patched module was then working properly in out-of-process mode.

> Luckily this was later determined to be a Windows ARM64 bug, and the fix was to be made in the Windows team. I did roll back the change of `LoadLibraryEx` to `LoadLibrary` in my pull request.

## The One Pull Request to Rule Them All

After finishing the investigation, it was time to put everything together and conclude with a pull request.

First, I needed to revise the WiX installer to install the correct x86 bits, and that was very simple.

Second, I needed to upgrade the WiX installer to install the x64 and ARM64 bits along with Arm64X pure forwarders. This was a bit more challenging because the build process must then add extra steps to produce the pure forwarder DLLs. Visual C++ does not yet have a project template to produce such binaries, so I had to write a custom build script to do the job, which took me quite a while as I needed to figure out all the details like how to locate the installed VC++ toolchain in my script.

> The pull request review did help me find a better way to locate the VC++ toolchain.

Third, I needed to add my one-line patch on `LoadLibrary` to ASP.NET Core module itself.

Finally, I opened [a new issue on GitHub](https://github.com/dotnet/aspnetcore/issues/47115) and attach [a pull request](https://github.com/dotnet/aspnetcore/pull/47290) to it.

## The Not-So-Happy Ending in 2023

The pull request was reviewed but closed because the team currently didn't see Windows 11 ARM64 a strategical platform that they put more resources into.

Instead of leaving any future brave Windows ARM64 explorers like me in the same situation, I decided to create simple PowerShell scripts to patch the flawed ASP.NET Core installation by reusing the existing binaries and you can visit this [new GitHub repo](https://github.com/lextm/ancm-arm64) to learn more.

> Thanks for reading this far, as it is such a long post and I rarely write in this way for a very long time. Hope now you understand more about Windows 11 ARM64 and ASP.NET Core.

## Turnaround in Dec 2024

People continued to use the workaround I proposed in `ancm-arm64` to patch their ASP.NET Core module installation on Windows ARM64, but this approach came with many pains,

* You have to remember to patch often, as ASP.NET Core module might be updated by new Microsoft installers. This won't work very well if you are in a large organization with many machines to patch. Luckily that should still be rare right now.
* Some Microsoft installers changed the versioning rules of the out-of-process module folder. I had to revise the patching script to adapt to those changes.

Of course, those pains are much less if compared to users stuck with Microsoft installers, who can only run ASP.NET Core web apps on IIS with pure ARM64 mode, which excludes all IIS out-of-band components (URL Rewrite module, ARR, etc.) which are currently only available in x86/x64 bitness. Thanks to those users who keep reporting the issues to Microsoft, and by the end of 2024 ASP.NET Core team decided to work on my proposed changes again.

This work was first brought back by Stephen Halter in [this pull request](https://github.com/dotnet/aspnetcore/pull/59481) on Dec 13, 2024 but we had to abandon it, simply because I moved all patches (including IIS Express related patches) to the HTTP Bridge Module for IIS repo. So, I created [a new pull request](https://github.com/dotnet/aspnetcore/pull/59483). The review process was much smoother than expected, because many minor issues were found and resolved during my work on HTTP Bridge Module for IIS.

However, we happened to find an important change probably made by the Windows team, who changed the behaviors of `LoadLibrary` call when it tries to load a pure forwarder. So, on certain old versions of Windows ARM64, when `LoadLibrary` sees `aspnetcorev2_outofprocess.dll` in the out-of-process folder, it won't check if the platform specific files are in the same folder. That was why I had to switch from `LoadLibrary` to `LoadLibraryEx`. On the latest Windows ARM64 release, `LoadLibrary` alone works as desired. I guess they just had to fix `LoadLibrary`, because it makes more sense than forcing everyone to switch to `LoadLibraryEx`.

So today is Feb 19, 2025 and the pull request has been merged to the main branch. Let's hope the patched installers for .NET 8/9/10 will come out soon and you don't need any workaround applied any more.

## Hints on Windows Installer Upgrade in Feb 2025

A few days ago some .NET 10.0 Preview testers reported that the changes I made broke IIS/IIS Express when upgrading from a previous release (like .NET 8/9), as `aspnetcorev2.dll` was missing. I was able to reproduce the issue after building two versions of ASP.NET Core module installers for IIS Express before and after my changes, which allowed me to acquire detailed Windows Installer logs.

``` text
install.log:815:MSI (s) (B4:90) [22:49:42:783]: PROPERTY CHANGE: Adding CA_ADD_MODULE property. Its value is 
'"C:\Program Files\IIS Express\appcmd.exe" install module /name:AspNetCoreModuleV2 /image:"%IIS_BIN%\Asp.Net Core 
Module\V2\aspnetcorev2.dll" /apphostconfig:"C:\Program Files\IIS Express\AppServer\applicationhost.config"'.
install.log:915:MSI (s) (B4:90) [22:49:42:889]: PROPERTY CHANGE: Adding CA_ADD_MODULE_TMP property. Its value is 
'"C:\Program Files\IIS Express\appcmd.exe" install module /name:AspNetCoreModuleV2 /image:"%IIS_BIN%\Asp.Net Core 
Module\V2\aspnetcorev2.dll" /apphostconfig:"C:\Program Files\IIS 
Express\config\templates\PersonalWebServer\applicationhost.config"'.
install.log:965:MSI (s) (B4:90) [22:49:42:927]: PROPERTY CHANGE: Adding CA_ADD_MODULE32 property. Its value is 
'"C:\Program Files (x86)\IIS Express\appcmd.exe" install module /name:AspNetCoreModuleV2 /image:"%IIS_BIN%\Asp.Net 
Core Module\V2\aspnetcorev2.dll" /apphostconfig:"C:\Program Files (x86)\IIS Express\AppServer\applicationhost.config"'.
install.log:1065:MSI (s) (B4:90) [22:49:43:046]: PROPERTY CHANGE: Adding CA_ADD_MODULE_TMP32 property. Its value is 
'"C:\Program Files (x86)\IIS Express\appcmd.exe" install module /name:AspNetCoreModuleV2 /image:"%IIS_BIN%\Asp.Net 
Core Module\V2\aspnetcorev2.dll" /apphostconfig:"C:\Program Files (x86)\IIS 
Express\config\templates\PersonalWebServer\applicationhost.config"'.
install.log:1127:MSI (s) (B4:90) [22:49:43:133]: Executing op: 
ComponentRegister(ComponentId={08968573-05C1-4BF1-8879-7B818AC9525B},KeyPath=C:\Program Files\IIS Express\Asp.Net Core 
Module\V2\aspnetcorev2.dll,State=3,,Disk=1,SharedDllRefCount=2,BinaryType=1)
install.log:1128:1: {730F296E-5C7F-4381-BA86-28EDC4FEFCC0} 2: {08968573-05C1-4BF1-8879-7B818AC9525B} 3: C:\Program 
Files\IIS Express\Asp.Net Core Module\V2\aspnetcorev2.dll 
install.log:1141:MSI (s) (B4:90) [22:49:43:141]: Executing op: 
ComponentRegister(ComponentId={45BA5011-A619-4D06-8A8D-155B1F9732B3},KeyPath=C:\Program Files (x86)\IIS 
Express\Asp.Net Core Module\V2\aspnetcorev2.dll,State=3,,Disk=1,SharedDllRefCount=0,BinaryType=0)
install.log:1142:1: {730F296E-5C7F-4381-BA86-28EDC4FEFCC0} 2: {45BA5011-A619-4D06-8A8D-155B1F9732B3} 3: C:\Program 
Files (x86)\IIS Express\Asp.Net Core Module\V2\aspnetcorev2.dll 
install.log:1143:MSI (s) (B4:90) [22:49:43:141]: WIN64DUALFOLDERS: Substitution in 'C:\Program Files (x86)\IIS 
Express\Asp.Net Core Module\V2\aspnetcorev2.dll' folder had been blocked by the 1 mask argument (the folder pair's 
iSwapAttrib member = 0).
install.log:1159:MSI (s) (B4:90) [22:49:43:157]: Executing op: CacheRTMFile(SourceFilePath=C:\Program Files (x86)\IIS 
Express\Asp.Net Core Module\V2\aspnetcorev2.dll,FileKey=AspNetCoreModuleDll.wow,,ProductCode={676B4A87-1027-45E1-88A1-4
11816838808},ProductVersion=110.0.25063,Attributes=512,,,,CopierFlags=0,,,,,,)
install.log:1162:MSI (s) (B4:90) [22:49:43:167]: Executing op: FileCopy(SourceName=3ajklagw.dll|aspnetcorev2.dll,Source
CabKey=AspNetCoreModuleDll.wow,DestName=aspnetcorev2.dll,Attributes=512,FileSize=351232,PerTick=65536,,VerifyMedia=1,,,
,,CheckCRC=0,Version=20.0.25064.0,Language=1033,InstallMode=58982400,,,,,,,)
install.log:1163:MSI (s) (B4:90) [22:49:43:167]: File: C:\Program Files (x86)\IIS Express\Asp.Net Core 
Module\V2\aspnetcorev2.dll;	Overwrite;	Won't patch;	Existing file is a lower version
install.log:1165:InstallFiles: File: aspnetcorev2.dll, Directory: C:\Program Files (x86)\IIS Express\Asp.Net Core 
Module\V2\, Size: 351232
install.log:1167:MSI (s) (B4:90) [22:49:43:175]: Verifying accessibility of file: aspnetcorev2.dll
install.log:1235:MSI (s) (B4:90) [22:49:44:451]: Executing op: CustomActionSchedule(Action=CA_ADD_MODULE,ActionType=313
7,Source=BinaryData,Target=CAQuietExec,CustomActionData="C:\Program Files\IIS Express\appcmd.exe" install module 
/name:AspNetCoreModuleV2 /image:"%IIS_BIN%\Asp.Net Core Module\V2\aspnetcorev2.dll" /apphostconfig:"C:\Program 
Files\IIS Express\AppServer\applicationhost.config")
install.log:1307:MSI (s) (B4:90) [22:49:46:722]: Executing op: CustomActionSchedule(Action=CA_ADD_MODULE_TMP,ActionType
=3137,Source=BinaryData,Target=CAQuietExec,CustomActionData="C:\Program Files\IIS Express\appcmd.exe" install module 
/name:AspNetCoreModuleV2 /image:"%IIS_BIN%\Asp.Net Core Module\V2\aspnetcorev2.dll" /apphostconfig:"C:\Program 
Files\IIS Express\config\templates\PersonalWebServer\applicationhost.config")
install.log:1332:MSI (s) (B4:90) [22:49:48:029]: Executing op: CustomActionSchedule(Action=CA_ADD_MODULE32,ActionType=3
137,Source=BinaryData,Target=CAQuietExec,CustomActionData="C:\Program Files (x86)\IIS Express\appcmd.exe" install 
module /name:AspNetCoreModuleV2 /image:"%IIS_BIN%\Asp.Net Core Module\V2\aspnetcorev2.dll" /apphostconfig:"C:\Program 
Files (x86)\IIS Express\AppServer\applicationhost.config")
install.log:1398:MSI (s) (B4:90) [22:49:50:604]: Executing op: CustomActionSchedule(Action=CA_ADD_MODULE_TMP32,ActionTy
pe=3137,Source=BinaryData,Target=CAQuietExec,CustomActionData="C:\Program Files (x86)\IIS Express\appcmd.exe" install 
module /name:AspNetCoreModuleV2 /image:"%IIS_BIN%\Asp.Net Core Module\V2\aspnetcorev2.dll" /apphostconfig:"C:\Program 
Files (x86)\IIS Express\config\templates\PersonalWebServer\applicationhost.config")
install.log:1418:MSI (s) (B4:90) [22:49:51:320]: Executing op: RegAddValue(Name=EventMessageFile,Value=#%C:\Program 
Files (x86)\IIS Express\Asp.Net Core Module\V2\aspnetcorev2.dll,)
install.log:1419:WriteRegistryValues: Key: \SYSTEM\CurrentControlSet\Services\EventLog\Application\IIS Express 
AspNetCore Module V2, Name: EventMessageFile, Value: #%C:\Program Files (x86)\IIS Express\Asp.Net Core 
Module\V2\aspnetcorev2.dll
install.log:2043:MSI (s) (B4:30) [22:49:51:867]: Executing op: 
FileRemove(,FileName=aspnetcorev2.dll,,ComponentId={84ED6CE6-C8A3-4FA8-A872-C98A1D15DD4F})
install.log:2044:RemoveFiles: File: aspnetcorev2.dll, Directory: C:\Program Files\IIS Express\Asp.Net Core Module\V2\
install.log:2045:MSI (s) (B4:30) [22:49:51:867]: Verifying accessibility of file: aspnetcorev2.dll
install.log:2248:Property(S): CA_ADD_MODULE = "C:\Program Files\IIS Express\appcmd.exe" install module 
/name:AspNetCoreModuleV2 /image:"%IIS_BIN%\Asp.Net Core Module\V2\aspnetcorev2.dll" /apphostconfig:"C:\Program 
Files\IIS Express\AppServer\applicationhost.config"
install.log:2253:Property(S): CA_ADD_MODULE_TMP = "C:\Program Files\IIS Express\appcmd.exe" install module 
/name:AspNetCoreModuleV2 /image:"%IIS_BIN%\Asp.Net Core Module\V2\aspnetcorev2.dll" /apphostconfig:"C:\Program 
Files\IIS Express\config\templates\PersonalWebServer\applicationhost.config"
install.log:2263:Property(S): CA_ADD_MODULE32 = "C:\Program Files (x86)\IIS Express\appcmd.exe" install module 
/name:AspNetCoreModuleV2 /image:"%IIS_BIN%\Asp.Net Core Module\V2\aspnetcorev2.dll" /apphostconfig:"C:\Program Files 
(x86)\IIS Express\AppServer\applicationhost.config"
install.log:2268:Property(S): CA_ADD_MODULE_TMP32 = "C:\Program Files (x86)\IIS Express\appcmd.exe" install module 
/name:AspNetCoreModuleV2 /image:"%IIS_BIN%\Asp.Net Core Module\V2\aspnetcorev2.dll" /apphostconfig:"C:\Program Files 
(x86)\IIS Express\config\templates\PersonalWebServer\applicationhost.config"
```

If digging further into the lines and [the actual changes I made to `ancm_iis_expressv2.wxs`](https://github.com/dotnet/aspnetcore/pull/59483/files), I can see that,

* `[22:49:43:167]: File: C:\Program Files (x86)\IIS Express\Asp.Net Core 
Module\V2\aspnetcorev2.dll;	Overwrite;	Won't patch;	Existing file is a lower version` indicates that the pure forwarder was compiled without proper version information.
* `[22:49:51:867]: Executing op: 
FileRemove(,FileName=aspnetcorev2.dll,,ComponentId={84ED6CE6-C8A3-4FA8-A872-C98A1D15DD4F})` indicates that since I gave the pure forwarder different component and file name, Windows Installer didn't consider it was an upgrade bit and then mistakenly removed the file in the end.

Luckily the fixes were not hard to find and [I sent a second pull request](https://github.com/dotnet/aspnetcore/pull/60769).

So, if you are building MSI packages for your own software, make sure you plan and maintain your installers properly so they don't just work for clean installs but also for upgrades.

## Remaining Work for IIS OOB

I recently moved my focus to help IIS out-of-band component users on Windows ARM64,

* HTTP Bridge Module for IIS (derived from ASP.NET Core module) was my latest achievement that fully supports Windows ARM64.
* [I created a workaround](https://github.com/lextm/rewrite-arm64) for you to use URL Rewrite module on Windows ARM64.

But Microsoft might ship official Windows ARM64 compatible installers for URL Rewrite module, ARR, etc. in the future. Let's see how soon these improvements might become available.

Stay tuned.
