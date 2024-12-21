---
layout: post
title: "How to Compile Bouncy Castle on Mono/Linux"
description: "This post is about how to compile Bouncy Castle on Mono/Linux."
tags: Mono Linux
permalink: /how-to-compile-bouncy-castle-on-mono-linux-ec90f43eeda7
excerpt_separator: <!--more-->
---
Bouncy Castle is a good library to perform certificate/encryption related tasks on .NET/Mono. However, it is not obvious how to compile its source code on Mono/Linux. This post will show you how. It applies to,

* Bouncy Castle 1.7
* Mono 2.10
* openSUSE 12.2
<!--more-->

First, you need to download Bouncy Castle source code package from here,

http://www.bouncycastle.org/csharp/

bccrypto-net-1.7-src-ext.zip contains all files we need, so please use this package instead of the other source package, which lacks of a few files.

Second, extract the source files out and use MonoDevelop to open csharp.sln.

Third, allow MonoDevelop to convert the solution to MSBuild format, and then compile crypto project alone.

Fourth, when MonoDevelop warns that on one of the lines, where Equals method cannot be called (this should be a bug of Mono C# compiler, https://bugzilla.xamarin.com/show_bug.cgi?id=8474),

``` csharp
return z.Square().Equals(this) ? z : null;
```

Please change it to

``` csharp
return z.Square().Equals((object)this) ? z : null;
```

After all these steps, you should have crypto project compiled without any problem.

There can still be some issues compiling crypto-test project, but that's a unit test project which does not matter much, so you can safely ignore it.

Linux
Mono
