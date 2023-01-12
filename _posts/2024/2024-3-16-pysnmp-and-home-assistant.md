---
layout: post
title: "PySNMP and Home Assistant"
description: A post about latest news on PySNMP and Home Assistant
tags: SNMP Python Home-Assistant
excerpt_separator: <!--more-->
---

Home Assistant is a popular open-source home automation platform. It is able to integrate with a wide variety of devices and services, and it is also able to monitor and control SNMP devices. The integration is done through the PySNMP library, which is a pure-Python SNMP library.
<!--more-->

When we decided to ship PySNMP 6.0, we intentionally brought a lot of breaking changes to adapt to new Python 3.12 release, so naturally it will affect Home Assistant. The good news is we are helping the Home Assistant team to update their code to work with PySNMP 6.0, and we are also shipping new releases of PySNMP to make the transition as smooth as possible.

So, the story goes.

## Initial Bug Report

[The initial report](https://github.com/home-assistant/core/issues/110100) was opened on Feb 9, and it was about Python 3.12 broke HA 2024.2.1 SNMP support. That's expected because PySNMP 5.0.x wasn't aiming to support Python 3.12, and we have moved to PySNMP 6.0.x. @bieniu was able to bump PySNMP to 6.0.2.

That's when my team jumped in to help, and we suggested to [bump PySNMP to 6.0.9](https://github.com/home-assistant/core/pull/112795).

> We even added some `oneliner` types back in PySNMP 6.0.9 to make the transition smoother.

While our hope was that this simple change would fix the issue, it turned out that it didn't work completely.

## Test Environments

To dive deeper into the issue, we started by building a test environment with HA OS VM (2024.3.1 release) on VirtualBox/macOS on Mar 14 on which we quickly identified the WALK v2 bug and fixed in PySNMP 6.0.11.

> As a sidenote, we didn't expect anyone to perform GET NEXT based WALK operations in SNMP v2c/v3, as GET BULK based WALK is more efficient, but it turned out that HA was doing that. A few unit test cases were missed in this field, but not anymore.
>
> Also note that HA OS is more end user centric, so later we have to switch to another environment setup.

That's how we opened [a new issue for tracking](https://github.com/home-assistant/core/issues/113457) and [the pull request](https://github.com/home-assistant/core/pull/113463) was accepted.

End users still reported issues with device tracker feature, so we wondered if something simple was missed.

To better investigate, we moved on to build a new test environment with Multipass/Ubuntu/HA Core on macOS on Mar 15. In this environment we were able to run our own fork so we were able to confirm sensor and switch features are working fine, but device tracker feature is still broken.

> HA Core seems to be the only feasible environment for developers to test out their own commits. While all other steps might be useful, we found [this section](https://developers.home-assistant.io/docs/development_environment#setup-local-repository) extremely important.

The problem was very strange that the first round of WALK seemed to work fine, but no further rounds of SNMP packets could be seen from Wireshark. That means somehow HA Core hanged the PySNMP session in the middle. Therefore, [a new issue](https://github.com/home-assistant/core/issues/113605) was opened to track this.

## Sudden Resolution

Before we spent time investigating further the root cause of this issue, we already knew that [@nmaggioni was helping to port device tracker to asyncio](https://github.com/home-assistant/core/pull/112815).

Thus, we took a shortcut to cherry pick his changes to our fork and found that the device tracker feature started to work again.

So now we are waiting for this pull request to be merged.

> [The sideline issue](https://github.com/home-assistant/core/issues/112984) can be closed as well.

## Extras

We did take a look at other open issues related to SNMP and found the `Opaque` related [issue](https://github.com/home-assistant/core/issues/112392) interesting. Hard to believe it in fact has been opened for 7 years, and even Ilya participated in [the previous discussion](https://github.com/home-assistant/core/issues/2767). So, in the end we just repeated the tradition to reach out to downstream to offer assistance.

Luckily the troubleshooting and resolution was already done by @ChristianKuehnel years ago in [an old pull request](https://github.com/home-assistant/core/pull/11239) which was not accepted just because the way he tried to test out the fix.

This time instead of running a test agent behind the scene, we went directly with mocking and the test cases became much simpler.

[Our pull request](https://github.com/home-assistant/core/pull/113624) has been accepted and we are happy to see the long time issue is finally closed.
