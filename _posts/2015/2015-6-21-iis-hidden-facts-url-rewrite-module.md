---
layout: post
title: "IIS Hidden Facts: URL Rewrite Module"
description: "This post is about some interesting facts about IIS URL Rewrite module."
tags: IIS
permalink: /iis-hidden-facts-url-rewrite-module-55214414ab89
excerpt_separator: <!--more-->
---
> I am working on a project called Jexus Manager, and as a result found many interesting facts about IIS. This series of posts are going to cover them.

IIS never ships URL Rewrite module (even in IIS 10 shipped with Windows 10 and Windows Server 2016). Why? There is never an official explanation. As an out-of-band component, this module is also fully covered by Microsoft support contracts.

Only when I tried to clone the same feature and dived deep into the module, I found its quality (or design) is different from other built-in features.
<!--more-->

## Nested Page Navigation

In other features, you rarely need to navigate to child pages. But URL Rewrite module heavily uses such pages in IIS Manager.

Note that in the Actions panel there are "Back to…" links to parent pages.

A negative effect of this approach is that you can easily lose track of what you are editing.

## Broken Schema File

When I tried to understand the usage of schema files (C:\Windows\System32\inetsrv\config\schema), I thought that IIS Manager loads them only when it is opened. But now I know I was wrong, as there is a bug in URL Rewrite module's schema file (rewrite_schema.xml).

So where is the bug?

``` xml
<element name="conditions">
    <attribute name="logicalGrouping" type="enum" defaultValue="MatchAll">
        <enum name="MatchAll" value="0" />
        <enum name="MatchAny" value="1" />
    </attribute>
    <attribute name="trackAllCaptures" type="bool" defaultValue="false" />
    <collection addElement="add">
        <attribute name="input" type="string" isCombinedKey="true" />
        <attribute name="matchType" type="enum" defaultValue="Pattern" isCombinedKey="true">
            <enum name="Pattern" value="0" />
        </attribute>
        <attribute name="pattern" type="string" isCombinedKey="true" />
        <attribute name="ignoreCase" type="bool" defaultValue="true" isCombinedKey="true" />
        <attribute name="negate" type="bool" defaultValue="false" isCombinedKey="true" />
    </collection>
</element>
```

Well, note that for `matchType` attribute, there seems to be only a single option called `Pattern`. But in fact, you can find from other materials that there are two other options, `IsFile` and `IsDirectory`.

Since the module works fine with such a buggy schema file, we can see the schema file (as well as others) is not read by the module at runtime. There might be a correct version embedded in the module binary somewhere I think.

## Other Minor Differences

If you take a closer look at the Actions panel in the above screen shot, you might observe another issue, that after the "Add Mapping Entry…" item, there is no separator. Such a separator is common in other modules (even in URL Rewrite module's other pages).

So we can only guess that this module was developed at a completely different time slot and by probably multiple persons.
