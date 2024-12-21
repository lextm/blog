---
layout: post
title: "Citrix Receiver Installation on openSUSE 12.1 64-bit"
description: "This post is about Citrix Receiver installation on openSUSE 12.1 64-bit."
tags: Linux
permalink: /citrix-receiver-installation-on-opensuse-12-1-64-bit-fc20b664928b
excerpt_separator: <!--more-->
---
I recently switched to openSUSE 12.1 fully as my desktop failed to serve Windows 7 without hang or crash. One difficulty right now is that I could not install Citrix Receiver as wished by downloading their 64 bit .rpm package [1].
<!--more-->

I did not want to give up easily, so I downloaded the .tar.gz package and attempted to install. It also failed, as it refused to work for 64 bit CPU architecture.

I was so used to WOW64 on Windows, and I ignored the fact that now Linux also supports something similar till today I launched the 32 bit Terminal for the first time.

Well, that's it. the .tar.gz installer worked fine in 32 bit Terminal (with sudo of course). Then I could see Citrix Receiver icon in Gnome 3.

``` bash
sudo ./setupwfc
```

The last issue was that SSL error 61 occurred. It was easily solved by copying Firefox certificates [2].

``` bash
sudo cp /usr/share/ca-certificates/mozilla/* /opt/Citrix/ICAClient/keystore/cacerts
```

## References

* [1]: http://www.citrix.com/English/ss/downloads/details.asp?downloadId=2323812&productId=1689163#top
* [2]: http://www.itswapshop.com/tutorial/how-install-citrix-receiver-linux-120-opensuse-121