---
layout: post
title: "GrapeVine Voice: Inno Setup Issue"
description: "This post talks about an issue I met when uninstalling CBC."
tags: Code-Beautifier-Collection Delphi
permalink: /grapevine-voice-inno-setup-issue-f54bda333a1b
excerpt_separator: <!--more-->
---
Today I will release M8. And the last issue I met is that uninstalling CBC caused an unhandled exception. What caused this exception? It was hard to debug. Inno Setup does not have a debugger like InstallAware. So I had to debug my own code. But my code ran well. Then I had to guess what happened by investigating what left in the folder. There was only one file, installforallusers.exe.
<!--more-->

What is your opinion? Oh, I forget to mention that installforallusers.exe is a C# application that references LeXDK assemblies. See the answer? LeXDK assemblies were uninstalled so this executable could not find its references.

So I have to say it is Inno Setup implementation caused this issue. I told it to run installforallusers.exe to remove GAC and registry keys, but it never checked if this executable requires other files in the installation folder. Inno Setup removed all files in the folder except this executable so an exception was raised.

I was about to report this issue to Inno Setup author but soon I expected a workaround. It is not Inno Setup's responsibility to analyze my files, and make everything okay. I rather take that responsibility myself.

In fact, a workaround is easy to find. Implementing an important procedure resolves the issue.

``` pascal
procedure CurUninstallStepChanged(CurUninstallStep: TUninstallStep);
var
    ErrorCode: Integer;
begin
    if (CurUninstallStep = usAppMutexCheck) then
    begin
        //run uninstallforallusers
        ShellExec('', ExpandConstant('{app}\installforallusers.exe'),
        '-i', '', SW_SHOW, ewWaitUntilTerminated, ErrorCode);
    end;
end;
```
