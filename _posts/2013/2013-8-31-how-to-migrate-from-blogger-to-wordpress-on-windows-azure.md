---
layout: post
title: "How to Migrate from Blogger to WordPress on Windows Azure"
description: "This post talks about how I migrated from Blogger to WordPress on Windows Azure."
tags: Azure
permalink: /how-to-migrate-from-blogger-to-wordpress-on-windows-azure-bcd9322df84a
excerpt_separator: <!--more-->
---
I used to use a Chinese blogging service called CSDN. As it is a closed system which has no open API I experienced difficulties migrating my posts from it to Blogger.

Recently I finally get tired of Blogger too, due to its service unavailable in China Mainland (not Google's fault though). So this time I decided to try out Windows Azure and WordPress.
<!--more-->

## MySQL Hosting on Windows Azure Virtual Machine

As my MSDN subscription only provides me credits in Windows Azure, I choose to [build a virtual machine and host MySQL on my own](https://learn.microsoft.com/samples/azure/azure-quickstart-templates/mysql-standalone-server-ubuntu/).

Well for WordPress alone, you might execute a few extra steps when following the above article,

* At step 7 and 8, replace localhost with %. Using this wild card ensures that your WordPress site on Windows Azure can access the database using the account mysqluser.
* Then step 9 is no longer needed. Continue to execute the remaining steps.

OK now put down the following information,

* MySQL host name (DB_HOST): the host name in step 14, **.cloudapp.net
* MySQL database name (DB_NAME): testdatabase
* MySQL account (DB_USER): mysqluser
* (DB_PASSWORD) The password.

> IMPORTANT: the default Linux virtual machines created by Azure wizard use a disk of only 30-GB, which might quickly run out of space if your site is huge. Make sure you attach more disk space to the machines after creating them.

Install WordPress on Windows

First install IIS on Windows and also [enable PHP support](http://www.iis.net/learn/install/installing-iis-7/installing-iis-on-windows-vista-and-windows-7).

Second we [install Git](https://help.github.com/articles/set-up-git) and [clone the WordPress source code](https://github.com/WordPress/WordPress).

Create a new web site in IIS and point to the WordPress folder. Then use this web site to host WordPress locally.

## Modify WordPress Binding to MySQL

Rename wp-config-sample.php to wp-config.php.

Open it in a text editor.

What we are going to modify are,

``` php
// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define('DB_NAME', '************');

/** MySQL database username */
define('DB_USER', '**********');

/** MySQL database password */
define('DB_PASSWORD', '*******');

/** MySQL hostname */
define('DB_HOST', '**************');
```

The information we write down for MySQL hosting should be now filled in to replace the existing values.

Save the file.

## Import from Blogger

Now it is time to go to your WordPress site and set up everything, such as [importing from Blogger](http://codex.wordpress.org/Importing_Content#Blogger).

Now check in all changes you make locally in Git and get ready to publish.

## Publish WordPress on Windows Azure

To go BitBucket.org and create [a private repository](https://confluence.atlassian.com/display/BITBUCKET/Bitbucket+101). Then you can push your local copy of WordPress to it.

Switch to Windows Azure and now create [a new Web Site with BitBucket back end](https://learn.microsoft.com/azure/app-service/quickstart-php?tabs=cli&pivots=platform-windows#push-to-azure-from-git). Once finished, Windows Azure will clone the repository and always take care of your new change sets.

## Setup Custom Domain

To set up custom domain, please follow [this guide](https://learn.microsoft.com/azure/app-service/manage-custom-dns-migrate-domain).

You also need to go to General Settings of WordPress site to set WordPress Address (URL) and Site Address (URL) to the custom domain URL.

For Blogger users like me, one thing painful is that you lost the permanent links, as Blogger and WordPress use different styles.

Thus, first I go to Permalink Settings of WordPress and choose the Month and name style, which will be my new style for URLs. Then I go back to my BlogSpot site to find out which are the famous links there and [create a web.config file to contain mappings from the old URLs to new ones](http://www.iis.net/downloads/microsoft/url-rewrite).

A portion of my file looks like this,

``` xml
<configuration>
    <system.webServer>
        <rewrite>
            <rewriteMaps>
                <rewriteMap name="famous">
                    <add key="/2012/07/if-you-cannot-installuninstall-iis-7.html" value="/2012/07/if-you-cannot-installuninstall-iis-7-part-ii/" />
                    <add key="/2011/02/if-you-cannot-installuninstall-iis-7.html" value="/2011/02/if-you-cannot-installuninstall-iis-7/" />
                    <add key="/2013/03/dockpanel-suite-how-to-write-new-theme.html" value="/2013/03/dockpanel-suite-how-to-write-a-new-theme/" />
                    <add key="/2007/09/inno-setup-script-sample-for-version.html" value="/2007/09/inno-setup-script-sample-for-version-comparison-advanced-version/" />
                    <add key="/2007/09/product-review-installshield-2008.html" value="/2007/09/product-review-installshield-2008/" />
                    <add key="/2009/05/trident-sign-snmp-v3-packet-format.html" value="/2009/05/trident-sign-snmp-v3-packet-format/" />
                </rewriteMap>
            </rewriteMaps>
            <rules>
                <rule name="Rewrite rule1 for famous" stopProcessing="true">
                    <match url=".*" />
                    <conditions>
                      <add input="{famous:{REQUEST_URI}}" pattern="(.+)" />
                    </conditions>
                    <action type="Redirect" url="{C:1}" appendQueryString="false" />
                </rule>
            </rules>
        </rewrite>
        <httpErrors>
            <remove statusCode="404" subStatusCode="-1" />
            <error statusCode="404" prefixLanguageFilePath="" path="/index.php?error=404" responseMode="ExecuteURL" />
        </httpErrors>
    </system.webServer>
</configuration>
```

Note that I also set up a custom 404 error handler. I am not sure if it is required for WordPress, so I just add it for safety.

In the Git repository, add a text file called web.config to contain the above settings, and push the change to BitBucket.

Your web site will start to accept old URLs and redirects them to corresponding new ones.

You can also install WordPress plugins to monitor 404 errors which can help you refine the rewrite rules.

## Redirection from Blogger to WordPress

There is no built-in way to redirect traffic from http://lextm.blogspot.com to http://www.lextm.com after the migration. But it is rather simple to utilize a piece of JavaScript,

1. Log in to Blogger and go to Layout of that blog.
1. Click Add a Gadget button and choose HTML/JavaScript gadget type.
1. Paste the below script fragment,

``` html
<script type='text/javascript'>
function redirectHttpToHttps()
{
    var newUrl = "http://www.lextm.com" + window.location.pathname + window.location.search;
    window.location.href = newUrl;
}
redirectHttpToHttps();
</script>
```

Make sure this gadget is saved and moved to just below the Header. That should ensure a quicker redirection before any page content is loaded.

## The End

If you have finished all previous steps, you almost finish 99% of the work. The rest is small tunings such as adding AD tags, applying new themes, and trying out more WordPress plugins. WordPress is highly extensible, so make sure you check out the funny themes and plugins to get more functionalities added to your site.
