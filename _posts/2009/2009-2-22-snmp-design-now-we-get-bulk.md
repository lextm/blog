---
layout: post
title: "#SNMP Design: Now We GET BULK"
description: "This post is about the GET BULK message type support."
tags: SNMP
permalink: /snmp-design-now-we-get-bulk-2db25fc8cd97
excerpt_separator: <!--more-->
---
GET BULK is an enhanced GET NEXT, which can boost performance significantly.. So how to understand that? You can ask the agent to return you ten objects after the seed OID you send in the request message. So in this case one GET BULK operation replaces 10 GET NEXT operations.

So now we have GET BULK automatically involved if you play with Manager.GetTable in SNMP v2c. Please check our the latest source code in the repository to see the changes. Well, we cannot yet handle sparse tables and multi-index tables at this moment. But you can expect continuous improvement all along the way.

Stay tuned.
<!--more-->