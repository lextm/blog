---
layout: post
title: "Windows Authentication Tips for HttpPlatformHandler"
description: "Learn how to properly enable Windows Authentication for non-Microsoft web applications hosted on IIS using HttpPlatformHandler, including configuration steps and code examples for Python and Ruby applications."
tags: iis windows httpplatformhandler
excerpt_separator: <!--more-->
---

When hosting web apps on IIS/Windows, some administrators prefer to use Windows authentication. So when the web stack is not from Microsoft, such as Node.js, Go, or Python, you might wonder how to properly enable Windows authentication for them so that your web apps know who are accessing them.
<!--more-->

## Enable Windows Authentication on IIS

The internet is full of articles on how to enable Windows authentication on IIS, so I won't repeat them here.

## Windows Authentication for HttpPlatformHandler

When you use HttpPlatformHandler to host your web apps, you might find that Windows authentication does not work as expected. This is because HttpPlatformHandler does not pass the Windows authentication information to the backend web apps by default.

To enable Windows authentication for HttpPlatformHandler, you need to add the following configuration to your `web.config`:

```xml
<configuration>
  <system.webServer>
    <handlers>
      <add name="myHandler" path="*" verb="*" modules="httpPlatformHandler" resourceType="Unspecified" requireAccess="Script" />
    </handlers>
    <httpPlatform processPath="xxxxx" arguments="xxxxx" stdoutLogEnabled="false" startupTimeLimit="3600" forwardWindowsAuthToken="true" />
  </system.webServer>
</configuration>
```

The `forwardWindowsAuthToken` attribute is the key to enabling Windows authentication for HttpPlatformHandler. When set to `true`, HttpPlatformHandler will pass the Windows authentication information to the backend web apps via the `X-IIS-WindowsAuthToken` header.

## Access Windows Authentication Information in Your Web App

After enabling Windows authentication for HttpPlatformHandler, you can access the Windows authentication information in your web app by reading the `X-IIS-WindowsAuthToken` header. The header contains the Windows authentication information in the format of a Windows token handle. Therefore, you need to call the relevant Windows API to query the user information from the token handle.

### Python Example

Here is an example of how to access the Windows authentication information in a Python web app:

```python
import win32api
import win32security
from flask import request
import logging

# Note if using aspNetCore instead of original httpPlatformHandler then the header would be 'Ms-Aspnetcore-Winauthtoken' instead of 'X-IIS-WindowsAuthToken'
# Also note that the header lookup is case-insensitive (for Flask at least, as in this example)
token_handle_str = request.headers.get('X-IIS-WindowsAuthToken', None)
if token_handle_str:
    token_handle = int(token_handle_str, 16) # need to convert from Hex / base 16
    sid = win32security.GetTokenInformation(token_handle, 1)[0] # TOKEN_INFORMATION_CLASS enum value 1 = TokenUser
    user, domain, account_type = win32security.LookupAccountSid(None, sid)
    win32api.CloseHandle(token_handle) # don't leak resources, need to close the handle!
    logging.warning(f'Request initiated by user {user}')
```

Note that the `win32api` and `win32security` modules are part of the `pywin32` package, which can be installed via pip:

```bash
pip install pywin32
```

### Ruby Example

Here is an example of how to access the Windows authentication information in a Ruby web app:

```ruby
module WIN32
  extend Fiddle::Importer
  dlload 'kernel32.dll'
  include Fiddle::Win32Types
  extern 'BOOL CloseHandle(HANDLE)'
end

module SelfServicesHelper
  def authorize_by_authtoken
    if request.headers.key? "HTTP_X_IIS_WINDOWSAUTHTOKEN"
      handle = request.headers["HTTP_X_IIS_WINDOWSAUTHTOKEN"].hex

      buflen = 64
      tokenInfo, len = "\0" * buflen, [0].pack("L!")
      if WIN32Security::GetTokenInformation(handle, WIN32Security::TokenUser, tokenInfo, buflen, len) != 0
        namelen, dnamelen, use = *[32,32].map{|e| [e].pack("L!")}, [0].pack("I")
        namebuf, dnamebuf = [namelen, dnamelen].map{|e| "\0".encode("utf-16le") * e.unpack1("L!")}
        # ... PSID is at the top of tokenInfo
        if WIN32Security::LookupAccountSidW(nil, tokenInfo.unpack1("Q!"), namebuf, namelen, dnamebuf, dnamelen, use) != 0
          namelen, dnamelen = [namelen, dnamelen].map{|e| e.unpack1("L!")}
          WIN32::CloseHandle(handle)
          logger.debug {"namebuf: %s, dnamebuf: %s" % [namebuf[0, namelen].encode("utf-8"), dnamebuf[0, dnamelen].encode("utf-8")}
        else
          logger.error "LookupAccountSidW returned false, last error: %d" % Fiddle.win32_last_error
        end
      else
        logger.error "GetTokenInformation returned false, last error: %d" % Fiddle.win32_last_error
      end
    else
      logger.debug "no HTTP_X_IIS_WINDOWSAUTHTOKEN"
    end
  end
end
```

### Node.js Example

To invoke Win32 API in Node.js apps, the `libwin32` package need to be installed via npm:

```bash
npm install libwin32
```

> Note that you will have to wait for [my pull request](https://github.com/Septh/libwin32/pull/3) to be accepted and merged, or install the package from my fork.

Then Windows authentication information can be accessed by the sample code,

```javascript
const express = require('express');
const win32 = require('libwin32');

const app = express();
const port = process.env.PORT || 3000;

app.get('/', (req, res) => {
    const tokenHandleStr = req.headers['x-iis-windowsauthtoken'];
    if (!tokenHandleStr) {
        console.debug('Missing x-iis-windowsauthtoken header');
        return res.status(400).send('Missing x-iis-windowsauthtoken header');
    }

    let tokenHandle;
    try {
        tokenHandle = parseInt(tokenHandleStr, 16);

        const TokenUser = 1;
        const returnLengthPtr = Buffer.alloc(8);

        const result = win32.GetTokenInformation(tokenHandle, TokenUser, null, 0, returnLengthPtr);

        const lastError = win32.GetLastError();
        if (lastError !== 122) {
            console.debug('GetTokenInformation failed 1', lastError);
            return res.status(500).send('GetTokenInformation failed 1');
        }

        const requiredSize = returnLengthPtr.readUInt32LE(0);
        console.debug('Required size for token information', requiredSize);
        if (requiredSize <= 0) {
            console.debug('Invalid return length', requiredSize);
            return res.status(500).send('Invalid return length');
        }

        const tokenInfoBuffer = Buffer.alloc(requiredSize);
        const actualSizePtr = Buffer.alloc(8);
        const success = win32.GetTokenInformation(tokenHandle, TokenUser, tokenInfoBuffer, requiredSize, actualSizePtr);

        if (!success) {
            console.debug('GetTokenInformation failed 2', win32.GetLastError());
            return res.status(500).send('GetTokenInformation failed 2');
        }

        const sidPtr = tokenInfoBuffer.readBigUInt64LE(0);
        if (!sidPtr) {
            console.debug('Invalid SID pointer', sidPtr);
            return res.status(500).send('Invalid SID pointer');
        }

        const nameBuffer = Buffer.alloc(256);
        const nameLengthPtr = Buffer.alloc(4);
        const domainBuffer = Buffer.alloc(256);
        const domainLengthPtr = Buffer.alloc(4);
        const usePtr = Buffer.alloc(4);

        nameLengthPtr.writeUInt32LE(nameBuffer.length, 0);
        domainLengthPtr.writeUInt32LE(domainBuffer.length, 0);

        const lookupSuccess = win32.LookupAccountSid(null, sidPtr, nameBuffer, nameLengthPtr, domainBuffer, domainLengthPtr, usePtr);
        if (!lookupSuccess) {
            console.debug('LookupAccountSidW failed', win32.GetLastError());
            return res.status(500).send('LookupAccountSidW failed');
        }

        const nameLength = nameLengthPtr.readUInt32LE(0) * 2;
        const domainLength = domainLengthPtr.readUInt32LE(0) * 2;

        const userName = nameBuffer.toString('utf16le', 0, nameLength).replace(/\0+$/, '');
        const domainName = domainBuffer.toString('utf16le', 0, domainLength).replace(/\0+$/, '');

        console.log(`User: ${userName}, Domain: ${domainName}`);
        res.send(`User: ${userName}, Domain: ${domainName}`);
    }
    catch (error) {
        console.error('Error processing request', error);
        res.status(500).send('Internal Server Error');
    }
    finally {
        if (tokenHandle) {
            win32.CloseHandle(tokenHandle);
        }
    }
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
```

### Go Example

There is [a dedicated package](https://pkg.go.dev/github.com/mfcollins3/windowsauthtoken) for this purpose in Go.

## Conclusion

This post talks about how to enable Windows authentication for HttpPlatformHandler and how to access the Windows authentication information in your web app. By following the steps in this post, you can enable Windows authentication for your web apps hosted on IIS/Windows and access the Windows authentication information in your web app.
