---
layout: post
title: "Obfuscar: The Story Behind 'Inconsistent virtual method obfuscation state detected'"
description: This post is going to cover the technical details of an issue related to virtual method renaming.
tags: .NET
permalink: /obfuscar-the-story-behind-inconsistent-virtual-method-obfuscation-state-detected-82c9f8c38667
excerpt_separator: <!--more-->
---
"Inconsistent virtual method obfuscation state detected" has been a well-known issue of Obfuscar for a while but users do not seem to fully understand the rationale behind it. This post is going to cover the technical details.
<!--more-->

## The Scenario

Assume that we have the following elements defined in a C# project,

``` csharp
namespace test
{
  internal interface MainInterface
  {
    void Test();
  }
  public class MainClass : MainInterface
  {
    public void Test(){
    }
  }
}
```

Then when we use Obfuscar to obfuscate the code, and use `KeepPublicApi=true` and `HidePrivateApi=true`, we will see the issue reported by Obfuscar.

``` text
An error occurred during processing:
Inconsistent virtual method obfuscation state detected. Abort. Please review the
following methods,
[test]test.MainInterface::Test[0]->WillRename:A
[test]test.MainClass::Test[0]->Skipped:KeepPublicApi option in configuration
```

So, how to understand the cause? `MainInterface` is going to be obfuscated, as it is internal. That obfuscation also applies to `MainInterface.Test`. That's why a `WillRename` action is set for it. However, `MainClass` is a public class, and its public `Test` method should not be obfuscated in this case. A `Skipped` action is marked. Obfuscar decides to break at this stage, because it cannot fulfill the two actions due to the relationship between the functions.

## The Thoughts

Do you know that before that Obfuscar silently changes actions of `Rename` to `Skipped`? Do you want to see the things you want to hide revealed unexpectedly? I personally go against silent operations.

Thus, when I determined to change Obfuscar in this way in this February, I was trying to make things simple and fully under control. The fact is that when Obfuscar reports such inconsistency to the developer, the issue can be easily fixed. Possible approaches include but are not limited to,

* Use attribute to force obfuscation of `MainClass.Test`.
* Use `<ForceMethod>` tag in configuration to force obfuscation of `MainClass.Test`.
* Use attribute to skip obfuscation of `MainInterface.Test`.
* Use `<SkipMethod>` tag in configuration to skip obfuscation of `MainInterface.Test`.

Anyway the developer controls what to hide or not.

Hope this post can help if you meet exactly this issue.
