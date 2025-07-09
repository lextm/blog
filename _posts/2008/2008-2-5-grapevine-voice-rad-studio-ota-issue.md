---
layout: post
title: "GrapeVine Voice: RAD Studio OTA Issue"
description: This post talks about a RAD Studio OTA issue.
tags: Code-Beautifier-Collection Delphi
permalink: /grapevine-voice-rad-studio-ota-issue-4b405586bbf3
excerpt_separator: <!--more-->
---
I thought it was a CBC bug at first. However, after debugging I am sure it is another OTA bug.
<!--more-->

Now all projects are MSBuild based. Therefore a Delphi project contains a .dproj wrapper and a real .dpr or dpk project file. The bug happens if these two files have different names. Then you cannot get a correctly string from IOTAProject.ProjectOptions.TargetName.

The workaround is also easy that I parse the .dproj file directly to locate the .dpr or .dpk file. The code is,

``` csharp
public static string GetProjectTarget(IOTAProject project) {
    if (project != null) {
        String targetName = project.ProjectOptions.TargetName;
        if (project.Personality == OTAIDEPersonalities.sDelphiDotNetPersonality
            || project.Personality == OTAIDEPersonalities.sDelphiDotNetPersonality)
        {
            string folder = Path.GetDirectoryName(targetName);
            string file = Path.GetFileName(OtaUtils.GetDelphiProjectFileName(project.FileName));
            return Path.ChangeExtension(Path.Combine(folder, file), Path.GetExtension(targetName));
        }
        return targetName;
    }
    return null;
}

public static string GetDelphiProjectFileName(string project)
{
    string content = File.ReadAllText(project, Encoding.UTF8);
        Match m = regex.Match(content);
        Debug.Assert(m.Success);
    string file = m.Groups["source_name"].Value;
    return Path.Combine(Path.GetDirectoryName(project), file);
}

readonly static Regex regex = new Regex(
".+)\">\\s* +
"urce>MainSource\\s*",
    RegexOptions.CultureInvariant
    | RegexOptions.Compiled
    );
```

I will fire a bug report to QC tomorrow. Oh, that would be Chinese New Year Eve

(Update: This bug is logged as QC#57890. And it applies to both Delphi for Win32 and .NET DLL/BPL projects. Strangely it does not affect EXE projects.)
