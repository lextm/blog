---
description: "A comprehensive guide for reviewers to test Esbonio VS Code extension 0.95.2, covering environment setup, virtual environment configuration, settings adjustment, and troubleshooting to provide valuable feedback for this reStructuredText documentation tool."
excerpt_separator: <!--more-->
layout: post
tags: python visual-studio-code restructuredtext
categories: [Programming Languages]
title: "Esbonio VS Code Reviewers' Guide"
---
I have been using the Esbonio extension 0.11 releases for a long while, and finally the 0.95 releases reached a stage where it is ready for reviewers to test out. This guide will be updated from time to time to serve as a comprehensive guide to ensure that reviewers can provide valuable feedback to the development team.
<!--more-->

## Environment Setup

* macOS 15.0
* VS Code 1.93.1
* Esbonio extension 0.95.2

> This is based on my local environment. You might need to adjust the steps based on your own environment. But make sure you use Esbonio 0.95.2 (or later if that version is stable).
>
> I believe the same steps should work fine on Windows/Linux, and other versions of VS Code.

## Demo Source Code

Before moving on to your own documentation project, I suggest you start with the demo project provided by the Esbonio team.

1. Clone from https://github.com/swyddfa/esbonio.git to your local drive (mine is `/Users/lextm/esbonio`).
2. Open the demo directory in VS Code (mine is `/Users/lextm/esbonio/lib/esbonio/tests/workspaces/demo`).

## Preparation

Now Esbonio VS Code extension requires many settings to be manually configured (instead of automatic detecting in its 0.11 releases), and the demo source code only has one setting in `pyproject.toml`, which isn't enough:

```toml
[tool.esbonio.sphinx]
buildCommand = ["sphinx-build", "-M", "dirhtml", ".", "./_build"]
```

You have to configure further settings to make it work.

### Virtual Environment

It's recommended to use a virtual environment to isolate the dependencies. I choose Pyenv and Pipenv to prepare the virtual environment:

``` bash
pyenv local 3.12
pipenv install "sphinx>=7.0.0,<8.0.0" sphinx-design myst-parser furo
pipenv --venv
```

> Note that Sphinx 8 wasn't yet supported by Esbonio right now. Others are dependencies of this demo project.
>
> Also note that you must use Python 3.9+ as older Python releases are no longer supported.
>
> Also note that esbonio isn't used as a dependency in this virtual environment because the extension itself bundles a version of esbonio already. So, if you used to install esbonio with your virtual environment, delete it there to avoid conflicts.
>
> If you never know pyenv or pipenv, you might need to learn about them first. If you prefer other tools, you can use them too but the steps might vary.

In VS Code, open `conf.py` and select this pipenv environment (mine is `/Users/lextm/.local/share/virtualenvs/demo-2cFbohxa`) so that it applies to Microsoft Python extension as well as others.

### Extra Esbonio Settings

Now you need to configure other Esbonio settings:

1. Create `.vscode/settings.json`
2. In its content, use
   ``` json
   {
     "esbonio.logging.level": "debug",
     "esbonio.sphinx.pythonCommand": ["/Users/lextm/.local/share/virtualenvs/demo-2cFbohxa/bin/python"],
     "esbonio.server.pythonPath": "/Users/lextm/.local/share/virtualenvs/demo-2cFbohxa/bin/python",
   }
   ```

> I prefer putting settings in VS Code settings file due to IntelliSense instead of `pyproject.toml`.
>
> `esbonio.server.pythonPath` is somehow necessary.
>
> If you use other virtual environment tools, you might need to adjust the paths accordingly.

## Testing

> You might need to restart VS Code or reload the window to make sure the settings are applied.

Now it's time to play with Esbonio features.

### Live Preview

1. Open a source file, like `rst/domains/python.rst`.
2. Click "Preview Documentation" button on the right top corner of the opened file section.
3. (Resize VS Code if needed) scroll the previewed contents and see how the source file scrolled along too.

> If you scroll the source code, the preview contents don't follow. This is a TODO item.

### Auto Completion

1. Open any `.rst` file, and add``:doc:`/` ``

2. Place the cursor behind `/` and trigger auto completion.
3. Select a suggested item from the popup list.

## Typical Errors

### No Applicable Project

The actual error messages might occur when you try to preview a file.

``` text
[esbonio.ProjectManager] No applicable project for uri: file:///Users/lextm/esbonio/lib/esbonio/tests/workspaces/demo/rst/roles.rst
```

You might review `esbonio.sphinx.pythonCommand` to make sure it is correctly configured.

## Conclusion

Now you know the necessary steps to test out the demo project. You can now apply the same steps to your own Sphinx documentation project and provide valuable feedback to the Esbonio team.

Keep in mind that this extension is still under development towards its ambitious goals of 1.0 release, so certain steps might not work well for another project or a newer version of the extension. But the development team is actively working on improving the extension, so your feedback is crucial to its success.

> If you encounter any issues, feel free to report them to the [Esbonio GitHub repository](https://github.com/swyddfa/esbonio/issues).
