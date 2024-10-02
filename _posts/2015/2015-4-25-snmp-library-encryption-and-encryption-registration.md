---
layout: post
title: "#SNMP Library, Encryption, and Encryption Registration"
description: "This post is about how I registered #SNMP Library with US government for encryption support."
tags: SNMP
permalink: /snmp-library-encryption-and-encryption-registration-2d68d88841bc
excerpt_separator: <!--more-->
---
One user wrote to me recently to ask if I can provide ECCN number of #SNMP Library. I was surprised initially, but later discovered that as a project hosted on both CodePlex and GitHub (US based), and a project with some encryption related code (SNMP v3 privacy support), #SNMP Library does fall into the category and some actions need to be taken. The question is how to get compliance without a lawyer. OK. Let's see whether US government makes it simple enough for an open source project coordinator to dig it out.
<!--more-->

## The Examples

If I could find good examples to follow, I think I would not be on the wrong path. So I started to [check out Mozilla](http://hecker.org/mozilla/eccn) and [Linux](http://www.linuxjournal.com/node/7318/print). So roughly speaking, open source projects with encryption support are self classified under a single ECCN 5D002.

## Extra Notifications
Thus, what else I need to do right now? I check out [section 740.139(e) of the EAR](http://www.bis.doc.gov/index.php/forms-documents/doc_download/986-740), and find the email addresses I should contact. Then I write a mail to detail #SNMP Library project and its source code on GitHub, and cc OpenSource.org (as this [indicates](http://opensource.org/node/505)).

That probably finishes all pieces of tasks this time (till the next modification on the encryption part).

Of course, if you get a lawyer you might get better advice.
