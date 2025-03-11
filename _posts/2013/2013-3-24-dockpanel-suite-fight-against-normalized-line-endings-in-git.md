---
layout: post
title: "DockPanel Suite: Fight Against Normalized Line Endings in Git"
description: "This post talks about how to fight against normalized line endings in Git."
tags: DockPanel-Suite
permalink: /dockpanel-suite-fight-against-normalized-line-endings-in-git-b5d897e17a07
excerpt_separator: <!--more-->
---
Git is a nice cross platform source control system. Therefore, it needs to fight against the different line endings of various operating systems (well, because of the death of Mac OS, we only have two dialects right now, CR LF and LF).
<!--more-->

If your Git repository comes from an import of another SCM, you might pay attention to the line ending issues by following this post,

https://help.github.com/articles/dealing-with-line-endings

We should have done such cleanup a long time ago for DockPanel Suite, but Ryan did it just a few days ago. So here is the trouble,

1. I made a new branch gh59 on Mar 2. There are a few change sets after Mar 2 lives on the new branch.
1. Ryan performed the normalization on master branch on Mar 10. Before that he made two change sets, and after that he also made a few change sets.

How can I now merge the two branches without being affected by the tens of thousands of line endings changed? Well, I am not sure if there is already a blog post about it.

After several attempts, I came across my approach which was bit of successfully, so I wrote this article to keep a record of it.

My solution is as below,

1. Create a new branch (we use development_3.0, which is for one of our planned releases) from gh59.
1. Merge the two change sets Ryan made before Mar 10 to 3.0 branch. This is trivial and any Git tool can happily help out.
1. (Important) Follow the GitHub article to perform the same line ending normalization on 3.0 branch.
1. Cherry-pick Ryan's other change sets after Mar 10 to 3.0 branch.
1. Merge master branch to 3.0 branch. Now the merge becomes very simple, and I only have a few conflicts to resolve.

Without step 2–4, the merge effort will be much more.

You can easily check out the check-in diagram from here,

https://github.com/dockpanelsuite/dockpanelsuite/network

Well, it seems that now we have many contributors working on their forks. Nice. We might review a few of them and merge to the main repository in the near future.

Stay tuned.