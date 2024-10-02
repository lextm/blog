---
layout: post
title: "Restart Singleton Applications"
description: This post talks about how to restart a singleton application.
tags: .NET
permalink: /restart-singleton-applications-8619bc5d6375
excerpt_separator: <!--more-->
---
When I talked about .NET internationalisation last time I mentioned that the application should be restarted in order to change UI languages. But that code only works when your application allows multiple instances. If you use any technique to make it singleton (only one application instance in the memory), you find the code I provided failed to restart.
<!--more-->

Why? Take a look at the original code I published in August,

``` csharp
private static void Restart()
{
    Process.Start(Application.ExecutablePath);
    Application.Exit();
}
```

Before the old instance exits, the new instance is already launched. So in the singleton case, no new instance is created and the old instance exits. Aha! You get nothing running.

A side note. You should avoid calling Application.Exit sometimes (especially in multi-threading cases). You may modify Restart to accept a main form reference. Closing the main form by calling Close usually meets your requirement.

Then, how to restart a singleton application? My solution is to bring in a restarter.exe helper executable which is a small and clean console program.

``` csharp
class Program
{
    public static void Main(string[] args)
    {
        if (args.Length != 1)
        {
            return;
        }
        string fileName = args[0];
        do
        {
            Thread.Sleep(5000);
        } while (Process.GetProcessesByName(Path.GetFileNameWithoutExtension(fileName)).Length > 0);
        Process.Start(fileName);
    }
}
```

Restart function should be modified as

``` csharp
static void Restart()
{
    using (Process p = new Process())
    {
        p.StartInfo.FileName = Path.Combine(Path.GetDirectoryName(Application.ExecutablePath),
            "restarter.exe");
        p.StartInfo.Arguments = "\"" + Application.ExecutablePath + "\"";
        p.StartInfo.CreateNoWindow = true;
        p.StartInfo.WindowStyle = ProcessWindowStyle.Hidden;
        p.Start();
    }
    Application.Exit();
}
```

Simply place the restarter.exe in the same folder containing your application, and everything should be OK.
