---
layout: post
title: "GrapeVine Voice: Checked Menu Items"
description: This post talks about how to create checked menu items.
tags: Code-Beautifier-Collection Delphi
permalink: /grapevine-voice-checked-menu-items-a33bb0aa51c4
excerpt_separator: <!--more-->
---
In David's legacy project SharpBuilderTools there is no such kind of checked menu items so I thought it was impossible. Then I started to wonder how the RemObjects guys creates checked menu items in their BDS expert named Everwood.

On Tuesday I suddenly found out how so I added a few new functions in LeXDK. You can see I created a new menu item like this,

``` csharp
RegisterAction(CreateCheckedMenu(MenuItemLocation.Child,
                                MenuProject,
                                MenuAutoActivateProject,
                                0,
"Auto Activate Project",
                                (bool)PropertyRegistry.Get("AutoActivateProject", true),
new EventHandler(DoAutoActivateProject)
                               ));
```

The sixth argument of CreateCheckedMenu is named as isChecked. And this is the initial check state.

Because there is no CheckOnClick property on IOTAMenuItem, the event handler must change the check state correctly like this,

``` csharp
private void DoAutoActivateProject(object sender, EventArgs e)
{
    bool state = (bool)PropertyRegistry.Get("AutoActivateProject", true);
    bool newState = !state;
    OtaUtils.SetMenuItemCheckState(MenuAutoActivateProject, newState);
    PropertyRegistry.Set("AutoActivateProject", newState);
}
```

The new functions will be available soon in a later version of LeXDK/CBC.

Why checked menu item is a must? Even though it is a pseudo standard to place all preferences in a global dialogue, in that way in order to change a simple setting like a boolean flag a long sequence of clicks is required. Therefore, sometimes simple settings should be provided as checked menu items so modification of them is straight forward.

Stay tuned.
<!--more-->