---
layout: post
title: CI/CD Pipeline with VSTS and Zapier
description: A post about how to set up CI/CD pipeline with VSTS and Zapier.
tags: Visual-Studio
permalink: /ci-cd-pipeline-with-vsts-and-zapier-b81d341088dd
excerpt_separator: <!--more-->
image:
  path: /images/summer-canal.jpg
  alt: Copyright © Lex Li. The canal in the summer, Montreal.
---

I just [wrote about how I started to self host Sphinx sites on Azure App Service]({% post_url 2018/2018-8-5-self-hosting-sphinx-sites-on-azure-app-service %}). Here I am writing about how to set up CI/CD pipeline to make it perfect.

<!--more-->

## Preparation 1: VSTS Repo for App Service

It is very important to learn Azure App Service, so as to know what built-in features we can use.

Clearly here I need to set its deployment method to a custom repo on VSTS (I cannot use GitHub or others because I need to handle private repos).

So I create a new project on Azure called AzureSites, a new repo under it called production, and hook my App Service to it by following [this article](https://learn.microsoft.com/azure/app-service/deploy-continuous-deployment?tabs=github#deploy-continuously-from-vsts).

> Note that I did not use VSTS pipeline here, because I need to handle it later.

## Preparation 2: VSTS Master Repo for All Sites

I had to create a second repo here called AllSites, because too many web sites are there to integrate, and each of them have their own repos (mostly on GitHub).

So in AllSites I added all such repos as submodules, and it looks like this,

![img-description](/images/sphinx-repos.png)
_Figure 1: Sphinx based sites as submodules._

I also added AzureSites as a submodule, so later I can copy all web pages into it.

## Preparation 3: A Single Pipeline for All

Then I went ahead to create a pipeline for the master repo,

1. It checks out all submodules and executes their builds.
1. Copy all web pages to AzureSites submodule.
1. Commit changes in AzureSites and push it.

> Note that Azure App Service will automatically pick up the changes from AzureSites, and we are done.

## Enhanced Version

What if now I modified one of the Sphinx sites? How can this pipeline pick up the changes? That's a good question. To solve the challenges, we need a few things,

1. Create your Zapier account and set up a Zap to trigger a VSTS build from the pipeline above, when a GitHub repo sees a commit. (You can use other similar services too.)
1. Add a task to the pipeline (usually the first step) to call git pull on all Sphinx submodules. In this way, all latest commits can be downloaded.
1. After pushing AzureSites, we should also stage the changes on the master repo and push it back.

> Note that free account on Zapier can only monitor five GitHub repos in this case, so I only monitored the most important ones.
>
> I also added a Zap to monitor my own Twitter feed, so if I write a magic tweet a build would be triggered.
>
> I still keep a daily build trigger in VSTS, in case I run out of Zapier free count (100 per month).

## Remaining Items

You might find it a waste of resources to always run the tasks in pipeline, if no submodule changes.

I showed you a way to abort the execution early in [a separate post]({% post_url 2018/2018-8-5-how-to-abort-cancel-a-build-in-vsts %}).

Stay tuned.
