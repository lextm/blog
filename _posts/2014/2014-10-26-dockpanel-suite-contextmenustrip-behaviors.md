---
layout: post
title: "DockPanel Suite: ContextMenuStrip Behaviors"
description: This post shows how I fixed a bug of DockPanel Suite related to context menu strip.
tags: .NET
permalink: /dockpanel-suite-contextmenustrip-behaviors-bef808f00342
excerpt_separator: <!--more-->
---
#255 on GitHub is an interesting bug of DPS, and this post aims to show how I came across the fix.
<!--more-->

You can see from the screenshot that the context menu strip for listed windows was wrongly rendered on the secondary screen. That can be easily reproduced and then the related code can be located.

``` csharp
int x = 0;
int y = ButtonWindowList.Location.Y + ButtonWindowList.Height;
SelectMenu.Show(ButtonWindowList, x, y);
```

OK. The code seems to be simple, and we can see that in some cases, the `x` given can be too large for current screen, and the menu strip can go to the wrong place (like in the bug report). It does not lead to something, only if `x + SelectMenu.Width` goes beyond the border of all screens (in that case WinForms automatically move the menu strip to a better place).

Alright, so the fix now is to take full control of x and y calculation, and the revised version is as below,

``` csharp
var workingArea = Screen.GetWorkingArea(ButtonWindowList.PointToScreen(new Point(ButtonWindowList.Width / 2, ButtonWindowList.Height / 2)));
var menu = new Rectangle(ButtonWindowList.PointToScreen(new Point(0, ButtonWindowList.Location.Y + ButtonWindowList.Height)), SelectMenu.Size);
var menuMargined = new Rectangle(menu.X - SelectMenuMargin, menu.Y - SelectMenuMargin, menu.Width + SelectMenuMargin, menu.Height + SelectMenuMargin);
if (workingArea.Contains(menuMargined))
{
    SelectMenu.Show(menu.Location);
}
else
{
    var newPoint = menu.Location;
    newPoint.X = DrawHelper.Balance(SelectMenu.Width, SelectMenuMargin, newPoint.X, workingArea.Left, workingArea.Right);
    newPoint.Y = DrawHelper.Balance(SelectMenu.Height, SelectMenuMargin, newPoint.Y, workingArea.Top, workingArea.Bottom);
    var button = ButtonWindowList.PointToScreen(new Point(0, ButtonWindowList.Height));
    if (newPoint.Y < button.Y)
    {
        // flip the menu up to be above the button.
        newPoint.Y = button.Y - SelectMenu.Height - ButtonWindowList.Height;
    }

    SelectMenu.Show(newPoint);
}
```

Well, it is rather complicated to do the calculation, as we need to first locate the middle point of the button, and then get the working area to render the menu strip. When the menu with margins happens to fall in the working area fully, we can safely render it at default location. But special care needs to be carried out otherwise.

The `else` block considers many possible cases, such as which `x` to use among three options (see Balance function for details), and which `y` to use. More importantly, if the calculated `y` is smaller than button's bottom Y, we need to show the menu strip above the button.

Is that the final solution? Unfortunately, it is NOT.

You probably never realize that SelectMenu.Height is varied!!! Its value changes from initial one to another just after being shown for the first time. So when the menu strip is rendered for the first time, it might still hide the button (when the button is near the bottom of the working area).

Thus, a quick workaround is to show this menu strip once before the calculation starts. That in fact leads to a quick flash. Another way is to use

``` csharp
if (newPoint.Y < button.Y)
{
    // flip the menu up to be above the button.
    newPoint.Y = button.Y - ButtonWindowList.Height;
    SelectMenu.Show(newPoint, ToolStripDropDownDirection.AboveRight);
}
else
{
    SelectMenu.Show(newPoint);
}
```

But this only fixed the button flip, but not all the calculation that relies on menu height and width.

Will have to do more investigation and update this article. Stay tuned.
