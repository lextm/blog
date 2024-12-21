---
layout: post
title: "GrapeVine Voice: Installer Revisited"
description: This post talks about CodeGear's installer and Code Beautifier Collection's installation experience.
tags: Code-Beautifier-Collection Delphi
permalink: /grapevine-voice-installer-revisited-183ac61b6026
excerpt_separator: <!--more-->
---
CodeGear has a tough issue to resolve now. That is RAD Studio 2007 installation experience (someone claims it is nightmare, but I don't agree). That MSI based installer powered by InstallAware technology can satisfy all those critical and complicated requirements (multilingual and multi-SKU and multi-personality in one installer; Web Deploy ) except one key point, speed. Personally speaking I prefer stability to speed, but others may hold a completely different idea. Let's wish Tiburon has a much better installer.
<!--more-->

For Code Beautifier Collection, installation experience is also a tough problem I'd like to solve as soon as possible. That's why I spent a lot of time on Inno Setup last month. However, have to confess part of this problem is not easy to solve.

I thought once that now CBC can be installed for all users. But in fact I was wrong. My knowledge about expert installation in Delphi IDE is still limited. So I posted a question on CodeGear newsgroup today and hoped that some experts could provide some tips so I could follow.

It seems that I cannot say that issue 5 is already solved in the latest build on my dev machine, but this version should provide a better implementation than M8. At least who installs CBC at first can see CBC launches in RAD Studio. But what about other users on the same computer? I wish my changes can install CBC for them.

Meantime, even if I can install CBC for all users, I have to say that I cannot remove it for all users. Binary files can be uninstalled while some registry keys are unreachable. Thus, when some user on the computer launches Delphi, he or she may see a warning that Lextm.CodeBeautifierCollection.Framework.dll cannot be found. If that happens one day on your machine, please don't hesitate to follow the dialog information to disable or remove this assembly from expert list. Only through that CBC can be removed completely.

Who should be blamed for this worst case? I have some responsibility, and CodeGear a little bit, while Microsoft shares some too. I will try to see if there is some workaround but I cannot promise anything now.

BTW, install for all users on the same computer may not be a critical issue for most CBC users. Therefore, it should be considered as an experimental feature for advanced users and most users should please click No when the installer prompts "Install Code Beautifier Collection for all users?". A detailed warning "This is an experimental feature. Click No if you don't want to participate in the trial." is now added to M9 installer.

I will keep you all updated about my research. Stay tuned.
