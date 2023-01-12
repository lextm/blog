---
layout: post
title: "TDD, IoC, and Mock Framework"
description: This post talks about my experience of using TDD, IoC, and Mock Framework.
tags: .NET
permalink: /tdd-ioc-and-mock-framework-a16825154e8b
excerpt_separator: <!--more-->
---
My experience is that some cool terms always come together. In my case the three words are: TDD, IoC, and mock framework. If you never knew how these terms connect to each other, I can tell you my story.
<!--more-->

Two weeks ago I decided to add a new feature in CBC that helps sign a Delphi for .NET project in Visual Studio way. And this time, I want to try TDD on this feature.

The development became difficult at first because I thought it was impossible to test a Delphi IDE wizard. However, after setting up a small unit case, I found my way and wrote out a few ugly lines to pass the test. However, there were a few issues that violated TDD principles,

1. The test could not run automatically because there were a few message boxes.
1. The code invokes a .NET SDK utility named sn.exe which is an external application.
1. In order to provide an IOTAProject object, I made a fake class that implemented this interface. This class contains a lot of useless members.

Then I started my refactoring by utilizing IoC pattern. Once you see the source code, you can navigate to this class, Manner20UnsignedHandler, which contains two dependencies I need to inject, an IUser, and an IGenerator. By providing fake objects in unit test, I could resolve the first two issues. However, the third issue became worse, because I provided three fake classes now.

http://martinfowler.com/articles/injection.html

Now came the Mock Framework. Although there is a lot of mock framework available for NUnit, I just simply picked up NMock (because I admire the ThoughtWorkers). I removed all fake classes I created and initialised a few mock objects instead.

What's the improvement? Even though a IOTAProject instance is mocked, I used only a few lines,

``` csharp
IOTAProject mockProject = mocks.NewMock();
// ....
string fileName = Path.Combine(Path.GetTempPath(), "test.dproj");
Expect.AtLeast(3).On(mockProject).GetProperty("FileName").
    Will(Return.Value(fileName));
Expect.Once.On(mockProject).Method("AddFile").WithAnyArguments().Will(Return.Value(null));
```

In this case I only provided two lines to implement two members used in the test, FileName property and AddFile method.

At last, I could go on to simplify the code and ensure everything is already by asking NUnit the result.
