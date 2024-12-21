---
layout: post
title: "Another Monkey: Analysis of the Mono Project's History and Future Based on Microsoft's Announcement"
description: "A deep dive into Microsoft's latest announcement on the Mono Project, exploring the project's historical background, technological evolution, and possible future directions. Understand Mono's significance within the .NET ecosystem and the reasons for its gradual marginalization."
tags: Mono .NET Microsoft Xamarin
excerpt_separator: <!--more-->
---

> "You must have heard stories about him. Some say he helped Tang Seng fetch the Buddhist scriptures becoming the "Victorious Fighting Buddha". From then on, he stayed in Lingshan. Some say it wasn't him who was granted Buddhahood. The real him was already dead on the journey to the West. Some say there is no such journey. He's just a storyteller's fictional monkey. But you must have not heard the story I'm going to tell." — *Black Myth: Wukong*

Recently, *Black Myth: Wukong* has created a buzz worldwide. However, this article doesn't focus on this Chinese mythical hero, nor the Destined Ones, but on another "monkey" that once made waves in the tech world, the Mono Project.

A few months after the Mono Project’s GitHub repository stopped receiving updates, Microsoft finally released [an important announcement](https://github.com/mono/mono/issues/21796). Combining insights from the historical context recorded in [*.NET Legend*](https://dotnet.lextudio.com/), this article will analyze and interpret the contents of this announcement step by step, exploring the role that the Mono Project has played in technological evolution and what this announcement means for its future.

## **Sentence 1**

> "The Mono Project (mono/mono) (‘original mono’) has been an important part of the .NET ecosystem since it was launched in 2001."

Since its launch in 2000, the Mono Project has indeed occupied a significant place in the .NET ecosystem. As detailed in *The .NET Legend*, the Mono Project was initiated and led by Miguel de Icaza with the aim of introducing .NET framework-related technologies to the Linux platform, enabling the rapid development of applications on Linux. Its outstanding cross-platform capabilities have made Mono a crucial component of the .NET ecosystem.

Like its name suggests, the Mono Project is like a nimble monkey, helping developers move freely between different platforms and providing immense convenience.

## **Sentence 2**

> "Microsoft became the steward of the Mono Project when it acquired Xamarin in 2016."

The golden age of the Mono Project was also the years when it powered the Unity gaming platform and the Xamarin mobile development platform, serving a vast number of developers. Microsoft became the steward of the Mono Project in 2016 through its acquisition of Xamarin. This marked a new phase in Mono's development. Before and after the acquisition, Microsoft integrated Xamarin with the .NET Framework/.NET Core ecosystem in the first round, offering developers using .NET/Mono technology an improved experience.

## **Sentence 3**

> "The last major release of the Mono Project was in July 2019, with minor patch releases since that time. The last patch release was February 2024."

2019 was a pivotal year for the .NET ecosystem. The official release of .NET Core 3.0/3.1 and the [announcement of the .NET 5 development plan](https://devblogs.microsoft.com/dotnet/introducing-net-5/) marked a significant acceleration in the modernization of the entire .NET platform, entering a second phase of deep integration. This greatly affected the importance of the Mono Project. As .NET Core gradually became mainstream, the marginalization of Mono became inevitable. Although the sudden emergence of Blazor indicated that part of Mono's core technology was something .NET Core lacked at that time, the announcement of .NET 5 made it clear that the .NET ecosystem was moving towards a unified platform.

Although the Mono Project underwent its last major update in 2019, subsequent development work focused mainly on fixing bugs and releasing minor patches, rather than introducing new features or improvements. The last patch version of the Mono Project under Microsoft’s management was released in February 2024, coinciding with the final days of the Xamarin brand within Microsoft’s products. After May 1, 2024, [the Xamarin brand officially exited the historical stage](https://dotnet.microsoft.com/en-us/platform/support/policy/xamarin), fully replaced by .NET MAUI.

## **Sentence 4**

> "We are happy to announce that the WineHQ organization will be taking over as the stewards of the Mono Project upstream at wine-mono / Mono · GitLab (winehq.org). Source code in existing mono/mono and other repos will remain available, although repos may be archived. Binaries will remain available for up to four years."

In its announcement, Microsoft stated that the management of the Mono Project would be transferred to WineHQ, marking a new historical stage for the project. With the steady advancement of .NET 5/6/7/8/9, the vast majority of developers have already completed their project migrations.

The Mono Project has been handed over to an organization dedicated to open-source and cross-platform compatibility. But what value can this project continue to provide under WineHQ’s stewardship? Despite the challenges of limited resources and accumulating technical debt, WineHQ may bring new vitality to the Mono Project.

> Friends enjoying *Black Myth* on Apple’s M2 hardware are undoubtedly benefiting from the efforts of WineHQ’s Wine project.

## **Sentence 5**

> "Microsoft maintains a modern fork of Mono runtime in the dotnet/runtime repo and has been progressively moving workloads to that fork. That work is now complete, and we recommend that active Mono users and maintainers of Mono-based app frameworks migrate to .NET which includes work from this fork."

During the .NET 5/6 era, Microsoft integrated Mono’s most valuable asset, MonoVM, into the .NET ecosystem. This integration fostered the healthy development of Blazor and .NET MAUI. The currently active version, .NET 8, and the upcoming .NET 9 are the modern, unified .NET platform that all developers rely on.

Therefore, for most developers, focusing on .NET 8 is sufficient, rather than on Mono.

## **Sentence 6**

> "We want to recognize that the Mono Project was the first .NET implementation on Android, iOS, Linux, and other operating systems. The Mono Project was a trailblazer for the .NET platform across many operating systems. It helped make cross-platform .NET a reality and enabled .NET in many new places and we appreciate the work of those who came before us."

Here, Microsoft highly praises the Mono Project, especially its pioneering role in cross-platform development. Mono was the first implementation of .NET technology on non-Windows platforms. Its contributions in recent years have helped Microsoft’s .NET ecosystem reach more operating systems and devices, achieving today’s mainstream development platform status. The historical contribution of the Mono Project cannot be overlooked, as I’ve similarly concluded in *The .NET Legend*.

### **Conclusion**

The history and future of the Mono Project are a microcosm of the development of the .NET ecosystem. From Miguel de Icaza to Microsoft’s acquisition, and finally to its transfer to WineHQ, each phase of the Mono Project has held different significance. The release of .NET 5/6/7/8/9 signifies that the historical mission of the Mono Project has been completed. The future of the ecosystem will increasingly depend on the development of Microsoft’s .NET platform.

WineHQ representatives have indicated that they are planning and researching the next phase of the Mono Project’s development and hope to reveal more details soon. I will continue to follow the future of the Mono Project closely.

> As for the connection between *Black Myth: Wukong* and the Mono Project, perhaps I’ll find another opportunity to write a special article about it.
