---
layout: post
title: "#SNMP Design: Agent Side Support Update"
description: "This post talks about the progress of agent side support."
tags: SNMP
permalink: /snmp-design-agent-side-support-update-41b47b2bcea3
excerpt_separator: <!--more-->
---
According to the poll, a moderate amount of developers want to create SNMP agent on .NET. This means I can help them by adding an Agent component in #SNMP. After handing over the browser to Steve, now I have time and energy to focus on the library, so there is no reason to delay new features like this.
<!--more-->

Yes, the current progress is that a basic Agent component is there in the repository. Because of the complexity, I divide agent side support into two parts roughly. The first part is an Agent component which provides a SNMP communication channel to managers. This part is almost done. Now if you drag this component into your form, and in a few seconds it can monitor incoming SNMP requests.

However, an SNMP agent is surely more than this component. Whenever a request is received, a correct response must be generated, and all managed objects need to be taken good care of. So the second part, an object repository, is in fact the key component. Right now I don't even have a clear plan on its design.

If you have any suggestions, please start a new discussion. Stay tuned. In the next post, I am going to discuss the first release candidate of TwinTower.

BTW, I have just added up total downloads for #SNMP releases (0.5, 0.9, 1.0, and 1.1). Guess what? 1026! It also indicates that 672 downloads are recorded for repository snapshots. Perfect number for a young project.
