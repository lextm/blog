---
layout: post
title: "Debugging on Mono: An xbuild Issue"
description: This post talks about an issue I encountered when trying to compile F# on Windows with Mono.
tags: Mono
permalink: /debugging-on-mono-an-xbuild-issue-44cda356cfa1
excerpt_separator: <!--more-->
---
I just attempted to answer [one StackOverflow question](http://stackoverflow.com/questions/14678414/installing-f-3-windows-xp-using-mono/14679719#14679719) about how to compile F# on Windows with Mono, but failed as there is something I don't know why. However, by using Mono 3.0.3 xbuild I noticed that it seems to support many MSBuild 3.5 goodies. So I decided to test it out to execute ANTLR targets.
<!--more-->

Well, in fact it stopped miserably

``` bash
XBuild Engine Version 3.0.3.0
Mono, Version 3.0.3.0
Copyright © Marek Sieradzki 2005–2008, Novell 2008–2011.

Build started 2/9/2013 11:57:55 AM.
__________________________________________________
E:\Projects\sharpsnmplib\SharpSnmpLib.md.sln: warning : Project file E:\Project
s\sharpsnmplib\WinFormsUI\WinFormsUI.csproj referenced in the solution file, not
found. Ignoring.
E:\Projects\sharpsnmplib\SharpSnmpLib.md.sln: warning : Don't know how to handl
e GlobalSection TeamFoundationVersionControl, Ignoring.
E:\Projects\sharpsnmplib\SharpSnmpLib.md.sln: warning : Don't know how to handl
e GlobalSection SubversionScc, Ignoring.
Project "E:\Projects\sharpsnmplib\SharpSnmpLib.md.sln" (default target(s)):
Target ValidateSolutionConfiguration:
Building solution configuration "Debug|Mixed Platforms".
Target Build:
Project "E:\Projects\sharpsnmplib\SharpSnmpLib\SharpSnmpLib.cspr
oj" (default target(s)):
Target PrepareForBuild:
Configuration: Debug Platform: AnyCPU
: error : Error building target CheckPrerequisites: Exception has been thrown by
the target of an invocation.
Done building project "E:\Projects\sharpsnmplib\SharpSnmpLib\Sha
rpSnmpLib.csproj". - FAILED
Project "E:\Projects\sharpsnmplib\Mono.Options\Mono.Options.cspr
oj" (default target(s)):
```

Therefore, I need to resolve this problem first.

## MonoDevelop Debugging - Failed
To begin with, I tried to use MonoDevelop to debug xbuild. Miguel did post about the details a long time ago. However, even if I got the steps right for MonoDevelop 3.0.6, I found that Mono's attaching method is no longer supported by Microsoft on Windows 8 (I did not test on other Windows versions yet),

``` bash
System.Runtime.InteropServices.COMException (0x80070032): The request is not supported. (Exception from HRESULT: 0x80070032)
at Microsoft.Samples.Debugging.CorDebug.NativeApi.ICorDebug.CreateProcess(String lpApplicationName, String lpCommandLine, SECURITY_ATTRIBUTES lpProcessAttributes, SECURITY_ATTRIBUTES lpThreadAttributes, Int32 bInheritHandles, UInt32 dwCreationFlags, IntPtr lpEnvironment, String lpCurrentDirectory, STARTUPINFO lpStartupInfo, PROCESS_INFORMATION lpProcessInformation, CorDebugCreateProcessFlags debuggingFlags, ICorDebugProcess& ppProcess)
at Microsoft.Samples.Debugging.CorDebug.CorDebugger.CreateProcess(String applicationName, String commandLine, SECURITY_ATTRIBUTES processAttributes, SECURITY_ATTRIBUTES threadAttributes, Boolean inheritHandles, Int32 creationFlags, IntPtr environment, String currentDirectory, STARTUPINFO startupInfo, PROCESS_INFORMATION& processInformation, CorDebugCreateProcessFlags debuggingFlags)
at Microsoft.Samples.Debugging.CorDebug.CorDebugger.CreateProcess(String applicationName, String commandLine, String currentDirectory, IDictionary`2 environment, Int32 flags)
at MonoDevelop.Debugger.Win32.CorDebuggerSession.OnRun(DebuggerStartInfo startInfo)
at Mono.Debugging.Client.DebuggerSession.<>c__DisplayClassc.b__a()
```
So I have to find another way :(

## Mono Tracing
I dumped the xbuild error details to a log file with the following command so that I can see what is the culprit,

``` bash
$ xbuild sharpsnmplib.md.sln /v:diag > error.log
Target PreBuildEvent skipped due to false condition: '$(PreBuildEvent)' != ''
: error : Error building target CheckPrerequisites: Exception has been thrown by the target of an invocation.
Error building target CheckPrerequisites: System.Reflection.TargetInvocationException: Exception has been thrown by the target of an invocation. --> System.ArgumentException: Illegal characters in path.
at System.IO.Path.IsPathRooted (System.String path) [0x00000] in :0
at Microsoft.Build.BuildEngine.ConditionFunctionExpression.Exists (System.String file, Microsoft.Build.BuildEngine.Project context) [0x00000] in :0
at (wrapper managed-to-native) System.Reflection.MonoMethod:InternalInvoke (System.Reflection.MonoMethod,object,object[],System.Exception&)
at System.Reflection.MonoMethod.Invoke (System.Object obj, BindingFlags invokeAttr, System.Reflection.Binder binder, System.Object[] parameters, System.Globalization.CultureInfo culture) [0x00000] in :0
-- End of inner exception stack trace --
at System.Reflection.MonoMethod.Invoke (System.Object obj, BindingFlags invokeAttr, System.Reflection.Binder binder, System.Object[] parameters, System.Globalization.CultureInfo culture) [0x00000] in :0
at System.Reflection.MethodBase.Invoke (System.Object obj, System.Object[] parameters) [0x00000] in :0
at Microsoft.Build.BuildEngine.ConditionFunctionExpression.BoolEvaluate (Microsoft.Build.BuildEngine.Project context) [0x00000] in :0
at Microsoft.Build.BuildEngine.ConditionNotExpression.BoolEvaluate (Microsoft.Build.BuildEngine.Project context) [0x00000] in :0
at Microsoft.Build.BuildEngine.ConditionAndExpression.BoolEvaluate (Microsoft.Build.BuildEngine.Project context) [0x00000] in :0
at Microsoft.Build.BuildEngine.ConditionParser.ParseAndEvaluate (System.String condition, Microsoft.Build.BuildEngine.Project context) [0x00000] in :0
at Microsoft.Build.BuildEngine.TaskBatchingImpl.Build (Microsoft.Build.BuildEngine.BuildTask buildTask, System.Boolean& executeOnErrors) [0x00000] in :0
at Microsoft.Build.BuildEngine.TargetBatchingImpl.RunTargetWithBucket (System.Collections.Generic.Dictionary`2 bucket, Microsoft.Build.BuildEngine.Target target, System.Boolean& executeOnErrors) [0x00000] in :0
at Microsoft.Build.BuildEngine.TargetBatchingImpl.Run (Microsoft.Build.BuildEngine.Target target, System.Boolean& executeOnErrors) [0x00000] in :0
at Microsoft.Build.BuildEngine.TargetBatchingImpl.Build (Microsoft.Build.BuildEngine.Target target, System.Boolean& executeOnErrors) [0x00000] in :0
at Microsoft.Build.BuildEngine.Target.DoBuild (System.Boolean& executeOnErrors) [0x00000] in :0
Done building project "E:\Projects\sharpsnmplib\SharpSnmpLib\SharpSnmpLib.csproj". -- FAILED
```

And since I could not debug Mono program I tried to use Mono tracing,

``` bash
mono --trace=M:System.IO.Path:IsPathRooted "C:\Program Files (x86)\Mono-3.0.3\lib\mono\4.5\xbuild.exe" SharpSnmpLib.md.sln /v:diag > details.log
```

It is unbelievably easy that now I can tell what happened,

``` bash
[00001830: 1.88729 0] ENTER: System.IO.Path:IsPathRooted (string)([STRING:040CA330:$([System.IO.Path]::Combine(E:\Projects\sharpsnmplib\, ".nuget"))\nuget.exe], )
: error : Error building target CheckPrerequisites: Exception has been thrown by the target of an invocation.
Error building target CheckPrerequisites: System.Reflection.TargetInvocationException: Exception has been thrown by the target of an invocation. --> System.ArgumentException: Illegal characters in path.
at System.IO.Path.IsPathRooted (System.String path) [0x00000] in :0
at Microsoft.Build.BuildEngine.ConditionFunctionExpression.Exists (System.String file, Microsoft.Build.BuildEngine.Project context) [0x00000] in :0
at (wrapper managed-to-native) System.Reflection.MonoMethod:InternalInvoke (System.Reflection.MonoMethod,object,object[],System.Exception&)
at System.Reflection.MonoMethod.Invoke (System.Object obj, BindingFlags invokeAttr, System.Reflection.Binder binder, System.Object[] parameters, System.Globalization.CultureInfo culture) [0x00000] in :0
-- End of inner exception stack trace --
at System.Reflection.MonoMethod.Invoke (System.Object obj, BindingFlags invokeAttr, System.Reflection.Binder binder, System.Object[] parameters, System.Globalization.CultureInfo culture) [0x00000] in :0
at System.Reflection.MethodBase.Invoke (System.Object obj, System.Object[] parameters) [0x00000] in :0
at Microsoft.Build.BuildEngine.ConditionFunctionExpression.BoolEvaluate (Microsoft.Build.BuildEngine.Project context) [0x00000] in :0
at Microsoft.Build.BuildEngine.ConditionNotExpression.BoolEvaluate (Microsoft.Build.BuildEngine.Project context) [0x00000] in :0
at Microsoft.Build.BuildEngine.ConditionAndExpression.BoolEvaluate (Microsoft.Build.BuildEngine.Project context) [0x00000] in :0
at Microsoft.Build.BuildEngine.ConditionParser.ParseAndEvaluate (System.String condition, Microsoft.Build.BuildEngine.Project context) [0x00000] in :0
at Microsoft.Build.BuildEngine.TaskBatchingImpl.Build (Microsoft.Build.BuildEngine.BuildTask buildTask, System.Boolean& executeOnErrors) [0x00000] in :0
at Microsoft.Build.BuildEngine.TargetBatchingImpl.RunTargetWithBucket (System.Collections.Generic.Dictionary`2 bucket, Microsoft.Build.BuildEngine.Target target, System.Boolean& executeOnErrors) [0x00000] in :0
at Microsoft.Build.BuildEngine.TargetBatchingImpl.Run (Microsoft.Build.BuildEngine.Target target, System.Boolean& executeOnErrors) [0x00000] in :0
at Microsoft.Build.BuildEngine.TargetBatchingImpl.Build (Microsoft.Build.BuildEngine.Target target, System.Boolean& executeOnErrors) [0x00000] in :0
at Microsoft.Build.BuildEngine.Target.DoBuild (System.Boolean& executeOnErrors) [0x00000] in :0
```

(Note that you can find [Path.cs from GitHub](https://github.com/mono/mono/blob/master/mcs/class/corlib/System.IO/Path.cs).)

At this moment we know that NuGet.targets uses an inline defined variable xbuild does not support yet,

``` text
$([System.IO.Path]::Combine($(SolutionDir), ".nuget"))
$([System.IO.Path]::Combine($(ProjectDir), "packages.config"))
```
It seems that I should now switch to Mono on Linux :)
