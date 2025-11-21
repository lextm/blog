---
layout: post
title: "Understanding Port Configuration in HttpPlatformHandler"
description: "Learn how HttpPlatformHandler allocates random ports for backend applications, and how to configure fixed ports for better control."
tags: iis httpplatformhandler windows
categories: [Tools and Platforms]
excerpt_separator: <!--more-->
---

When hosting web apps on IIS using HttpPlatformHandler, understanding how it allocates ports is important. By default, it picks a random port for your backend app each time the app pool starts or recycles.
<!--more-->

## Why Random Ports?

Though not well documented on Microsoft Learn, HttpPlatformHandler might have chosen random ports by default for several reasons:

- Avoiding port conflicts between multiple apps.
- Enhancing security by making ports less predictable.
- Simplifying deployment without manual port management.

Your users never see these random ports. They only interact with IIS on standard HTTP/HTTPS ports (80/443) if you set up good site bindings.

## Using a Dynamic Port

If you prefer HttpPlatformHandler to allocate a random port automatically, your `web.config` should look like this:

```xml
<configuration>
    <system.webServer>
        <handlers>
            <add name="httpPlatformHandler" path="*" verb="*" modules="httpPlatformHandler" resourceType="Unspecified" />
        </handlers>
        <httpPlatform processPath="node.exe"
                      arguments="path\to\your\app.js"
                      stdoutLogEnabled="false"
                      stdoutLogFile=".\logs\stdout">
            <environmentVariables>
                <environmentVariable name="PORT" value="%HTTP_PLATFORM_PORT%" /> <!-- backend app listens on dynamic port -->
            </environmentVariables>
        </httpPlatform>
    </system.webServer>
</configuration>
```

Here, `%HTTP_PLATFORM_PORT%` is automatically set by HttpPlatformHandler at runtime, and your backend app should read this environment variable to determine the port to listen on.

## Using a Fixed Port

Sometimes you need a fixed port. For example, when debugging or integrating with other services that expect a specific port.

Starting from HTTP Bridge Module for IIS, you can specify a fixed port easily. Just update your `web.config` like this:

```xml
<configuration>
    <system.webServer>
        <handlers>
            <add name="httpPlatformHandler" path="*" verb="*" modules="httpPlatformHandler" resourceType="Unspecified" />
        </handlers>
        <httpPlatform processPath="node.exe"
                      arguments="path\to\your\app.js"
                      stdoutLogEnabled="false"
                      stdoutLogFile=".\logs\stdout">
            <environmentVariables>
                <environmentVariable name="PORT" value="5000" /> <!-- backend app listens here -->
                <environmentVariable name="HTTP_PLATFORM_PORT" value="5000" /> <!-- HttpPlatformHandler forwards traffic here -->
            </environmentVariables>
        </httpPlatform>
    </system.webServer>
</configuration>
```

Here, I show you a Node.js example, and the `PORT` variable tells your backend app which port to listen on, and `HTTP_PLATFORM_PORT` instructs HttpPlatformHandler to forward requests to that port.

## Reading the Port in Your App

Your backend app needs to read the port number from the environment variable. The same code works for both dynamic and fixed ports. For example, in Node.js:

```javascript
const express = require('express');
const app = express();

const port = process.env.PORT || 3000;

app.get('/', (req, res) => {
  res.send('Hello from IIS-hosted Node.js app!');
});

app.listen(port, () => {
  console.log(`Listening on port ${port}`);
});
```

## When to Use Fixed Ports?

Fixed ports are helpful in these scenarios:

- **Debugging**: Consistent environment for troubleshooting.
- **Integration**: Other services expect your app on a specific port.
- **Network Rules**: Firewall or network configurations require known ports.
- **Containers**: Migrating apps originally designed for Docker or similar platforms.

## Important Considerations

When using fixed ports, remember:

- **Avoid conflicts**: Make sure the port isn't already in use.
- **Security**: Fixed ports can be easier targets for attackers.

## Troubleshooting Common Issues

If you encounter issues with port allocation, consider the following troubleshooting steps:

- **Check Logs**: Enable `stdoutLogEnabled` in your `web.config` to capture detailed logs.
- **Port Conflicts**: Use tools like `netstat` or `TCPView` to identify port conflicts.
- **Permissions**: Ensure IIS and your backend app have sufficient permissions to bind to the specified port.

## Conclusion

Random ports simplify deployment and enhance security, but fixed ports give you more control when needed. Knowing how to configure both helps you manage your IIS-hosted apps effectively.

Have you used fixed ports with HttpPlatformHandler? Let me know your experience in the comments.

## Related HttpPlatformHandler Articles

> This article is part of a series on using HttpPlatformHandler with IIS. To explore all related articles, please visit the [httpplatformhandler tag page]({{ site.baseurl }}/tags/httpplatformhandler/) for the complete collection of guides and tutorials.
