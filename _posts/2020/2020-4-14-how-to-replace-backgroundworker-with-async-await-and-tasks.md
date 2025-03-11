---
layout: post
title: How to Replace BackgroundWorker with Async/Await and Tasks
description: A post about how to replace BackgroundWorker with async/await and tasks to make your code more readable and maintainable
tags: .NET Visual-Studio Microsoft
permalink: /how-to-replace-backgroundworker-with-async-await-and-tasks-80d7c8ed89dc
excerpt_separator: <!--more-->
image:
  path: /images/clouds-over-woods.jpg
  alt: Copyright © Lex Li. Clouds over the woods in Montreal.
---

`BackgroundWorker` was introduced early in .NET Framework as an easy way to do asynchronous tasks in Windows Forms applications. Though it is WinForms centric and not considered part of the async patterns, its beauty lies in the simplicity and just enough encapsulation. You don't need to know much about the async patterns to use this tiny little class in your code base, and things often just work.

> [Different async patterns](https://docs.microsoft.com/dotnet/standard/asynchronous-programming-patterns/interop-with-other-asynchronous-patterns-and-types) were developed by Microsoft to assist developers.

However, after .NET Framework 4.x came with `Task` based classes (Task Parallel Library), and especially 4.5 where `async`/`await` was introduced, you should move away from `BackgroundWorker` whenever possible.

Well, the only challenge is, how we can convert the code base from `BackgroundWorker` to `async`/`await`, which I will show you in this post.
<!--more-->

## What The Sample Demonstrates
So for this sample project we want some background operations to execute (which execute in a sequence and each of them takes 1 second to finish) and monitor the overall progress (percentage of completed operations). Of course, cancellation is another most wanted feature so if cancellation is triggered the remaining operations are skipped.

Since the sample will show you how to properly do multithreading operations, its UI runs on the main thread, while all operations execute on a single background thread or on multiple background threads.

## How The Sample Project Starts with BackgroundWorker
[The project](https://github.com/lextm/backgroundworker-sample/commit/d2ca2509e06cc7bdbe9492cb54c181cdd704e22e) hosted on GitHub is based on Windows Forms and .NET Framework 4.7.2.

To make full use of `BackgroundWorker`'s capability, both progress reporting and cancellation are utilized. As you can see it is rather simple, and easy to understand.

This pattern does have its problems, like

* You need to memorize that `DoWork` event handler runs on a separate thread, not the UI thread (aka main thread), though that's not quite obvious from the code.

> `ProgressChanged` and `RunWorkerCompleted` event handlers, however, are executed on the UI thread. That's why there the text of label can be updated directly.

* Cancellation required several pieces to be set, and if you miss one piece the result won't meet your expectation.
* Here `Thread.Sleep` is used to mimic a slow sync function call (usually in your own project here should be slow function calls like `SqlCommand.ExecuteScalar`).
  > When you need to call an async function like `SqlCommand.ExecuteScalarAsync`, it is not obvious how to write the correct code inside `DoWork`. This is a bigger issue with new .NET APIs, as they are full of async functions (SignalR for example).

## How to Remove BackgroundWorker from The Sample
Well, now it's time to kill the bird. And you can easily see the changes here in [the commit](https://github.com/lextm/backgroundworker-sample/commit/2e4cdf37c14b4e049407ea91db82dbefb125cc64).

Obvious parts are,

* `CancellationTokenSource` and `CancellationToken` are needed now to implement cancellation.
* There is no need to have separate methods and everything can come together in a single method.
* Most importantly the heavy task now is a simple `Task` object, and here I use `Task.Delay` as an example (again in your project things like `SqlCommand.ExecuteScalarAsync` should be here).

You must keep in mind there are many important tips on proper usage of `async`/`await`, including but not limited to

* `async void` is only used for the button click event handler as Microsoft documented.
* While the heavy task is executed in the background (and awaited), changing the text of label is on UI thread, as after the `await` line the execution context is restored.
  > Capturing/restoring such context is expensive, so you should suppress that with `ConfigureAwait(false)` if you don't need the context. Microsoft guys wrote [a must-read post here](https://devblogs.microsoft.com/dotnet/configureawait-faq/).

## Conclusion

`Task` and `async`/`await` have been very important addition to .NET ecosystem, so use them whenever possible and that's going to make your life a lot easier.
