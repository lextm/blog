---
layout: post
title: "Infinite Loops Best Practice (Not a real best practice)"
description: "This post talks about how to write an infinite loop in .NET."
tags: .NET
permalink: /infinite-loops-best-practice-not-a-real-best-practice-e47b8922f445
excerpt_separator: <!--more-->
---
[Updated: This post is too old to be correct. Even #SNMP starts to use a completely different way to handle incoming packets http://code.google.com/p/sharpsnmplib/source/browse/SharpSnmpLib/Messaging/ListenerBinding.cs. So please read it carefully.]

In .NET (especially when you program with socket), sometimes you have to write an infinite loop. In #SNMP Library, this loop exists in TrapListener.Worker_DoWork method. As a UDP server that monitors incoming diagrams, this loop is unavoidable. However, if it is not correctly and efficiently implemented, you mess things up.
<!--more-->

## The Real Infinite Loop
At the very beginning, I used the following loop.

``` csharp
while (!((BackgroundWorker)sender).CancellationPending)
{
    int number = _watcher.Available;
    if (number == 0)
    {
        continue;
    }
    // handle diagrams here
}
```

Unfortunately my machine is Intel Core 2 Duo powered, so I did not find any issue until a user complained that it ate up all CPU resources. Yes, this user uses a single core CPU.

## The Sleeping Loop
A quick fix for the infinite loop issue is to add Thread.Sleep. Now the code looks like this,

``` csharp
while (!((BackgroundWorker)sender).CancellationPending)
{
    int number = _watcher.Available;
    if (number == 0)
    {
        Thread.Sleep(100);
        continue;
    }
    // handle diagrams
}
```

Although it is correct, how efficient is it? It depends on the number used in Sleep, and it does not perform well on multi-core CPU because Sleep always triggers a context switch which consumes extra resources.

## The Composite Loop
It was a post of CSDN about how to use SpinWait that reminded me of a new approach. By Googling I found this wonderful post.

http://www.bluebytesoftware.com/blog/2006/08/23/PriorityinducedStarvationWhySleep1IsBetterThanSleep0AndTheWindowsBalanceSetManager.aspx

``` csharp
while (!((BackgroundWorker)sender).CancellationPending)
{
    int number = _watcher.Available;
    if (number == 0)
    {
        if (Environment.ProcessorCount == 1 || unchecked(++loops % 100) == 0)
        {
            Thread.Sleep(1);
        }
        else
        {
            Thread.SpinWait(20);
        }

        continue;
    }
    // handle diagrams here
}
```

Oh, isn't it a wonder? On single core CPUs, this loop falls back to the sleeping only approach, while SpinWait is used to optimize performance on multi-core CPUs.

This composite loop is already available in #SNMP repository.
