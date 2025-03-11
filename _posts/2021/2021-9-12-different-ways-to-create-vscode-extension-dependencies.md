---
layout: post
title: Different Ways to Create VSCode Extension Dependencies
description: A post about different ways to define VSCode extension dependencies and which might work best for your case
tags: Visual-Studio-Code
excerpt_separator: <!--more-->
---

If you are developing your own VSCode extensions, you might find a need to specify dependencies on other extensions. There are more than one way to manage such relationship, so this post is going to discuss the pros and cons of each approaches, so that you can easily choose the right one for your case.
<!--more-->

## Extension Dependencies in Configuration

In `project.json` you can easily specify what extensions are prerequisites of your extension using the `extensionDependencies` setting (which is [documented here](https://code.visualstudio.com/api/references/extension-manifest)).

For example, a Python related extension might hope that Microsoft's Python extension is always installed aside, so the following snippet can be used,

``` json
"extensionDependencies": [
    "ms-python.python"
]
```

This is probably the most likely option you are going to use, as it is very simple to configure. VSCode takes care of the rest for you by installing the specified dependencies ahead of installing your extension.

However, this builds up a very strong binding between your extension and the dependencies. So if some of the dependencies are recommended and optional, but not mandatory, you should avoid putting them here.

## Recommendation in Code

In your extension's source code, it is very flexible to detect what extensions are already installed. Then you can prompt which extensions the user might install to get better experience.

``` typescript
    const msPythonName = 'ms-python.python';
    // guide the users to install Microsoft Python extension.
    const msPython = vscode.extensions.getExtension(msPythonName);
    if (!msPython && vscode.workspace.getConfiguration('myExtension').get('recommendPython', true)) {
        const message = 'It is recommended to install Microsoft Python extension. Do you want to install it now?';
        const choice = await vscode.window.showInformationMessage(message, 'Install', 'Not now', 'Do not show again');
        if (choice === 'Install') {
            await vscode.commands.executeCommand('extension.open', msPythonName); // open Extension tab and show extension details.
            await vscode.commands.executeCommand('workbench.extensions.installExtension', msPythonName); // install the extension.
        } else if (choice === 'Do not show again') {
            vscode.workspace.getConfiguration('myExtension').set('recommendPython', false);
        }
    }
```

You can see that the above snippet shows exactly the logic. If the user chooses to install the dependency, then the installation is automatically kicked out. A custom configuration setting `myExtension.recommendPython` is also utilized to suppress recommendation if the user decides never to install it.

> Note that `myExtension.recommendPython` needs to be defined in `project.json` file.

This approach requires some TypeScript code in `function activate(context: vscode.ExtensionContext)`, but offers you all kinds of flexibility. I use this trick a lot to recommend optional dependencies.

> Note that you can also use similar code block to detect conflicting extensions and prompt users to uninstall them.

## Extension Pack

If you just want the users to install a bunch of extensions together, you might write your own extension packs, following [the documentation](https://code.visualstudio.com/api/references/extension-manifest#extension-packs). When an extension pack is being installed by VSCode, all extensions defined in this pack are being installed.

This is rather useful even if you are authoring a specific extension, as even without writing a single line of JavaScript/TypeScript you can create an extension pack based on excellent extensions from others.
