---
layout: post
title: ".NET 和 Mono 的一点历史"
description: "这篇文章是关于 .NET 和 Mono 的历史故事。"
tags: .NET Mono
categories: [History, .NET]
permalink: /net-和-mono-的一点历史-772aebf42e24
excerpt_separator: <!--more-->
---
提到微软公司研发 .NET Framework 的初衷，难免要提到 SUN 公司1995年推出的 Java 语言。由于 Java 在业界得到了广泛的支持而且迅速建立了庞大的生态系统，微软也不得不考虑如何加以应对，毕竟自己手里的 Visual Basic 和 Visual C++ 和 Java 一比都有不小的差距。这也就导致了1996年3月12日发生了让业界吃惊的一幕，微软居然从 SUN 取得了 Java 的相关授权，可以开发 Java 平台的 IDE 产品[1]。微软当时预计大约1996年年中便可以推出相关的开发工具。跳票许久，10月15日，微软正式发布 SDK for Java，两个月内下载次数超过50,000。11月，Anders Hejlsberg 离开 Borland 公司，加入微软。
<!--more-->

1997年1月微软终于推出了 Visual J++ 1.0。然后由于测试的失误，发布后由于安装镜像无法支持当时已经很火的 Windows 95 操作系统，微软不得不宣布将尽快修复这一问题[4]。3月3日，微软推出 Visual J++ 1.1[5]。由于 Visual J++ 并不符合 Java 相关规范，甚至没有实现 JNI 等基础功能，SUN 对微软提出了诉讼[6]。5月，Scott Guthrie 从 Duke University 计算机系毕业，加入微软。

在诉讼期间，1998年10月6日微软又发布了 Visual J++ 6.0。由于新引入的 Microsoft Foundation Classes 使得通过 Java 语言能够十分便利的开发 Windows 各种类型的应用程序[7]，微软进一步惹怒了 SUN。该诉讼直到2001年才初步和解。2004年，双方进一步达成合作[8]。

也就是由于这场旷日持久的诉讼，以及 Visual J++ 6.0 发布之后获得的用户支持，微软决心独立研发自己的开发平台来和 Java 竞争。于是1998年、1999年两年它都在招兵买马。Scott Guthrie 便是在1999年11月加入了ASP.NET设计团队，随后主导了WebForms框架的设计[9]。

2000年6月22日，微软对外公开 .NET 平台 [10]，随后于7月11日在PDC大会上发布了 .NET Framework 和 Visual Studio .NET 测试版。由于全新工具和语言带来的开发便利性，.NET 这一概念很快获得了广泛关注。比如，在XP2000大会上，Philip Craig 演示了 NUnit 框架的原型[11]。9月11日，Mike Kruger 启动了 SharpDevelop 项目，开始开发一个开源的 C# IDE[12]。2001年1月，Lutz Roeder 开始发布 .NET Reflector，一个可以反编译 MSIL 的工具[13]。2001年6月，Neoworks Limited 开始研发 log4net[14]。2001年7月5日，Gerry Shaw 开始发布 NAnt [15]。9月29日，Kral Ferch、Jason Diamond 开始开发 NDoc [16]。开源社区和微软社区专家们只用了很短时间就将 Java 平台的主要框架迁移到了 .NET 平台。

2001年5月3日，微软宣布了 Shared Source 计划，有限制的向开发者公开部分产品的源代码[17]，而没有采取开源自己产品代码的方式。

2002年2月13日，微软正式发布 .NET Framework 1.0 [18]。7月11日，Jim Newkirk 开始设计 NUnit 2.0 [19]。8月6日，Borland 发布 Delphi 7，包含 Delphi for .NET 预览版[20]。

2003年2月，DevExpress 收购 CodeRush，Mark Miller 开始设计 CodeRush for Visual Studio[21]。4月3日，微软正式发布 .NET Framework 1.1[22]。4月23日，微软发布 Windows Server 2003[23]。5月6日 Borland 公布 C#Builder 产品。C#Builder 1.0 于6月6日正式发布。12月22日，Delphi for .NET 正式发布[24]。

2004年1月，Peter Waldschmidt 开始发布 NCover [25]。1月28日，微软发布 Enterprise Libraries 1.0 [26]。3月25日，DevExpress 发布 CodeRush for Visual Studio .NET[27]。4月5日，微软在 SourceForge 上开源 WiX 项目[28]。7月3日，微软发布 .NET Framework 2.0 Beta 1 [29]，构建工具 MSBuild 和 Visual Studio 内置的 MSTest 公布。7月22日，JetBrains 发布 ReSharper 1.0[30]。10月12日，Borland 发布 Delphi 2005，包含 Delphi for .NET 和 C#Builder 2.0。

2005年4月18日，微软发布 .NET Framework 2.0 Beta 2。5月1日，RemObjects 发布 Chrome 1.0[31]。10月10日，Borland 发布 Delphi 2006[24]。

2005年11月7日，微软正式发布.NET Framework 2.0和Visual Studio 2005[32]。同日，RemObjects 发布 Chrome 1.5，全面支持微软的新平台[31]。

2006年6月27日，在Jim NewKirk 领导下，微软的开源托管平台 CodePlex 正式上线[33]。7月26日，NDoc 项目负责人 Kevin Downs 表示该项目开发工作停止[34]。7月29日，微软发布 Sandcastle CTP[35]。11月2日，Novell 和微软宣布达成深度合作和专利授权[36]。11月6日微软发布.NET Framework 3.0，引入 WPF、WCF 和 WF 等全新框架 [32]。

2007年4月19日，微软发布.NET Framework 3.5 Beta 1。7月21日，Scott Hanselman 宣布将加入微软公司[37]。9月5日，微软发布 Silverlight 1.0[38]。9月17日，NCover 宣布转为收费软件[39]。9月19日，Brad Wilson 和 Jim Newkirk 发布 xUnit.net 项目1.0 Beta 1，一个全新的单元测试框架[40]。10月3日，微软宣布基于参考协议公布部分.NET Framework 源代码，但该协议不符合 OSI 开源软件定义，因此并非开源代码[41]。11月19日，微软发布 .NET Framework 3.5 和 Visual Studio 2008[42]。

2008年5月15日，微软正式开源 Enterprise Libraries 4.0[43]。5月30日，RemObjects 发布 Oxygene 3.0，正式加入 MonoDevelop IDE 支持[44]。7月2日，微软开源 Sandcastle[35]。8月11日，微软发布 .NET Framework 3.5 SP1[45]。8月20日，Red Gate 宣布接手 .NET Reflector 的代码[13]。10月2日，微软开源MEF [46]。10月14日，微软发布Silverlight 2.0[47]。10月29日，Anders 在 PDC 上演示了 Roslyn[48]。同日，Miguel 演示了 Mono 的新进展，包括 C# Shell [49]。

2009年2月12日，Novell 在微软的协助下推出 Moonlight 1.0，兼容 Silverlight[50]。4月2日，微软发布 ASP.NET MVC 1.0 并完全开源[51]。4月27日，NancyFx 项目开启[52]。7月9日，微软发布 Silverlight 3.0[53]。

2010年2月15日，微软公开了 Windows Phone 7 移动操作系统 [54]。4月12日，微软推出 .NET Framework 4.0和 Visual Studio 2010 [55]。4月15日，微软发布 Silverlight 4.0 [56]。4月21日，微软基于 MS-PL 公开 Dynamic Language Runtime 1.0源代码 [57]，7月17日起授权协议改为更加宽松的 Apache 协议[58]。10月21日搭载 Windows Phone 7的手机上市销售 [54]。11月4日，微软开源 F# 编译器和运行时 [59]。

2011年1月3日，微软发布 NuGet 包管理器 [60]。4月18日，微软发布.NET Framework 4.0.1。10月19日，微软发布 .NET Framework 4.0.2。12月9日，微软发布 Silverlight 5.0[61]。

2012年3月28日，微软开放 ASP.NET MVC，Web API 和 Razor 源代码 [62]。6月20日，微软公开了 Windows Phone 8[63]。7月19日，微软开源 Entity Framework [64]。8月1日，微软发布 Windows 8 操作系统，并引入 Windows Runtime 这个新开发平台。8月15日，微软发布.NET Framework 4.5和Visual Studio 2012[65]。10月9日，微软停止开发 Sandcastle，该项目移交给 Eric Woodruff [66]。10月29日，搭载 Windows Phone 8的手机正式发布。

2013年10月17日，微软发布 .NET Framework 4.5.1 和 Visual Studio 2013[67]。

2014年4月2日，微软公开了 Windows Phone 8.1[68]。4月3日，微软宣布开源 Roslyn 项目[69]。4月14日，Windows Phone 8.1正式向开发者发布。4月16日，DevExpress 宣布将开发 CodeRush for Roslyn。Mark Miller 确认前 CodeRush 开发人员 Dustin Campbell 领导了 Roslyn 的设计[70]。5月5日，微软发布 .NET Framework 4.5.2[71]。5月14日，ASP.NET 项目源代码从 CodePlex 迁往 GitHub [72]。7月21日，TypeScript 项目也迁往 GitHub[73]。11月12日，微软宣布开源 .NET Core，同时参考代码的授权协议也修改为 MIT 协议从而完全开放[74]。

2015年1月10日，Roslyn 项目代码迁往 GitHub[75]。1月13日，F# 代码迁往 GitHub[76]。1月21日，微软公开 Windows 10 Mobile[77]。2月3日，微软在 GitHub 发布 CoreCLR [78]。3月18日，微软开源 MSBuild [79]。4月29日，微软公开了 Visual Studio Code [80]。7月20日，微软发布 .NET Framework 4.6和 Visual Studio 2015[81]。7月29日，微软发布 Windows 10[82]。8月11日，NuGet 项目迁往 GitHub [83]。11月17日，微软发布 .NET Framework 4.6.1和 Visual Studio 2015 Update 1。11月18日，微软宣布开源 Visual Studio Code。同日，微软发布 .NET Core 5和 ASP.NET 5 RC 1[84]。11月20日，微软正式发布 Windows 10 Mobile。

2016年1月13日，JetBrains 公布了 Project Rider，一个基于 IntelliJ 平台的 C# IDE[85]。1月19日，微软将新平台的名称改为 .NET Core 1.0和ASP.NET Core 1.0[86]。2月24日，微软宣布收购 Xamarin [87]。3月1日，Project Rider 封闭测试开始[88]。

[1] https://news.microsoft.com/1996/03/12/microsoft-and-sun-microsystems-conclude-agreement-to-license-technology-for-java/
[2] https://news.microsoft.com/1996/12/11/microsoft-sdk-for-java-attracts-more-than-50000-developers-in-nearly-two-months/
[3] https://www.linkedin.com/in/ahejlsberg
[4] http://www.javaworld.com/article/2077619/developer-tools-ide/visual-j---1-0-runs-into-a-little-installation-snag.html
[5] https://news.microsoft.com/1997/03/03/microsoft-announces-visual-j-1-1/
[6] https://news.microsoft.com/2001/01/23/microsoft-reaches-agreement-to-settle-contract-dispute-with-sun-microsystems/
[7] https://news.microsoft.com/1998/10/06/microsoft-ships-enterprise-solutions-with-microsoft-visual-j-6-0/
[8] https://news.microsoft.com/2004/04/02/microsoft-and-sun-microsystems-enter-broad-cooperation-agreement-settle-outstanding-litigation/
[9] https://www.linkedin.com/in/guthriescott
[10] https://news.microsoft.com/2000/07/11/microsoft-announces-groundswell-of-support-for-net-platform/
[11] https://groups.google.com/forum/#!topic/nunit-discuss/Js-N_eqMkGU
[12] https://en.wikipedia.org/wiki/SharpDevelop
[13] https://en.wikipedia.org/wiki/.NET_Reflector
[14] https://logging.apache.org/log4net/history.html
[15] http://nant.sourceforge.net/nightly/latest/releasenotes.html
[16] https://github.com/twpol/ndoc/commit/1ceacb37a404169f0d6574dec754009d9a1e1b43
[17] https://news.microsoft.com/speeches/speech-transcript-craig-mundie-the-new-york-university-stern-school-of-business/
[18] https://en.wikipedia.org/wiki/.NET_Framework_version_history#.NET_Framework_1.0
[19] https://github.com/nunit/nunitv2/commit/82b7fd3361733d3504377ca21996ac9e431b9679
[20] http://delphi.wikia.com/wiki/Delphi_7
[21] https://www.linkedin.com/in/mark-miller-a718761
[22] https://en.wikipedia.org/wiki/.NET_Framework_version_history#.NET_Framework_1.1
[23] https://en.wikipedia.org/wiki/Windows_Server_2003
[24] http://www.drbob42.com/delphi/index.htm
[25] https://en.wikipedia.org/wiki/NCover
[26] http://www.peterprovost.org/blog/2005/01/28/Enterprise-Library-10-Release-to-Web-(RTW)/
[27] http://www.pcreview.co.uk/threads/ann-coderush-for-net-now-available.1406578/
[28] https://en.wikipedia.org/wiki/WiX
[29] https://jonathanparker.wordpress.com/2014/12/05/list-of-net-framework-versions/
[30] https://resharper-support.jetbrains.com/hc/en-us/community/posts/206097229-ReSharper-1-0-is-released
[31] http://blogs.remobjects.com/2008/05/01/three-years-of-chrome/
[32] https://en.wikipedia.org/wiki/.NET_Framework#Release_history
[33] https://blogs.msdn.microsoft.com/codeplex/2006/06/27/welcome-to-codeplex/
[34] http://charliedigital.com/2006/07/26/ndoc-2-is-officially-dead/
[35] https://en.wikipedia.org/wiki/Sandcastle_(software)#History
[36] http://news.microsoft.com/2006/11/02/microsoft-and-novell-announce-broad-collaboration-on-windows-and-linux-interoperability-and-support/
[37] http://www.hanselman.com/blog/BlueBadge.aspx
[38] https://en.wikipedia.org/wiki/Microsoft_Silverlight
[39] http://www.ncover.com/blog/uncovering-the-new-ncover/
[40] http://jamesnewkirk.typepad.com/posts/2008/04/xunitnet-10-rel.html
[41] http://weblogs.asp.net/scottgu/releasing-the-source-code-for-the-net-framework-libraries
[42] https://en.wikipedia.org/wiki/Microsoft_Visual_Studio#Visual_Studio_2008
[43] https://entlib.codeplex.com/releases/view/13498
[44] http://blogs.remobjects.com/2008/04/24/remobjects-oxygene-3-0/
[45] https://en.wikipedia.org/wiki/.NET_Framework_version_history#Service_Pack_1
[46] http://blogs.msdn.com/gblock/archive/2008/10/02/mef-going-ms-pl-the-little-engine-that-could.aspx
[47] http://weblogs.asp.net/scottgu/silverlight-2-released
[48] https://channel9.msdn.com/blogs/pdc2008/tl16
[49] http://channel9.msdn.com/pdc2008/PC54/
[50] https://weblogs.asp.net/scottgu/moonlight-1-0-release
[51] http://www.hanselman.com/blog/MicrosoftASPNETMVC10IsNowOpenSourceMSPL.aspx
[52] https://github.com/NancyFx/Nancy/commit/9a26209feb52a347f5de4aaf38abb55e0b408a63
[53] https://en.wikipedia.org/wiki/Microsoft_Silverlight_version_history#Silverlight_3
[54] https://en.wikipedia.org/wiki/Windows_Phone_7
[55] https://en.wikipedia.org/wiki/.NET_Framework_version_history#History
[56] https://en.wikipedia.org/wiki/Microsoft_Silverlight_version_history#Silverlight_4
[57] https://dlr.codeplex.com/releases/view/21425
[58] http://tirania.org/blog/archive/2010/Jul-17-1.html
[59] https://blogs.msdn.microsoft.com/dsyme/2010/11/04/announcing-the-f-compiler-library-source-code-drop/
[60] https://docs.nuget.org/release-notes/nuget-1.1
[61] https://en.wikipedia.org/wiki/Microsoft_Silverlight_version_history#Silverlight_5
[62] http://weblogs.asp.net/scottgu/asp-net-mvc-web-api-razor-and-open-source
[63] https://en.wikipedia.org/wiki/Windows_Phone_8
[64] http://weblogs.asp.net/scottgu/entity-framework-and-open-source
[65] https://en.wikipedia.org/wiki/.NET_Framework_version_history#.NET_Framework_4.5
[66] http://sandcastle.codeplex.com/discussions/398496
[67] https://blogs.msdn.microsoft.com/visualstudio/2013/10/17/visual-studio-2013-released-to-web/
[68] https://en.wikipedia.org/wiki/Windows_Phone_8.1
[69] http://visualstudiomagazine.com/articles/2014/04/03/microsoft-open-sources-roslyn-compiler.aspx
[70] https://community.devexpress.com/blogs/markmiller/archive/2014/04/16/is-there-a-roslyn-based-coderush-in-your-future.aspx
[71] https://en.wikipedia.org/wiki/.NET_Framework_version_history#.NET_Framework_4.5.2
[72] http://sdtimes.com/sd-times-blog-microsoft-open-sources-asp-net-on-github/
[73] https://blogs.msdn.microsoft.com/typescript/2014/07/21/new-compiler-and-moving-to-github/
[74] https://blogs.msdn.microsoft.com/dotnet/2014/11/12/net-core-is-open-source/
[75] https://blogs.msdn.microsoft.com/csharpfaq/2015/01/10/were-moving-to-github/
[76] https://blogs.msdn.microsoft.com/fsharpteam/2015/01/13/visual-f-has-moved-to-github/
[77] https://en.wikipedia.org/wiki/Windows_10_Mobile
[78] https://blogs.msdn.microsoft.com/dotnet/2015/02/03/coreclr-is-now-open-source/
[79] https://blogs.msdn.microsoft.com/dotnet/2015/03/18/msbuild-engine-is-now-open-source-on-github/
[80] https://en.wikipedia.org/wiki/Visual_Studio_Code
[81] https://en.wikipedia.org/wiki/.NET_Framework_version_history#.NET_Framework_4.6
[82] https://en.wikipedia.org/wiki/Windows_10
[83] http://blog.nuget.org/20150811/NuGet2-MoveToGitHub.html
[84] https://blogs.msdn.microsoft.com/dotnet/2015/11/18/announcing-net-core-and-asp-net-5-rc/
[85] https://blog.jetbrains.com/dotnet/2016/01/13/project-rider-a-csharp-ide/
[86] http://www.hanselman.com/blog/ASPNET5IsDeadIntroducingASPNETCore10AndNETCore10.aspx
[87] https://weblogs.asp.net/scottgu/welcoming-the-xamarin-team-to-microsoft
[88] https://www.reddit.com/r/csharp/comments/48ierd/project_rider_eap_started/
