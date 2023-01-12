
---
layout: post
title: "Jexus Manager Server Side Update: Security Concerns"
description: "This post is about how Jexus Manager server side is updated to address security concerns."
tags: Jexus-Manager Linux Mono
permalink: /jexus-manager-server-side-update-security-concerns-4ecb6dd3ff1d
excerpt_separator: <!--more-->
---
Before the 1.0 release of Jexus Manager, several security protection were added gradually.
<!--more-->

## HTTPS Enforcement (1.0)

This is the very basic protection added by encrypting network packets.

## Simple Authentication (1.0)

Jexus Manager server component allows user name and passphrase to be passed via command line parameters. Then at client side the credentials can be used for server authentication.

## Time Stamp Check (1.0)

To prevent attackers from recording packets on the wire and replaying them to attack the server, the change was made to verify time stamps.

Packets that fall out of permitted time slots are going to be dropped.

## Automatic Certificate Generation (1.0)

The initial beta releases use a dedicate test certificate, which is public to everyone (including the attackers), so that the private key can be used to decrypt the HTTPS packets if captured.

To avoid the vulnerability, a warning was initially added to the documentation to ask server administrators to generate and configure their own server certificates for Jexus Manager. Finally the server component was updated to automatically generate and install a self-signed certificate if no certificate is yet configured.

Since the private keys then become server-dependent and hidden, the vulnerability is fixed.

## Hello and Goodbye Test (1.0)

If there are multiple clients connecting to the same server, then there might be potential issues such as configuration corruption. In edge cases that might also be an indicator of being compromised. 

Thus, at beginning and the end of a remote connection, Jexus Manager client sends Hello and Goodbye messages to inform the server, and meanwhile queries if other clients have already connected.

## Auto Update (1.0)

As new releases of Jexus Manager components deliver new features as well as bug fixes, the users should be notified once they are available. Thus, the server component allows the client to query its version.

Now I'd like to introduce a few new protection added in the next release (1.1).

## Parent Path Disabled (1.1)

It is clear that many methods allowing file paths that contain `..` to be passed. Then unauthorized Jexus Manager users might be able to query system information that they don't usually have access to. Thus, such file paths will be forbidden.

## Localhost Test (1.1)

Several methods are only designed for Jexus Manager clients that connect from localhost. Thus, now they check incoming requests to see if the packets come from localhost. This ultimately prevents remote calls.

## Sensitive Information Removed (1.1)

Hello and Goodbye test in fact sends back IP addresses of valid clients that already connect to the server. Such information might be sensitive if clients connect remotely, so unless the client connects from localhost the IP address won't be revealed.

## Summary

Security is a very important concept in web server field. Jexus Manager is going to be periodically updated to address security vulnerabilities. Please install updates once they are available.

Stay tuned.
