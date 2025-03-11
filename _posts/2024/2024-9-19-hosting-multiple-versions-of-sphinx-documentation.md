---
layout: post
title: "Sphinx Documentation: Hosting Multiple Versions for Your Project"
description: ""
tags: Sphinx Python
excerpt_separator: <!--more-->
---

If you are maintaining a project, the best practice is to stick to a single version. It simplifies coding, testing, and hosting documentation. However, in reality, you may need to maintain multiple versions of your project, including the documentation. This post will guide you through how to host multiple versions of Sphinx documentation for your project using `sphinx-polyversion`.

<!--more-->

## Why Not ReadTheDocs?

ReadTheDocs is a popular platform for hosting documentation. It supports multiple versions of documentation, and it's free for open-source projects. While it might work for some, my team encountered limitations that led us to move all our documentation to self-hosting a few years ago. We've found Cloudflare Pages to be a great fit for our needs, but any other static site hosting service ([Azure Static Web Apps](https://learn.microsoft.com/en-us/azure/static-web-apps/)) could work just as well.

## What Is the Best Option?

In the past, we evaluated several existing solutions but didn’t find any that fit our needs perfectly. Without naming them, I’ll say that they either lacked automation or were too complex for the task at hand. Recently, however, we came across a project called [sphinx-polyversion](https://github.com/real-yfprojects/sphinx-polyversion). Unlike previous solutions, this one won our hearts due to its simplicity and ease of use.

At its core, `sphinx-polyversion` automates the process of checking out different versions of your project from source control (Git), setting up environments, building versioned documentation, and aggregating them in a single place. The simplicity of this approach is its strength.

You can see it in action by reviewing the project’s own [documentation](https://real-yfprojects.github.io/sphinx-polyversion/), which serves as an example of how the tool works.

## How To Use It?

If you're just starting with a Sphinx project, I suggest forking the `sphinx-polyversion` repo and use it as your starting point. Learning by doing is the best way to understand how it operates.

However, my focus in this post is on how my team integrated `sphinx-polyversion` into PySNMP, which has been around for a while and now supports four versions concurrently: 6.1, 6.2, 7.0, and 7.1.

### The Configuration

Before diving into the integration, our team outlined several goals:

1. Only specific version tags should be hosted—no branches.
2. We only wanted to host major.minor version tags (e.g., 6.1), excluding tags for minor patch versions like 6.1.1.
3. The documentation should work seamlessly in both Preview and Production environments hosted on Cloudflare Pages.

With these objectives in mind, we started configuring `sphinx-polyversion`. The configuration file is relatively simple, and you can see it in [this commit](https://github.com/lextudio/pysnmp/commit/8689cc7cc6cdfe3fe019c0cbfd1f09ae9c95ec10) and [this one](https://github.com/lextudio/pysnmp/commit/caef832b19bb012f6a7816f109571a662091bab5):

- `TAG_REGEX` captures selected version tags. In our case, we had to create and maintain major.minor tags since they weren't used before.
- `BRANCH_REGEX` ensures branches are excluded by either leaving it empty or using a pattern that never matches.
- (Optional) `docs/templates/index.html` is essential for redirecting users at homepage to versioned URLs.
- The original `docs/source` must be upgraded to include version selector elements in the sidebar, requiring several modifications to `conf.py`.
- Finally, latter commit was cherry-picked across all selected release branches. This step ensures that previous versions include the necessary versioning elements.

You can track future configuration changes for polyversion in the [PySNMP repo](https://github.com/lextudio/pysnmp/tree/docs/docs).

### Reverse Proxy Configuration

It’s crucial to configure the reverse proxy correctly to ensure old URLs redirect to the new versioned URLs. Since we use nginx, here’s a simple configuration example:

```nginx
location /pysnmp/ {
    # If the URL does NOT contain a version pattern (non-versioned URL)
    if ($uri !~* "^/pysnmp/v\d+\.\d+/") {
        # Redirect non-versioned URLs to /v7.1/
        rewrite ^/pysnmp/(.*)$ https://docs.lextudio.com/pysnmp/v7.1/$1 permanent;
    }

    # For versioned URLs, proxy the request
    proxy_ssl_server_name on;
    proxy_pass https://pysnmp.pages.dev/;
    proxy_set_header Host "pysnmp.pages.dev";
}
```

This configuration ensures that users visiting non-versioned URLs are automatically redirected to the latest stable version (v7.1 in this case), while versioned URLs are correctly proxied.

## Conclusion

By leveraging `sphinx-polyversion`, we simplified the management of multiple versions of our Sphinx documentation. This tool provides an efficient and scalable way to host versioned docs without adding unnecessary complexity. Whether you're supporting one version or many, `sphinx-polyversion` helps you keep everything organized in a maintainable way.

If you're interested in hosting multiple versions of Sphinx documentation, I recommend giving `sphinx-polyversion` a try. It’s a powerful yet simple tool that could be the solution you're looking for.

> We don't intend to cover all possible features of `sphinx-polyversion` in this post. If you have specific questions or need help with your Sphinx documentation, feel free to reach out to its creator.
