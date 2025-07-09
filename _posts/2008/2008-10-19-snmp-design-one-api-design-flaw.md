---
layout: post
title: "#SNMP Design: One API Design Flaw"
description: "This post is about a design flaw of the current #SNMP APIs."
tags: SNMP
permalink: /snmp-design-one-api-design-flaw-d1a3f72a9966
excerpt_separator: <!--more-->
---
When I reviewed the message classes, I suddenly realized that there is a design flaw. Do you notice?
<!--more-->

Let's forget about existing code, and think about this case. You want to query system description from two agents in the network, so how to write some code? Probably this is the simplest code,

``` csharp
Message message = new Message(/* arguments */);
message.SendTo(agent1);
message.SendTo(agent2);
```

Therefore, when you create the message instance the IP address should not be specified. Yes, the current design fails to support this simple use case, which is obviously a design flaw. But why I did not realize this flaw earlier? Why the early design is like this? That is because TrapV1Message was the first message class, and to create its instance an IP address must be specified. Now I fully understand why people think SNMP v1 TRAP is a bad thing, it does not fit in to the whole image.

At this moment, I don't want to change the existing code because TwinTower is almost ready. Thus, this change will be introduced for CrossRoad. OK, next time I may provide backward compatibility (current APIs will still be available but marked as obsolete while new APIs are introduced side by side. Time after time, I will remove obsolete code so you have time to prepare the migration).

Stay tuned.
