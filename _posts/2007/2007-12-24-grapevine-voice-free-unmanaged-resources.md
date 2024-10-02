---
layout: post
title: "GrapeVine Voice: Free Unmanaged Resources"
description: This post is about how to free up unmanaged resources.
tags: Code-Beautifier-Collection Delphi
permalink: /grapevine-voice-free-unmanaged-resources-2bd41102062a
excerpt_separator: <!--more-->
---
I have been programming in C# for a few years, but I never dig deeper to unmanaged resources related topics until last Friday I met an exception when launching Favourite feature is WiseEditor Plus.
<!--more-->

I set break points in order to locate the bug but I failed. The debugger just could not tell me where the issue was. Suddenly I noticed some modifications I introduced a few weeks ago in ExtractIcon.cs.

I followed MSDN reference to Icon.FromHandle to free the handle with DestroyIcon. The following is the sample code from MSDN.

``` csharp
[System.Runtime.InteropServices.DllImport("user32.dll", CharSet=CharSet.Auto)]
extern static bool DestroyIcon(IntPtr handle);

private void GetHicon_Example(PaintEventArgs e)
{
    // Create a Bitmap object from an image file.
    Bitmap myBitmap = new Bitmap(@"c:\FakePhoto.jpg");

    // Draw myBitmap to the screen.
    e.Graphics.DrawImage(myBitmap, 0, 0);

    // Get an Hicon for myBitmap.
    IntPtr Hicon = myBitmap.GetHicon();

    // Create a new icon from the handle.
    Icon newIcon = Icon.FromHandle(Hicon);

    // Set the form Icon attribute to the new icon.
    this.Icon = newIcon;

    // Destroy the Icon, since the form creates
    // its own copy of the icon.
    DestroyIcon(newIcon.Handle);
}
```

You can check GrapeVine code to see what I have written and the bug is not hard to find. I destroyed the handle already but continued to return the Icon instance to the caller. Even though the exception is raised later, you cannot locate the bug in a glance.

David's original code fails to free the unmanaged resource because DestroyIcon is not called. It is a horrible mistake that my modifications mess things up. BTW, the fix is really easy after reading MSDN carefully ("since the form creates its own copy of the icon").

Yes, simply return a clone (created by Icon.Clone) of the Icon instance (created by Icon.FromHandle), and call DestroyIcon on the first Icon instance (created by Icon.FromHandle). And there should be no more baggage.

This fix is part of GrapeVine Final which will be available soon. Stay tuned.
