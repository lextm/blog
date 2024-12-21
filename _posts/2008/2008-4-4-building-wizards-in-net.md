---
layout: post
title: "Building Wizards In .NET"
description: This post talks about how to build wizards in .NET.
tags: .NET
permalink: /building-wizards-in-net-6cc9e085d600
excerpt_separator: <!--more-->
---
(Originally posted to CSDN on Feb 21, 2006)
<!--more-->

Wizard dialogue is a useful UI element that comes in nearly all software. But how to create a wizard in .NET?

If you have searched around the net, you will see a lot of open source libraries. However, not all of them suit your unique requirements.

In my case, I don't need a fancy look. But I call for flexibility. For example, my work flow has a branch somewhere, so I wish the wizard library supports branching.

So I take a look at David Hervieux's choice. He used this component in Sharp Builder Tools for NUnit support. Can this component satisfy me?

http://www.codeguru.com/csharp/csharp/cs_controls/wizards/article.php/c4799/

I spent a whole afternoon on this component yesterday, and found it perfect. I can split a big form into pieces, and insert them into different WizardPage instances. A WizardForm descendent holds the pages. Thus, clients no longer need to move their mouse around a big form, but fluently input information with this smart wizard.

And what's more? I have more space in every wizard page to provide more information about the choices.

Branching can be easily done because every WizardPage instances allows you to override the settings. For example,

``` csharp
protected override string OnWizardNext()
{
    return radioButton1.Checked ? "ThirdPage" : "FourthPage";
}
```

The code above defines the next page according to radio buttons group on the current page.

I have so much fun with this 2002 born component. Therefore, I have to say its author Steven Soloff is a real guru.

Forget to mention that Steven does not explicitly mention a license for the source code so you can use it freely.
