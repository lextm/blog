---
layout: post
title: "How I Migrated SharpSnmpLib From Mercurial to Git"
description: "This post is about how I migrated #SNMP repo from Mercurial to Git."
tags: Others
permalink: /how-i-migrated-sharpsnmplib-from-mercurial-to-git-54a19d4419a5
excerpt_separator: <!--more-->
---
There are tons of articles on this topic. Here I just summarized what I have done.
<!--more-->

## Generate Local Git Repository via Hg-Git

The Mercurial repository of #SNMP is at d:\sharpsnmplib

I am on Windows 7 and using the latest TortoiseHg. In this case I have to roll back to TortoiseHg 2.0.5 (because Hg-Git does not support latest Hg) first.

Then I install Hg-Git following http://candidcode.com/2010/01/12/a-guide-to-converting-from-mercurial-hg-to-git-on-a-windows-client/. However,

* TortoiseHg 2.0.5 does have Dulwich, so I don't need to install it right now.
* So I can go to step 3 directly, and clone the Mercurial repository of Hg-Git from http://bitbucket.org/durin42/hg-git/ to d:\temp\hg-git
* Then I modified `d:\sharpsnmplib\.hg\hgrc` to include the following lines,

  ``` ini
  [extensions]
  hgext.bookmarks =
  hggit = d:\temp\hg-git\hggit
  ```

You can now try to push to GitHub in `d:\sharpsnmplib` by executing `hg push git+ssh://git@github.com/schacon/hg-git.git`.

## Troubleshooting Issues

This push may fail due to an SSH error. In that case assuming you have set up Git following [this guide](http://help.github.com/win-set-up-git/), you may install TortoiseGit, and launch puttygen.exe from its installation folder to load your private key. Then you can save the key in PuTTY format (.ppk) and launch pageant.exe from TortoiseHg installation folder so as to add this new key. After that you can push again to see if everything works fine.

In my case it failed with an invalid parameter error which I cannot address. But the local Git repository is ready in d:\sharpsnmplib\.hg\git

## Consolidate Local Git Repository

To be safe, I used TortoiseGit to create an empty Git repository at d:\temp\sharpsnmplib. Then I copy d:\sharpsnmplib\.hg\git to d:\temp\sharpsnmplib\.git.

Next I followed http://christoph.ruegg.name/blog/2011/7/30/cleaning-up-after-migrating-from-hg-to-git.html to perform the housekeeping at d:\temp\sharpsnmplib,

``` bash
git fsck --full
git prune
git gc --aggressive
```

If you don't know how to find git command, you may read http://help.github.com/win-set-up-git/.

## Upload to GitHub

Finally I went to GitHub to create a repository. It is time to upload everything to it,

``` bash
git push --mirror --progress git@github.com:lextudio/sharpsnmplib.git
```

## Remaining Issues

If you use branching heavily, then you may experience more issues like me. Here are my fixes,

### 1. Unnamed Branches

Use TortoiseGit to show log on d:\temp\sharpsnmplib and I can see unnamed branches (the branch names seem to be removed during conversion). To rename them, we can simply create new branches in the log view, http://superuser.com/questions/382602/git-repository-migrated-from-mercurial-shows-unnamed-branches .

### 2. Messy Committers and Authors

I was not able to find a suitable way to clean up them without breaking the repository, so I decided to leave it as it was. This is bit of expected after Subversion to Mercurial to Git migration.
