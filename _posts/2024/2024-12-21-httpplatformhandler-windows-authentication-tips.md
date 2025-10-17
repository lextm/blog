---
layout: post
title: "Windows Authentication Tips for HttpPlatformHandler"
description: "Learn how to properly enable Windows Authentication for non-Microsoft web applications hosted on IIS using HttpPlatformHandler, including configuration steps and code examples for Python and Ruby applications."
tags: iis windows httpplatformhandler
categories: [Tools and Platforms]
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

There might be framework specific packages to simplify the process, such as [this dedicated package for Django](https://pypi.org/project/django-windowsauth/).

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
npm install koffi
```

Then Windows authentication information can be accessed by the sample code,

```javascript
const express = require('express');
const koffi = require('koffi');

const app = express();
const port = process.env.PORT || 3000;

// Define Win32 constants
const TokenUser = 1; // TOKEN_INFORMATION_CLASS value for TokenUser

// Define Win32 API structures and functions
const kernel32 = koffi.load('kernel32.dll');
const advapi32 = koffi.load('advapi32.dll');

// Define the CloseHandle function according to Microsoft docs
// BOOL CloseHandle(HANDLE hObject);
const closeHandleFn = kernel32.func('bool CloseHandle(void* hObject)');

// Define the GetTokenInformation function according to Microsoft docs
// BOOL GetTokenInformation(
//   HANDLE                  TokenHandle,
//   TOKEN_INFORMATION_CLASS TokenInformationClass,
//   LPVOID                  TokenInformation,
//   DWORD                   TokenInformationLength,
//   PDWORD                  ReturnLength
// );
const getTokenInformationFn = advapi32.func(
    'bool GetTokenInformation(void* TokenHandle, int TokenInformationClass, void* TokenInformation, uint32 TokenInformationLength, void* ReturnLength)'
);

// Define the LookupAccountSidW function according to Microsoft docs
// BOOL LookupAccountSidW(
//   LPCWSTR       lpSystemName,
//   PSID          Sid,
//   LPWSTR        Name,
//   LPDWORD       cchName,
//   LPWSTR        ReferencedDomainName,
//   LPDWORD       cchReferencedDomainName,
//   PSID_NAME_USE peUse
// );
const lookupAccountSidWFn = advapi32.func(
    'bool LookupAccountSidW(void* lpSystemName, void* Sid, void* Name, void* cchName, void* ReferencedDomainName, void* cchReferencedDomainName, void* peUse)'
);

// Helper function to get user information from token
function getUserInfoFromToken(tokenHandle) {
    try {
        // Allocate buffers for token information
        const buflen = 256; // Increase buffer size
        const tokenInfo = Buffer.alloc(buflen);
        const returnLength = Buffer.alloc(4); // DWORD size

        console.log(`Getting token information for handle: ${tokenHandle}`);
        
        // Get token information
        const tokenInfoResult = getTokenInformationFn(
            tokenHandle,
            TokenUser,
            tokenInfo,
            buflen,
            returnLength
        );

        if (!tokenInfoResult) {
            const error = new Error('GetTokenInformation failed');
            console.error(error.message);
            throw error;
        }

        const returnedLength = returnLength.readUInt32LE(0);
        console.log(`Token information retrieved. Length: ${returnedLength} bytes`);
        
        // The TOKEN_USER structure has a SID pointer at offset 0
        // We need to read this pointer to get the actual SID
        const sidPointer = tokenInfo.readBigUInt64LE(0);
        console.log(`SID pointer extracted: ${sidPointer}`);
        
        if (sidPointer === 0n) {
            console.error('SID pointer is NULL');
            throw new Error('Invalid SID pointer');
        }

        // Prepare buffers for LookupAccountSidW
        const nameBufferSize = 256; // Increase buffer size
        const domainBufferSize = 256; // Increase buffer size
        
        const nameBuffer = Buffer.alloc(nameBufferSize * 2); // UTF-16LE (2 bytes per char)
        const domainBuffer = Buffer.alloc(domainBufferSize * 2); // UTF-16LE (2 bytes per char)
        
        const nameLength = Buffer.alloc(4); // DWORD size
        nameLength.writeUInt32LE(nameBufferSize, 0);
        
        const domainLength = Buffer.alloc(4); // DWORD size
        domainLength.writeUInt32LE(domainBufferSize, 0);
        
        const sidUseType = Buffer.alloc(4); // SID_NAME_USE size

        console.log('Calling LookupAccountSidW...');
        
        // Look up the account SID - use the SID pointer directly
        const lookupResult = lookupAccountSidWFn(
            null, // lpSystemName (NULL for local system)
            BigInt(sidPointer), // Convert to BigInt for consistency
            nameBuffer,
            nameLength,
            domainBuffer,
            domainLength,
            sidUseType
        );

        if (!lookupResult) {
            // Get the Windows error code
            const lastError = getLastError();
            console.error(`LookupAccountSidW failed with error code: ${lastError}`);
            throw new Error(`LookupAccountSidW failed with error code: ${lastError}`);
        }

        // Convert buffers to strings, trim null characters
        const nameSize = nameLength.readUInt32LE(0);
        const domainSize = domainLength.readUInt32LE(0);
        
        const userName = nameBuffer.toString('utf16le', 0, nameSize * 2).replace(/\0+$/, '');
        const domainName = domainBuffer.toString('utf16le', 0, domainSize * 2).replace(/\0+$/, '');

        console.log(`User info retrieved - Name: ${userName}, Domain: ${domainName}`);
        
        // Close the handle
        closeHandleFn(tokenHandle);

        return {
            user: userName,
            domain: domainName
        };
    } catch (error) {
        // Make sure we close the handle even if there's an error
        try {
            if (tokenHandle) {
                closeHandleFn(tokenHandle);
            }
        } catch (closeError) {
            console.error('Error closing handle:', closeError);
        }
        
        throw error;
    }
}

// Add a function to get the last Windows error
function getLastError() {
    try {
        const getLastErrorFn = kernel32.func('uint32 GetLastError()');
        return getLastErrorFn();
    } catch (error) {
        console.error('Error getting last error code:', error);
        return -1;
    }
}

app.get('/', (req, res) => {
    try {
        const tokenHeader = req.headers['x-iis-windowsauthtoken'];

        if (!tokenHeader) {
            return res.status(400).send('No HTTP_X_IIS_WINDOWSAUTHTOKEN header found.');
        }

        // Convert the token from hex to a number
        const handle = parseInt(tokenHeader, 16);
        
        if (isNaN(handle)) {
            return res.status(400).send('Invalid token format in header.');
        }

        const userInfo = getUserInfoFromToken(handle);
        
        return res.json({
            status: 'success',
            data: userInfo
        });
    } catch (error) {
        console.error('Error processing request:', error);
        return res.status(500).send(`Error: ${error.message}`);
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

## Related HttpPlatformHandler Articles

> This article is part of a series on using HttpPlatformHandler with IIS. To explore all related articles, please visit the [httpplatformhandler tag page]({{ site.baseurl }}/tags/httpplatformhandler/) for the complete collection of guides and tutorials.
